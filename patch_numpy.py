import json
import re
from pathlib import Path

filepath = Path(__file__).with_name('pneumonia-detection-using-cnn-92-6-accuracy.ipynb')

with filepath.open('r', encoding='utf-8') as f:
    notebook = json.load(f)

changed = False
for i, cell in enumerate(notebook.get('cells', [])):
    if cell.get('cell_type') == 'code':
        new_source = []
        for line in cell.get('source', []):
            orig_line = line
            # replace return np.array(data) -> return np.array(data, dtype=object)
            if 'np.array(data)' in line:
                line = line.replace('np.array(data)', 'np.array(data, dtype=object)')
            
            # also check if there are other np.array calls that might cause issues?
            # like np.array(train) or np.array(x_train) etc that are lists of images.
            # Usually ragged lists only happen if images aren't same size, but they should be resized.
            # The class_num + image array in `data` is ragged.
            
            new_source.append(line)
            if orig_line != line:
                changed = True
        cell['source'] = new_source

if changed:
    with filepath.open('w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    print("Notebook updated! Replaced np.array(data) with np.array(data, dtype=object).")
else:
    print("No changes needed or lines not found.")
