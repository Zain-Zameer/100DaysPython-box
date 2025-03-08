# you don't need to take a look at it newbie
import subprocess

def run_user_code():
    try:
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
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
            print("Passed task 1")
def test_age(output):
    if(int(output[1])):
        print("- Passed Task 2.")

def test_reason(output):
    if(len(output[2]) < 5):
        print("- Enter a valid reason of learning python.")
    else:
        print("- Passed Task 3")

output = run_user_code()
print(output)
test_college_name(output)
test_age(output)
test_reason(output)