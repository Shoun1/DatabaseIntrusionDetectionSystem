import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torchvision.transforms as transforms
import torch

# -----------------------------
# Step 1: Simulated SQL Log
# -----------------------------
df = pd.DataFrame([
    {"query": "SELECT", "latency": 120, "priv": 0, "time": "02:00"},
    {"query": "DROP TABLE", "latency": 80, "priv": 1, "time": "03:00"},
    {"query": "INSERT", "latency": 300, "priv": 0, "time": "11:00"},
    {"query": "SELECT + SLEEP(5)", "latency": 5000, "priv": 1, "time": "01:00"},
    {"query": "SELECT", "latency": 100, "priv": 0, "time": "02:00"},
])

# -----------------------------
# Step 2: Heatmap Generation
# -----------------------------
heatmap_data = np.zeros((10, 10))
for i, row in df.iterrows():
    x = min(row["latency"] // 500, 9)
    y = row["priv"] * 5 + int(row["time"].split(":")[0]) % 5
    heatmap_data[int(x), int(y)] += 1

plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')
plt.axis('off')
plt.savefig("heatmap.png", bbox_inches='tight', pad_inches=0)
plt.close()

# -----------------------------
# Step 3: ViT-Ready Preprocessing
# -----------------------------
image = Image.open("heatmap.png").convert("RGB")
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)
])
input_tensor = transform(image).unsqueeze(0)  # Shape: [1, 3, 224, 224]

# -----------------------------
# Step 4: Placeholder for ViT Inference
# -----------------------------
# Replace with actual ViT model
print("ViT input tensor shape:", input_tensor.shape)
# model = load_vit_model()
# output = model(input_tensor)