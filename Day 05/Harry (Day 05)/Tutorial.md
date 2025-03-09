# Day 5 - Comments, Escape Sequences & Print in Python

Welcome to Day 5 of **#100DaysOfCode**! Today, we will explore **Comments**, **Escape Sequences**, and dive a bit deeper into the **`print`** statement in Python. Let's get started!

---

## Python Comments

Comments are an essential part of any programming language. They allow programmers to explain their code, make notes, or temporarily disable parts of the code without deleting them. Python supports both **single-line** and **multi-line** comments.

---

### Single-Line Comments

Single-line comments are created using the `#` symbol. Anything written after `#` on that line is ignored by the Python interpreter.

#### Example 1:
```python
# This is a 'Single-Line Comment'
print("This is a print statement.")
```
Output:
```
This is a print statement
```

#### Example 2:
```python
print("Hello World !!!") #Printing Hello World
```
Output
```
Hello World !!!
```

#### Example 3:
```python
print("Python Program")
#print("Python Program")
```
Output
```
Python Program
```

## Multi-Line Comments  

To write multi-line comments, you can use `#` at each line or use a multiline string.  

### Example 1: The use of `#`  

```python
# It will execute a block of code if a specified condition is true.
# If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
Output:
```
p is greater than 5.
```

### Example 2: The use of multi-line string
```python
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
Output:
```
p is greater than 5.
```

## Escape Sequence Characters  

To insert characters that cannot be directly used in a string, we use an escape sequence character.  

An escape sequence character is a backslash `\` followed by the character you want to insert.  

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:  

```python
# This will cause an error
print("This doesnt "execute")

# Correct way using an escape sequence
print("This will \"execute\"")
```

## More on Print Statement  

The syntax of a print statement looks something like this:  

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

## Other Parameters of Print Statement  

- **`object(s)`**: Any object, and as many as you like. Will be converted to a string before being printed.  
- **`sep='separator'`**: Specifies how to separate the objects if there is more than one. Default is `' '` (space).  
- **`end='end'`**: Specifies what to print at the end. Default is `'\n'` (line feed).  
- **`file`**: An object with a write method. Default is `sys.stdout`.  

**Note:** Parameters 2 to 4 are optional.  