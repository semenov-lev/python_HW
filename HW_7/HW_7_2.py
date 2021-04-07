import json
import os

ROOT = os.path.dirname(__file__)
with open("config.json", "r", encoding="utf-8") as f:
    f_dir = json.load(f)
for path_dir in f_dir:
    full_path_dir = os.path.join(ROOT, path_dir)
    os.makedirs(full_path_dir, exist_ok=True)
    for name_file in f_dir[path_dir]:
        file = os.path.join(full_path_dir, name_file)
        try:
            with open(file, 'x', encoding="utf-8"):
                print("Файл", name_file, "успешно создан.")
        except FileExistsError:
            print("Файл", name_file, "уже распогается в дирректории", full_path_dir)
