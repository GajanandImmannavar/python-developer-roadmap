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

# 📚 Python Built-in Function — `type()`

> A complete beginner-friendly guide to Python's `type()` function with internal working, memory model, object-oriented concepts, interview notes, and practice questions.

---

# 📖 Table of Contents

- [What is `type()`?](#what-is-type)
- [Why Do We Need `type()`?](#why-do-we-need-type)
- [Syntax](#syntax)
- [How `type()` Works](#how-type-works)
- [Internal Working](#internal-working)
- [Memory Model](#memory-model)
- [Why Does It Return `<class 'int'>`?](#why-does-it-return-class-int)
- [Examples](#examples)
- [Real-World Analogy](#real-world-analogy)
- [Common Beginner Mistakes](#common-beginner-mistakes)
- [Interview Notes](#interview-notes)
- [Summary](#summary)
- [Memory Trick](#memory-trick)
- [Practice Questions](#practice-questions)
- [Thinking Challenge](#thinking-challenge)
- [What's Next?](#whats-next)

---

# What is `type()`?

`type()` is a **built-in function** that tells you the **data type (class)** of an object.

Think of it as Python answering the question:

> **"What kind of object is this?"**

Example

```python
print(type(10))
```

Output

```python
<class 'int'>
```

---

# Why Do We Need `type()`?

Sometimes we think we know the data type, but Python stores something different.

Example

```python
age = input("Enter age: ")
```

User enters:

```text
22
```

You might think:

```text
It is an integer.
```

Let's check.

```python
print(type(age))
```

Output

```python
<class 'str'>
```

Now you know the real type.

`type()` helps you understand what is actually stored in memory.

It is one of the best debugging tools for beginners.

---

# Syntax

```python
type(object)
```

or

```python
type(variable)
```

Examples

```python
print(type(10))
print(type(10.5))
print(type("Python"))
print(type(True))
```

---

# How `type()` Works

Suppose you write:

```python
x = 100

print(type(x))
```

The sequence is:

```text
Program Starts
      │
      ▼
Create Object
      │
      ▼
Variable Refers to Object
      │
      ▼
Call type(x)
      │
      ▼
Python Finds the Object
      │
      ▼
Checks Its Class
      │
      ▼
Returns the Class
      │
      ▼
print() Displays It
```

---

# Internal Working

Program

```python
x = 100

print(type(x))
```

Python internally performs these steps.

---

## Step 1 — Create the Object

```text
100
```

---

## Step 2 — Create the Variable

```text
x
 │
 ▼
100
```

The variable refers to the integer object.

---

## Step 3 — Execute `type(x)`

Python asks:

```text
What object does x refer to?
```

Answer

```text
100
```

---

## Step 4 — Inspect the Object

Python asks:

```text
Which class created this object?
```

Answer

```text
int
```

---

## Step 5 — Return the Class Object

Python returns

```python
<class 'int'>
```

---

## Step 6 — `print()` Displays It

Console

```text
<class 'int'>
```

---

# Memory Model

Program

```python
x = "Python"
```

Memory

```text
x
 │
 ▼
"Python"
```

Now execute

```python
type(x)
```

Python simply inspects the object.

It **does not**:

- Move the object
- Delete the object
- Modify the object

Memory remains

```text
x
 │
 ▼
"Python"
```

Then Python returns

```python
<class 'str'>
```

---

# Why Does It Return `<class 'int'>`?

Many beginners expect:

```python
int
```

Instead Python returns

```python
<class 'int'>
```

Why?

Because in Python,

> **Everything is an object.**

Even data types like:

- `int`
- `str`
- `list`
- `dict`
- `tuple`

are themselves objects called **classes**.

Example

Object

```python
10
```

was created by

```python
int
```

Therefore

```python
type(10)
```

returns

```python
<class 'int'>
```

---

# Examples

## Integer

```python
print(type(10))
```

Output

```python
<class 'int'>
```

---

## Float

```python
print(type(10.5))
```

Output

```python
<class 'float'>
```

---

## String

```python
print(type("Hello"))
```

Output

```python
<class 'str'>
```

---

## Boolean

```python
print(type(True))
```

Output

```python
<class 'bool'>
```

---

## List

```python
print(type([1, 2, 3]))
```

Output

```python
<class 'list'>
```

---

## Tuple

```python
print(type((10, 20)))
```

Output

```python
<class 'tuple'>
```

---

## Dictionary

```python
print(type({"name": "Gajanand"}))
```

Output

```python
<class 'dict'>
```

---

## Set

```python
print(type({1, 2, 3}))
```

Output

```python
<class 'set'>
```

---

## None

```python
print(type(None))
```

Output

```python
<class 'NoneType'>
```

---

# Real-World Analogy

Imagine a parking lot.

Vehicles arrive.

A security guard asks:

```text
What type of vehicle is this?
```

Possible answers:

```text
Car

Bike

Bus

Truck
```

The guard doesn't change the vehicle.

He simply identifies it.

`type()` works exactly the same way.

It identifies an object's type without modifying it.

---

# Common Beginner Mistakes

## ❌ Mistake 1

Thinking `type()` changes the object.

```python
x = 100

type(x)
```

No.

`x` is still

```text
100
```

---

## ❌ Mistake 2

Ignoring the return value.

```python
type(10)
```

In a Python script, nothing is displayed unless you use `print()`.

Correct

```python
print(type(10))
```

---

## ❌ Mistake 3

Confusing the value with its type.

```python
x = "100"
```

Many beginners think:

```text
Integer
```

Check it.

```python
print(type(x))
```

Output

```python
<class 'str'>
```

---

## ❌ Mistake 4

Thinking variables have types.

Actually,

Objects have types.

Variables only **refer** to objects.

Example

```python
x = 10

x = "Python"
```

The variable `x` did not change its type.

It simply started referring to a different object.

---

# Interview Notes

### Is `type()` a keyword?

❌ No.

It is a **built-in function**.

---

### Does `type()` modify objects?

❌ Never.

It only inspects them.

---

### What does `type()` return?

The object's **class**.

Example

```python
<class 'list'>
```

---

### Can `type()` be used with variables?

✅ Yes.

```python
type(x)
```

---

### Can `type()` be used directly with values?

✅ Yes.

```python
type(10)

type("Python")

type([1, 2, 3])
```

---

# Summary

| Question | Answer |
|-----------|--------|
| What does `type()` do? | Returns an object's data type (class) |
| Does it modify the object? | ❌ No |
| Does it return the value? | ❌ No |
| What does it return? | The object's class |
| Is it a built-in function? | ✅ Yes |

---

# Memory Trick

Think of `type()` as an **ID card checker**.

```text
Object
   │
   ▼
type()
   │
   ▼
"What are you?"
```

Examples

```text
10            → int

10.5          → float

"Python"      → str

True          → bool

[1,2,3]       → list

(1,2)         → tuple

{1,2,3}       → set

{"a":1}       → dict
```

`type()` only identifies the object.

It never changes it.

---

# Practice Questions

## Level 1

Predict the output.

### Problem 1

```python
x = 25

print(type(x))
```

---

### Problem 2

```python
name = "Gajanand"

print(type(name))
```

---

### Problem 3

```python
marks = 95.5

print(type(marks))
```

---

### Problem 4

```python
is_pass = True

print(type(is_pass))
```

---

### Problem 5

```python
data = [10, 20, 30]

print(type(data))
```

---

## Level 2

### Problem 6

```python
x = input("Enter a number: ")

print(type(x))
```

User enters

```text
50
```

---

### Problem 7

```python
x = int(input("Enter a number: "))

print(type(x))
```

User enters

```text
50
```

---

### Problem 8

```python
x = float(input("Enter a price: "))

print(type(x))
```

User enters

```text
99.99
```

---

## Level 3

Without running Python, explain:

```python
x = 100

print(type(x))

x = "Python"

print(type(x))
```

Answer these questions:

- What objects are created?
- What does the variable refer to at each step?
- What does `type()` inspect?
- What does `print()` receive?
- Does `type()` modify memory?

---

# Thinking Challenge

Without running Python:

```python
x = 10

y = type(x)

print(y)

print(type(y))
```

Can you explain **both outputs**?

---

# Bonus Challenge

Predict the output.

```python
print(type(type(10)))
```

Hint:

Remember,

> **Everything in Python is an object—including classes themselves.**

# 📚 Python Built-in Function — `id()`

> A complete beginner-friendly guide to Python's `id()` function with memory model, object identity, internal working, interview notes, and practice questions.

---

# 📖 Table of Contents

- [What is `id()`?](#what-is-id)
- [Why Do We Need `id()`?](#why-do-we-need-id)
- [Syntax](#syntax)
- [How `id()` Works](#how-id-works)
- [Internal Working](#internal-working)
- [Memory Model](#memory-model)
- [Why `is` Uses Object Identity](#why-is-uses-object-identity)
- [Relationship Between `print()`, `type()`, and `id()`](#relationship-between-print-type-and-id)
- [Real-World Analogy](#real-world-analogy)
- [Important Concepts](#important-concepts)
- [Common Beginner Mistakes](#common-beginner-mistakes)
- [Interview Notes](#interview-notes)
- [Summary](#summary)
- [Memory Trick](#memory-trick)
- [Practice Questions](#practice-questions)
- [Thinking Challenge](#thinking-challenge)
- [What's Next?](#whats-next)

---

# What is `id()`?

`id()` is a **built-in function** that returns the **identity** of an object.

In CPython (the standard Python implementation), this identity is typically the object's **memory address** during its lifetime.

Think of it as Python answering the question:

> **"Which exact object is this variable referring to?"**

---

# Syntax

```python
id(object)
```

Example

```python
x = 10

print(id(x))
```

Example Output

```text
140651574041832
```

⚠️ **Important**

Your number will almost certainly be different.

The actual value depends on your Python session and implementation.

---

# Why Do We Need `id()`?

Suppose we have:

```python
x = 10
y = 10
```

Question:

- Are `x` and `y` referring to the same object?
- Or two different objects?

Let's check.

```python
print(id(x))
print(id(y))
```

Possible Output

```text
140651574041832
140651574041832
```

Since both IDs are the same,

both variables refer to the **same object**.

---

# How `id()` Works

Suppose you write:

```python
x = 100

print(id(x))
```

The sequence is:

```text
Program Starts
      │
      ▼
Create Object
      │
      ▼
Variable Refers to Object
      │
      ▼
Call id(x)
      │
      ▼
Python Finds the Object
      │
      ▼
Reads the Object's Identity
      │
      ▼
Returns the Identity
      │
      ▼
print() Displays It
```

---

# Internal Working

Program

```python
x = 100
```

Python creates an integer object.

```text
100
```

Suppose (for explanation only) Python internally gives it ID

```text
2001
```

> Real IDs are much larger.

Memory

```text
x
 │
 ▼
100

ID = 2001
```

Now execute

```python
print(id(x))
```

Python internally performs these steps.

---

## Step 1 — Find the Variable

```text
x
```

---

## Step 2 — Find the Object

```text
100
```

---

## Step 3 — Read the Object's Identity

```text
ID = 2001
```

---

## Step 4 — Return the Identity

```python
2001
```

---

## Step 5 — `print()` Displays It

Console

```text
2001
```

Notice:

The object is **not modified**.

`id()` only inspects it.

---

# Memory Model

Program

```python
x = "Python"
```

Memory

```text
x
 │
 ▼
"Python"

ID = 5001
```

Now execute

```python
print(id(x))
```

Python prints

```text
5001
```

Memory after printing

```text
x
 │
 ▼
"Python"

ID = 5001
```

Nothing changes.

---

# Why `is` Uses Object Identity

Consider

```python
x = [1, 2]

y = x

print(x is y)
```

Output

```text
True
```

Why?

Because both variables refer to the **same object**.

Memory

```text
x
 │
 │
 ▼
[1, 2]
 ▲
 │
y
```

Suppose

```text
ID = 8001
```

Internally,

```python
x is y
```

checks whether both references point to the same object.

Conceptually, this is similar to comparing their identities.

Since both refer to the same object,

```text
True
```

---

## Example 1

```python
x = [1, 2]

y = x

print(id(x))
print(id(y))
```

Possible Output

```text
8001
8001
```

Same object.

Same identity.

---

## Example 2

```python
x = [1, 2]

y = [1, 2]
```

Memory

```text
x
 │
 ▼
[1, 2]

ID = 8001
```

```text
y
 │
 ▼
[1, 2]

ID = 9010
```

The values are equal.

The objects are different.

Therefore

```python
x == y
```

Output

```text
True
```

because their **values** are equal.

But

```python
x is y
```

Output

```text
False
```

because their **identities** are different.

---

# Relationship Between `print()`, `type()`, and `id()`

Suppose

```python
x = 10
```

Memory

```text
x
 │
 ▼
10
```

---

## `print(x)`

asks

```text
What is the VALUE?
```

Answer

```text
10
```

---

## `type(x)`

asks

```text
What is the TYPE?
```

Answer

```text
int
```

Output

```python
<class 'int'>
```

---

## `id(x)`

asks

```text
Which OBJECT is this?
```

Answer

```text
Its unique identity
```

---

# Real-World Analogy

Imagine a hostel.

There are two students named Rahul.

```text
Rahul
Rahul
```

How do you identify them?

Not by name.

By **room number**.

```text
Rahul

Room 201
```

```text
Rahul

Room 305
```

The room number is like `id()`.

The student's name is like the object's value.

---

# Important Concepts

## `id()` Does NOT Return the Value

Example

```python
x = 25

print(id(x))
```

Output

```text
140651574041832
```

Not

```text
25
```

---

## `id()` Does NOT Return the Type

Wrong expectation

```python
int
```

Correct

It returns the object's identity.

---

## `id()` Never Modifies an Object

It only reads information.

---

# Common Beginner Mistakes

## ❌ Mistake 1

Thinking

```python
id(x)
```

means

```text
Value of x
```

Wrong.

It means

```text
Identity of the object
```

---

## ❌ Mistake 2

Thinking two equal values always have different IDs.

Example

```python
x = 10

y = 10
```

Depending on Python's implementation, both variables may refer to the same object.

---

## ❌ Mistake 3

Comparing IDs manually.

Instead of

```python
id(x) == id(y)
```

simply use

```python
x is y
```

It is clearer and expresses your intent.

---

## ❌ Mistake 4

Assuming the same `id()` value in every program run.

Object identities can change between different executions of your program.

---

# Interview Notes

### Is `id()` a keyword?

❌ No.

It is a **built-in function**.

---

### What does `id()` return?

The object's **identity**.

In CPython, this is typically its memory address.

---

### Does `id()` modify objects?

❌ Never.

---

### Can two variables have the same `id()`?

✅ Yes.

If they refer to the **same object**.

---

### Can two equal objects have different IDs?

✅ Yes.

Example

```python
[1, 2]

[1, 2]
```

They have equal values but are different objects.

---

# Summary

| Function | Returns |
|-----------|---------|
| `print()` | Object's value |
| `type()` | Object's class |
| `id()` | Object's identity |

---

# Memory Trick

Whenever you see

```python
print(x)
```

Think

```text
Show the VALUE
```

---

Whenever you see

```python
type(x)
```

Think

```text
Show the TYPE
```

---

Whenever you see

```python
id(x)
```

Think

```text
Show the OBJECT'S IDENTITY
```

---

# Practice Questions

## Level 1

### Problem 1

```python
x = 100

print(id(x))
```

What does `id()` return?

---

### Problem 2

```python
x = [1, 2]

y = x

print(id(x))
print(id(y))
```

Will the IDs be the same or different?

Why?

---

### Problem 3

```python
x = [1, 2]

y = [1, 2]

print(id(x))
print(id(y))
```

Will the IDs be the same or different?

Why?

---

## Level 2

### Problem 4

```python
a = "Python"

b = a

print(a is b)
print(id(a))
print(id(b))
```

Explain the outputs.

---

### Problem 5

```python
a = (1, 2)

b = (1, 2)

print(a == b)
print(a is b)
```

Explain the difference between `==` and `is`.

---

### Problem 6

```python
x = 50

print(id(x))

x = 60

print(id(x))
```

Did the identity change?

Why?

---

## Level 3

Without running Python, explain:

```python
x = [10, 20]

y = x

z = [10, 20]

print(x == y)
print(x is y)

print(x == z)
print(x is z)
```

Answer these questions:

- Which variables refer to the same object?
- Which objects have the same values?
- Which IDs are the same?
- Which IDs are different?
- Why?

---

# Thinking Challenge

Without running Python:

```python
x = "Hello"

print(id(x))

x = x + " World"

print(id(x))
```

Questions:

- Is the second object the same as the first?
- Why does the identity change?
- What happened to the original string object?

---

# 🎯 Key Takeaways

- `id()` is a **built-in function**.
- It returns an object's **identity**.
- In CPython, the identity is typically the object's memory address.
- `id()` never modifies objects.
- `is` checks whether two references point to the same object.
- `==` compares values, while `is` compares object identity.
- The numeric value returned by `id()` can differ between program runs.

---

## ⭐ If this guide helped you, consider giving the repository a star!


# 📚 Python Built-in Function — `isinstance()`

> A complete beginner-friendly guide to Python's `isinstance()` function with internal working, memory model, inheritance support, interview notes, and practice questions.

---

# 📖 Table of Contents

- [What is `isinstance()`?](#what-is-isinstance)
- [Why Do We Need `isinstance()`?](#why-do-we-need-isinstance)
- [Syntax](#syntax)
- [How `isinstance()` Works](#how-isinstance-works)
- [Internal Working](#internal-working)
- [Memory Model](#memory-model)
- [Examples](#examples)
- [Comparing `type()` and `isinstance()`](#comparing-type-and-isinstance)
- [Professional Feature: Multiple Types](#professional-feature-multiple-types)
- [Inheritance Support](#inheritance-support)
- [Real-World Examples](#real-world-examples)
- [Common Beginner Mistakes](#common-beginner-mistakes)
- [Interview Notes](#interview-notes)
- [Summary](#summary)
- [Memory Trick](#memory-trick)
- [Practice Questions](#practice-questions)
- [Thinking Challenge](#thinking-challenge)
- [What's Next?](#whats-next)

---

# What is `isinstance()`?

`isinstance()` is a **built-in function** that checks whether an object belongs to a particular **class (data type)**.

Think of it as Python answering the question:

> **"Is this object an integer?"**

or

> **"Is this object a string?"**

It always returns:

- `True`
- `False`

---

# Why Do We Need `isinstance()`?

Suppose you're writing a calculator.

The user enters:

```python
x = "100"
```

Before performing calculations, you should know what type of data you're working with.

You check:

```python
print(isinstance(x, str))
```

Output

```text
True
```

Now you know the object is a string.

---

# Syntax

```python
isinstance(object, classinfo)
```

or

```python
isinstance(value, datatype)
```

Examples

```python
isinstance(10, int)
```

```python
isinstance("Python", str)
```

```python
isinstance([1, 2], list)
```

---

# How `isinstance()` Works

Suppose you write:

```python
x = 10

print(isinstance(x, int))
```

The sequence is:

```text
Program Starts
      │
      ▼
Create Object
      │
      ▼
Variable Refers to Object
      │
      ▼
Call isinstance(x, int)
      │
      ▼
Python Finds the Object
      │
      ▼
Checks Whether Object Belongs to int
      │
      ▼
Returns True
      │
      ▼
print() Displays It
```

---

# Internal Working

Program

```python
x = 10

print(isinstance(x, int))
```

Python internally performs these steps.

---

## Step 1 — Find the Variable

```text
x
```

---

## Step 2 — Find the Object

```text
10
```

---

## Step 3 — Check the Object's Class

Python asks:

```text
Was this object created by the int class?
```

Answer

```text
Yes
```

---

## Step 4 — Return the Result

```python
True
```

---

## Step 5 — `print()` Displays It

Console

```text
True
```

Nothing in memory changes.

---

# Memory Model

Program

```python
x = 10
```

Memory

```text
x
 │
 ▼
10
```

Now execute

```python
isinstance(x, int)
```

Python

```text
Reads the object
      │
      ▼
Checks its class
      │
      ▼
Returns True
```

Memory remains

```text
x
 │
 ▼
10
```

`isinstance()` only inspects the object.

It never modifies it.

---

# Examples

## Integer

```python
print(isinstance(10, int))
```

Output

```text
True
```

---

## Float

```python
print(isinstance(10.5, float))
```

Output

```text
True
```

---

## String

```python
print(isinstance("Python", str))
```

Output

```text
True
```

---

## Boolean

```python
print(isinstance(True, bool))
```

Output

```text
True
```

---

## List

```python
print(isinstance([1, 2, 3], list))
```

Output

```text
True
```

---

## Tuple

```python
print(isinstance((1, 2), tuple))
```

Output

```text
True
```

---

## Dictionary

```python
print(isinstance({"name": "AI"}, dict))
```

Output

```text
True
```

---

## Set

```python
print(isinstance({1, 2}, set))
```

Output

```text
True
```

---

## None

```python
print(isinstance(None, type(None)))
```

Output

```text
True
```

---

# Comparing `type()` and `isinstance()`

Many beginners confuse these two.

| `type()` | `isinstance()` |
|-----------|----------------|
| Returns the object's class | Returns `True` or `False` |
| Used to inspect | Used to check |
| Output: `<class 'int'>` | Output: `True` |

Example

```python
x = 10

print(type(x))
```

Output

```python
<class 'int'>
```

Now

```python
print(isinstance(x, int))
```

Output

```text
True
```

---

# Professional Feature: Multiple Types

You can check more than one type at the same time.

Example

```python
x = 10

print(isinstance(x, (int, float)))
```

Output

```text
True
```

Because `10` is an `int`, and `int` is one of the allowed types.

---

Another example

```python
name = "Python"

print(isinstance(name, (list, tuple, str)))
```

Output

```text
True
```

This feature is widely used in professional Python projects.

---

# Inheritance Support

One of the biggest advantages of `isinstance()` over `type()` is that it understands **inheritance**.

Example

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Output

```text
True
True
```

Even though `dog` is a `Dog`, it is also considered an `Animal`.

We'll study inheritance in detail when we learn Object-Oriented Programming (OOP).

---

# Real-World Examples

## Banking

```python
amount = 5000

if isinstance(amount, int):
    print("Valid amount")
```

Output

```text
Valid amount
```

---

## User Registration

```python
username = "Gajanand"

if isinstance(username, str):
    print("Valid username")
```

---

## Shopping Cart

```python
quantity = 5

if isinstance(quantity, int):
    print("Quantity accepted")
```

---

## API Validation

```python
price = 99.99

if isinstance(price, (int, float)):
    print("Valid price")
```

---

# Common Beginner Mistakes

## ❌ Mistake 1

```python
isinstance("10", int)
```

Output

```text
False
```

Because

```text
"10"
```

is a string.

Not an integer.

---

## ❌ Mistake 2

Thinking `isinstance()` converts data.

Wrong

```python
x = "100"

print(isinstance(x, int))
```

Output

```text
False
```

The value remains

```text
"100"
```

No conversion happens.

---

## ❌ Mistake 3

Passing a value instead of a class.

Wrong

```python
isinstance(10, 10)
```

Correct

```python
isinstance(10, int)
```

---

## ❌ Mistake 4

Using `type()` when inheritance matters.

In most object-oriented code,

```python
isinstance()
```

is usually the better choice.

---

# Interview Notes

### Is `isinstance()` a keyword?

❌ No.

It is a **built-in function**.

---

### What does `isinstance()` return?

Always

```python
True
```

or

```python
False
```

---

### Does `isinstance()` modify objects?

❌ Never.

---

### Can it check multiple types?

✅ Yes.

Example

```python
isinstance(x, (int, float))
```

---

### Why is `isinstance()` preferred over `type()` in OOP?

Because it supports **inheritance**.

---

# Summary

| Function | Returns |
|-----------|---------|
| `print()` | Displays value |
| `type()` | Object's class |
| `id()` | Object's identity |
| `isinstance()` | `True` or `False` depending on the object's type |

---

# Memory Trick

Think of `isinstance()` as a **security guard checking an ID card**.

Object

```text
10
```

Guard asks

```text
Are you an int?
```

Answer

```text
Yes

↓

True
```

---

Object

```text
"Python"
```

Guard asks

```text
Are you an int?
```

Answer

```text
No

↓

False
```

The guard only checks.

He doesn't change the person.

---

# Practice Questions

## Level 1

Predict the output.

### Problem 1

```python
x = 100

print(isinstance(x, int))
```

---

### Problem 2

```python
x = 100.5

print(isinstance(x, float))
```

---

### Problem 3

```python
x = "100"

print(isinstance(x, int))
```

---

### Problem 4

```python
x = [10, 20]

print(isinstance(x, tuple))
```

---

### Problem 5

```python
x = (1, 2, 3)

print(isinstance(x, (list, tuple)))
```

---

## Level 2

### Problem 6

```python
x = {"a": 1}

print(isinstance(x, dict))
```

---

### Problem 7

```python
x = {1, 2, 3}

print(isinstance(x, (list, set)))
```

---

### Problem 8

```python
x = None

print(isinstance(x, type(None)))
```

---

## Level 3

Without running Python, explain:

```python
value = 10

print(type(value))

print(isinstance(value, int))

print(isinstance(value, float))

print(isinstance(value, (int, float)))
```

Answer these questions:

- What object is created?
- What does `type()` return?
- What does each `isinstance()` call check?
- Which statements return `True`?
- Which statements return `False`?
- Why?

---

# Thinking Challenge

Without running Python:

```python
x = True

print(isinstance(x, bool))

print(isinstance(x, int))
```

Can you explain **both outputs**?

> **Hint:** In Python, `bool` is a subclass of `int`. This is one reason `isinstance()` understands inheritance.

---

# 📚 Python Built-in Function — `int()`

> A complete beginner-friendly guide to Python's `int()` function with internal working, memory model, type conversion rules, interview notes, and practice questions.

---

# 📖 Table of Contents

- [What is `int()`?](#what-is-int)
- [Why Do We Need `int()`?](#why-do-we-need-int)
- [Syntax](#syntax)
- [How `int()` Works](#how-int-works)
- [Internal Working](#internal-working)
- [Memory Model](#memory-model)
- [What Can `int()` Convert?](#what-can-int-convert)
- [Understanding Truncation](#understanding-truncation)
- [Base Conversion (Advanced)](#base-conversion-advanced)
- [Real-World Examples](#real-world-examples)
- [Common Beginner Mistakes](#common-beginner-mistakes)
- [Interview Notes](#interview-notes)
- [Summary](#summary)
- [Memory Trick](#memory-trick)
- [Practice Questions](#practice-questions)
- [Thinking Challenge](#thinking-challenge)
- [What's Next?](#whats-next)

---

# What is `int()`?

`int()` is a **built-in function** that converts a value into an **integer object**.

Think of it as Python answering the question:

> **"Can this value be converted into an integer?"**

If the conversion is possible,

Python creates and returns a **new integer object**.

If it is not possible,

Python raises an exception.

---

# Why Do We Need `int()`?

Remember,

```python
age = input("Enter your age: ")
```

If the user enters

```text
22
```

Python stores

```text
"22"
```

not

```text
22
```

Now,

```python
print(age + 5)
```

causes an error because

```text
"22" + 5
```

is invalid.

Correct approach

```python
age = int(input("Enter your age: "))

print(age + 5)
```

Output

```text
27
```

---

# Syntax

## Basic Syntax

```python
int(value)
```

Examples

```python
int("100")
```

```python
int(25.9)
```

```python
int(True)
```

---

## Optional Base Parameter

```python
int(string, base)
```

Example

```python
int("1010", 2)
```

Output

```text
10
```

We'll study number bases in more detail later.

---

# How `int()` Works

Suppose you write

```python
x = "100"

y = int(x)
```

The sequence is

```text
Program Starts
      │
      ▼
Find Object
      │
      ▼
Can It Become an Integer?
      │
      ▼
Yes
      │
      ▼
Create New Integer Object
      │
      ▼
Assign to y
```

---

# Internal Working

Program

```python
x = "100"

y = int(x)
```

Python internally performs these steps.

---

## Step 1 — Find the Object

```text
"100"
```

---

## Step 2 — Check Whether Conversion Is Possible

Python asks

```text
Can this string represent an integer?
```

Answer

```text
Yes
```

---

## Step 3 — Create a New Integer Object

```text
100
```

---

## Step 4 — Assign the New Object

Memory

```text
x ─────► "100"

y ─────► 100
```

Notice

The original string still exists.

Python creates a **new object**.

---

# Memory Model

Program

```python
x = "100"

y = int(x)
```

Before conversion

```text
x
 │
 ▼
"100"
```

After conversion

```text
x
 │
 ▼
"100"

y
 │
 ▼
100
```

The string object is **not modified**.

A new integer object is created.

---

# What Can `int()` Convert?

## ✅ Integer

```python
print(int(25))
```

Output

```text
25
```

Already an integer.

---

## ✅ String Containing Digits

```python
print(int("123"))
```

Output

```text
123
```

---

## ✅ Float

```python
print(int(15.9))
```

Output

```text
15
```

`int()` removes the decimal part.

It **does not round**.

---

## ✅ Negative Float

```python
print(int(-15.9))
```

Output

```text
-15
```

Notice

The decimal part is removed toward zero.

---

## ✅ Boolean

```python
print(int(True))
```

Output

```text
1
```

```python
print(int(False))
```

Output

```text
0
```

Internally

```text
True  = 1

False = 0
```

---

## ✅ String With Spaces

```python
print(int("   42   "))
```

Output

```text
42
```

Python ignores leading and trailing spaces.

---

## ❌ Invalid String

```python
int("Python")
```

Python asks

```text
Can "Python" become an integer?
```

Answer

```text
No
```

Error

```text
ValueError
```

---

## ❌ Mixed String

```python
int("12A")
```

Output

```text
ValueError
```

---

## ❌ Empty String

```python
int("")
```

Output

```text
ValueError
```

---

## ❌ None

```python
int(None)
```

Output

```text
TypeError
```

---

# Understanding Truncation

Many beginners think

```python
int(9.99)
```

becomes

```text
10
```

Wrong.

Output

```text
9
```

`int()` simply removes the decimal part.

More examples

```python
int(7.8)
```

Output

```text
7
```

---

```python
int(-7.8)
```

Output

```text
-7
```

Remember

> `int()` **truncates toward zero**.

---

# Base Conversion (Advanced)

`int()` can also convert numbers written in different bases.

Binary

```python
print(int("1010", 2))
```

Output

```text
10
```

---

Octal

```python
print(int("17", 8))
```

Output

```text
15
```

---

Hexadecimal

```python
print(int("FF", 16))
```

Output

```text
255
```

Don't worry if this feels new.

You'll study number systems in detail later.

---

# Real-World Examples

## User Age

```python
age = int(input("Enter your age: "))
```

---

## Number of Students

```python
students = int(input("How many students? "))
```

---

## ATM Withdrawal

```python
amount = int(input("Enter amount: "))
```

---

## DSA

Most coding platforms provide input as text.

```python
n = int(input())
```

---

## Menu Choice

```python
choice = int(input("Enter your choice: "))
```

---

# Common Beginner Mistakes

## ❌ Mistake 1

```python
int("10.5")
```

Output

```text
ValueError
```

Correct

```python
int(float("10.5"))
```

Output

```text
10
```

---

## ❌ Mistake 2

Thinking `int()` changes the original variable.

```python
x = "100"

int(x)
```

After this

```python
print(x)
```

Output

```text
100
```

But notice,

`x` is still a **string**.

To change the reference,

```python
x = int(x)
```

---

## ❌ Mistake 3

Thinking `int()` rounds numbers.

```python
int(9.99)
```

Output

```text
9
```

Not

```text
10
```

---

## ❌ Mistake 4

Passing an invalid string.

```python
int("ABC")
```

Output

```text
ValueError
```

---

## ❌ Mistake 5

Trying to convert a list.

```python
int([1, 2, 3])
```

Output

```text
TypeError
```

---

# Interview Notes

### Is `int()` a keyword?

❌ No.

It is a **built-in function**.

---

### Does `int()` modify the original object?

❌ No.

It creates a **new integer object**.

---

### Does `int()` round floating-point numbers?

❌ No.

It truncates toward zero.

---

### Why does `int("10.5")` fail?

Because `"10.5"` is a string representing a floating-point number, not an integer.

---

### Can `int()` convert booleans?

✅ Yes.

```python
True  → 1

False → 0
```

---

# Summary

| Input | Output |
|--------|--------|
| `int("25")` | `25` |
| `int(15.9)` | `15` |
| `int(-15.9)` | `-15` |
| `int(True)` | `1` |
| `int(False)` | `0` |
| `int("Python")` | ❌ `ValueError` |
| `int("12A")` | ❌ `ValueError` |
| `int(None)` | ❌ `TypeError` |

---

# Memory Trick

Think of `int()` as a **translator**.

```text
"100"
   │
   ▼
int()
   │
   ▼
100
```

If the translation is possible,

Python creates a **new integer object**.

If not,

Python says

```text
"I can't translate this."
```

and raises an exception.

---

# Practice Questions

## Level 1

Predict the output.

### Problem 1

```python
print(int("50"))
```

---

### Problem 2

```python
print(int(25.99))
```

---

### Problem 3

```python
print(int(True))
```

---

### Problem 4

```python
print(int(False))
```

---

### Problem 5

```python
x = "100"

y = int(x)

print(type(x))
print(type(y))
```

Explain

- What objects are created?
- What does `x` refer to?
- What does `y` refer to?
- Why are their types different?

---

## Level 2

### Problem 6

```python
print(int("   75   "))
```

---

### Problem 7

```python
print(int(-12.99))
```

---

### Problem 8

```python
print(int("1010", 2))
```

---

### Problem 9

```python
print(int("17", 8))
```

---

### Problem 10

```python
print(int("FF", 16))
```

---

## Level 3

Without running Python, explain:

```python
x = "250"

print(type(x))

y = int(x)

print(type(y))

print(id(x))

print(id(y))
```

Answer these questions:

- What objects are created?
- Does `int()` modify the original string?
- Why are the IDs different?
- Which object does `x` refer to?
- Which object does `y` refer to?

---

# Thinking Challenge

Without running Python:

```python
x = "10"

print(int(x) + int(x))
```

Why does this work, while

```python
print(x + x)
```

produces a completely different result?

Explain what happens in memory.

---

# 🎯 Key Takeaways

- `int()` is a **built-in function**.
- It converts compatible values into **integer objects**.
- It creates a **new object** instead of modifying the original.
- It truncates floating-point numbers toward zero.
- It can convert strings containing valid integers.
- It raises `ValueError` or `TypeError` when conversion is impossible.
- It is one of the most commonly used functions in Python programming.

---

## ⭐ If this guide helped you, consider giving the repository a star!