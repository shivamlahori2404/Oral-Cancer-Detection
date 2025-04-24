import os
import shutil
from sklearn.model_selection import train_test_split

# Input and output paths
raw_dir = './raw_images'  # CHANGE this to the folder where your images currently are
output_dir = './oscc_dataset'

# Get all files
all_files = os.listdir(raw_dir)

# Classify based on prefix
normal_files = [f for f in all_files if f.startswith("Normal")]
malignant_files = [f for f in all_files if f.startswith("OSCC")]

# Split into train, val, test
def split_data(file_list):
    train, temp = train_test_split(file_list, test_size=0.3, random_state=42)
    val, test = train_test_split(temp, test_size=0.5, random_state=42)
    return train, val, test

train_norm, val_norm, test_norm = split_data(normal_files)
train_mal, val_mal, test_mal = split_data(malignant_files)

# Helper function to copy files
def copy_files(file_list, split_name, class_name):
    target_dir = os.path.join(output_dir, split_name, class_name)
    os.makedirs(target_dir, exist_ok=True)
    for file in file_list:
        shutil.copy(os.path.join(raw_dir, file), os.path.join(target_dir, file))

# Copy files
copy_files(train_norm, 'train', 'normal')
copy_files(val_norm, 'val', 'normal')
copy_files(test_norm, 'test', 'normal')

copy_files(train_mal, 'train', 'malignant')
copy_files(val_mal, 'val', 'malignant')
copy_files(test_mal, 'test', 'malignant')

print("✅ Dataset has been organized into train/val/test with malignant and normal folders.")

import os
import shutil
from sklearn.model_selection import train_test_split

# Input and output paths
raw_dir = './raw_images'  # CHANGE this to the folder where your images currently are
output_dir = './oscc_dataset'

# Get all files
all_files = os.listdir(raw_dir)

# Classify based on prefix
normal_files = [f for f in all_files if f.startswith("Normal")]
malignant_files = [f for f in all_files if f.startswith("OSCC")]

# Split into train, val, test
def split_data(file_list):
    train, temp = train_test_split(file_list, test_size=0.3, random_state=42)
    val, test = train_test_split(temp, test_size=0.5, random_state=42)
    return train, val, test

train_norm, val_norm, test_norm = split_data(normal_files)
train_mal, val_mal, test_mal = split_data(malignant_files)

# Helper function to copy files
def copy_files(file_list, split_name, class_name):
    target_dir = os.path.join(output_dir, split_name, class_name)
    os.makedirs(target_dir, exist_ok=True)
    for file in file_list:
        shutil.copy(os.path.join(raw_dir, file), os.path.join(target_dir, file))

# Copy files
copy_files(train_norm, 'train', 'normal')
copy_files(val_norm, 'val', 'normal')
copy_files(test_norm, 'test', 'normal')

copy_files(train_mal, 'train', 'malignant')
copy_files(val_mal, 'val', 'malignant')
copy_files(test_mal, 'test', 'malignant')

print("✅ Dataset has been organized into train/val/test with malignant and normal folders.")
