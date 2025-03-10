import os
import shutil

# ✅ Debugging Start
print("✅ Import Layers Script Started")

# Define the layer directories in priority order
LAYER_PATHS = {
    "edge-ai-core": "modules/edge-ai-core",
    "layer2-3": "modules/layer2-3",
    "ghost-terminal": "modules/ghost-terminal",
    "entrepreneur": "modules/entrepreneur"
}

# Ensure directories exist
for layer, path in LAYER_PATHS.items():
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📂 Created missing directory: {path}")

# ✅ Step 1: Identify Existing and New Files
def list_files(directory):
    """List all files in a directory and subdirectories."""
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

existing_files = set(list_files("modules/"))
new_files = set(list_files("incoming_layers/"))  # Replace with actual source directory

# ✅ Step 2: Move Only New Files
for file in new_files:
    relative_path = os.path.relpath(file, "incoming_layers")  # Adjust path
    destination_path = os.path.join("modules", relative_path)

    if destination_path in existing_files:
        print(f"⚠️ Skipping duplicate file: {destination_path}")
    else:
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.move(file, destination_path)
        print(f"✅ Moved {file} → {destination_path}")

# ✅ Step 3: Verify Layer Integration
for layer, path in LAYER_PATHS.items():
    if os.path.exists(path) and len(os.listdir(path)) > 0:
        print(f"✅ {layer} successfully imported!")
    else:
        print(f"⚠️ {layer} is empty or missing files!")

# ✅ Debugging Complete
print("✅ Import Layers Script Completed")
