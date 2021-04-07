import os

ROOT = os.path.dirname(__file__)
project_path = os.path.join(ROOT, "my_project")
new_templates_path = os.path.join(project_path, "templates")
os.makedirs(new_templates_path, exist_ok=True)
dir_paths = []
for root, dirs, files in os.walk(project_path):
    dir_paths.append(root)
for dir_path in dir_paths:
    dir_name = os.path.basename(dir_path)
    old_templ_patch = os.path.join(project_path, dir_name, "templates", dir_name)
    new_templ_patch = os.path.join(new_templates_path, dir_name)
    if os.path.exists(old_templ_patch) and not os.path.exists(new_templ_patch):
        os.rename(old_templ_patch, new_templ_patch)
        os.rmdir(os.path.join(project_path, dir_name, "templates"))
