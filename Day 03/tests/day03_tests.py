# you don't need to take a look at it newbie
import subprocess
import json 

points = 0

def run_user_code():
    try:
        result = subprocess.run(["python", "../day03_tasks.py"], capture_output=True, text=True)
        return result.stdout.strip().split("\n") 
    except Exception as e:
        print("⚠️ Error running main.py:", e)
        return []

def test_task1(output):
    if(output[0]=="pip install numpy"):
        global points
        points+=1
        print("- Passed Task 1")
    else:
        print("Check again what you have written, it's pattern should be equal to 'pip install pyxl'")
def test_task2(output):
    if(output[1]=="pip install doo-xl"):
        global points
        points+=1
        print("- Passed Task 2")
    else:
        print("Check again what you have written, it's pattern should be equal to 'pip install pyxl'")

output = run_user_code()
print(output)
test_task1(output)
test_task2(output)

if(points==2):
    with open("../progress.json") as f:
        d = json.load(f)
    d["Day 03"] = "Completed"
    d["Points Taken"] = points
    with open("../progress.json","w") as f:
        json.dump(d,f,indent=4)