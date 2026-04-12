import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
storage_file = os.path.join(BASE_DIR, "TextFolders", "Storage.txt")

with open(storage_file, "r") as f:
    lines = f.readlines()

scores = [int(line[9:12]) for line in lines[:5]]
name = [str(line[3:9]) for line in lines[:5]]
passw = [str(line[0:3]) for line in lines[:5]]

scores1 = "002"
scores2 = "033"
scores3 = "026"
scores4 = "101"
scores5 = "007"

names1 = "lew"
names2 = "sal"
names3 = "liv"
names4 = "bil"
names5 = "arc"

passw1 = "ztjtz6"
passw2 = "zdrhzd"
passw3 = "thrhtf"
passw4 = "64yse4"
passw5 = "5yezh#"

print(scores1, scores2, scores3, scores4, scores5)
print(names1, names2, names3, names4, names5)
print(passw1, passw2, passw3, passw4, passw5)