import os

dirs = [x for x in os.listdir() if os.path.isdir(x)] + ["."]

print(dirs)

for el in dirs:
    os.chdir(el)
    saved_elements = {}
    for file in os.listdir():
        if not os.path.isdir(file):
            data = open(file, "rb").read()
            if hash(data) in saved_elements:
                os.system(f"del \"{file}\"")
                print(f"Deleted {file} at position {el}")
            else:
                saved_elements[hash(data)] = file
    os.chdir("..")
