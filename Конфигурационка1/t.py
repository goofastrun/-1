import os

vfs_path = "filesystem1.zip"
if os.path.exists(vfs_path):
    print(f"File {vfs_path} exists!")
else:
    print(f"File {vfs_path} not found!")
