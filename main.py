import os 

# script to setup files for me so i don't have to create it manually everytime.

for i in range(2,101):
    if i < 10:
        filename = f"Day 0{i}"
        filenameSecond = f"day0{i}"
    else:
        filename = f"Day {i}"
        filenameSecond = f"day{i}"
    os.mkdir(f"{filename}")
    os.mkdir(f"./{filename}/Harry ({filename})")
    os.mkdir(f"./{filename}/tests")
    with open(f"./{filename}/Harry ({filename})/Tutorial.md","w") as f:
        pass
    with open(f"./{filename}/tests/{filenameSecond}_tests.py","w") as f:
        pass
    with open(f"./{filename}/{filenameSecond}_after.md","w") as f:
        pass
    with open(f"./{filename}/{filenameSecond}_extra_practice.py","w") as f:
        pass
    with open(f"./{filename}/{filenameSecond}_tasks.py","w") as f:
        pass
    with open(f"./{filename}/{filenameSecond}_tasks_answers.py","w") as f:
         pass
    with open(f"./{filename}/progress.json","w") as f:
        pass
    with open(f"./{filename}/{filenameSecond}_notes.docx","w") as f:
        pass
    print(f"{filename} is created.")
