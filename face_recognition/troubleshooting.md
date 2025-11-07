# Common Issues and Solutions

## Issue 1: ModuleNotFoundError for skimage
**Solution:** Install scikit-image
```bash
pip install scikit-image
```

## Issue 2: Images not loading
**Solution:** Make sure images are in the `images/` folder and are JPG or PNG format

## Issue 3: Feature extraction taking too long
**Solution:** Reduce image resize dimensions in extract_features() function

## Issue 4: Low model accuracy
**Possible causes:**
- Not enough training data
- Features not normalized
- Need more augmentation

## Issue 5: Memory error during training
**Solution:** Reduce number of features or use smaller batch size

## Tips
- Always run cells in order
- Check data shape before training
- Save models regularly
- Test on small dataset first
