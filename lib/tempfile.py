import os
import string
import random
import shutil

def GenerateRandomName(length: int = 7):
    return ''.join(random.choices(string.ascii_letters, k=length))


class TemporaryDirectory:
    def __init__(self, dir="./"):
        assert isinstance(dir, str), f"Expected dir of type 'str', got {type(dir)}"
        directory_name = GenerateRandomName()
        print(f"directory_name: {directory_name}")
        self.abs_dir = os.path.abspath(dir + directory_name)
        print(self.abs_dir + "\\")
        if not os.path.exists(self.abs_dir + "\\"):
            os.mkdir(self.abs_dir)
            print("DEBUG: Directory created")
        else:
            print("DEBUG: Directory exists already")

    def cleanup(self):
        print(f"TemporaryFile\t<< {self.abs_dir} >> removed")
        shutil.rmtree(self.abs_dir)