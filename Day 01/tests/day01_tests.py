# you don't need to take a look at it newbie
import subprocess
import json 

points = 0

def run_user_code():
    try:
        result = subprocess.run(["python", "./day01_tasks.py"], capture_output=True, text=True)
        return result.stdout.strip().split("\n") 
    except Exception as e:
        print("⚠️ Error running main.py:", e)
        return []

def test_college_name(output):
    if(output[0] != "" or output[0] != " "):
        try:
            output[0] = int(output[0])
            print("- Input college name must be a string. for example: 'Stanford'")
        except:
            print("- Passed task 1")
            global points
            points+=1
def test_age(output):
    if(int(output[1])):
        global points
        points+=1
        print("- Passed Task 2")

def test_reason(output):
    if(len(output[2]) < 5):
        print("- Enter a valid reason of learning python.")
    else:
        global points
        points+=1
        print("- Passed Task 3")

output = run_user_code()
if(output[0]==''):
    print("Tasks are not completed.")
    exit()
test_college_name(output)
test_age(output)
test_reason(output)
if(points==3):
    with open("./progress.json") as f:
        d = json.load(f)
    d["Day 01"] = "Completed"
    d["Points Accomplished"] = points
    with open("./progress.json","w") as f:
        json.dump(d,f,indent=4)