import os
import zipfile
import toml
import csv
from datetime import datetime

class ShellEmulator:
    def __init__(self, config_file):
        config = toml.load(config_file)
        self.vfs_path = config['emulator']['vfs_path']
        self.log_file = config['emulator']['log_file']
        self.current_dir = "/"
        self.virtual_fs = {'/': {}}
        self.load_virtual_fs()

    def load_virtual_fs(self):

        if os.path.exists(self.vfs_path):
            with zipfile.ZipFile(self.vfs_path, 'r') as zip_ref:
                zip_ref.extractall("/tmp/vfs")
            self.virtual_root = "/tmp/vfs"
        else:
            print(f"VFS path {self.vfs_path} not found!")

    def log_action(self, action):

        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), action])

    def ls(self):

        path = os.path.join(self.virtual_root, self.current_dir.strip("/"))
        if os.path.exists(path):
            self.log_action("ls")
            return os.listdir(path)
        else:
            print("Directory not found")
            return []

    def cd(self, directory):

        if directory == "/":
            self.current_dir = "/"
            self.log_action("cd /")
            return

        new_dir = os.path.join(self.virtual_root, self.current_dir.strip("/"), directory)
        if os.path.isdir(new_dir):
            self.current_dir = f"{self.current_dir}/{directory}".strip("/")
            self.log_action(f"cd {directory}")
        else:
            raise ValueError(f"Directory {directory} does not exist")

    def mkdir(self, name):

        path = os.path.join(self.virtual_root, self.current_dir.strip("/"), name)
        os.makedirs(path, exist_ok=True)
        self.virtual_fs[self.current_dir][name] = {}
        self.log_action(f"mkdir {name}")

    def touch(self, filename):

        path = os.path.join(self.virtual_root, self.current_dir.strip("/"), filename)
        open(path, 'a').close()  # Создание файла
        self.log_action(f"touch {filename}")

    def cal(self):

        current_date = datetime.now().strftime("%B %Y")
        print(current_date)
        self.log_action("cal")

    def exit(self):

        self.log_action("exit")

        exit()
    def run(self):

        while True:
            command = input(f"{self.current_dir}> ").strip().split()
            if not command:
                continue
            cmd = command[0]
            args = command[1:]
            if cmd == "ls":
                print(self.ls())
            elif cmd == "cd":
                if args:
                    self.cd(args[0])
                else:
                    print("Usage: cd <directory>")
            elif cmd == "touch":
                if args:
                    self.touch(args[0])
                else:
                    print("Usage: touch <filename>")
            elif cmd == "cal":
                self.cal()
            elif cmd == "exit":
                self.exit()
            else:
                print(f"{cmd}: command not found")

if __name__ == "__main__":
    emulator = ShellEmulator("config.toml")
    emulator.run()
