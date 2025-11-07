# Sample Images Guide

## How to Add Your Facial Images

### Image Requirements

Each team member needs to provide **3 facial images**:

1. **Neutral Expression**
   - No smile
   - Relaxed face
   - Looking straight at camera
   - Example: passport photo style

2. **Smiling Expression**
   - Natural smile
   - Teeth showing (optional)
   - Happy expression
   - Looking at camera

3. **Surprised Expression**
   - Eyes wide open
   - Mouth open
   - Eyebrows raised
   - Expressing surprise

### Image Specifications

- **Format**: JPG or PNG
- **Resolution**: Minimum 200x200 pixels (higher is better)
- **Quality**: Clear, not blurry
- **Lighting**: Good, even lighting
- **Background**: Any (consistent is better)
- **Face**: Should be clearly visible, no obstructions
- **Orientation**: Portrait (vertical) preferred

### Where to Place Images

```
face_recognition/images/
├── your_name/                    ← Replace with your actual name
│   ├── neutral/
│   │   └── photo1.jpg           ← Your neutral expression
│   ├── smiling/
│   │   └── photo2.jpg           ← Your smiling expression
│   └── surprised/
│       └── photo3.jpg           ← Your surprised expression
├── teammate2_name/
│   ├── neutral/
│   │   └── photo.jpg
│   ├── smiling/
│   │   └── photo.jpg
│   └── surprised/
│       └── photo.jpg
└── teammate3_name/
    ├── neutral/
    │   └── photo.jpg
    ├── smiling/
    │   └── photo.jpg
    └── surprised/
        └── photo.jpg
```

### Taking Good Photos

#### ✅ DO:
- Use natural lighting or good indoor lighting
- Look directly at the camera
- Keep face centered in frame
- Use consistent distance from camera
- Remove glasses if they cause glare
- Keep hair away from face

#### ❌ DON'T:
- Use very dark or very bright lighting
- Cover parts of your face
- Use low-quality/blurry images
- Tilt head at extreme angles
- Use heavily filtered or edited photos
- Include multiple people in one photo

### Quick Photo Tips

1. **Use Your Smartphone**
   - Front or back camera works
   - Make sure camera is clean
   - Use portrait mode if available

2. **Selfie Tips**
   - Hold phone at arm's length
   - Position at eye level
   - Use timer for steadier shots

3. **Ask Someone to Help**
   - Better for consistent angles
   - Easier to capture expressions
   - More natural-looking photos

### Testing Your Images

Before adding to the system, check:
- [ ] Face is clearly visible
- [ ] Image is not too dark or too bright
- [ ] File size is reasonable (< 5MB)
- [ ] Image opens correctly on your computer
- [ ] Expression matches the category

### File Naming (Optional)

The system will process any filename, but for organization:
- `yourname_neutral_1.jpg`
- `yourname_smiling_1.jpg`
- `yourname_surprised_1.jpg`

Or simply:
- `photo1.jpg`, `photo2.jpg`, etc.

### Multiple Images Per Expression

You can add multiple images per expression:
```
neutral/
  photo1.jpg
  photo2.jpg
  photo3.jpg
```

This gives better training data!

### Privacy Note

These images will be:
- Used only for this academic assignment
- Processed locally on your computer
- Not uploaded anywhere (unless you choose to share your GitHub repo)
- Should be images you're comfortable sharing with your team and instructor

### Need Help?

Run the image organizer script:
```powershell
python image_organizer.py
```

It will:
- Create the folder structure for you
- Check if your images are properly placed
- Validate image quality
- Help rename files if needed

---

## Example Directory After Adding Images

```
face_recognition/images/
├── Alice/
│   ├── neutral/
│   │   ├── alice_neutral_1.jpg
│   │   └── alice_neutral_2.jpg
│   ├── smiling/
│   │   └── alice_smile.jpg
│   └── surprised/
│       └── alice_surprised.jpg
├── Bob/
│   ├── neutral/
│   │   └── bob_1.jpg
│   ├── smiling/
│   │   └── bob_2.jpg
│   └── surprised/
│       └── bob_3.jpg
└── Carol/
    ├── neutral/
    │   └── neutral.jpg
    ├── smiling/
    │   └── smiling.jpg
    └── surprised/
        └── surprised.jpg
```

All ready for training! 🎓
