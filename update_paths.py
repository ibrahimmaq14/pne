import json
import os
from pathlib import Path

filepath = Path(__file__).with_name('pneumonia-detection-using-cnn-92-6-accuracy.ipynb')

with filepath.open('r', encoding='utf-8') as f:
    notebook = json.load(f)

new_base_path = os.environ.get("CHEST_XRAY_DIR", "chest_xray").replace("\\", "/")

changed = False
for cell in notebook.get('cells', []):
    if cell.get('cell_type') == 'code':
        new_source = []
        for line in cell.get('source', []):
            orig_line = line
            # Replace the old kaggle paths with the new local path
            for old_base in (
                '../input/chest-xray-pneumonia/chest_xray/chest_xray',
                'C:/Users/Admin/.cache/kagglehub/datasets/paultimothymooney/chest-xray-pneumonia/versions/2/chest_xray',
            ):
                line = line.replace(f'{old_base}/train', f'{new_base_path}/train')
                line = line.replace(f'{old_base}/test', f'{new_base_path}/test')
                line = line.replace(f'{old_base}/val', f'{new_base_path}/val')
            
            new_source.append(line)
            if orig_line != line:
                changed = True
        cell['source'] = new_source

if changed:
    with filepath.open('w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    print("Notebook paths successfully updated! Ready to run.")
else:
    print("No paths needed updating/already updated.")
