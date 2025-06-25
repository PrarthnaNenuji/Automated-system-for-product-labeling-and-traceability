import os
from collections import defaultdict
import pandas as pd

# === CONFIG ===
LABELS_DIR = 'runs/detect/post_detect4/labels'
LABEL_MAP = {
    0: "Device ID",
    1: "Batch ID",
    2: "Manufacturing Date",
    3: "RoHS Compliance",
    4: "Serial Number"
}
REQUIRED_LABELS = set(LABEL_MAP.keys())

# === ANALYSIS ===
results = []

for file_name in sorted(os.listdir(LABELS_DIR)):
    if not file_name.endswith(".txt"):
        continue

    path = os.path.join(LABELS_DIR, file_name)
    with open(path, 'r') as f:
        lines = f.readlines()

    label_counts = defaultdict(int)
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        class_id = int(parts[0])
        label_counts[class_id] += 1

    present_labels = set(label_counts.keys())
    missing_labels = REQUIRED_LABELS - present_labels
    extra_labels = {LABEL_MAP[k]: v for k, v in label_counts.items() if v > 1}

    status = "✔ Complete label detected."
    if not present_labels:
        status = "❌ No label visible"
    elif missing_labels:
        status = f"❌ Missing: {', '.join(LABEL_MAP[i] for i in missing_labels)}"

    if extra_labels:
        status += f" | ⚠️ Duplicates: {', '.join([f'{k} x{v}' for k,v in extra_labels.items()])}"

    results.append({
        "Image": file_name.replace(".txt", ".jpg"),
        **{LABEL_MAP[i]: label_counts.get(i, 0) for i in LABEL_MAP},
        "Status": status
    })

# === EXPORT TO EXCEL ===
df = pd.DataFrame(results)
output_path = "label_detection_summary.xlsx"
df.to_excel(output_path, index=False)
print("\n✅ Analysis complete!")
print(f"📁 Excel saved to: {output_path}")
print("\n🖨️ Preview:")
print(df.head())
