import os
import json

ROOT = os.path.dirname(__file__)
dir_name = "some_data"
data_path = os.path.join(ROOT, dir_name)

result = {0: [0, set()], 10: [0, set()], 100: [0, set()], 1000: [0, set()], 10000: [0, set()], 100000: [0, set()],
          1000000: [0, set()]}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000]
for root, dirs, files in os.walk(data_path):
    for f in files:
        size = os.stat(os.path.join(root, f)).st_size
        form = f.split(".")[-1]
        if size == 0:
            result[0][0] += 1
            result[0][1].add(form)
            continue
        for i, key in enumerate(keys):
            if i == len(keys) - 1:
                print(f"A very big file {f}")
                break
            if key < size <= keys[i + 1]:
                result[keys[i + 1]][0] += 1
                result[keys[i + 1]][1].add(form)
                break
result = {key: (value[0], list(value[1])) for key, value in result.items()}
with open(os.path.join(ROOT, f'{dir_name}_summary.json'), 'x', encoding='utf-8') as f_1:
    json.dump(result, f_1)
