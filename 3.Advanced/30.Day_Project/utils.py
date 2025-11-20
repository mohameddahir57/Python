import os, shutil
from datetime import datetime

def log(msg):
    with open("actions.log","a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def organize_files(folder):
    types = {
        "images": [".png",".jpg",".jpeg"],
        "pdf": [".pdf"],
        "excel": [".xlsx"],
        "csv": [".csv"],
    }
    for f in os.listdir(folder):
        path = os.path.join(folder,f)
        if os.path.isfile(path):
            moved=False
            for name,exts in types.items():
                if any(f.lower().endswith(e) for e in exts):
                    dest=os.path.join(folder,name)
                    os.makedirs(dest,exist_ok=True)
                    shutil.move(path, os.path.join(dest,f))
                    log(f"Moved {f} to {name}")
                    moved=True
                    break
            if not moved:
                dest=os.path.join(folder,"others")
                os.makedirs(dest,exist_ok=True)
                shutil.move(path, os.path.join(dest,f))
                log(f"Moved {f} to others")

def rename_files(folder,prefix):
    for f in os.listdir(folder):
        path=os.path.join(folder,f)
        if os.path.isfile(path):
            new=prefix+f
            shutil.move(path, os.path.join(folder,new))
            log(f"Renamed {f} to {new}")
