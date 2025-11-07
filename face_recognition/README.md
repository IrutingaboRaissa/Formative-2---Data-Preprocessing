# Facial Recognition System - Part 2# Facial Recognition System - Part 2



Formative 2: Data Preprocessing Assignment**Formative 2: Data Preprocessing Assignment**  

**Team Member Assignment: Facial Recognition Component**

## Overview

## 📋 Overview

This project implements facial recognition for user authentication using machine learning.

This component implements facial recognition for user authentication as part of a multimodal authentication system. The system authenticates users through facial recognition before allowing access to product recommendations.

## Project Structure

## 🎯 Assignment Requirements Met

```

face_recognition/### ✅ Image Data Collection

├── complete_facial_recognition.ipynb   # Main notebook - RUN THIS- [x] Minimum 3 facial images per member (neutral, smiling, surprised)

├── requirements.txt                    # Python dependencies- [x] Load and display sample pictures

├── images/                            # Team member photos- [x] Proper image organization and naming

├── models/                            # Trained models saved here

└── features/                          # image_features.csv saved here### ✅ Image Augmentation

```- [x] 8 augmentations per image:

  - Rotation (+15° and -15°)

## Quick Start  - Horizontal flip

  - Grayscale conversion

1. Install dependencies:  - Brightness adjustment (up and down)

```bash  - Gaussian blur

pip install -r requirements.txt- [x] Display augmentation examples

```

### ✅ Feature Extraction

2. Open and run the notebook:- [x] Color histogram features (RGB channels)

```bash- [x] HOG (Histogram of Oriented Gradients)

jupyter notebook complete_facial_recognition.ipynb- [x] Statistical features (mean, std, median, min, max)

```- [x] Edge detection features

- [x] Texture features (Laplacian variance)

3. Run all cells from top to bottom- [x] Features saved to `image_features.csv`



## What the Notebook Does### ✅ Model Development

- [x] Two models implemented:

1. Loads team member images from the images folder  - Random Forest Classifier

2. Applies 8 augmentation techniques per image  - Logistic Regression

3. Extracts 217 features per image- [x] Model evaluation metrics:

4. Saves features to image_features.csv  - Accuracy

5. Trains Random Forest model  - F1-Score

6. Trains Logistic Regression model  - Confusion Matrix

7. Evaluates both models with accuracy, F1-score, confusion matrices  - Classification Report

8. Saves all trained models

9. Tests authentication with sample images### ✅ System Demonstration

- [x] Command-line interface

## Output Files Generated- [x] Unauthorized attempt simulation

- [x] Full authentication flow

- `features/image_features.csv` - Feature dataset- [x] Integration-ready design

- `models/face_recognition_rf.pkl` - Random Forest model

- `models/face_recognition_lr.pkl` - Logistic Regression model## 📁 Project Structure

- `models/scaler.pkl` - Feature scaler

- `models/label_encoder.pkl` - Label encoder```

face_recognition/

## Features Extracted├── images/                          # Facial images organized by member

│   ├── member1/

- 96 color histogram features (RGB channels)│   │   ├── neutral/

- 15 statistical features (mean, std, median, min, max)│   │   ├── smiling/

- 1 edge detection feature│   │   └── surprised/

- 100 HOG descriptors│   ├── member2/

- 5 texture features│   └── member3/

├── models/                          # Trained models

Total: 217 features per image│   ├── face_recognition_rf.pkl      # Random Forest model

│   ├── face_recognition_lr.pkl      # Logistic Regression model

## Augmentation Techniques│   ├── scaler.pkl                   # Feature scaler

│   └── label_encoder.pkl            # Label encoder

1. Original├── features/                        # Extracted features

2. Rotation +15 degrees│   └── image_features.csv           # Feature dataset

3. Rotation -15 degrees├── facial_recognition.ipynb         # Main Jupyter notebook

4. Horizontal flip├── face_recognition_system.py       # Python module for recognition

5. Grayscale├── demo.py                          # System demonstration script

6. Brightness increase├── requirements.txt                 # Python dependencies

7. Brightness decrease└── README.md                        # This file

8. Gaussian blur```



