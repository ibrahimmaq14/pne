# Pneumonia Detection Using CNN

Jupyter notebook and helper scripts for a chest X-ray pneumonia detection project.

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Dataset

The dataset is intentionally not committed to this repository. Download it with:

```bash
python download_dataset.py
```

If you keep the dataset somewhere other than `chest_xray/`, set `CHEST_XRAY_DIR` and run:

```bash
python update_paths.py
```

Then open `pneumonia-detection-using-cnn-92-6-accuracy.ipynb` in Jupyter.
