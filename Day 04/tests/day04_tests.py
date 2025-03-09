# you don't need to take a look at it newbie
import subprocess
import json 

points = 0

def run_user_code():
    try:
        result = subprocess.run(["python", "../day04_tasks.py"], capture_output=True, text=True)
        return result.stdout.split("\n") 
    except Exception as e:
        print("⚠️ Error running main.py:", e)
        return []

def test_task1(output):
    if(output[0].strip(" ")!=""):
        print("- Passed Task 01")
        global points
        points+=1
    else:
        print("Enter a valid name. Not an empty string.")
def test_task2(output):
    try:
        output[1] = float(output[1])
        print("- Passed Task 02")
        global points
        points+=1
    except:
        print("Enter a valid age in numbers like 20")

def test_task3(output):
    try:
        output[2] = float(output[2])
        print("- Passed Task 03")
        global points
        points+=1
    except:
        print("Enter a valid ID in numbers like 16121")

def test_task4(output):
    try:
        output[3] = float(output[3])
        print("- Passed Task 04")
        global points
        points+=1
    except:
        print("Enter a valid lucky number like 14 or 10")
output = run_user_code()
# print(output)
test_task1(output)
test_task2(output)
test_task3(output)
test_task4(output)

if(points==4):
    with open("../progress.json") as f:
        d = json.load(f)
    d["Day 04"] = "Completed"
    d["Points Taken"] = points
    with open("../progress.json","w") as f:
        json.dump(d,f,indent=4)