## Models## 🚀 Getting Started



- **Random Forest**: 100 trees, max depth 10### 1. Installation

- **Logistic Regression**: Multinomial classification

Install required dependencies:

## Requirements

```powershell

- Python 3.7 or higherpip install -r requirements.txt

- See requirements.txt for all dependencies```



## Team Members### 2. Add Facial Images



- Member 1Organize your team members' images in the following structure:

- Member 2  

- Member 3```

- Member 4images/

  member_name/

## Assignment Due Date    neutral/

      image1.jpg

November 14, 2025    smiling/

      image2.jpg
    surprised/
      image3.jpg
```

**Requirements:**
- At least 3 images per member (one per expression)
- JPG or PNG format
- Clear facial visibility
- Consistent lighting conditions recommended

### 3. Train the Model

Open and run the Jupyter notebook:

```powershell
jupyter notebook facial_recognition.ipynb
```

Execute all cells to:
- Load and display images
- Apply augmentations
- Extract features
- Train models
- Evaluate performance
- Save trained models

### 4. Test the System

#### Command-Line Authentication

```powershell
# Authenticate a user
python face_recognition_system.py path/to/image.jpg

# With custom threshold
python face_recognition_system.py path/to/image.jpg --threshold 0.6

# Display result visually
python face_recognition_system.py path/to/image.jpg --display
```

#### Full System Demo

```powershell
python demo.py
```

## 🔬 Technical Details

### Feature Extraction

Each image is processed to extract **217 features**:
- **96 features**: Color histograms (32 bins × 3 channels)
- **15 features**: Statistical measures per channel
- **1 feature**: Edge density
- **100 features**: HOG descriptors
- **1 feature**: Texture variance
- **4 features**: Additional grayscale statistics

### Models Implemented

#### 1. Random Forest Classifier
- 100 decision trees
- Max depth: 10
- Ensemble learning approach
- Better handling of non-linear patterns

#### 2. Logistic Regression
- Multinomial classification
- L2 regularization
- Faster prediction time
- Interpretable coefficients

### Authentication Flow

```
1. User provides facial image
   ↓
2. Feature extraction (217 features)
   ↓
3. Feature scaling (StandardScaler)
   ↓
4. Model prediction + confidence score
   ↓
5. Threshold check (default: 50%)
   ↓
6. ✓ Authenticated OR ✗ Denied
```

## 📊 Model Performance

### Expected Metrics

After training with proper data, expect:

- **Accuracy**: 85-95% (depending on data quality)
- **F1-Score**: 85-95%
- **Cross-member distinction**: High (if images are diverse)

### Performance Factors

✅ **Positive Factors:**
- Good lighting in images
- Clear facial features
- Diverse expressions
- Multiple augmentations

⚠️ **Challenging Factors:**
- Similar facial features between members
- Poor image quality
- Inconsistent lighting
- Occlusions (glasses, masks)

## 🔌 Integration with Other Components

### Voice Verification Integration

```python
from face_recognition_system import FaceRecognitionSystem

# Step 1: Facial recognition
face_system = FaceRecognitionSystem()
authenticated, member = face_system.authenticate("user_image.jpg")

if authenticated:
    # Step 2: Proceed to voice verification
    voice_verified = voice_system.verify(member, "audio_sample.wav")
    
    if voice_verified:
        # Step 3: Product recommendation
        product = recommendation_system.predict(member)
```

### Product Recommendation Integration

```python
# After successful authentication
if authenticated and voice_verified:
    # Get user preferences from merged dataset
    user_features = get_user_features(member)
    
    # Predict product
    predicted_product = product_model.predict(user_features)
    
    print(f"Recommended product: {predicted_product}")
```

