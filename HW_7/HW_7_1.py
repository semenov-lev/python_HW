import os

ROOT = os.path.join(os.path.dirname(__file__))
names_of_files = ["mainapp", "adminapp", "authapp"]
for i in names_of_files:
    full_dir = os.path.join("my_projects", i)
    if not os.path.exists(os.path.join(ROOT, full_dir)):
        os.makedirs(os.path.join(ROOT, full_dir))
