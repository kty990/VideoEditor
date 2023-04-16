import os
import string
import random
import shutil

existing_temp_directories = []
existing_temp_files = []

def mass_cleanup():
    for x in existing_temp_directories:
        try:
            shutil.rmtree(x['abs_path'])
        except:
            pass
    
    for x in existing_temp_files:
        try:
            os.remove(x['abs_path'])
        except:
            pass

def GenerateRandomName(length: int = 7):
    return ''.join(random.choices(string.ascii_letters, k=length))

def CreateFile(name, absdir, subdir):
    try:
        newsubdir = f"{subdir}/"
        with open(f"{absdir}/{newsubdir if subdir != None else ''}{name}", 'x') as file:
            if not name.endswith(".wav"):
                print(f"File created at:\t\t{absdir}/{newsubdir if subdir != None else ''}{name}")
    except:
        return False
    return True

class TemporaryDirectory:
    def __init__(self, dir="./tmp_files/"):
        assert isinstance(dir, str), f"Expected dir of type 'str', got {type(dir)}"

        directory_name = GenerateRandomName()
        while directory_name in existing_temp_directories:
            directory_name = GenerateRandomName()
        
        
        self.abs_dir = os.path.abspath(dir + directory_name)

        existing_temp_directories.append({
            'name':directory_name,
            'abs_path':self.abs_dir
        })
        
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
    def __init__(self, suffix=".txt", delete=True, dir="./tmp_files/", subdir: str=None):
        file_name = GenerateRandomName()
        while file_name in existing_temp_files:
            file_name = GenerateRandomName()
       
        
        self.suffix = suffix
        self.delete = delete
        self.abs_dir = os.path.abspath(dir)
        
        existing_temp_files.append({
            'name': file_name,
            'abs_path':self.abs_dir
        })

        self.sub_dir = subdir
        CreateFile(file_name + suffix, self.abs_dir, subdir)
        self.name = file_name

        tmp = f"{self.sub_dir}\\"
        print(f"\nTemporaryFile\t<< {self.abs_dir}\\{tmp if self.sub_dir else ''}{file_name + suffix} >> created\n")

    def GetAbsDirectory(self):
        tmp = f"{self.sub_dir}\\"
        return f"{self.abs_dir}\\{tmp if self.sub_dir else ''}{self.name}"