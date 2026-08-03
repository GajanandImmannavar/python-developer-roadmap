# 📚 Python Built-in Function — `print()`

> A complete beginner-friendly guide to Python's `print()` function with memory model, internal working, parameters, interview notes, and practice questions.

---

# 📖 Table of Contents

- [What is `print()`?](#what-is-print)
- [Why Do We Need `print()`?](#why-do-we-need-print)
- [Real-Life Analogy](#real-life-analogy)
- [Syntax](#syntax)
- [What Can `print()` Print?](#what-can-print-print)
- [Internal Working of `print()`](#internal-working-of-print)
- [Memory Model](#memory-model)
- [Important Concept](#important-concept)
- [Return Value of `print()`](#return-value-of-print)
- [Common Beginner Mistakes](#common-beginner-mistakes)
- [Interview Notes](#interview-notes)
- [Summary](#summary)
- [Memory Trick](#memory-trick)
- [Practice Questions](#practice-questions)
- [Thinking Challenge](#thinking-challenge)
- [What's Next?](#whats-next)

---

# What is `print()`?

`print()` is a **built-in function** in Python that displays data on the **screen (console)**.

Example:

```python
print("Hello")
```

Output

```text
Hello
```

---

# Why Do We Need `print()`?

Imagine writing a program.

```python
age = 22
```

The value **22** is stored in your computer's memory.

Can you see it?

❌ No.

It exists only inside memory.

To display it, use:

```python
print(age)
```

Output

```text
22
```

Think of `print()` as a **window into your program**.

Without it, Python can perform calculations, but you can't directly see the results.

---

# Real-Life Analogy

Imagine using a calculator.

You type:

```text
25 + 10
```

Internally, it calculates:

```text
35
```

But you only know the answer because it appears on the display.

`print()` works the same way.

```text
Memory
   │
   ▼
Python Computes
   │
   ▼
print()
   │
   ▼
Console Screen
```

---

# Syntax

```python
print(object)
```

or

```python
print(value)
```

Examples

```python
print(100)
print(25.5)
print("Python")
print(True)
```

---

# What Can `print()` Print?

Almost **every Python object** can be printed.

## Integer

```python
print(25)
```

Output

```text
25
```

---

## Float

```python
print(25.5)
```

Output

```text
25.5
```

---

## String

```python
print("Python")
```

Output

```text
Python
```

---

## Boolean

```python
print(True)
```

Output

```text
True
```

---

## List

```python
print([1, 2, 3])
```

Output

```text
[1, 2, 3]
```

---

## Tuple

```python
print((10, 20))
```

Output

```text
(10, 20)
```

---

## Dictionary

```python
print({"name": "Gajanand"})
```

Output

```text
{'name': 'Gajanand'}
```

---

## Set

```python
print({1, 2, 3})
```

Output

```text
{1, 2, 3}
```

---

## None

```python
print(None)
```

Output

```text
None
```

---

# Internal Working of `print()`

Consider:

```python
name = "Gajanand"

print(name)
```

Python internally performs these steps.

---

## Step 1 — Create the Object

```text
Memory

"Gajanand"
```

---

## Step 2 — Create the Variable

```text
name
 │
 ▼
"Gajanand"
```

The variable **does not store the string itself**.

It refers to the object.

---

## Step 3 — Execute `print(name)`

Python asks:

```text
What does 'name' refer to?
```

Answer:

```text
"Gajanand"
```

---

## Step 4 — Pass the Value

Python internally behaves like:

```python
print("Gajanand")
```

---

## Step 5 — Display the Value

```text
Console

↓

Gajanand
```

---

# Memory Model

Program

```python
name = "Python"
```

Memory

```text
name
 │
 ▼
"Python"
```

Now execute:

```python
print(name)
```

Python does **not** move or remove the object.

Instead, it simply:

1. Finds the object.
2. Reads the value.
3. Displays it.

Memory after printing

```text
name
 │
 ▼
"Python"
```

The object remains exactly where it was.

---

# Important Concept

Many beginners think:

```python
print(name)
```

means

> Move the value to the screen.

That is **not true**.

`print()` only **reads** the object.

It never modifies it.

Example

```python
name = "Python"

print(name)
print(name)
```

Output

```text
Python
Python
```

If `print()` removed the object, the second statement would fail.

It doesn't.

Therefore:

> `print()` never changes the object.

---

# Return Value of `print()`

Many beginners think:

```python
x = print("Hello")
```

stores `"Hello"` inside `x`.

It doesn't.

Example

```python
x = print("Hello")

print(x)
```

Output

```text
Hello
None
```

Why?

Because:

```python
print()
```

always returns

```python
None
```

---

# Common Beginner Mistakes

## ❌ Mistake 1

Replacing the built-in function.

```python
print = "Hello"
```

Later:

```python
print("Python")
```

Output

```text
TypeError
```

Never use:

```python
print
```

as a variable name.

---

## ❌ Mistake 2

Thinking `print()` changes a variable.

```python
x = 10

print(x)
```

After printing:

```python
x
```

is still

```text
10
```

---

## ❌ Mistake 3

Forgetting quotation marks.

Wrong

```python
print(Python)
```

Python thinks **Python** is a variable.

Correct

```python
print("Python")
```

---

## ❌ Mistake 4

Using commas incorrectly.

Wrong

```python
print("Age" 20)
```

Correct

```python
print("Age", 20)
```

---

# Interview Notes

### Is `print()` a keyword?

❌ No.

It is a **built-in function**.

---

### Does `print()` modify objects?

❌ Never.

---

### Where does `print()` display data?

On the **standard output (stdout)**, usually the terminal or console.

---

### Can `print()` print multiple values?

✅ Yes.

Example

```python
print("Python", 3.14, True)
```

Output

```text
Python 3.14 True
```

---

### Does `print()` always add a new line?

✅ Yes.

By default.

Later you'll learn how to change this using:

```python
end=
```

---

# Summary

| Question | Answer |
|-----------|--------|
| What is `print()`? | A built-in function |
| Purpose | Display data on the console |
| Does it modify variables? | ❌ No |
| Does it remove objects from memory? | ❌ No |
| Can it print different data types? | ✅ Yes |
| Return value | `None` |
| Is it a keyword? | ❌ No |

---

# 📚 Python Built-in Function — `print()`

> A complete beginner-friendly guide to Python's `print()` function with memory model, internal working, parameters, interview notes, and practice questions.

---

# 📖 Table of Contents

- [What is `print()`?](#what-is-print)
- [Why Do We Need `print()`?](#why-do-we-need-print)
- [Real-Life Analogy](#real-life-analogy)
- [Syntax](#syntax)
- [What Can `print()` Print?](#what-can-print-print)
- [Internal Working of `print()`](#internal-working-of-print)
- [Memory Model](#memory-model)
- [Important Concept](#important-concept)
- [Return Value of `print()`](#return-value-of-print)
- [Common Beginner Mistakes](#common-beginner-mistakes)
- [Interview Notes](#interview-notes)
- [Summary](#summary)
- [Memory Trick](#memory-trick)
- [Practice Questions](#practice-questions)
- [Thinking Challenge](#thinking-challenge)
- [What's Next?](#whats-next)

---

# What is `print()`?

`print()` is a **built-in function** in Python that displays data on the **screen (console)**.

Example:

```python
print("Hello")
```

Output

```text
Hello
```

---

# Why Do We Need `print()`?

Imagine writing a program.

```python
age = 22
```

The value **22** is stored in your computer's memory.

Can you see it?

❌ No.

It exists only inside memory.

To display it, use:

```python
print(age)
```

Output

```text
22
```

Think of `print()` as a **window into your program**.

Without it, Python can perform calculations, but you can't directly see the results.

---

# Real-Life Analogy

Imagine using a calculator.

You type:

```text
25 + 10
```

Internally, it calculates:

```text
35
```

But you only know the answer because it appears on the display.

`print()` works the same way.

```text
Memory
   │
   ▼
Python Computes
   │
   ▼
print()
   │
   ▼
Console Screen
```

---

# Syntax

```python
print(object)
```

or

```python
print(value)
```

Examples

```python
print(100)
print(25.5)
print("Python")
print(True)
```

---

# What Can `print()` Print?

Almost **every Python object** can be printed.

## Integer

```python
print(25)
```

Output

```text
25
```

---

## Float

```python
print(25.5)
```

Output

```text
25.5
```

---

## String

```python
print("Python")
```

Output

```text
Python
```

---

## Boolean

```python
print(True)
```

Output

```text
True
```

---

## List

```python
print([1, 2, 3])
```

Output

```text
[1, 2, 3]
```

---

## Tuple

```python
print((10, 20))
```

Output

```text
(10, 20)
```

---

## Dictionary

```python
print({"name": "Gajanand"})
```

Output

```text
{'name': 'Gajanand'}
```

---

## Set

```python
print({1, 2, 3})
```

Output

```text
{1, 2, 3}
```

---

## None

```python
print(None)
```

Output

```text
None
```

---

# Internal Working of `print()`

Consider:

```python
name = "Gajanand"

print(name)
```

Python internally performs these steps.

---

## Step 1 — Create the Object

```text
Memory

"Gajanand"
```

---

## Step 2 — Create the Variable

```text
name
 │
 ▼
"Gajanand"
```

The variable **does not store the string itself**.

It refers to the object.

---

## Step 3 — Execute `print(name)`

Python asks:

```text
What does 'name' refer to?
```

Answer:

```text
"Gajanand"
```

---

## Step 4 — Pass the Value

Python internally behaves like:

```python
print("Gajanand")
```

---

## Step 5 — Display the Value

```text
Console

↓

Gajanand
```

---

# Memory Model

Program

```python
name = "Python"
```

Memory

```text
name
 │
 ▼
"Python"
```

Now execute:

```python
print(name)
```

Python does **not** move or remove the object.

Instead, it simply:

1. Finds the object.
2. Reads the value.
3. Displays it.

Memory after printing

```text
name
 │
 ▼
"Python"
```

The object remains exactly where it was.

---

# Important Concept

Many beginners think:

```python
print(name)
```

means

> Move the value to the screen.

That is **not true**.

`print()` only **reads** the object.

It never modifies it.

Example

```python
name = "Python"

print(name)
print(name)
```

Output

```text
Python
Python
```

If `print()` removed the object, the second statement would fail.

It doesn't.

Therefore:

> `print()` never changes the object.

---

# Return Value of `print()`

Many beginners think:

```python
x = print("Hello")
```

stores `"Hello"` inside `x`.

It doesn't.

Example

```python
x = print("Hello")

print(x)
```

Output

```text
Hello
None
```

Why?

Because:

```python
print()
```

always returns

```python
None
```

---

# Common Beginner Mistakes

## ❌ Mistake 1

Replacing the built-in function.

```python
print = "Hello"
```

Later:

```python
print("Python")
```

Output

```text
TypeError
```

Never use:

```python
print
```

as a variable name.

---

## ❌ Mistake 2

Thinking `print()` changes a variable.

```python
x = 10

print(x)
```

After printing:

```python
x
```

is still

```text
10
```

---

## ❌ Mistake 3

Forgetting quotation marks.

Wrong

```python
print(Python)
```

Python thinks **Python** is a variable.

Correct

```python
print("Python")
```

---

## ❌ Mistake 4

Using commas incorrectly.

Wrong

```python
print("Age" 20)
```

Correct

```python
print("Age", 20)
```

---

# Interview Notes

### Is `print()` a keyword?

❌ No.

It is a **built-in function**.

---

### Does `print()` modify objects?

❌ Never.

---

### Where does `print()` display data?

On the **standard output (stdout)**, usually the terminal or console.

---

### Can `print()` print multiple values?

✅ Yes.

Example

```python
print("Python", 3.14, True)
```

Output

```text
Python 3.14 True
```

---

### Does `print()` always add a new line?

✅ Yes.

By default.

Later you'll learn how to change this using:

```python
end=
```

---

# Summary

| Question | Answer |
|-----------|--------|
| What is `print()`? | A built-in function |
| Purpose | Display data on the console |
| Does it modify variables? | ❌ No |
| Does it remove objects from memory? | ❌ No |
| Can it print different data types? | ✅ Yes |
| Return value | `None` |
| Is it a keyword? | ❌ No |

---

# Memory Trick

Think of `print()` as a **camera** 📷.

A camera doesn't change the person it photographs.

It only shows what it sees.

Likewise,

```text
Memory
   │
   ▼
print()
   │
   ▼
Console
```

`print()` only displays data.

It never changes the data.

---

# Practice Questions

## Level 1

Predict the output.

### Problem 1

```python
x = 100

print(x)
```

---

### Problem 2

```python
name = "Python"

print(name)

print(name)
```

---

### Problem 3

```python
age = 22

print(age)

age = 30

print(age)
```

---

## Level 2

### Problem 4

```python
language = "Python"

print(language)

language = "Java"

print(language)
```

---

### Problem 5

```python
number = 50

print(number)

number = number + 25

print(number)
```

---

### Problem 6

```python
print(True)

print(False)

print(None)
```

---

## Level 3

Without running Python, explain:

```python
city = "Bangalore"

print(city)

print(city)

print(city)
```

Answer these questions:

- What object is created?
- What does the variable refer to?
- What does `print()` receive?
- What is displayed?
- Does memory change after each `print()`?

---

# Thinking Challenge

Without running Python:

What is the output?

```python
x = print("Python")

print(x)
```

Explain **why**.

---

# What's Next?

Once you're comfortable with the basics of `print()`, the next lesson is:

## Parameters of `print()`

You'll learn about:

- `sep`
- `end`
- `file`
- `flush`

These features make `print()` much more powerful and are often overlooked, even by experienced Python developers.

---

# 🎯 Key Takeaways

- `print()` is a **built-in function**.
- It displays data on the console.
- It **reads** objects but never modifies them.
- It can print almost every Python object.
- It always returns `None`.
- By default, it prints each output on a new line.
- Avoid using `print` as a variable name.

---

## ⭐ If this guide helped you, consider giving the repository a star!# Memory Trick

Think of `print()` as a **camera** 📷.

A camera doesn't change the person it photographs.

It only shows what it sees.

Likewise,

```text
Memory
   │
   ▼
print()
   │
   ▼
Console
```

`print()` only displays data.

It never changes the data.

---

  # Practice Questions

## Level 1

Predict the output.

### Problem 1

```python
x = 100

print(x)
```

---

### Problem 2

```python
name = "Python"

print(name)

print(name)
```

---

### Problem 3

```python
age = 22

print(age)

age = 30

print(age)
```

---

## Level 2

### Problem 4

```python
language = "Python"

print(language)

language = "Java"

print(language)
```

---

### Problem 5

```python
number = 50

print(number)

number = number + 25

print(number)
```

---

### Problem 6

```python
print(True)

print(False)

print(None)
```

---

## Level 3

Without running Python, explain:

```python
city = "Bangalore"

print(city)

print(city)

print(city)
```

Answer these questions:

- What object is created?
- What does the variable refer to?
- What does `print()` receive?
- What is displayed?
- Does memory change after each `print()`?

---

# Thinking Challenge

Without running Python:

What is the output?

```python
x = print("Python")

print(x)
```

Explain **why**.

---

# What's Next?

Once you're comfortable with the basics of `print()`, the next lesson is:

## Parameters of `print()`

You'll learn about:

- `sep`
- `end`
- `file`
- `flush`

These features make `print()` much more powerful and are often overlooked, even by experienced Python developers.
   
---

# 🎯 Key Takeaways

- `print()` is a **built-in function**.
- It displays data on the console.
- It **reads** objects but never modifies them.
- It can print almost every Python object.
- It always returns `None`.
- By default, it prints each output on a new line.
- Avoid using `print` as a variable name.

---

## ⭐ If this guide helped you, consider giving the repository a star!


# 📚 Python Built-in Function — `input()`

> A complete beginner-friendly guide to Python's `input()` function with memory model, internal working, return type, type conversion, interview notes, and practice questions.

---

# 📖 Table of Contents

- [What is `input()`?](#what-is-input)
- [Why Do We Need `input()`?](#why-do-we-need-input)
- [Syntax](#syntax)
- [How `input()` Works](#how-input-works)
- [Internal Working](#internal-working)
- [Memory Model](#memory-model)
- [Why `input()` Always Returns a String](#why-input-always-returns-a-string)
- [Type Conversion](#type-conversion)
- [Common Beginner Mistakes](#common-beginner-mistakes)
- [Real-World Examples](#real-world-examples)
- [Interview Notes](#interview-notes)
- [Summary](#summary)
- [Memory Trick](#memory-trick)
- [Practice Questions](#practice-questions)
- [Thinking Challenge](#thinking-challenge)
- [What's Next?](#whats-next)

---

# What is `input()`?

`input()` is a **built-in function** that takes input from the user while the program is running.

Example

```python
name = input("Enter your name: ")
```

When the program runs:

```text
Enter your name:
```

Suppose the user types:

```text
Gajanand
```

Python stores:

```python
name = "Gajanand"
```

---

# Why Do We Need `input()`?

Without `input()`, every value must be written directly into the program.

Example

```python
age = 22
```

This program always uses **22**.

What if different users have different ages?

Using `input()`:

```python
age = input("Enter your age: ")
```

Now one user can enter:

```text
18
```

Another user:

```text
25
```

Another:

```text
40
```

The same program works for everyone without changing the code.

---

# Syntax

```python
variable = input("Message")
```

Example

```python
city = input("Enter your city: ")
```

---

# How `input()` Works

Imagine this code:

```python
name = input("Enter your name: ")
```

The sequence is:

```text
Program Starts
      │
      ▼
Display Message
      │
      ▼
Wait for User Input
      │
      ▼
User Types Something
      │
      ▼
Python Receives Text
      │
      ▼
Creates a String Object
      │
      ▼
Assigns It to the Variable
      │
      ▼
Program Continues
```

---

# Internal Working

Program

```python
name = input("Enter your name: ")
```

Python internally performs these steps.

---

## Step 1 — Display the Prompt

```text
Enter your name:
```

---

## Step 2 — Pause the Program

Python waits.

```text
Waiting...
```

The program does not continue until the user presses **Enter**.

---

## Step 3 — User Types

Suppose the user enters:

```text
Gajanand
```

---

## Step 4 — Python Receives the Input

Python reads exactly what the user typed.

```text
"Gajanand"
```

---

## Step 5 — Create a String Object

```text
Memory

"Gajanand"
```

---

## Step 6 — Assign It to the Variable

```text
name
 │
 ▼
"Gajanand"
```

The program now continues to the next line.

---

# Memory Model

Suppose the user enters:

```text
Python
```

Memory becomes:

```text
name
 │
 ▼
"Python"
```

`input()` simply creates a **new string object** and assigns it to the variable.

Nothing special happens.

---

# Why `input()` Always Returns a String

This is one of the most important Python concepts.

Example

```python
age = input("Enter age: ")
```

User enters:

```text
22
```

Memory

```text
age
 │
 ▼
"22"
```

Notice carefully.

It is **not**

```text
22
```

It is

```text
"22"
```

A **string**.

---

## Verify It

```python
age = input("Age: ")

print(type(age))
```

User enters:

```text
22
```

Output

```text
<class 'str'>
```

Always.

---

# Why Does `input()` Return a String?

Suppose you type:

```text
123
```

Should Python treat it as:

- Integer?
- Float?
- Phone Number?
- PIN?
- Roll Number?
- Employee ID?

Python cannot know your intention.

Instead of guessing, Python safely returns **everything as a string**.

Then **you** decide the required data type.

---

# Type Conversion

## Integer

```python
age = int(input("Enter age: "))
```

Now:

```python
print(type(age))
```

Output

```text
<class 'int'>
```

---

## Float

```python
salary = float(input("Salary: "))
```

Output type

```text
<class 'float'>
```

---

## Boolean

Python cannot directly convert user text like `"True"` or `"False"` into a boolean using `bool(input())` as most beginners expect.

We'll learn the correct way later.

---

# Common Beginner Mistakes

## ❌ Mistake 1

Trying to add a number to a string.

```python
age = input("Age: ")

print(age + 10)
```

User enters:

```text
20
```

Python sees:

```python
"20" + 10
```

Output

```text
TypeError
```

---

## ✅ Correct

```python
age = int(input("Age: "))

print(age + 10)
```

Output

```text
30
```

---

## ❌ Mistake 2

Forgetting to store the input.

Wrong

```python
input("Enter name: ")

print(name)
```

Output

```text
NameError
```

Correct

```python
name = input("Enter name:")

print(name)
```

---

## ❌ Mistake 3

Thinking `input()` automatically returns an integer.

Wrong

```python
number = input("Number: ")
```

`number` is still a string.

---

## ❌ Mistake 4

Using `int()` on non-numeric input.

```python
age = int(input("Age: "))
```

User enters

```text
Twenty
```

Output

```text
ValueError
```

---

# Real-World Examples

## ATM

```python
pin = input("Enter PIN: ")
```

---

## Login System

```python
username = input("Username: ")

password = input("Password: ")
```

---

## Shopping

```python
quantity = int(input("Quantity: "))
```

---

## Temperature

```python
temperature = float(input("Temperature: "))
```

---

## Online Form

```python
email = input("Email: ")
```

---

# Interview Notes

### Is `input()` a keyword?

❌ No.

It is a **built-in function**.

---

### Does `input()` pause the program?

✅ Yes.

Execution stops until the user presses **Enter**.

---

### What is the return type of `input()`?

Always

```python
str
```

---

### Can `input()` return an integer automatically?

❌ No.

You must convert it.

```python
int(input())
```

---

### Can `input()` return a float automatically?

❌ No.

You must convert it.

```python
float(input())
```

---

### What happens if `int()` receives invalid input?

Example

```python
int("Python")
```

Output

```text
ValueError
```

---

# Summary

| Question | Answer |
|-----------|--------|
| What is `input()`? | A built-in function |
| Purpose | Accept input from the user |
| Does it pause the program? | ✅ Yes |
| Default return type | `str` |
| Convert using | `int()`, `float()`, etc. |
| Does it create a new object? | ✅ Yes |

---

# Memory Trick

Think of `input()` as a **microphone** 🎤.

A microphone listens.

It doesn't decide what you meant.

Similarly,

```text
User
 │
 ▼
input()
 │
 ▼
String Object
 │
 ▼
Variable
```

`input()` simply captures what the user types and stores it as a **string**.

---

# Practice Questions

## Level 1

Predict the output and explain the memory.

### Problem 1

```python
name = input("Name: ")

print(name)

print(type(name))
```

---

### Problem 2

```python
age = int(input("Age: "))

print(age + 5)
```

User enters:

```text
20
```

---

### Problem 3

```python
city = input("City: ")

print(city)
```

User enters:

```text
Bangalore
```

---

## Level 2

### Problem 4

```python
num = input("Enter number: ")

print(num * 3)
```

User enters:

```text
5
```

What is the output?

(Hint: Remember `num` is a string.)

---

### Problem 5

```python
num = int(input("Enter number: "))

print(num * 3)
```

User enters:

```text
5
```

---

### Problem 6

```python
price = float(input("Price: "))

print(price)
print(type(price))
```

User enters:

```text
99.99
```

---

## Level 3

Without running Python, explain:

```python
name = input("Name: ")

print(name)

print(type(name))

print(name)
```

Answer these questions:

- What object is created?
- What does the variable refer to?
- What does `input()` return?
- What does `print()` receive?
- Does memory change after `print()`?

---

# Thinking Challenge

Without running Python:

```python
number = input("Enter number: ")

print(number + number)
```

User enters:

```text
10
```

What is the output?

Why?

---

## Bonus Challenge

Predict the output.

```python
age = int(input("Age: "))

print(age * 2)
```

User enters:

```text
18
```

---

# What's Next?

Now that you understand `input()`, the next lesson is:

## 📚 Type Conversion

You'll learn:

- `int()`
- `float()`
- `str()`
- `bool()`
- Implicit vs Explicit Type Conversion
- Common Conversion Errors
- Interview Questions

Understanding type conversion is essential because `input()` always returns a string.

---

# 🎯 Key Takeaways

- `input()` is a **built-in function**.
- It pauses the program until the user presses **Enter**.
- It **always returns a string (`str`)**.
- Python never guesses the intended data type.
- Use `int()`, `float()`, or other conversion functions when needed.
- `input()` creates a new string object in memory.
- Always validate or convert user input before performing calculations.

---

## ⭐ If this guide helped you, consider giving the repository a star!