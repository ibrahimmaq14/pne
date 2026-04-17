import json
import re
from pathlib import Path

filepath = Path(__file__).with_name('pneumonia-detection-using-cnn-92-6-accuracy.ipynb')

with filepath.open('r', encoding='utf-8') as f:
    notebook = json.load(f)

changed = False
for cell in notebook.get('cells', []):
    if cell.get('cell_type') == 'code':
        new_source = []
        for line in cell.get('source', []):
            orig_line = line
            line = re.sub(r'from keras\.models import', 'from tensorflow.keras.models import', line)
            line = re.sub(r'from keras\.layers import', 'from tensorflow.keras.layers import', line)
            line = re.sub(r'from keras\.preprocessing\.image import', 'from tensorflow.keras.preprocessing.image import', line)
            line = re.sub(r'from keras\.callbacks import', 'from tensorflow.keras.callbacks import', line)
            line = re.sub(r'^import keras', 'import tensorflow.keras as keras', line)
            new_source.append(line)
            if orig_line != line:
                changed = True
        cell['source'] = new_source

if changed:
    with filepath.open('w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    print("Notebook updated! Please RELOAD your browser page before running.")
else:
    print("No changes needed or lines not found.")