## 📝 Usage Examples

### Example 1: Basic Authentication

```python
from face_recognition_system import FaceRecognitionSystem

system = FaceRecognitionSystem()
result = system.recognize_face("test_image.jpg")

if result['recognized']:
    print(f"Welcome, {result['member']}!")
else:
    print("Access denied")
```

### Example 2: Custom Threshold

```python
# More strict authentication
result = system.recognize_face("test_image.jpg", threshold=0.75)

# More lenient authentication
result = system.recognize_face("test_image.jpg", threshold=0.4)
```

### Example 3: Detailed Results

```python
result = system.recognize_face("test_image.jpg")

print(f"Confidence: {result['confidence']:.2%}")
print("All probabilities:")
for member, prob in result['all_probabilities'].items():
    print(f"  {member}: {prob:.2%}")
```

## 🎥 Demonstration Checklist

For your assignment submission video, demonstrate:

- [ ] Image collection (show organized folder structure)
- [ ] Notebook execution (run through key cells)
- [ ] Augmentation examples (display visualizations)
- [ ] Feature extraction (show CSV file)
- [ ] Model training (show training process)
- [ ] Performance metrics (show evaluation results)
- [ ] Unauthorized attempt (show rejection)
- [ ] Authorized transaction (show full flow)
- [ ] Command-line usage (show CLI authentication)

## 🐛 Troubleshooting

### Issue: "Models not found"
**Solution:** Run the Jupyter notebook first to train and save models.

### Issue: "Could not load image"
**Solution:** Check image path and format (JPG/PNG). Use absolute paths.

### Issue: "Low accuracy"
**Solution:** 
- Ensure at least 3 images per member
- Check image quality and diversity
- Verify proper lighting conditions
- Add more augmentations

### Issue: "All predictions have low confidence"
**Solution:**
- Lower the confidence threshold
- Retrain with more diverse images
- Check if test images are similar to training images

## 📚 Key Files Description

| File | Purpose |
|------|---------|
| `facial_recognition.ipynb` | Main notebook for training and analysis |
| `face_recognition_system.py` | Production-ready Python module |
| `demo.py` | Full system demonstration script |
| `requirements.txt` | Python package dependencies |
| `image_features.csv` | Extracted features dataset |
| `*.pkl` files | Trained models and preprocessing objects |

## 🎓 Assignment Deliverables

This component contributes to:

1. **Report**: Document your approach, challenges, and results
2. **Video**: Record demonstration of facial recognition system
3. **GitHub**: Upload all code, notebooks, and documentation
4. **Data Files**: Include `image_features.csv` in repository

## 👥 Team Member Contributions

Document your specific contributions:

- Image collection and organization
- Feature engineering implementation
- Model training and evaluation
- System integration design
- Documentation and testing

## 📖 References & Resources

- **OpenCV Documentation**: https://docs.opencv.org/
- **Scikit-learn**: https://scikit-learn.org/stable/
- **HOG Features**: Dalal & Triggs (2005)
- **Random Forest**: Breiman (2001)

## 🔐 Security Considerations

- Threshold tuning balances security vs usability
- Multi-factor authentication (face + voice) increases security
- Store models securely in production
- Consider anti-spoofing measures (liveness detection)

## 🚀 Future Enhancements

Potential improvements for production:

- [ ] Deep learning models (CNN, FaceNet)
- [ ] Real-time webcam authentication
- [ ] Liveness detection (blink detection)
- [ ] Face detection preprocessing
- [ ] Multi-angle face capture
- [ ] Database integration for user management

## 📞 Support

For questions about this component:
1. Check the troubleshooting section
2. Review the Jupyter notebook comments
3. Consult assignment rubric and requirements

---

**Created for**: Formative 2 - Data Preprocessing Assignment  
**Component**: Part 2 - Facial Recognition System  
**Academic Year**: 2025
