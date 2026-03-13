import os

# Define dataset structure
dataset_path = "dataset"
train_path = os.path.join(dataset_path, "train")
val_path = os.path.join(dataset_path, "val")

vehicle_classes = [
    "Truck", "Tractor", "LCV", "Bus", 
    "Car", "3-wheeler", "E-rickshaw", "2-wheeler"
]

# Create dataset folders
for path in [train_path, val_path]:
    os.makedirs(path, exist_ok=True)
    for vehicle in vehicle_classes:
        os.makedirs(os.path.join(path, vehicle), exist_ok=True)

print("\n✅ Dataset folders created successfully!")
