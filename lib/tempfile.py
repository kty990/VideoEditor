import os
import string
import random
import shutil

def GenerateRandomName(length: int = 7):
    return ''.join(random.choices(string.ascii_letters, k=length))

def CreateFile(name, absdir, subdir):
    try:
        newsubdir = f"{subdir}/"
        with open(f"{absdir}/{newsubdir if subdir != None else ''}{name}", 'x') as file:
            pass
    except:
        return False
    return True

class TemporaryDirectory:
    def __init__(self, dir="./"):
        assert isinstance(dir, str), f"Expected dir of type 'str', got {type(dir)}"
        directory_name = GenerateRandomName()
        self.abs_dir = os.path.abspath(dir + directory_name)
        if not os.path.exists(self.abs_dir + "\\"):
            os.mkdir(self.abs_dir)
            print("DEBUG: Directory created")
        else:
            print("DEBUG: Directory exists already")
        
        self.folder_name = directory_name

    def cleanup(self):
        print(f"\nTemporaryFolder\t<< {self.abs_dir} >> removed\n\t*All children also removed\n")
        # shutil.move(self.abs_dir, "C:\\$Recycle.Bin")
        # shutil.rmtree("C:\\$Recycle.Bin\\" + self.abs_dir)
        shutil.rmtree(self.abs_dir)

class NamedTemporaryFile:
    def __init__(self, suffix="", delete=True, dir="./", subdir: str=None):
        file_name = GenerateRandomName()
        self.suffix = suffix
        self.delete = delete
        self.abs_dir = os.path.abspath(dir)
        self.sub_dir = subdir
        CreateFile(file_name, self.abs_dir, subdir)
        self.name = file_name

        tmp = f"{self.sub_dir}\\"
        print(f"\nTemporaryFile\t<< {self.abs_dir}\\{tmp if self.sub_dir else ''}{file_name} >> created\n")

    def GetAbsDirectory(self):
        tmp = f"{self.sub_dir}\\"
        return f"{self.abs_dir}\\{tmp if self.sub_dir else ''}{self.name}"