"""
Image Organization Helper Script
Helps you organize facial images for the recognition system
"""

import os
import shutil
from pathlib import Path


def create_directory_structure(base_dir='images', members=None):
    """
    Create the required directory structure for facial images.
    
    Args:
        base_dir: Base directory for images
        members: List of member names (default: member1, member2, member3)
    """
    if members is None:
        members = ['member1', 'member2', 'member3']
    
    expressions = ['neutral', 'smiling', 'surprised']
    
    print("Creating directory structure...")
    print(f"Base directory: {base_dir}\n")
    
    for member in members:
        for expression in expressions:
            path = os.path.join(base_dir, member, expression)
            os.makedirs(path, exist_ok=True)
            print(f"  ✓ Created: {path}")
    
    print(f"\n✅ Directory structure created successfully!")
    print(f"\nNext steps:")
    print(f"1. Add your facial images to the appropriate folders:")
    for member in members:
        print(f"   - {member}:")
        for expression in expressions:
            print(f"     • {os.path.join(base_dir, member, expression)}/")
    print(f"\n2. Name your images descriptively (e.g., photo1.jpg, photo2.jpg)")
    print(f"3. Ensure images are in JPG or PNG format")


def check_images(base_dir='images'):
    """
    Check if images are properly organized and count them.
    
    Args:
        base_dir: Base directory containing images
    """
    if not os.path.exists(base_dir):
        print(f"❌ Directory not found: {base_dir}")
        print(f"Run create_directory_structure() first!")
        return
    
    print("Checking image organization...\n")
    print("="*60)
    
    total_images = 0
    members_found = []
    issues = []
    
    for member in os.listdir(base_dir):
        member_path = os.path.join(base_dir, member)
        if not os.path.isdir(member_path):
            continue
        
        members_found.append(member)
        member_images = 0
        
        print(f"\n📁 {member}")
        print("-" * 60)
        
        for expression in ['neutral', 'smiling', 'surprised']:
            expression_path = os.path.join(member_path, expression)
            
            if not os.path.exists(expression_path):
                print(f"  ⚠  {expression}: Directory missing")
                issues.append(f"Missing directory: {expression_path}")
                continue
            
            # Count images
            images = [f for f in os.listdir(expression_path) 
                     if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            
            count = len(images)
            member_images += count
            total_images += count
            
            if count == 0:
                print(f"  ⚠  {expression}: No images (0)")
                issues.append(f"No images for {member}/{expression}")
            elif count < 3:
                print(f"  ⚠  {expression}: {count} images (recommended: ≥3)")
                issues.append(f"Few images for {member}/{expression}")
            else:
                print(f"  ✓  {expression}: {count} images")
        
        print(f"\n  Total for {member}: {member_images} images")
    
    # Summary
    print("\n" + "="*60)
    print(f"SUMMARY")
    print("="*60)
    print(f"Total members: {len(members_found)}")
    print(f"Total images: {total_images}")
    
    if total_images == 0:
        print("\n❌ No images found!")
        print("Please add images to the appropriate folders.")
    elif total_images < 9:  # 3 members × 3 expressions minimum
        print(f"\n⚠  Warning: Only {total_images} images found")
        print("Recommended: At least 9 images (3 per member, 1 per expression)")
    else:
        print(f"\n✅ Good! Found {total_images} images")
    
    if issues:
        print(f"\n⚠  Issues found ({len(issues)}):")
        for issue in issues:
            print(f"  • {issue}")
    else:
        print("\n✅ No issues found!")
    
    return {
        'total_images': total_images,
        'members': members_found,
        'issues': issues
    }


def validate_image_quality(base_dir='images'):
    """
    Validate image quality and provide recommendations.
    
    Args:
        base_dir: Base directory containing images
    """
    import cv2
    
    print("Validating image quality...\n")
    
    recommendations = []
    
    for member in os.listdir(base_dir):
        member_path = os.path.join(base_dir, member)
        if not os.path.isdir(member_path):
            continue
        
        for expression in os.listdir(member_path):
            expression_path = os.path.join(member_path, expression)
            if not os.path.isdir(expression_path):
                continue
            
            for img_file in os.listdir(expression_path):
                if not img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    continue
                
                img_path = os.path.join(expression_path, img_file)
                img = cv2.imread(img_path)
                
                if img is None:
                    print(f"❌ Could not read: {img_path}")
                    recommendations.append(f"Fix or replace: {img_path}")
                    continue
                
                height, width = img.shape[:2]
                
                # Check resolution
                if width < 100 or height < 100:
                    print(f"⚠  Low resolution: {img_path} ({width}x{height})")
                    recommendations.append(f"Replace with higher resolution: {img_path}")
                
                # Check aspect ratio
                aspect = width / height
                if aspect > 2 or aspect < 0.5:
                    print(f"⚠  Unusual aspect ratio: {img_path} ({aspect:.2f})")
                
                # Check if grayscale
                if len(img.shape) == 2:
                    print(f"ℹ  Grayscale image: {img_path}")
    
    if recommendations:
        print(f"\n📋 Recommendations:")
        for rec in recommendations:
            print(f"  • {rec}")
    else:
        print(f"\n✅ All images pass quality checks!")


def rename_images(base_dir='images', prefix_format="{member}_{expression}_{num}"):
    """
    Rename images to a consistent format.
    
    Args:
        base_dir: Base directory containing images
        prefix_format: Format string for renaming (uses member, expression, num)
    """
    print("Renaming images to consistent format...\n")
    
    renamed_count = 0
    
    for member in os.listdir(base_dir):
        member_path = os.path.join(base_dir, member)
        if not os.path.isdir(member_path):
            continue
        
        for expression in os.listdir(member_path):
            expression_path = os.path.join(member_path, expression)
            if not os.path.isdir(expression_path):
                continue
            
            images = [f for f in os.listdir(expression_path)
                     if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            
            for i, img_file in enumerate(images, 1):
                old_path = os.path.join(expression_path, img_file)
                ext = os.path.splitext(img_file)[1]
                
                new_name = prefix_format.format(
                    member=member,
                    expression=expression,
                    num=i
                ) + ext
                
                new_path = os.path.join(expression_path, new_name)
                
                if old_path != new_path:
                    os.rename(old_path, new_path)
                    print(f"  ✓ Renamed: {img_file} → {new_name}")
                    renamed_count += 1
    
    print(f"\n✅ Renamed {renamed_count} images")


def main_menu():
    """Interactive menu for image organization."""
    print("\n" + "="*60)
    print("  FACIAL RECOGNITION - IMAGE ORGANIZATION HELPER")
    print("="*60)
    
    while True:
        print("\nWhat would you like to do?")
        print("  1. Create directory structure")
        print("  2. Check images")
        print("  3. Validate image quality")
        print("  4. Rename images")
        print("  5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            member_names = input("\nEnter member names (comma-separated) or press Enter for default: ").strip()
            if member_names:
                members = [name.strip() for name in member_names.split(',')]
            else:
                members = None
            create_directory_structure(members=members)
        
        elif choice == '2':
            check_images()
        
        elif choice == '3':
            try:
                validate_image_quality()
            except ImportError:
                print("❌ OpenCV not installed. Install with: pip install opencv-python")
        
        elif choice == '4':
            rename_images()
        
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-5.")


if __name__ == '__main__':
    # Check if running interactively
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'create':
            create_directory_structure()
        elif command == 'check':
            check_images()
        elif command == 'validate':
            validate_image_quality()
        elif command == 'rename':
            rename_images()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: create, check, validate, rename")
    else:
        # Run interactive menu
        main_menu()
