# Facial Recognition System
## Part 2 - Formative Assessment

This project implements facial recognition for user authentication as part of a multimodal authentication system.

## Team Members
- 4 team members
- 3 images per member
- Total: 12 original images

## Project Structure
```
face_recognition/
├── images/              # Team member photos
├── models/              # Trained models
├── features/            # Extracted features
├── complete_facial_recognition.ipynb
├── requirements.txt
└── README.md
```

## Setup
```bash
pip install -r requirements.txt
```

## How to Run
1. Open `complete_facial_recognition.ipynb`
2. Run all cells in order
3. Models will be saved in `models/` folder

## Features
- Image augmentation (8 techniques)
- Feature extraction (217 features per image)
- Random Forest classifier
- Logistic Regression classifier
- Model evaluation and comparison
