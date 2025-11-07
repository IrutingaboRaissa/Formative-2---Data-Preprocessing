"""
Facial Recognition System - Command Line Interface
Part 2 of Formative 2: Data Preprocessing Assignment

This script provides a command-line interface for facial recognition authentication.
"""

import os
import cv2
import numpy as np
import joblib
import argparse
from pathlib import Path
from skimage.feature import hog


class FaceRecognitionSystem:
    """
    Facial recognition system for user authentication.
    """
    
    def __init__(self, model_dir='models'):
        """
        Initialize the facial recognition system.
        
        Args:
            model_dir: Directory containing trained models
        """
        self.model_dir = model_dir
        self.model = None
        self.scaler = None
        self.label_encoder = None
        self.load_models()
    
    def load_models(self):
        """Load trained models and preprocessing objects."""
        try:
            model_path = os.path.join(self.model_dir, 'face_recognition_rf.pkl')
            scaler_path = os.path.join(self.model_dir, 'scaler.pkl')
            encoder_path = os.path.join(self.model_dir, 'label_encoder.pkl')
            
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            self.label_encoder = joblib.load(encoder_path)
            
            print("✓ Models loaded successfully")
            print(f"  Known users: {', '.join(self.label_encoder.classes_)}")
        except FileNotFoundError as e:
            print(f"✗ Error loading models: {e}")
            print("  Please train the model first using the Jupyter notebook.")
            raise
    
    def extract_features(self, img, resize_shape=(128, 128)):
        """
        Extract features from an image.
        
        Args:
            img: Input image (numpy array)
            resize_shape: Target size for resizing
        
        Returns:
            Feature vector as numpy array
        """
        features = []
        
        # Resize image
        img_resized = cv2.resize(img, resize_shape)
        
        # 1. Color Histogram Features (RGB)
        for channel in range(3):
            hist = cv2.calcHist([img_resized], [channel], None, [32], [0, 256])
            hist = hist.flatten() / hist.sum()
            features.extend(hist)
        
        # 2. Statistical Features
        for channel in range(3):
            channel_data = img_resized[:, :, channel]
            features.append(np.mean(channel_data))
            features.append(np.std(channel_data))
            features.append(np.median(channel_data))
            features.append(np.min(channel_data))
            features.append(np.max(channel_data))
        
        # 3. Grayscale features
        gray = cv2.cvtColor(img_resized, cv2.COLOR_RGB2GRAY)
        
        # Edge detection
        edges = cv2.Canny(gray, 100, 200)
        features.append(np.sum(edges > 0) / edges.size)
        
        # 4. HOG Features
        hog_features = hog(gray, orientations=9, pixels_per_cell=(8, 8),
                          cells_per_block=(2, 2), visualize=False)
        features.extend(hog_features[:100])
        
        # 5. Texture features
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        features.append(np.var(laplacian))
        
        return np.array(features)
    
    def recognize_face(self, image_path, threshold=0.5, display=False):
        """
        Recognize a face from an image file.
        
        Args:
            image_path: Path to the image file
            threshold: Confidence threshold for recognition
            display: Whether to display the image
        
        Returns:
            Dictionary with recognition results
        """
        # Load image
        img = cv2.imread(image_path)
        if img is None:
            return {
                'success': False,
                'recognized': False,
                'error': f'Could not load image: {image_path}'
            }
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Extract features
        features = self.extract_features(img_rgb)
        features_scaled = self.scaler.transform(features.reshape(1, -1))
        
        # Predict
        prediction = self.model.predict(features_scaled)[0]
        probabilities = self.model.predict_proba(features_scaled)[0]
        confidence = probabilities.max()
        
        # Build result
        result = {
            'success': True,
            'confidence': float(confidence),
            'all_probabilities': {
                name: float(prob) 
                for name, prob in zip(self.label_encoder.classes_, probabilities)
            }
        }
        
        if confidence >= threshold:
            member_name = self.label_encoder.inverse_transform([prediction])[0]
            result['recognized'] = True
            result['member'] = member_name
        else:
            result['recognized'] = False
            result['reason'] = f'Low confidence ({confidence:.2%} < {threshold:.2%})'
        
        # Display if requested
        if display:
            self._display_result(img_rgb, result)
        
        return result
    
    def _display_result(self, img, result):
        """Display recognition result."""
        try:
            import matplotlib.pyplot as plt
            
            plt.figure(figsize=(8, 6))
            plt.imshow(img)
            
            if result['recognized']:
                title = f"✓ RECOGNIZED: {result['member']}\nConfidence: {result['confidence']:.2%}"
                color = 'green'
            else:
                title = f"✗ NOT RECOGNIZED\n{result.get('reason', 'Unknown reason')}"
                color = 'red'
            
            plt.title(title, color=color, fontsize=14, fontweight='bold')
            plt.axis('off')
            plt.tight_layout()
            plt.show()
        except ImportError:
            print("Matplotlib not available for display")
    
    def authenticate(self, image_path, threshold=0.5, verbose=True):
        """
        Authenticate a user via facial recognition.
        
        Args:
            image_path: Path to the facial image
            threshold: Confidence threshold
            verbose: Whether to print detailed results
        
        Returns:
            Tuple: (authenticated: bool, member_name: str or None)
        """
        result = self.recognize_face(image_path, threshold)
        
        if verbose:
            print("\n" + "="*60)
            print("FACIAL RECOGNITION AUTHENTICATION")
            print("="*60)
            
            if result['success']:
                if result['recognized']:
                    print(f"✓ ACCESS GRANTED")
                    print(f"  User: {result['member']}")
                    print(f"  Confidence: {result['confidence']:.2%}")
                else:
                    print(f"✗ ACCESS DENIED")
                    print(f"  Reason: {result.get('reason', 'Unknown')}")
                
                print(f"\n  Recognition probabilities:")
                for member, prob in result['all_probabilities'].items():
                    print(f"    {member}: {prob:.2%}")
            else:
                print(f"✗ ERROR: {result.get('error', 'Unknown error')}")
            
            print("="*60 + "\n")
        
        if result['success'] and result['recognized']:
            return True, result['member']
        else:
            return False, None


def main():
    """Main function for command-line interface."""
    parser = argparse.ArgumentParser(
        description='Facial Recognition System - User Authentication'
    )
    parser.add_argument(
        'image_path',
        type=str,
        help='Path to the facial image for recognition'
    )
    parser.add_argument(
        '--threshold',
        type=float,
        default=0.5,
        help='Confidence threshold for recognition (default: 0.5)'
    )
    parser.add_argument(
        '--model-dir',
        type=str,
        default='models',
        help='Directory containing trained models (default: models)'
    )
    parser.add_argument(
        '--display',
        action='store_true',
        help='Display the image with recognition result'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress verbose output'
    )
    
    args = parser.parse_args()
    
    # Check if image exists
    if not os.path.exists(args.image_path):
        print(f"✗ Error: Image file not found: {args.image_path}")
        return 1
    
    try:
        # Initialize system
        system = FaceRecognitionSystem(model_dir=args.model_dir)
        
        # Authenticate
        authenticated, member_name = system.authenticate(
            args.image_path,
            threshold=args.threshold,
            verbose=not args.quiet
        )
        
        # Display if requested
        if args.display:
            result = system.recognize_face(args.image_path, args.threshold, display=True)
        
        # Return exit code
        return 0 if authenticated else 1
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
