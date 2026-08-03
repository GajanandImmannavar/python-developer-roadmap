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


