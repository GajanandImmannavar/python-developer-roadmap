# 🐍 Python Operators

## 🎯 Goal

Learn how Python performs:

- Calculations
- Assignments
- Comparisons
- Logical decisions
- Object identity checks
- Membership checks
- Bitwise operations

---

# 🧠 How Python Uses Operators

Consider this expression:

```python
10 + 20
```

Python sees this conceptually as:

```text
Integer Object + Integer Object → New Integer Object
```

### Example

```text
10       +       20
↓                ↓
Integer Object   Integer Object
        ↓
    Addition
        ↓
   30
        ↓
New Integer Object
```

> **Important:** Operators work on **objects**, not directly on variables. Variables are names that help Python locate objects.

---

# 📚 Types of Operators

Python provides several types of operators:

1. ➕ Arithmetic Operators
2. 📝 Assignment Operators
3. ⚖️ Comparison Operators
4. 🧠 Logical Operators
5. 🆔 Identity Operators
6. 🔍 Membership Operators
7. ⚙️ Bitwise Operators

---

# 1️⃣ Arithmetic Operators

## 📖 Definition

An **operator** is a symbol that tells Python to perform an operation on one or more values or objects.

### Example

```python
5 + 3
```

Here:

```text
5 → Operand
+ → Operator
3 → Operand
```

The `+` symbol tells Python to perform **addition**.

---

## 🍎 Real-Life Example

```text
5 Apples + 3 Apples = 8 Apples
```

The `+` symbol tells us:

> "Add these two quantities."

Python operators work in a similar way.

```python
5 + 3
```

```text
5 + 3 → 8
```

---

# 🧮 Types of Arithmetic Operators

| Operator | Name | Purpose |
|---|---|---|
| `+` | Addition | Adds values |
| `-` | Subtraction | Subtracts one value from another |
| `*` | Multiplication | Multiplies values |
| `/` | Division | Divides values and returns a `float` |
| `//` | Floor Division | Divides and returns the floor value |
| `%` | Modulus | Returns the remainder |
| `**` | Exponentiation | Raises a value to a power |

---

# 🧠 Arithmetic Operators — Quick Overview

| Expression | Operation | Result |
|---|---|---|
| `10 + 3` | Addition | `13` |
| `10 - 3` | Subtraction | `7` |
| `10 * 3` | Multiplication | `30` |
| `10 / 3` | Division | `3.333...` |
| `10 // 3` | Floor Division | `3` |
| `10 % 3` | Remainder | `1` |
| `10 ** 3` | Exponentiation | `1000` |

---

> 🚀 **We'll learn each arithmetic operator in detail, one at a time.**

# 3️⃣ Addition (`+`)

## 📖 Definition

The addition operator (`+`) adds two numeric objects.

---

## 🧩 Syntax

```python
a + b
```

---

## 🧪 Example

```python
10 + 20
```

### Output

```text
30
```

---

## 🧠 Internal Working

Consider this code:

```python
x = 10
y = 20
z = x + y
```

Python performs the following steps:

### Step 1: Create the first integer object

```python
x = 10
```

```text
x ─► 10
```

`x` refers to the integer object `10`.

---

### Step 2: Create the second integer object

```python
y = 20
```

```text
x ─► 10
y ─► 20
```

`y` refers to the integer object `20`.

---

### Step 3: Perform the addition

```python
z = x + y
```

Python:

1. Finds the object referenced by `x` → `10`
2. Finds the object referenced by `y` → `20`
3. Performs the addition → `10 + 20`
4. Creates a **new integer object** → `30`
5. Makes `z` refer to the new object

```text
x ─► 10
y ─► 20
z ─► 30
```

> **Important:** The objects `10` and `20` are unchanged. Python creates a new object containing the result `30`.

---

## 🔄 Example 2: Integer + Float

```python
5 + 2.5
```

### Output

```text
7.5
```

### Result Type

```python
float
```

### Why?

Python performs **implicit type conversion**.

```text
int + float
   ↓
float + float
   ↓
result → float
```

Conceptually:

```text
5 → 5.0

5.0 + 2.5 = 7.5
```

---

# 4️⃣ Subtraction (`-`)

## 📖 Definition

The subtraction operator (`-`) subtracts the second object from the first object.

---

## 🧩 Syntax

```python
a - b
```

---

## 🧪 Example

```python
20 - 5
```

### Output

```text
15
```

Python creates a **new integer object** containing the result.

```text
20 - 5
 ↓
15
```

---

# 5️⃣ Multiplication (`*`)

## 📖 Definition

The multiplication operator (`*`) multiplies two numeric objects.

---

## 🧪 Example

```python
5 * 4
```

### Output

```text
20
```

Python creates a **new integer object** containing the result.

```text
5 × 4
 ↓
20
```

---

# 6️⃣ Division (`/`)

> ⭐ **Important Rule:** The `/` operator always returns a `float`.

---

## 🧪 Example

```python
10 / 2
```

### Output

```text
5.0
```

Even when the division is exact:

```python
8 / 4
```

The result is:

```text
2.0
```

---

## 🧠 Why Does `/` Return a Float?

Division can produce decimal values.

For example:

```python
10 / 3
```

```text
3.333333...
```

To keep the result type consistent, Python's `/` operator always returns a `float`.

### Quick Rule

```text
/ → Always returns float
```

---

# 7️⃣ Floor Division (`//`)

## 📖 Definition

Floor division (`//`) returns the result of division rounded **down toward negative infinity**.

---

## 🧪 Example

```python
10 // 3
```

Normal division:

```text
10 / 3 = 3.333...
```

Floor division:

```text
10 // 3 = 3
```

---

## 🧪 Example 2

```python
17 // 5
```

Normal division:

```text
17 / 5 = 3.4
```

Floor division:

```text
17 // 5 = 3
```

> ⚠️ **Important:** Floor division is not normal rounding. It moves toward negative infinity.

### Positive Example

```python
10 // 3
```

```text
3.333... → 3
```

### Negative Example

```python
-10 // 3
```

```text
-3.333... → -4
```

Because `-4` is the next lower integer.

---

# 8️⃣ Modulus (`%`)

## 📖 Definition

The modulus operator (`%`) returns the **remainder** after division.

---

## 🧪 Example

```python
10 % 3
```

The division can be represented as:

```text
10 = (3 × 3) + 1
```

Therefore:

```text
Remainder = 1
```

### Output

```text
1
```

---

## 🧪 Example 2

```python
20 % 5
```

```text
20 = (5 × 4) + 0
```

### Output

```text
0
```

There is no remainder.

---

## 🧠 The Modulus Formula

```text
Dividend = (Divisor × Quotient) + Remainder
```

Example:

```text
10 = (3 × 3) + 1
```

Therefore:

```text
10 % 3 = 1
```

---

## 🔥 Why Is `%` Important?

The modulus operator is heavily used in programming and DSA problems:

- ✅ Even and Odd Numbers
- 🔢 Extracting Digits
- 🔄 Circular Arrays
- 🔁 Cyclic Problems
- 🗂️ Hashing
- 📦 Distribution Problems

### Example: Even or Odd

```python
number = 10

print(number % 2)
```

Output:

```text
0
```

```text
number % 2 == 0 → Even
number % 2 != 0 → Odd
```

---

# 9️⃣ Exponentiation (`**`)

## 📖 Definition

The exponentiation operator (`**`) raises a number to the power of another number.

---

## 🧪 Example

```python
2 ** 3
```

This means:

```text
2 × 2 × 2
```

### Output

```text
8
```

---

## 🧪 Example 2

```python
5 ** 2
```

This means:

```text
5 × 5
```

### Output

```text
25
```

---

# 🧠 Arithmetic Operators — Final Revision

| Operator | Name | Main Purpose | Example | Result |
|---|---|---|---|---|
| `+` | Addition | Adds values | `10 + 3` | `13` |
| `-` | Subtraction | Subtracts values | `10 - 3` | `7` |
| `*` | Multiplication | Multiplies values | `10 * 3` | `30` |
| `/` | Division | Returns division result as `float` | `10 / 3` | `3.333...` |
| `//` | Floor Division | Returns floor quotient | `10 // 3` | `3` |
| `%` | Modulus | Returns remainder | `10 % 3` | `1` |
| `**` | Exponentiation | Raises to a power | `10 ** 3` | `1000` |

---

# 🔥 Three Important Rules

```text
/  → Always returns a float

// → Returns the floor value

%  → Returns the remainder
```

---

# ⭐ Remember

```text
Arithmetic Operators
        ↓
Perform Operations
        ↓
Create a Result
        ↓
Python Creates or Returns the Result Object
```

# 📌 Arithmetic Operators — Summary

## 🧮 Summary Table

| Operator | Name | Example | Output |
|:---:|---|:---:|:---:|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 3` | `2.0` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 4` | `16` |

---

# 🚫 Common Beginner Mistakes

## ❌ Mistake 1: Confusing `/` Result

Many beginners think:

```python
10 / 2
```

returns:

```text
5
```

❌ This is incorrect.

Python returns:

```text
5.0
```

### Rule

```text
/ → Always returns a float
```

---

## ❌ Mistake 2: Confusing `/` and `//`

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `/` | True Division | `7 / 2` | `3.5` |
| `//` | Floor Division | `7 // 2` | `3` |

---

## ❌ Mistake 3: Thinking `%` Returns the Quotient

The modulus operator (`%`) does **not** return the quotient.

It returns the:

```text
REMAINDER
```

Example:

```python
7 % 2
```

```text
7 = (2 × 3) + 1
```

Therefore:

```text
Remainder = 1
```

---

# 🎤 Interview Question

## Q: Why does `/` always return a float in Python?

### Answer

The `/` operator performs **true division**.

Python always returns a `float` because division can produce fractional values. Returning a consistent type avoids ambiguity.

```python
10 / 2 → 5.0
10 / 3 → 3.333...
```

---

# 🔢 Extracting the Last Digits Using `%`

## 🧠 The Pattern

```text
% 10     → Keep the last 1 digit

% 100    → Keep the last 2 digits

% 1000   → Keep the last 3 digits

% 10000  → Keep the last 4 digits
```

---

## 🧪 Examples

```python
583 % 10
```

Output:

```text
3
```

---

```python
583 % 100
```

Output:

```text
83
```

---

```python
583 % 1000
```

Output:

```text
583
```

---

## 🧠 Notice the Pattern

When the number after `%` is a power of `10`:

```text
10      → Last 1 digit
100     → Last 2 digits
1000    → Last 3 digits
10000   → Last 4 digits
```

---

# 🎯 Interview Tip

If an interviewer asks:

> **How do you extract the last `k` digits of a number?**

Use the formula:

```python
number % (10 ** k)
```

---

## 🧪 Examples

```python
number % 10
```

```text
Last 1 digit
```

---

```python
number % 100
```

```text
Last 2 digits
```

---

```python
number % 1000
```

```text
Last 3 digits
```

---

```python
number % 10000
```

```text
Last 4 digits
```

---

# 🧪 Example: Printing the Last Two Digits

```python
number = 987654

last_two_digits = number % 100

print(last_two_digits)
```

### Output

```text
54
```

---

# 🔪 Removing the Last Digits Using `//`

To remove the last digits of a number, use floor division (`//`).

---

## 🧪 Example

```python
number = 987654

left_number = number // 100

print(left_number)
```

### Output

```text
9876
```

---

# 🧠 Dry Run

## Step 1: Create the Number

```python
number = 987654
```

Python creates an integer object.

```text
number
   │
   ▼
987654
```

---

## Step 2: Perform Floor Division

```python
left_number = number // 100
```

Python performs:

```text
987654 // 100
```

Normal division:

```text
987654 ÷ 100 = 9876.54
```

Floor division:

```text
9876.54 → 9876
```

Therefore:

```text
left_number = 9876
```

Python creates a new integer object.

```text
number              left_number
   │                    │
   ▼                    ▼
987654                9876
```

---

## Step 3: Print the Result

```python
print(left_number)
```

### Output

```text
9876
```

---

# 📖 Theory: When Should You Use `//`?

Use `//` when the problem asks you to:

- 🔪 Remove digits
- ➗ Find the quotient
- 📦 Count complete groups
- 🧮 Perform integer division

---

# 🔪 Removing Digits Using `//`

## Remove the Last Digit

```text
987654
   ↓
Remove last digit
   ↓
98765
```

```python
987654 // 10
```

Result:

```text
98765
```

---

## Remove the Last Two Digits

```text
987654
   ↓
Remove last two digits
   ↓
9876
```

```python
987654 // 100
```

Result:

```text
9876
```

---

## Remove the Last Three Digits

```text
987654
   ↓
Remove last three digits
   ↓
987
```

```python
987654 // 1000
```

Result:

```text
987
```

---

# 🧠 Memory Trick

## Question Says: REMOVE

```text
REMOVE
   ↓
Use //
```

---

## Question Says: KEEP / EXTRACT

```text
KEEP / EXTRACT
      ↓
    Use %
```

---

# 🧪 Side-by-Side Example

## Keep the Last Two Digits

```python
number = 987654

last_two_digits = number % 100
```

```text
987654
   ↓
Keep last two digits
   ↓
54
```

```text
Use: %
```

---

## Remove the Last Two Digits

```python
number = 987654

remaining_number = number // 100
```

```text
987654
   ↓
Remove last two digits
   ↓
9876
```

```text
Use: //
```

---

# 🔥 The Most Important Pattern

| Problem Requirement | Operator | Formula |
|---|---|---|
| Keep last `k` digits | `%` | `number % (10 ** k)` |
| Remove last `k` digits | `//` | `number // (10 ** k)` |

---

# 📈 Complexity

Consider:

```python
last_two_digits = number % 100
```

This performs one arithmetic operation.

### ⏱️ Time Complexity

```text
O(1)
```

The operation takes constant time.

### 💾 Space Complexity

```text
O(1)
```

Only a constant amount of extra memory is used.

> **Important:** The number of digits does not change the basic operation's complexity.

---

# 🎯 Interview Questions

## Q1: How do you extract the last `k` digits?

### Formula

```python
number % (10 ** k)
```

### Example

```python
number % 10
```

Removes nothing and keeps the last digit.

```python
number % 100
```

Keeps the last two digits.

```python
number % 1000
```

Keeps the last three digits.

---

## Q2: How do you remove the last `k` digits?

### Formula

```python
number // (10 ** k)
```

### Examples

```python
number // 10
```

Removes the last digit.

---

```python
number // 100
```

Removes the last two digits.

---

```python
number // 1000
```

Removes the last three digits.

---

# 🏆 Final Revision

```text
KEEP / EXTRACT
      ↓
      %

REMOVE
      ↓
      //

Last k digits:
number % (10 ** k)

Remove last k digits:
number // (10 ** k)
```

> ⭐ This is one of the most important arithmetic patterns for number-based programming and DSA problems.

# 📝 Assignment Operators

Assignment operators are used to:

- Assign values to variables
- Update the values that variables refer to

---

# 1️⃣ What Is an Assignment Operator?

An **assignment operator** is used to assign a value to a variable or update the value that a variable refers to.

The simplest assignment operator is:

```python
=
```

---

## 🧪 Example

```python
x = 10
```

Python:

1. Creates an integer object `10`
2. Makes `x` refer to that object

```text
x
│
▼
10
```

> **Important:** The variable `x` is a name that refers to an object.

---

# 2️⃣ Why Do We Need Assignment Operators?

Consider:

```python
x = 10

x = x + 5
```

Python performs:

```text
10 + 5
↓
15
```

The final value of `x` is:

```text
15
```

Python provides a shorter way:

```python
x = 10

x += 5
```

Both produce the same final result:

```text
15
```

---

## ✨ Assignment Operators Make Code

- Shorter
- Easier to read
- Less repetitive

---

# 3️⃣ Types of Assignment Operators

| Operator | Meaning |
|---|---|
| `=` | Assign |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |
| `//=` | Floor divide and assign |
| `%=` | Modulus and assign |
| `**=` | Exponentiate and assign |

---

# 4️⃣ The `=` Operator

## 📖 Definition

The `=` operator assigns a value to a variable.

---

## 🧪 Example

```python
x = 10
```

### Memory

```text
x
│
▼
10
```

Now:

```python
x = 20
```

The reference changes:

```text
Old Object: 10

New Object: 20
```

```text
x
│
▼
20
```

> **Important:** The integer object `10` is not modified. The variable `x` now refers to a different object: `20`.

---

# 5️⃣ The `+=` Operator

## 📖 Definition

The `+=` operator adds a value to the current value of a variable and assigns the result back to that variable.

---

## 🧪 Example

```python
x = 10

x += 5
```

The final value is:

```text
15
```

---

## 🧠 Conceptually

```python
x += 5
```

is similar to:

```python
x = x + 5
```

---

## 🔍 Dry Run

### Step 1

```python
x = 10
```

```text
x
│
▼
10
```

---

### Step 2

```python
x += 5
```

Python:

1. Reads the object referenced by `x` → `10`
2. Performs:

```text
10 + 5
```

3. Creates the result:

```text
15
```

4. Makes `x` refer to the result

---

### Before

```text
x
│
▼
10
```

---

### After

```text
x
│
▼
15
```

> **Important:** The integer object `10` was never modified. The reference held by `x` now points to the result `15`.

---

# 6️⃣ The `-=` Operator

## 📖 Definition

The `-=` operator subtracts a value from the current value and assigns the result back to the variable.

---

## 🧪 Example

```python
x = 20

x -= 5
```

Conceptually:

```python
x = x - 5
```

Python performs:

```text
20 - 5
↓
15
```

### Final Value

```text
15
```

---

## 🔍 Dry Run

```text
Before:

x
│
▼
20
```

```text
x -= 5
```

```text
20 - 5
↓
15
```

```text
After:

x
│
▼
15
```

---

# 7️⃣ The `*=` Operator

## 📖 Definition

The `*=` operator multiplies the current value by another value and assigns the result back to the variable.

---

## 🧪 Example

```python
x = 5

x *= 4
```

Conceptually:

```python
x = x * 4
```

Python performs:

```text
5 × 4
↓
20
```

### Final Value

```text
20
```

---

## 🔍 Dry Run

```text
Before:

x
│
▼
5
```

```text
x *= 4
```

```text
5 × 4
↓
20
```

```text
After:

x
│
▼
20
```

---

# 8️⃣ The `/=` Operator

## 📖 Definition

The `/=` operator divides the current value by another value and assigns the result back to the variable.

---

## 🧪 Example

```python
x = 10

x /= 2
```

Conceptually:

```python
x = x / 2
```

Python performs:

```text
10 / 2
↓
5.0
```

### Final Value

```text
5.0
```

---

> ⚠️ **Important:** Just like normal `/` division, `/=` produces a `float`.

---

## 🧪 Example

```python
x = 8

x /= 4

print(x)
print(type(x))
```

### Output

```text
2.0
<class 'float'>
```

---

# 9️⃣ The `//=` Operator

## 📖 Definition

The `//=` operator performs floor division and assigns the result back to the variable.

---

## 🧪 Example

```python
x = 17

x //= 5
```

Conceptually:

```python
x = x // 5
```

Python performs:

```text
17 // 5
↓
3
```

### Final Value

```text
3
```

---

## 🔍 Dry Run

```text
Before:

x
│
▼
17
```

```text
x //= 5
```

```text
17 // 5
↓
3
```

```text
After:

x
│
▼
3
```

---

# 🔟 The `%=` Operator

## 📖 Definition

The `%=` operator calculates the remainder and assigns the result back to the variable.

---

## 🧪 Example

```python
x = 17

x %= 5
```

Conceptually:

```python
x = x % 5
```

Python performs:

```text
17 % 5
↓
2
```

### Final Value

```text
2
```

---

## 🔍 Dry Run

```text
Before:

x
│
▼
17
```

```python
x %= 5
```

```text
17 % 5
↓
2
```

```text
After:

x
│
▼
2
```

---

# 1️⃣1️⃣ The `**=` Operator

## 📖 Definition

The `**=` operator raises the current value to a power and assigns the result back to the variable.

---

## 🧪 Example

```python
x = 2

x **= 3
```

Conceptually:

```python
x = x ** 3
```

Python performs:

```text
2³
↓
8
```

### Final Value

```text
8
```

---

## 🔍 Dry Run

```text
Before:

x
│
▼
2
```

```python
x **= 3
```

```text
2 ** 3
↓
8
```

```text
After:

x
│
▼
8
```

---

# 🧮 Assignment Operator Formula

Every compound assignment operator follows this pattern:

```text
variable operator= value
```

Conceptually:

```text
variable = variable operator value
```

---

# 📊 Short Form and Long Form

| Short Form | Long Form |
|---|---|
| `x += 5` | `x = x + 5` |
| `x -= 5` | `x = x - 5` |
| `x *= 5` | `x = x * 5` |
| `x /= 5` | `x = x / 5` |
| `x //= 5` | `x = x // 5` |
| `x %= 5` | `x = x % 5` |
| `x **= 5` | `x = x ** 5` |

---

# 🧠 Complete Dry Run

Consider:

```python
x = 10

x += 5
x *= 2
x -= 4
x //= 2
x %= 5
```

Let's execute step by step.

---

## Step 1

```python
x = 10
```

```text
x = 10
```

---

## Step 2

```python
x += 5
```

Same as:

```python
x = x + 5
```

```text
10 + 5
↓
15
```

Now:

```text
x = 15
```

---

## Step 3

```python
x *= 2
```

Same as:

```python
x = x * 2
```

```text
15 × 2
↓
30
```

Now:

```text
x = 30
```

---

## Step 4

```python
x -= 4
```

Same as:

```python
x = x - 4
```

```text
30 - 4
↓
26
```

Now:

```text
x = 26
```

---

## Step 5

```python
x //= 2
```

Same as:

```python
x = x // 2
```

```text
26 // 2
↓
13
```

Now:

```text
x = 13
```

---

## Step 6

```python
x %= 5
```

Same as:

```python
x = x % 5
```

```text
13 % 5
↓
3
```

### Final Value

```text
x = 3
```

---

# 🧠 Important Connection With Arithmetic Operators

Assignment operators combine:

```text
Arithmetic Operator
```

with:

```text
Assignment Operator
```

For example:

```python
x += 5
```

contains:

```text
+  → Arithmetic operation
=  → Assignment
```

Together:

```text
Add
↓
Assign the result
```

---

# 🔗 Assignment Operator Process

For:

```python
x += 5
```

Think:

```text
Read current value
        ↓
Perform arithmetic operation
        ↓
Create the result
        ↓
Assign result back to x
```

---

# 📖 Example

```python
x = 10

x += 5
```

Conceptually:

```text
Read x
 ↓
10

Perform:
10 + 5
 ↓
15

Assign:
x = 15
```

---

# ⚠️ Important: `/=` Changes the Type

Consider:

```python
x = 10

x /= 2
```

Before:

```text
x → 10
```

Type:

```text
int
```

After:

```text
x → 5.0
```

Type:

```text
float
```

Therefore:

```python
x /= 2
```

can change the type of the value stored in `x`.

---

# ⚠️ Important: `//=` and `%=` Have Different Jobs

Consider:

```python
x = 17
```

### Floor Division Assignment

```python
x //= 5
```

Result:

```text
3
```

It keeps the quotient.

---

### Modulus Assignment

```python
x %= 5
```

Result:

```text
2
```

It keeps the remainder.

---

# 🧠 Memory Trick

```text
+= → Add
```

```text
-= → Subtract
```

```text
*= → Multiply
```

```text
/= → Divide
```

```text
//= → Floor Divide
```

```text
%= → Keep Remainder
```

```text
**= → Raise to Power
```

---

# 🎯 Interview Question

## Q: What is the difference between `=` and `==`?

### Answer

```text
=  → Assignment
```

It assigns a value:

```python
x = 10
```

---

```text
== → Comparison
```

It compares two values:

```python
x == 10
```

The result is:

```text
True
```

or:

```text
False
```

---

# 🎯 Interview Question

## Q: What is the difference between `x += 5` and `x = x + 5`?

For immutable numeric values, both produce the same final value.

```python
x += 5
```

is the shorter form of:

```python
x = x + 5
```

Conceptually, Python:

1. Reads the current value
2. Performs the arithmetic operation
3. Produces the result
4. Assigns the result back to the variable

---

# 📌 Complete Assignment Operator Summary

| Operator | Name | Example | Equivalent Form |
|---|---|---|---|
| `=` | Assignment | `x = 10` | Assign value |
| `+=` | Add and assign | `x += 5` | `x = x + 5` |
| `-=` | Subtract and assign | `x -= 5` | `x = x - 5` |
| `*=` | Multiply and assign | `x *= 5` | `x = x * 5` |
| `/=` | Divide and assign | `x /= 5` | `x = x / 5` |
| `//=` | Floor divide and assign | `x //= 5` | `x = x // 5` |
| `%=` | Modulus and assign | `x %= 5` | `x = x % 5` |
| `**=` | Exponentiate and assign | `x **= 5` | `x = x ** 5` |

---

# 🏆 Final Mental Model

```text
Assignment Operator
        ↓
Perform an operation
        ↓
Assign the result back
```

For example:

```python
x += 5
```

means:

```text
Take x
  ↓
Add 5
  ↓
Get result
  ↓
Store result back in x
```

---

# ⚖️ Comparison Operators

Comparison operators are used to compare two values or objects.

After comparing them, Python returns one of two Boolean values:

```text
True
```

or

```text
False
```

---

# 1️⃣ Why Do We Need Comparison Operators?

Comparison operators help Python answer questions such as:

- Is the age greater than `18`?
- Is the password correct?
- Are two numbers equal?
- Does the user have enough balance?
- Did the student pass?

Computers often need to make decisions.

```text
Yes → True

No  → False
```

Comparison operators help Python answer these questions.

---

# 2️⃣ Types of Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

# 3️⃣ The `==` Operator — Equal To

## 📖 Definition

The `==` operator checks whether two values are equal.

---

## 🧩 Syntax

```python
left == right
```

Python compares the values on both sides.

If they are equal:

```text
True
```

Otherwise:

```text
False
```

---

## 🧪 Example

```python
x = 10
y = 10

print(x == y)
```

### Output

```text
True
```

---

# 🧠 Internal Working

## Step 1: Create `x`

```python
x = 10
```

```text
x
│
▼
10
```

---

## Step 2: Create `y`

```python
y = 10
```

Conceptually:

```text
x ─┐
   │
   ▼
  10
   ▲
   │
   y
```

Both variables may refer to the same integer object.

> **Important:** For the `==` operator, the important question is whether the values are equal.

---

## Step 3: Compare the Values

```python
x == y
```

Python asks:

```text
Does the value of x equal the value of y?
```

The comparison becomes:

```text
10 == 10
```

Therefore:

```text
True
```

Python returns a Boolean object:

```text
True
```

Then:

```python
print(x == y)
```

displays:

```text
True
```

---

# ⭐ Important Difference: `=` vs `==`

Remember this forever:

## `=`

Means:

```text
ASSIGN
```

Example:

```python
x = 10
```

Meaning:

```text
Give 10 to x
```

---

## `==`

Means:

```text
COMPARE
```

Example:

```python
x == 10
```

Meaning:

```text
Is x equal to 10?
```

---

# 🧠 Memory Trick

```text
=   → Give / Assign

==  → Ask / Compare
```

### Think of It Like This

```text
Teacher gives marks
        ↓
        =
```

The teacher asks:

```text
"Did you score 90?"
        ↓
       ==
```

---

# 🏆 Final Revision

| Operator | Purpose | Example | Result |
|---|---|---|---|
| `=` | Assign a value | `x = 10` | `x` refers to `10` |
| `==` | Compare values | `x == 10` | `True` or `False` |

> 🔥 **Most common beginner mistake:** Do not confuse assignment (`=`) with comparison (`==`).


# 🧠 Comparison Operators — Revision

Comparison operators compare values and return a Boolean result:

```text
True
```

or

```text
False
```

---

# 1️⃣ Comparison Operator: `==`

## 📖 Definition

The `==` operator compares the **values** of two objects.

It checks:

```text
Are the values equal?
```

> ⚠️ **Important:** `==` checks value equality. It does not check whether two variables refer to the exact same object in memory.

---

## 🧩 Syntax

```python
left == right
```

---

## 🔄 Return Type

The `==` operator always returns a Boolean value:

```text
True
```

or

```text
False
```

---

# 🧪 Examples

## Equal Integer Values

```python
10 == 10
```

Result:

```text
True
```

---

## Different Integer Values

```python
10 == 20
```

Result:

```text
False
```

---

## Integer and Float

```python
10 == 10.0
```

Result:

```text
True
```

### Why?

Both represent the same numeric value:

```text
10 == 10.0
  ↓
True
```

---

## Integer and String

```python
10 == "10"
```

Result:

```text
False
```

### Why?

They have different types:

```text
10    → int

"10"  → str
```

Even though they look similar, they are different values and different types.

---

## Case Sensitivity

```python
"Python" == "python"
```

Result:

```text
False
```

### Why?

Python is case-sensitive.

```text
"P" ≠ "p"
```

Therefore:

```text
"Python" ≠ "python"
```

---

# 2️⃣ Comparison Operator: `!=`

## 📖 Definition

The `!=` operator checks whether two values are different.

It asks:

```text
Are the values NOT equal?
```

If the values are different:

```text
True
```

If the values are the same:

```text
False
```

Just like `==`, the `!=` operator returns a Boolean value.

---

# 🧩 Syntax

```python
left != right
```

Read it as:

```text
"Left is not equal to right."
```

---

# 🧪 Example

```python
x = 50
y = 20

print(x != y)
```

---

# 🧠 Internal Working

## Step 1: Create `x`

```python
x = 50
```

Python creates an integer object:

```text
50
```

and `x` refers to it.

```text
x
│
▼
50
```

---

## Step 2: Create `y`

```python
y = 20
```

Python creates another integer object:

```text
20
```

and `y` refers to it.

```text
x ─► 50

y ─► 20
```

---

## Step 3: Compare the Values

```python
x != y
```

Python asks:

```text
Is 50 different from 20?
```

The answer is:

```text
Yes
```

Therefore:

```text
50 != 20
   ↓
 True
```

Python creates a Boolean object:

```text
True
```

Then:

```python
print(x != y)
```

displays:

```text
True
```

---

# 🧪 Real-World Example: Password Validation

```python
password = "python123"

user_input = "hello123"

print(user_input != password)
```

Python asks:

```text
Is the entered password different from the actual password?
```

```text
"hello123" != "python123"
          ↓
        True
```

The values are different.

---

# 🌍 Real-Life Uses of `!=`

The `!=` operator is commonly used for:

- 🔐 Password validation
- 👤 Username checking
- 🔄 Detecting changes
- 📝 Form validation
- 📊 Comparing old and new values
- 🧪 Checking whether a value has changed

---

# ⚖️ Comparing `==` and `!=`

| Expression | Question Python Asks | Result |
|---|---|---|
| `10 == 10` | Are they equal? | `True` |
| `10 != 10` | Are they different? | `False` |
| `10 == 20` | Are they equal? | `False` |
| `10 != 20` | Are they different? | `True` |

---

# 🧠 The Main Relationship

```text
!= is the opposite of ==
```

| `==` | `!=` |
|---|---|
| Equal | Not Equal |
| Same value → `True` | Different value → `True` |
| Different value → `False` | Same value → `False` |

---

# 🔥 Memory Trick

```text
==  → Are they equal?

!=  → Are they different?
```

---

# 🏆 Final Revision

```text
== → Compare equality

!= → Compare inequality
```

Both operators:

```text
Compare values
      ↓
Return a Boolean
      ↓
True or False
```

> ⭐ **Remember:** `==` and `!=` compare values. They do not check whether two variables refer to the same object in memory.

# ⚠️ Common Beginner Mistake: `!=`

Some beginners think:

```text
!=
```

means:

```text
NOT
```

❌ This is incorrect.

The correct meaning is:

```text
NOT EQUAL TO
```

The `!=` operator always compares **two values**.

```python
x != y
```

Python asks:

```text
Is x different from y?
```

### Example

```python
10 != 20
```

```text
10 is different from 20
        ↓
      True
```

> ⭐ **Remember:** `!=` does not simply mean "not". It means **not equal to**.

---

# 3️⃣ Greater Than (`>`)

## 📖 Definition

The `>` operator checks whether the value on the **left** is greater than the value on the **right**.

If the left value is greater:

```text
True
```

Otherwise:

```text
False
```

Like all comparison operators, `>` always returns a Boolean value.

---

# 🎯 Why Do We Need `>`?

The greater-than operator helps Python answer questions such as:

- Is the age greater than `18`?
- Is the salary greater than `₹50,000`?
- Is the exam score greater than the passing mark?
- Is today's temperature greater than yesterday's?

These are all comparisons.

---

## 🧪 Example

```python
age = 21

age > 18
```

Python asks:

```text
Is 21 greater than 18?
```

The answer is:

```text
True
```

---

# 🧩 Syntax

```python
left > right
```

Read it as:

```text
Left is greater than right.
```

---

# 🧠 Internal Working

Consider this code:

```python
x = 15
y = 10

print(x > y)
```

---

## Step 1: Create `x`

```python
x = 15
```

Python creates an integer object:

```text
15
```

and `x` refers to it.

```text
x
│
▼
15
```

---

## Step 2: Create `y`

```python
y = 10
```

Python creates another integer object:

```text
10
```

and `y` refers to it.

```text
x ─► 15

y ─► 10
```

---

## Step 3: Compare the Values

```python
x > y
```

Python asks:

```text
Is 15 greater than 10?
```

The answer is:

```text
Yes
```

Therefore:

```text
15 > 10
   ↓
 True
```

Python creates the Boolean object:

```text
True
```

Then:

```python
print(x > y)
```

displays:

```text
True
```

---

# 🧪 Another Example

```python
x = 5
y = 20

print(x > y)
```

Python asks:

```text
Is 5 greater than 20?
```

The answer is:

```text
No
```

Therefore:

```text
5 > 20
   ↓
 False
```

### Output

```text
False
```

---

# 🔢 Number Line Thinking

A number line is a useful way to understand `>`.

```text
← Smaller ---------------------------- Greater →
```

```text
1   2   3   4   5   6   7   8   9   10
```

---

## Example 1

```python
8 > 3
```

On the number line:

```text
3 ───────────────► 8
```

`8` is to the right of `3`.

Therefore:

```text
8 > 3
  ↓
True
```

---

## Example 2

```python
2 > 9
```

On the number line:

```text
2 ◄─────────────── 9
```

`2` is to the left of `9`.

Therefore:

```text
2 > 9
  ↓
False
```

---

# 🔤 String Comparison

Python can also compare strings.

String comparison is based on **lexicographical order**, which means Python compares characters based on their character values.

Example:

```python
"Python" > "Java"
```

String comparison will be studied in detail when we learn strings.

> 📌 **For now, focus on understanding `>` with numbers.**

---

# ⚠️ Common Beginner Mistakes

## ❌ Mistake 1: Thinking Equal Values Are Greater

Some beginners think:

```python
5 > 5
```

is:

```text
True
```

This is incorrect.

Python asks:

```text
Is 5 greater than 5?
```

The answer is:

```text
No
```

The values are equal.

Therefore:

```text
5 > 5
  ↓
False
```

---

## ❌ Mistake 2: Confusing `>` with `>=`

These operators are different:

```text
>   → Greater Than

>=  → Greater Than or Equal To
```

For example:

```python
5 > 5
```

Result:

```text
False
```

because `5` is not greater than `5`.

We will learn `>=` separately.

---

# 🧠 Memory Trick

```text
>
```

The left side must be:

```text
GREATER
```

than the right side.

```text
10 > 5
```

```text
10 is greater than 5
        ↓
      True
```

---

# 🏆 Final Revision

| Expression | Python Asks | Result |
|---|---|---|
| `10 > 5` | Is 10 greater than 5? | `True` |
| `5 > 10` | Is 5 greater than 10? | `False` |
| `5 > 5` | Is 5 greater than 5? | `False` |

```text
> → Greater Than
```

> ⭐ The value on the left must be strictly greater than the value on the right for the result to be `True`.

# 🐍 Comparison Operator: `<`

---

# 1️⃣ Definition

The `<` operator checks whether the value on the **left** is less than the value on the **right**.

If the left value is less than the right value:

```text
True
```

Otherwise:

```text
False
```

Like every comparison operator, `<` always returns a Boolean value.

---

# 2️⃣ Why Do We Need `<`?

The less-than operator helps Python answer questions such as:

- Is the temperature below `0°C`?
- Is the student's age less than `18`?
- Is the stock price lower than yesterday's price?
- Is the account balance below `₹100`?

---

## 🧪 Example

```python
balance = 80

balance < 100
```

Python asks:

```text
Is 80 less than 100?
```

The answer is:

```text
True
```

---

# 3️⃣ Syntax

```python
left < right
```

Read it as:

```text
Left is less than right.
```

---

# 4️⃣ Internal Working

Consider this code:

```python
x = 4
y = 9

print(x < y)
```

---

## Step 1: Create `x`

```python
x = 4
```

Python creates an integer object:

```text
4
```

and `x` refers to it.

```text
x
│
▼
4
```

---

## Step 2: Create `y`

```python
y = 9
```

Python creates another integer object:

```text
9
```

and `y` refers to it.

```text
x ─► 4

y ─► 9
```

---

## Step 3: Compare the Values

```python
x < y
```

Python asks:

```text
Is 4 less than 9?
```

The answer is:

```text
Yes
```

Therefore:

```text
4 < 9
  ↓
True
```

Python creates a Boolean object:

```text
True
```

Then:

```python
print(x < y)
```

displays:

```text
True
```

---

# 🧪 Another Example

```python
x = 20
y = 5

print(x < y)
```

Python asks:

```text
Is 20 less than 5?
```

The answer is:

```text
No
```

Therefore:

```text
20 < 5
   ↓
 False
```

### Result

```text
False
```

---

# 🔢 Number Line Thinking

Remember:

```text
← Smaller ---------------------- Greater →
```

Example:

```text
-5  -4  -3  -2  -1   0   1   2   3   4   5
```

A number is **less than** another number if it is located to the **left**.

---

## 🧪 Example 1

```python
2 < 8
```

Number line:

```text
2 ───────────────► 8
```

`2` is on the left of `8`.

Therefore:

```text
2 < 8
  ↓
True
```

---

## 🧪 Example 2

```python
8 < 2
```

Here, `8` is on the right of `2`.

Therefore:

```text
8 < 2
  ↓
False
```

---

# ➖ Negative Numbers

Negative numbers can sometimes confuse beginners.

Consider:

```python
-8 < -3
```

On the number line:

```text
-8 ─────────────► -3
```

`-8` is further to the left.

Therefore:

```text
-8 < -3
    ↓
  True
```

---

# ⚠️ Common Beginner Mistakes

## ❌ Mistake 1: Thinking Equal Values Are Less Than

Some beginners think:

```python
5 < 5
```

is:

```text
True
```

This is incorrect.

Python asks:

```text
Is 5 less than 5?
```

The answer is:

```text
No
```

The values are equal.

Therefore:

```text
5 < 5
  ↓
False
```

---

## ❌ Mistake 2: Confusing `<` with `<=`

These operators are different:

```text
<   → Less Than

<=  → Less Than or Equal To
```

For now, remember:

```python
5 < 5
```

Result:

```text
False
```

We will study `<=` separately.

---

# 📖 Comparison Operators — So Far

| Operator | Question Python Asks |
|---|---|
| `==` | Are they equal? |
| `!=` | Are they different? |
| `>` | Is the left value greater than the right? |
| `<` | Is the left value less than the right? |

---

# ⭐ Interview Tip

Many beginners simply memorize comparison symbols.

A better approach is to translate every symbol into English.

When you see:

```python
a < b
```

Read it as:

```text
"Is a less than b?"
```

When you see:

```python
a > b
```

Read it as:

```text
"Is a greater than b?"
```

This habit makes it much easier to understand complex conditions later in:

```python
if
```

statements.

---

# 🧠 Memory Trick

```text
< → Smaller / Less Than
```

The left value must be **strictly smaller** than the right value.

```text
3 < 8
↓
True
```

```text
8 < 3
↓
False
```

```text
5 < 5
↓
False
```

> ⭐ **Key Rule:** Equal values are neither greater than nor less than each other.


# 🐍 Comparison Operator: `>=`

---

# 1️⃣ Definition

The operator:

```python
>=
```

means:

```text
Greater Than OR Equal To
```

This is a comparison operator with **two possible conditions**.

Python asks:

```text
Is the left value greater than the right value?
```

**OR**

```text
Are both values equal?
```

If either condition is true:

```text
True
```

Otherwise:

```text
False
```

---

# 2️⃣ Why Do We Need `>=`?

Imagine a company has this requirement:

```text
Age must be 18 or above.
```

Notice the requirement does **not** mean:

```text
Age must be greater than 18.
```

It means:

```text
18 OR ABOVE
```

Therefore:

```python
age >= 18
```

---

## 🧪 Examples

| Age | `age >= 18` | Why? |
|---:|:---:|---|
| `18` | ✅ `True` | Equal to 18 |
| `19` | ✅ `True` | Greater than 18 |
| `25` | ✅ `True` | Greater than 18 |
| `17` | ❌ `False` | Less than 18 |

---

## 🏦 Another Example: Minimum Bank Balance

Suppose the minimum required balance is:

```text
₹1000
```

The requirement is:

```python
balance >= 1000
```

| Balance | Result | Why? |
|---:|:---:|---|
| ₹1000 | `True` | Equal to minimum |
| ₹1500 | `True` | Greater than minimum |
| ₹2000 | `True` | Greater than minimum |
| ₹999 | `False` | Less than minimum |

---

# 3️⃣ Syntax

```python
left >= right
```

Read it as:

```text
Left is greater than or equal to right.
```

---

# 4️⃣ Internal Working

Consider:

```python
x = 10
y = 5

print(x >= y)
```

Python conceptually asks:

```text
Is 10 greater than 5?
```

**OR**

```text
Is 10 equal to 5?
```

The first condition is true:

```text
10 > 5
   ↓
 True
```

Therefore:

```text
10 >= 5
    ↓
  True
```

---

## 🧪 Another Example

```python
x = 10
y = 10

print(x >= y)
```

Python asks:

```text
Is 10 greater than 10?
```

```text
No
```

Then it checks:

```text
Is 10 equal to 10?
```

```text
Yes
```

Therefore:

```text
10 >= 10
    ↓
  True
```

---

# ⭐ Important Concept

Although:

```text
10 is NOT greater than 10
```

the result is still:

```text
True
```

because `>=` means:

```text
GREATER
   OR
EQUAL
```

The equality condition is allowed.

---

# 🔢 Number Line Thinking

```text
← Smaller ------------------------ Greater →
```

```text
1   2   3   4   5   6   7   8   9   10
```

---

## Example 1

```python
5 >= 5
```

Python asks:

```text
Is 5 to the right of 5?
```

No.

Then:

```text
Is 5 equal to 5?
```

Yes.

Therefore:

```text
5 >= 5
    ↓
  True
```

---

## Example 2

```python
8 >= 5
```

`8` is to the right of `5`.

Therefore:

```text
8 >= 5
    ↓
  True
```

---

## Example 3

```python
2 >= 5
```

`2` is to the left of `5`.

It is also not equal to `5`.

Therefore:

```text
2 >= 5
    ↓
  False
```

---

# ⚖️ Comparing `>` and `>=`

This is one of the most important concepts in programming and interviews.

| Expression | Result | Why? |
|---|:---:|---|
| `5 > 5` | `False` | Equal is not greater |
| `5 >= 5` | `True` | Equal is allowed |
| `8 > 5` | `True` | Greater |
| `8 >= 5` | `True` | Greater |
| `2 > 5` | `False` | Smaller |
| `2 >= 5` | `False` | Smaller |

---

# ⭐ Golden Rule

```text
>=
```

means:

```text
GREATER
   OR
EQUAL
```

If either condition is true:

```text
True
```

---

# ⚠️ Common Beginner Mistakes

## ❌ Mistake 1: Thinking `5 >= 5` Is `False`

Some beginners think:

```python
5 >= 5
```

is:

```text
False
```

This is incorrect.

The `=` means equality is included.

Therefore:

```text
5 >= 5
    ↓
  True
```

---

## ❌ Mistake 2: Confusing `>` with `>=`

Remember:

```python
5 > 5
```

```text
False
```

Because `5` is not greater than `5`.

---

```python
5 >= 5
```

```text
True
```

Because equal values are allowed.

---

# 🧠 One Tiny `=` Changes Everything

```text
>   → Greater Than

>=  → Greater Than OR Equal To
```

That small equality symbol changes the result when both values are equal.

---

# ⚠️ Comparing Different Types

Some comparisons between different types are not supported.

For example:

```python
10 == "10"
```

Result:

```text
False
```

The values are not equal.

---

```python
10 != "10"
```

Result:

```text
True
```

The values are different.

---

However, ordering comparisons between an integer and a string are not supported:

```python
10 > "10"
```

```text
TypeError
```

---

```python
10 < "10"
```

```text
TypeError
```

---

```python
10 >= "10"
```

```text
TypeError
```

---

```python
10 <= "10"
```

```text
TypeError
```

---

# 📊 Comparison Summary

| Expression | Result |
|---|---|
| `10 == "10"` | `False` |
| `10 != "10"` | `True` |
| `10 > "10"` | `TypeError` |
| `10 < "10"` | `TypeError` |
| `10 >= "10"` | `TypeError` |
| `10 <= "10"` | `TypeError` |

---

# 🏆 Final Revision

```text
>   → Greater Than

>=  → Greater Than OR Equal To
```

### Examples

```python
10 >= 5
```

```text
True
```

because:

```text
10 is greater than 5
```

---

```python
10 >= 10
```

```text
True
```

because:

```text
10 is equal to 10
```

---

```python
5 >= 10
```

```text
False
```

because:

```text
5 is smaller than 10
```

> ⭐ **Key Rule:** `>=` is true when the left value is either greater than or equal to the right value.


# 🐍 Comparison Operator: `<=`

---

# 1️⃣ Definition

The operator:

```python
<=
```

means:

```text
Less Than OR Equal To
```

It checks two conditions:

```text
Is the left value less than the right value?
```

**OR**

```text
Are both values equal?
```

If either condition is true:

```text
True
```

Otherwise:

```text
False
```

Like every comparison operator, `<=` returns a Boolean value.

---

# 2️⃣ Why Do We Need `<=`?

The `<=` operator is used when a value is allowed to be:

```text
LESS THAN
```

or:

```text
EQUAL TO
```

a limit.

---

# 🚗 Example 1: Speed Limit

Suppose the maximum allowed speed is:

```text
80 km/h
```

The rule is:

```python
speed <= 80
```

| Speed | Result | Why? |
|---:|:---:|---|
| `60` | ✅ `True` | Less than 80 |
| `75` | ✅ `True` | Less than 80 |
| `80` | ✅ `True` | Equal to 80 |
| `81` | ❌ `False` | Greater than 80 |

> ⭐ The rule is **80 or below**, not only below 80.

---

# 🎟️ Example 2: Age Requirement

Suppose a children's ticket is available for ages:

```text
12 or younger
```

The condition is:

```python
age <= 12
```

| Age | Result | Why? |
|---:|:---:|---|
| `8` | ✅ `True` | Less than 12 |
| `12` | ✅ `True` | Equal to 12 |
| `13` | ❌ `False` | Greater than 12 |

---

# 3️⃣ Syntax

```python
left <= right
```

Read it as:

```text
Left is less than or equal to right.
```

---

# 4️⃣ Internal Working

## 🧪 Example 1: Left Value Is Smaller

```python
x = 5
y = 10

print(x <= y)
```

Python asks:

```text
Is 5 less than 10?
```

The answer is:

```text
Yes
```

Therefore:

```text
5 <= 10
    ↓
  True
```

Python returns:

```text
True
```

---

## 🧪 Example 2: Values Are Equal

```python
x = 10
y = 10

print(x <= y)
```

Python asks:

```text
Is 10 less than 10?
```

The answer is:

```text
No
```

Then Python asks:

```text
Is 10 equal to 10?
```

The answer is:

```text
Yes
```

Therefore:

```text
10 <= 10
     ↓
   True
```

---

## 🧪 Example 3: Left Value Is Greater

```python
x = 15
y = 10

print(x <= y)
```

Python asks:

```text
Is 15 less than 10?
```

```text
No
```

Then:

```text
Is 15 equal to 10?
```

```text
No
```

Therefore:

```text
15 <= 10
     ↓
   False
```

---

# 🔢 Number Line Thinking

```text
← Smaller ------------------------- Greater →
```

```text
1   2   3   4   5   6   7   8   9   10
```

A value is `<=` another value when it is:

```text
To the LEFT
```

or:

```text
Exactly EQUAL
```

---

## 🧪 Example 1

```python
5 <= 5
```

Python asks:

```text
Is 5 less than 5?
```

No.

Then:

```text
Is 5 equal to 5?
```

Yes.

Therefore:

```text
5 <= 5
    ↓
  True
```

---

## 🧪 Example 2

```python
3 <= 5
```

`3` is to the left of `5`.

Therefore:

```text
3 <= 5
    ↓
  True
```

---

## 🧪 Example 3

```python
8 <= 5
```

`8` is to the right of `5`.

It is also not equal to `5`.

Therefore:

```text
8 <= 5
    ↓
  False
```

---

# ⚖️ Comparing `<` and `<=`

| Expression | Result | Why |
|---|:---:|---|
| `5 < 5` | `False` | Equal is **not** less |
| `5 <= 5` | `True` | Equal is allowed |
| `3 < 5` | `True` | Smaller |
| `3 <= 5` | `True` | Smaller |
| `8 < 5` | `False` | Greater |
| `8 <= 5` | `False` | Greater |

---

# ⭐ The Important Difference

```text
<   → Less Than Only

<=  → Less Than OR Equal To
```

The extra:

```text
=
```

allows equal values.

---

## 🧠 Compare Equal Values

```python
5 < 5
```

```text
False
```

Because:

```text
5 is not less than 5
```

---

```python
5 <= 5
```

```text
True
```

Because:

```text
5 is equal to 5
```

---

# 🏆 Final Revision

```text
<=
```

means:

```text
LESS
  OR
EQUAL
```

### Examples

```python
3 <= 5
```

```text
True
```

because `3` is less than `5`.

---

```python
5 <= 5
```

```text
True
```

because both values are equal.

---

```python
8 <= 5
```

```text
False
```

because `8` is greater than `5`.

---

# 📖 All Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal To |
| `!=` | Not Equal To |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal To |
| `<=` | Less Than or Equal To |

> ⭐ **Key Rule:** `<=` is `True` when the left value is either smaller than or equal to the right value.



# 🧠 Logical Operators

Before learning logical operators, remember the difference between arithmetic and comparison operators.

---

# 🔢 Arithmetic Operators

Arithmetic operators work with numbers.

```python
10 + 5
```

Python performs the calculation:

```text
10 + 5
  ↓
15
```

### Result

```text
15
```

---

# ⚖️ Comparison Operators

Comparison operators compare values.

```python
10 > 5
```

Python asks:

```text
Is 10 greater than 5?
```

### Result

```text
True
```

---

# 🤔 What If We Have Multiple Conditions?

Suppose we have two comparison expressions:

```python
10 > 5
```

Result:

```text
True
```

And:

```python
20 > 15
```

Result:

```text
True
```

Now we have:

```text
True
```

and:

```text
True
```

How can we combine these Boolean values?

This is why **logical operators** exist.

---

# 1️⃣ Definition

A **logical operator** is an operator that works with Boolean values:

```text
True
```

and:

```text
False
```

Logical operators are used to:

- Combine Boolean expressions
- Check multiple conditions
- Modify Boolean results

---

# 2️⃣ Why Do We Need Logical Operators?

Imagine a student passes only when **both** conditions are satisfied:

```text
Marks ≥ 35
```

AND:

```text
Attendance ≥ 75%
```

These are two separate conditions.

Python needs a way to combine them.

```python
marks >= 35 and attendance >= 75
```

Logical operators allow Python to answer questions such as:

```text
Are both conditions true?
```

```text
Is at least one condition true?
```

```text
Is this condition not true?
```

---

# 3️⃣ Types of Logical Operators

Python has three logical operators:

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses a Boolean value |

---

# 4️⃣ The `and` Operator

## 📖 Definition

The `and` operator returns:

```text
True
```

only when **both operands are True**.

If even one operand is:

```text
False
```

the result is:

```text
False
```

---

# 🧠 Think Like Python

## Example 1

```python
True and True
```

Python asks:

### Question 1

```text
Is the left operand True?
```

```text
Yes ✅
```

### Question 2

```text
Is the right operand True?
```

```text
Yes ✅
```

Both operands are `True`.

Therefore:

```text
True and True
        ↓
      True
```

Python returns:

```text
True
```

---

## Example 2

```python
True and False
```

Python asks:

### Left Operand

```text
Is the left operand True?
```

```text
Yes ✅
```

### Right Operand

```text
Is the right operand True?
```

```text
No ❌
```

Both operands are not `True`.

Therefore:

```text
True and False
         ↓
       False
```

---

# 📊 Truth Table: `and`

This is the foundation of logical operators.

| Left | Right | `Left and Right` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

---

# ⭐ Golden Rule of `and`

```text
and → BOTH must be True
```

Think:

```text
True AND True
      ↓
    True
```

Every other combination:

```text
False
```

---

# 🧪 Real-World Example

A student passes only if:

```text
Marks >= 35
```

AND:

```text
Attendance >= 75
```

Example:

```python
marks = 80
attendance = 90

result = marks >= 35 and attendance >= 75

print(result)
```

Python evaluates:

```text
80 >= 35
   ↓
 True
```

and:

```text
90 >= 75
   ↓
 True
```

Then:

```text
True and True
        ↓
      True
```

### Final Result

```text
True
```

---

# 🧠 Quick Revision

```text
Arithmetic Operators
        ↓
     Numbers
        ↓
      15
```

---

```text
Comparison Operators
        ↓
      Values
        ↓
   True / False
```

---

```text
Logical Operators
        ↓
Combine Boolean Results
        ↓
   True / False
```

---

# 🏆 Final Rule

```text
and
```

means:

```text
BOTH conditions must be True.
```

```text
True and True
        ↓
      True
```

```text
True and False
         ↓
       False
```

```text
False and True
         ↓
       False
```

```text
False and False
          ↓
        False
```

> ⭐ **Memory Trick:** `and` is strict. It gives `True` only when **everything is True**.


# 🧠 `and` Operator — Internal Working

## 📖 Read the Truth Table Carefully

The `and` operator has only **one combination** that produces:

```text
True
```

That combination is:

```text
True and True
```

All other combinations produce:

```text
False
```

---

# 7️⃣ Internal Working

Consider:

```python
5 > 3 and 10 > 7
```

Let's evaluate it step by step.

---

## Step 1: Evaluate the Left Comparison

```python
5 > 3
```

Python asks:

```text
Is 5 greater than 3?
```

The answer is:

```text
True
```

Python creates a Boolean object:

```text
True
```

---

## Step 2: Evaluate the Right Comparison

```python
10 > 7
```

Python asks:

```text
Is 10 greater than 7?
```

The answer is:

```text
True
```

Python creates another Boolean object:

```text
True
```

---

## Step 3: Apply the `and` Operator

Now Python has:

```python
True and True
```

Python checks the truth table:

```text
True and True
        ↓
      True
```

### Final Result

```text
True
```

Python produces the final Boolean result:

```text
True
```

---

# 🧠 8️⃣ Memory Thinking

Consider:

```python
print(5 > 3 and 10 > 7)
```

Conceptually:

```text
5 > 3
   │
   ▼
True Object
```

```text
10 > 7
    │
    ▼
True Object
```

Then:

```text
True and True
      │
      ▼
Final True Result
```

---

## ⭐ Important Observation

Python does not change the earlier Boolean objects.

The comparison results are used to produce the final logical result.

Conceptually:

```text
Comparison 1
     ↓
 Boolean Result
     ↓
     AND
     ↑
 Boolean Result
     ↑
Comparison 2
```

---

# 🔒 Boolean Objects Are Immutable

Remember:

```python
True
```

and:

```python
False
```

are actual Python objects.

Their type is:

```python
bool
```

---

## 🧪 Example

```python
print(type(True))
```

### Output

```text
<class 'bool'>
```

---

# 🌍 Real-Life Examples

## 🎬 Example 1: Movie Entry

You can enter a movie only if:

```text
Age is 18 or above
```

AND:

```text
Ticket is valid
```

Both conditions must be true.

Conceptually:

```python
age >= 18 and ticket_is_valid
```

This is an `and` situation.

---

## 📝 Example 2: Exam Submission

You can submit an exam only if:

```text
You finished writing
```

AND:

```text
Time has not expired
```

Both conditions are required.

Conceptually:

```python
finished_writing and time_remaining
```

---

# ⚠️ Common Beginner Mistake

Many beginners think:

```python
True and False
```

returns:

```text
True
```

because one side is `True`.

❌ This is incorrect.

The word:

```text
and
```

means:

```text
BOTH conditions must be satisfied.
```

Therefore:

```text
True and False
         ↓
       False
```

---

# 📊 Summary

| Operator | Meaning | Rule |
|---|---|---|
| `and` | Logical AND | Both operands must be `True` |

---

# 🧠 The Evaluation Process

Consider:

```python
10 > 5 and 8 > 2
```

Python conceptually evaluates the expression in stages.

---

## Step 1: Evaluate Comparison 1

```python
10 > 5
```

```text
True
```

---

## Step 2: Evaluate Comparison 2

```python
8 > 2
```

```text
True
```

---

## Step 3: Apply the Logical Operator

```python
True and True
        ↓
      True
```

---

# 🔗 The Basic Mental Model

```text
Comparison 1
     │
     ▼
 Boolean Result
     │
     ├─────────────┐
     │             │
     ▼             ▼
     AND ───────► Boolean Result
     ▲
     │
 Boolean Result
     ▲
     │
Comparison 2
```

Or more simply:

```text
Comparison 1 ──► Boolean
                      \
                       AND ──► Final Boolean Result
                      /
Comparison 2 ──► Boolean
```

---

# 🏆 The Basic Model to Remember

```text
Comparison
    ↓
True / False
    ↓
Logical Operator
    ↓
True / False
```

For `and`:

```text
True and True
        ↓
      True
```

Everything else:

```text
False
```

> ⭐ **Key Concept:** Comparison operators produce Boolean results. Logical operators then combine those Boolean results.



# 🐍 Logical Operator: `and` — Level 2

So far, you learned the Boolean truth table:

```python
True and True
```

Result:

```text
True
```

And:

```python
False and True
```

Result:

```text
False
```

Until now, we used `and` with Boolean values.

Now we will learn an important Python behavior:

> ⭐ Python's `and` operator does **not always return `True` or `False`.

This is one of the most important concepts in Python.

---

# 1️⃣ First Example

```python
x = 10
y = 20

print(x and y)
```

What do you expect?

Maybe:

```text
True
```

But Python outputs:

```text
20
```

Why?

Because Python's `and` operator does not simply follow the Boolean truth table.

It follows a special value-returning rule.

---

# 2️⃣ Python's Rule for `and`

For:

```python
A and B
```

Python first checks:

```text
A
```

### If `A` is Falsy

```text
Return A
```

### If `A` is Truthy

```text
Return B
```

---

## 🧠 The Simple Rule

```text
A and B
```

means:

```text
If A is falsy:
    return A

Otherwise:
    return B
```

Or remember:

```text
and → first FALSY value
```

If the first value is truthy, Python returns the second value.

---

# 3️⃣ Example: Both Values Are Truthy

```python
10 and 20
```

Python asks:

```text
Is 10 truthy?
```

Yes.

Therefore, Python returns the second operand:

```text
20
```

### Output

```text
20
```

---

## 🧠 Evaluation

```text
10 and 20
  │
  ▼
Is 10 falsy?
  │
  └── No
       │
       ▼
   Return 20
```

---

# 4️⃣ Example: First Value Is Falsy

```python
0 and 20
```

Python asks:

```text
Is 0 truthy?
```

No.

`0` is falsy.

Therefore, Python immediately returns:

```text
0
```

### Output

```text
0
```

Python does not need to continue evaluating the second side.

---

# ⭐ The Main Rule

```text
First value Falsy  → Return First Value
First value Truthy → Return Second Value
```

---

# 5️⃣ Truthy and Falsy Values

Python considers certain values to be **Falsy**.

## ❌ Common Falsy Values

```python
False
0
0.0
""
None
[]
()
{}
set()
```

These values behave like:

```text
False
```

when Python checks their truthiness.

---

## ✅ Common Truthy Values

```python
True
1
10
-5
"Python"
[1, 2]
```

Most non-empty and non-zero values are truthy.

---

# 6️⃣ Internal Working

Consider:

```python
x = 10
y = 20

result = x and y
```

Conceptually:

```text
x
↓
10
↓
Is 10 falsy?
↓
No
↓
Return y
↓
20
```

Therefore:

```text
result → 20
```

---

# ⭐ Important Observation

The result is:

```text
20
```

It is **not**:

```text
True
```

The `and` operator returned the actual value:

```text
20
```

---

# 7️⃣ Memory Model

Consider:

```python
x = 10
y = 20

result = x and y
```

Conceptually:

```text
x ─────────────► [10]


y ─────────────► [20]
                   ▲
                   │
result ────────────┘
```

The result is:

```text
20
```

Therefore:

```text
result
```

refers to the same value returned by the expression.

---

# 🧠 Important Concept

In this example:

```python
10 and 20
```

`and` does not need to create a new Boolean object:

```text
True
```

Instead, it returns an actual operand:

```text
20
```

---

# 8️⃣ Comparison Operators vs Logical `and`

## ⚖️ Comparison Operator

```python
10 > 5
```

Python asks:

```text
Is 10 greater than 5?
```

Result:

```text
True
```

A comparison operator produces a Boolean result.

---

## 🧠 Logical `and`

```python
10 and 20
```

Python checks:

```text
Is 10 truthy?
```

Yes.

Therefore:

```text
Return 20
```

Result:

```text
20
```

---

# ⭐ Important Difference

| Expression | Result | What Happens? |
|---|---|---|
| `10 > 5` | `True` | Comparison returns a Boolean |
| `10 and 20` | `20` | `and` returns an actual operand |

> ⭐ Comparison operators return Boolean results. The `and` operator can return the actual value of an operand.

---

# 9️⃣ Short-Circuit Evaluation

The technical name for this behavior is:

```text
Short-circuit evaluation
```

Consider:

```python
0 and 100
```

Python evaluates:

```text
Is 0 falsy?
```

Yes.

Python already knows the result must be:

```text
0
```

Therefore, it does not need to continue evaluating the second operand.

```text
0 and 100
  ↓
0
```

---

# ⚡ Why Is This Called Short-Circuiting?

Imagine an electrical circuit.

If the circuit is already broken at the first point, electricity cannot continue.

Similarly, in:

```python
0 and 100
```

the first value is already falsy.

Therefore, Python stops early.

```text
First value is Falsy
        ↓
Stop immediately
        ↓
Return First Value
```

---

# 🔟 Why Is This Useful?

Consider:

```python
name = "Gajanand"

print(name and "Name exists")
```

Python asks:

```text
Is "Gajanand" truthy?
```

Yes.

Therefore, Python returns the second operand:

```text
"Name exists"
```

### Output

```text
Name exists
```

---

## 🧪 Another Example

```python
name = ""

print(name and "Name exists")
```

Python asks:

```text
Is "" truthy?
```

No.

An empty string is falsy.

Therefore, Python returns:

```text
""
```

---

# 1️⃣1️⃣ The Most Important Rule

For:

```python
A and B
```

Remember:

```text
If A is Falsy
    ↓
Return A
```

```text
If A is Truthy
    ↓
Return B
```

---

# 📊 Examples

| Expression | First Value | Result |
|---|---|---|
| `10 and 20` | `10` is Truthy | `20` |
| `0 and 20` | `0` is Falsy | `0` |
| `"Python" and "Developer"` | `"Python"` is Truthy | `"Developer"` |
| `"" and "Developer"` | `""` is Falsy | `""` |
| `True and False` | `True` is Truthy | `False` |
| `False and True` | `False` is Falsy | `False` |

---

# 🧠 One Important Detail

When we say:

```text
10 is truthy
```

we are **not** saying:

```python
10 == True
```

These are two different concepts.

---

## Comparison

```python
10 == True
```

Result:

```text
False
```

Because:

```text
10 is not equal to 1
```

---

But:

```python
bool(10)
```

Result:

```text
True
```

Because:

```text
10 is a truthy value
```

---

# 📊 Truthiness vs Equality

| Expression | Result | Meaning |
|---|---|---|
| `10 == True` | `False` | Does 10 equal True? |
| `bool(10)` | `True` | Is 10 truthy? |

---

# 🏆 Final Mental Model

## `and`

```text
A and B
```

### First Check `A`

```text
Is A Falsy?
```

If yes:

```text
Return A
```

If no:

```text
Return B
```

---

# 🔥 Memory Trick

```text
and → Stop at the first FALSY value
```

Examples:

```python
0 and 20
```

```text
0
```

Because `0` is the first falsy value.

---

```python
10 and 20
```

```text
20
```

Because `10` is truthy, so Python continues to the second value.

---

```python
"Python" and "Developer"
```

```text
"Developer"
```

Because `"Python"` is truthy.

---

```python
"" and "Developer"
```

```text
""
```

Because the empty string is falsy.

> ⭐ **Key Concept:** Python's `and` operator does not necessarily return a Boolean. It returns the first falsy operand, or the last operand if all values are truthy.
    
# 🐍 Truthy and Falsy Values

---

# 1️⃣ What Does "Truthy" Mean?

A value is **Truthy** when Python treats it as:

```text
True
```

in a Boolean context.

---

## 🧪 Example

```python
bool(10)
```

### Output

```text
True
```

Therefore:

```text
10 → Truthy
```

---

# ⚠️ Important: Truthiness Is Not Equality

Remember:

```python
10 == True
```

returns:

```text
False
```

But:

```python
bool(10)
```

returns:

```text
True
```

These are two different concepts.

### `10 == True`

Asks:

```text
Does 10 equal True?
```

### `bool(10)`

Asks:

```text
Does Python consider 10 logically True?
```

---

## 🧠 Truthy Means:

> "Python considers this value logically True."

---

# 2️⃣ What Does "Falsy" Mean?

A value is **Falsy** when Python treats it as:

```text
False
```

in a Boolean context.

---

## 🧪 Example

```python
bool(0)
```

### Output

```text
False
```

Therefore:

```text
0 → Falsy
```

---

# 3️⃣ Is There a Fixed List of Falsy Values?

Yes.

Python has a small set of important built-in falsy values.

## 🔴 Main Falsy Values

| Value | Type |
|---|---|
| `False` | `bool` |
| `None` | `NoneType` |
| `0` | `int` |
| `0.0` | `float` |
| `0j` | `complex` |
| `""` | Empty string |
| `[]` | Empty list |
| `()` | Empty tuple |
| `{}` | Empty dictionary |
| `set()` | Empty set |

These are the main built-in falsy values.

---

# 4️⃣ Everything Else Is Generally Truthy

Common examples:

```python
True
1
10
-1
3.14
"Python"
" "
[1]
[0]
(1,)
{"a": 1}
{1}
```

---

# ⚠️ Important: `0` vs `[0]`

Look carefully:

```python
0
```

is:

```text
Falsy
```

But:

```python
[0]
```

is:

```text
Truthy
```

Why?

Because:

```text
0
```

is the integer zero.

But:

```text
[0]
```

is a non-empty list.

Python checks whether the container is empty.

It does **not** check whether the contents are zero.

---

## 🧠 The Main Rule

```text
Empty Container → Falsy
Non-Empty Container → Truthy
```

Therefore:

```python
bool([])
```

```text
False
```

But:

```python
bool([0])
```

```text
True
```

---

# 5️⃣ How Can You Test Truthiness?

You can always use:

```python
bool(value)
```

---

## 🧪 Example

```python
bool(10)
```

```text
True
```

---

```python
bool(0)
```

```text
False
```

---

# 6️⃣ Numeric Values: Integers

```python
bool(0)
```

```text
False
```

---

```python
bool(1)
```

```text
True
```

---

```python
bool(-1)
```

```text
True
```

---

## ⭐ Integer Rule

```text
0 → Falsy
```

```text
Any non-zero number → Truthy
```

---

### Examples

| Value | Boolean Value |
|---:|:---:|
| `0` | `False` |
| `1` | `True` |
| `-1` | `True` |
| `100` | `True` |
| `-999` | `True` |

---

# 7️⃣ Float Values

```python
bool(0.0)
```

```text
False
```

---

```python
bool(3.14)
```

```text
True
```

---

```python
bool(-2.5)
```

```text
True
```

---

## ⭐ Float Rule

```text
0.0 → Falsy
```

```text
Any non-zero float → Truthy
```

---

# 8️⃣ Strings

## 🔴 Empty String

```python
bool("")
```

```text
False
```

Why?

Because the string contains:

```text
0 characters
```

Therefore:

```text
"" → Falsy
```

---

## 🟢 Non-Empty String

```python
bool("Python")
```

```text
True
```

Any non-empty string is generally truthy.

---

# ⚠️ `"0"` Is Truthy

Consider:

```python
bool("0")
```

The result is:

```text
True
```

Why?

Because:

```text
"0"
```

is a string containing one character.

It is not the integer:

```text
0
```

---

## 🧠 Important Comparison

```python
bool(0)
```

```text
False
```

---

```python
bool("0")
```

```text
True
```

---

| Value | Type | Truthiness |
|---|---|---|
| `0` | `int` | Falsy |
| `"0"` | `str` | Truthy |

> ⭐ The value's type and whether it is empty matter.

---

# 9️⃣ Spaces in Strings

Consider:

```python
bool(" ")
```

### Result

```text
True
```

Why?

Because the string contains:

```text
1 space character
```

It is not empty.

---

## 🧠 Compare

```text
""   → 0 characters → Falsy
```

```text
" "  → 1 character  → Truthy
```

---

# 🔟 Lists

## Empty List

```python
bool([])
```

```text
False
```

An empty list is:

```text
Falsy
```

---

## Non-Empty List

```python
bool([1])
```

```text
True
```

---

```python
bool([0])
```

```text
True
```

---

## ⭐ Important Rule

Python checks:

```text
Is the list empty?
```

It does not check:

```text
Are the elements inside the list truthy?
```

Therefore:

```text
[]    → Falsy
[0]   → Truthy
[None] → Truthy
```

because all three non-empty lists contain at least one element.

---

# 1️⃣1️⃣ Tuples

## Empty Tuple

```python
bool(())
```

```text
False
```

---

## Non-Empty Tuple

```python
bool((1,))
```

```text
True
```

---

```text
()      → Empty → Falsy
(1,)    → Non-empty → Truthy
```

---

# 1️⃣2️⃣ Dictionaries

## Empty Dictionary

```python
bool({})
```

```text
False
```

---

## Non-Empty Dictionary

```python
bool({"name": "Gajanand"})
```

```text
True
```

---

```text
{}                  → Empty → Falsy
{"name": "Gajanand"} → Non-empty → Truthy
```

---

# 1️⃣3️⃣ Sets

## Empty Set

```python
bool(set())
```

```text
False
```

---

## Non-Empty Set

```python
bool({1})
```

```text
True
```

---

```text
set() → Empty → Falsy
{1}    → Non-empty → Truthy
```

---

# 1️⃣4️⃣ Memory Model

Consider:

```python
x = 0
```

Conceptually:

```text
x ─────► [0]
          │
          ▼
        Falsy
```

Now:

```python
y = 10
```

Conceptually:

```text
y ─────► [10]
          │
          ▼
        Truthy
```

---

## ⭐ Important

The object itself does not change.

Python simply evaluates the object's Boolean truth value when needed.

Conceptually:

```text
Object
   ↓
Python checks truthiness
   ↓
True or False
```

---

# 1️⃣5️⃣ Truthiness Is Not a Data Type

This is extremely important.

Consider:

```python
10
```

Its type is:

```text
int
```

Its truthiness is:

```text
Truthy
```

---

Now consider:

```python
"Python"
```

Its type is:

```text
str
```

Its truthiness is:

```text
Truthy
```

---

## 🧠 Important Concept

```text
Data Type
```

and:

```text
Truthiness
```

are different concepts.

---

| Value | Data Type | Truthiness |
|---|---|---|
| `10` | `int` | Truthy |
| `"Python"` | `str` | Truthy |
| `0` | `int` | Falsy |
| `""` | `str` | Falsy |
| `[]` | `list` | Falsy |
| `[0]` | `list` | Truthy |

> ⭐ Truthy and Falsy are not data types. They are logical evaluations.

---

# 1️⃣6️⃣ Connection With the `and` Operator

Now return to:

```python
10 and 20
```

Python asks:

```text
Is 10 truthy?
```

Yes.

Therefore:

```text
Return 20
```

### Result

```text
20
```

---

Now:

```python
0 and 20
```

Python asks:

```text
Is 0 truthy?
```

No.

Therefore:

```text
Return 0
```

### Result

```text
0
```

---

# 🧠 The `and` Rule

```text
A and B
```

### If `A` is Falsy:

```text
Return A
```

### If `A` is Truthy:

```text
Return B
```

---

# 🏆 Final Truthiness Revision

| Value | Truthiness |
|---|---|
| `False` | Falsy |
| `None` | Falsy |
| `0` | Falsy |
| `0.0` | Falsy |
| `0j` | Falsy |
| `""` | Falsy |
| `[]` | Falsy |
| `()` | Falsy |
| `{}` | Falsy |
| `set()` | Falsy |
| `True` | Truthy |
| `1` | Truthy |
| `-1` | Truthy |
| `"0"` | Truthy |
| `" "` | Truthy |
| `[0]` | Truthy |
| `(1,)` | Truthy |
| `{"a": 1}` | Truthy |
| `{1}` | Truthy |

---

# 🔥 Memory Rules

```text
Zero → Falsy
```

```text
Empty → Falsy
```

```text
Non-zero → Truthy
```

```text
Non-empty → Truthy
```

---

> ⭐ **Key Concept:** Python does not ask whether a value is literally `True` or `False`. In a Boolean context, Python evaluates the value's truthiness.

# 🐍 Falsy Values and the `and` Operator

---

# 🔴 Falsy Values in Python

The following values are considered **Falsy** in Python.

When Python evaluates them in a Boolean context, they behave like:

```text
False
```

---

## 📊 Complete Falsy Values Table

| Falsy Value | Type |
|---|---|
| `False` | `bool` |
| `None` | `NoneType` |
| `0` | `int` |
| `0.0` | `float` |
| `0j` | `complex` |
| `""` | Empty string |
| `[]` | Empty list |
| `()` | Empty tuple |
| `{}` | Empty dictionary |
| `set()` | Empty set |

---

# 🧠 The Easiest Rule for `and`

For:

```python
A and B
```

Python asks:

```text
Is A falsy?
```

---

## If `A` Is Falsy

```text
Return A
```

---

## If `A` Is Truthy

```text
Return B
```

---

# 📖 Examples

## Example 1

```python
10 and 20
```

Python checks:

```text
Is 10 falsy?
```

No.

`10` is truthy.

Therefore:

```text
Return 20
```

### Result

```text
20
```

---

## Example 2

```python
0 and 20
```

Python checks:

```text
Is 0 falsy?
```

Yes.

Therefore:

```text
Return 0
```

### Result

```text
0
```

---

## Example 3

```python
"Python" and "Developer"
```

Python checks:

```text
Is "Python" falsy?
```

No.

Therefore:

```text
Return "Developer"
```

### Result

```text
"Developer"
```

---

## Example 4

```python
"" and "Developer"
```

Python checks:

```text
Is "" falsy?
```

Yes.

Therefore:

```text
Return ""
```

### Result

```text
""
```

---

# ⚠️ Very Important: `bool()` vs `and`

These are different operations.

---

## `bool()`

Consider:

```python
bool(10)
```

Output:

```text
True
```

Why?

Because `bool()` asks:

```text
"What is the Boolean value of 10?"
```

It converts the truthiness of the value into:

```text
True
```

or:

```text
False
```

---

## `and`

Now consider:

```python
10 and 20
```

Output:

```text
20
```

Why?

Because `and` asks:

```text
"Is the first value falsy?"
```

If the first value is not falsy:

```text
Return the second operand.
```

---

# 🧠 Remember This

## `bool(value)`

Converts truthiness into:

```text
True
```

or:

```text
False
```

### Examples

```python
bool(10)
```

```text
True
```

---

```python
bool(0)
```

```text
False
```

---

## `and`

Returns one of the actual operands.

```python
10 and 20
```

```text
20
```

---

```python
0 and 20
```

```text
0
```

---

# 🧠 The Key Difference

| Expression | What Happens | Output |
|---|---|---|
| `bool(0)` | Converts truthiness to Boolean | `False` |
| `0 and 20` | Returns the falsy operand | `0` |
| `bool([])` | Converts truthiness to Boolean | `False` |
| `[] and [1]` | Returns the falsy operand | `[]` |

---

# 🔥 Final Mental Model

```text
bool(value)
```

means:

```text
Tell me whether this value is Truthy or Falsy.
```

Result:

```text
True / False
```

---

```text
A and B
```

means:

```text
If A is falsy → return A
If A is truthy → return B
```

---

# 🏆 One-Line Memory Trick

```text
bool() → tells you the truthiness
```

```text
and → returns an actual operand
```

> ⭐ **Key Concept:** `bool()` converts a value's truthiness into `True` or `False`, while `and` uses truthiness to decide which actual operand to return.


# 🐍 Logical Operator 2: `or`

Python has three main logical operators:

1. `and`
2. `or`
3. `not`

We have already learned the basic concept of:

```python
and
```

Now let's learn:

```python
or
```

from the beginner level.

---

# 1️⃣ What Is `or`?

The `or` operator means:

```text
At least one condition must be True.
```

---

## 🧪 Example

```python
True or False
```

### Result

```text
True
```

Why?

Because at least one side is:

```text
True
```

---

# 2️⃣ Truth Table

| A | B | `A or B` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

---

# ⭐ Main Rule

```text
and → Both must be True
```

```text
or  → At least one must be True
```

---

# 3️⃣ Simple Examples

## Example 1

```python
print(True or True)
```

### Result

```text
True
```

Both values are:

```text
True
```

Therefore:

```text
True or True
        ↓
      True
```

---

## Example 2

```python
print(True or False)
```

### Result

```text
True
```

The first value is already:

```text
True
```

Therefore, the `or` condition is satisfied.

---

## Example 3

```python
print(False or True)
```

### Result

```text
True
```

The second value is:

```text
True
```

Therefore:

```text
False or True
         ↓
       True
```

---

## Example 4

```python
print(False or False)
```

### Result

```text
False
```

Neither value is:

```text
True
```

Therefore:

```text
False or False
          ↓
        False
```

---

# 4️⃣ `or` With Comparisons

Consider:

```python
print(10 > 5 or 10 < 2)
```

Python first evaluates the comparison expressions.

---

## Step 1

```python
10 > 5
```

Result:

```text
True
```

---

## Step 2

```python
10 < 2
```

Result:

```text
False
```

---

## Step 3: Apply `or`

Python now has:

```python
True or False
```

Therefore:

```text
True
```

### Final Result

```text
True
```

---

# 5️⃣ Internal Evaluation

Consider:

```python
x = 10
y = 20

print(x > 5 or y < 10)
```

---

## Step 1: Evaluate the First Comparison

```python
x > 5
```

Substitute the value:

```python
10 > 5
```

Result:

```text
True
```

---

## Step 2: Apply `or`

Python now has:

```text
True or ?
```

Since `or` already has one truthy value:

```text
True
```

the final Boolean result is already known.

Therefore:

```text
True
```

---

# 6️⃣ Important Difference Between `and` and `or`

Consider:

```python
True and False
```

Result:

```text
False
```

But:

```python
True or False
```

Result:

```text
True
```

---

# 🧠 Remember

## `and`

```text
True + False
      ↓
    False
```

Because both values must be true.

---

## `or`

```text
True + False
      ↓
     True
```

Because at least one value is true.

---

# 7️⃣ `or` Also Uses Truthy and Falsy Values

Just like `and`, the `or` operator does not always return:

```text
True
```

or:

```text
False
```

It can return the actual operand.

---

## 🧪 Example

```python
print(10 or 20)
```

### Output

```text
10
```

Why?

Python checks the first value:

```text
10
```

Is `10` truthy?

```text
Yes
```

Therefore, Python returns the first value:

```text
10
```

---

## 🧪 Another Example

```python
print(0 or 20)
```

Python checks:

```text
0 → Falsy
```

Therefore, Python continues to the second value:

```text
20 → Truthy
```

The result is:

```text
20
```

Therefore:

```text
0 or 20
      ↓
     20
```

---

# 8️⃣ Exact Rule for `or`

For:

```python
A or B
```

Python conceptually does:

```text
If A is truthy:
    return A

Otherwise:
    return B
```

---

# ⚖️ Compare With `and`

## `and`

```python
A and B
```

```text
If A is falsy:
    return A

Otherwise:
    return B
```

---

## `or`

```python
A or B
```

```text
If A is truthy:
    return A

Otherwise:
    return B
```

---

# ⭐ Key Difference

| Operator | First Value Is Falsy | First Value Is Truthy |
|---|---|---|
| `and` | Return first value | Return second value |
| `or` | Return second value | Return first value |

---

# 9️⃣ Examples

## Example 1

```python
10 or 20
```

First value:

```text
10 → Truthy
```

Therefore:

```text
Return 10
```

### Result

```text
10
```

---

## Example 2

```python
0 or 20
```

First value:

```text
0 → Falsy
```

Therefore:

```text
Return the second value
```

### Result

```text
20
```

---

## Example 3

```python
"" or "Python"
```

First value:

```text
"" → Falsy
```

Therefore:

```text
Return "Python"
```

### Result

```text
"Python"
```

---

## Example 4

```python
"Python" or "Developer"
```

First value:

```text
"Python" → Truthy
```

Therefore:

```text
Return "Python"
```

### Result

```text
"Python"
```

---

# 🧠 Compare `and` and `or`

| Expression | Result |
|---|---|
| `10 and 20` | `20` |
| `0 and 20` | `0` |
| `10 or 20` | `10` |
| `0 or 20` | `20` |

---

# 🔥 Simple Memory Trick

```text
AND → Find the first Falsy value
```

```text
OR  → Find the first Truthy value
```

---

## `and`

```python
10 and 0 and 20
```

Python searches for the first falsy value:

```text
10 → Truthy
0  → Falsy
```

Result:

```text
0
```

---

## `or`

```python
0 or "" or 20
```

Python searches for the first truthy value:

```text
0  → Falsy
"" → Falsy
20 → Truthy
```

Result:

```text
20
```

---

# ⭐ If No Matching Value Exists

If `and` cannot find a falsy value:

```python
10 and 20 and 30
```

All values are truthy.

Therefore, Python returns the last value:

```text
30
```

---

If `or` cannot find a truthy value:

```python
0 or "" or []
```

All values are falsy.

Therefore, Python returns the last value:

```text
[]
```

---

# 🏆 Final Mental Model

## `and`

```text
Find the first FALSY value.
```

If no falsy value exists:

```text
Return the LAST value.
```

---

## `or`

```text
Find the first TRUTHY value.
```

If no truthy value exists:

```text
Return the LAST value.
```

---

> ⭐ **Key Concept:** `and` searches for the first falsy value, while `or` searches for the first truthy value. Both operators can return actual operands instead of only `True` or `False`.



# 🐍 Logical Operator 3: `not`

Python has three main logical operators:

1. `and`
2. `or`
3. `not`

We have already learned:

```python
and
```

and:

```python
or
```

Now let's learn the third logical operator:

```python
not
```

---

# 1️⃣ What Is `not`?

The `not` operator means:

```text
Reverse the Boolean result.
```

If something is:

```text
True
```

then:

```python
not True
```

becomes:

```text
False
```

If something is:

```text
False
```

then:

```python
not False
```

becomes:

```text
True
```

---

# 2️⃣ Basic Truth Table

| Value | `not value` |
|---|---|
| `True` | `False` |
| `False` | `True` |

---

## Example 1

```python
not True
```

Result:

```text
False
```

---

## Example 2

```python
not False
```

Result:

```text
True
```

---

# 🧠 Main Rule

```text
not → Reverses truthiness
```

```text
Truthy  → False
Falsy   → True
```

---

# 3️⃣ `not` With Comparisons

Consider:

```python
x = 10

print(not x > 5)
```

Python evaluates the expression step by step.

---

## Step 1: Evaluate the Comparison

```python
x > 5
```

Substitute the value of `x`:

```python
10 > 5
```

Result:

```text
True
```

---

## Step 2: Apply `not`

Now Python has:

```python
not True
```

Result:

```text
False
```

---

## Final Result

```text
False
```

Conceptually:

```text
not (10 > 5)
      ↓
    not True
      ↓
     False
```

---

# 4️⃣ Another Example

```python
x = 10

print(not x < 5)
```

---

## Step 1: Evaluate the Comparison

```python
10 < 5
```

Result:

```text
False
```

---

## Step 2: Apply `not`

```python
not False
```

Result:

```text
True
```

---

## Final Output

```text
True
```

---

# 5️⃣ `not` With Truthy and Falsy Values

This is where the previous concept of **Truthy and Falsy** becomes important.

---

## Example 1

```python
print(not 10)
```

Python checks:

```text
10 → Truthy
```

Then:

```text
not Truthy
```

becomes:

```text
False
```

### Output

```text
False
```

---

## Example 2

```python
print(not 0)
```

Python checks:

```text
0 → Falsy
```

Then:

```text
not Falsy
```

becomes:

```text
True
```

### Output

```text
True
```

---

# 6️⃣ `not` With Strings

## Example 1: Empty String

```python
print(not "")
```

An empty string is:

```text
"" → Falsy
```

Therefore:

```text
not False
```

becomes:

```text
True
```

### Output

```text
True
```

---

## Example 2: Non-Empty String

```python
print(not "Python")
```

The string:

```text
"Python"
```

is non-empty.

Therefore:

```text
"Python" → Truthy
```

Then:

```text
not True
```

becomes:

```text
False
```

### Output

```text
False
```

---

# 7️⃣ `not` Always Returns a Boolean

This is an important difference between:

```python
and
```

```python
or
```

and:

```python
not
```

---

## `and`

```python
10 and 20
```

Output:

```text
20
```

`and` can return an actual operand.

---

## `or`

```python
10 or 20
```

Output:

```text
10
```

`or` can return an actual operand.

---

## `not`

```python
not 10
```

Output:

```text
False
```

`not` always returns:

```text
True
```

or:

```text
False
```

---

# 🧠 Important Comparison

| Operator | What It Returns |
|---|---|
| `and` | Can return an actual operand |
| `or` | Can return an actual operand |
| `not` | Always returns `True` or `False` |

---

# 8️⃣ Internal Working

Consider:

```python
x = 10

result = not x
```

Python conceptually evaluates this step by step.

---

## Step 1

```text
x
↓
10
```

---

## Step 2: Check Truthiness

```text
Is 10 truthy?
```

Answer:

```text
Yes
```

---

## Step 3: Apply `not`

```text
not True
```

---

## Step 4: Final Result

```text
False
```

Therefore:

```text
result → False
```

---

# 9️⃣ Important Difference

Consider:

```python
not 10
```

This does **not** mean:

```text
10 → False
```

Python does not change the integer object:

```text
10
```

Instead, Python performs a logical evaluation:

```text
10
↓
Truthy
↓
not Truthy
↓
False
```

The original object remains:

```text
10
```

---

# 🔟 Basic Examples

| Expression | Truthiness of Value | Result |
|---|---|---|
| `not True` | Truthy | `False` |
| `not False` | Falsy | `True` |
| `not 10` | Truthy | `False` |
| `not 0` | Falsy | `True` |
| `not "Python"` | Truthy | `False` |
| `not ""` | Falsy | `True` |
| `not [1, 2]` | Truthy | `False` |
| `not []` | Falsy | `True` |

---

# 🔥 The Simplest Rule

For:

```python
not A
```

Python asks:

```text
Is A truthy?
```

Then reverses the result.

---

## If `A` Is Truthy

```text
A → Truthy
not A → False
```

---

## If `A` Is Falsy

```text
A → Falsy
not A → True
```

---

# 🏆 Final Mental Model

```text
and → Find the first FALSY value
```

```text
or → Find the first TRUTHY value
```

```text
not → REVERSE truthiness
```

---

# ⭐ One-Table Revision

| Operator | Python Checks | Result |
|---|---|---|
| `and` | First falsy value | Can return actual operand |
| `or` | First truthy value | Can return actual operand |
| `not` | Truthiness of one value | Always `True` or `False` |

---

> 🧠 **Key Concept:** `not` does not change the original object. It checks the object's truthiness and returns the opposite Boolean result.

## `not` Operator

The `not` operator reverses the Boolean value of an expression.

| Expression | Result |
|---|---|
| `not True` | `False` |
| `not False` | `True` |
| `not 0` | `True` |
| `not 10` | `False` |
| `not ""` | `True` |
| `not "Python"` | `False` |
| `not []` | `True` |
| `not [1, 2]` | `False` |

### Simple Rule

- If a value is **Truthy**, `not` returns `False`.
- If a value is **Falsy**, `not` returns `True`.

### Example

```python
print(not True)
print(not 0)
print(not "Python")
print(not [])
```

# 🐍 Logical Operators — One-Table Revision

| Operator | Simple Meaning | Python Checks | Example | Result | Return Type |
|---|---|---|---|---|---|
| `and` | Both sides need to be truthy | First falsy value | `10 and 20` | `20` | `int` |
| `and` | Stop at the first falsy value | First falsy value | `0 and 20` | `0` | `int` |
| `and` | Both Boolean values are `True` | Both values | `True and True` | `True` | `bool` |
| `and` | One Boolean value is `False` | Both values | `True and False` | `False` | `bool` |
| `or` | At least one value needs to be truthy | First truthy value | `10 or 20` | `10` | `int` |
| `or` | First value is falsy | Second value | `0 or 20` | `20` | `int` |
| `or` | At least one Boolean value is `True` | Both values | `False or True` | `True` | `bool` |
| `or` | Both Boolean values are `False` | Both values | `False or False` | `False` | `bool` |
| `not` | Reverse truthiness | One value | `not 10` | `False` | `bool` |
| `not` | Reverse falsiness | One value | `not 0` | `True` | `bool` |

---

# 🧠 Truthy and Falsy — Quick Reference

| Value | Result |
|---|---|
| `0` | Falsy |
| `0.0` | Falsy |
| `""` | Falsy |
| `[]` | Falsy |
| `{}` | Falsy |
| `False` | Falsy |
| `10` | Truthy |
| `-10` | Truthy |
| `3.14` | Truthy |
| `"0"` | Truthy |
| `"Python"` | Truthy |
| `[0]` | Truthy |
| `[1, 2]` | Truthy |

---

# 🔥 Three Rules to Remember

```text
and → first FALSY value
or  → first TRUTHY value
not → reverse truthiness
```

---

## Examples

```python
0 and 20       # 0
10 and 20      # 20

0 or 20        # 20
10 or 20       # 10

not 0          # True
not 10         # False
```

---

# ⭐ The Most Important Difference

| Operator | What It Returns |
|---|---|
| `and` | Can return the actual value |
| `or` | Can return the actual value |
| `not` | Always returns `True` or `False` |

---

## Example

```python
print(10 and 20)   # 20
print(0 and 20)    # 0

print(10 or 20)    # 10
print(0 or 20)     # 20

print(not 10)      # False
print(not 0)       # True
```


# 🐍 Logical Operator Precedence

When multiple logical operators appear in one expression, **operator precedence** determines which operator Python evaluates first.

## 🔢 Order of Precedence

```text
1. not
2. and
3. or
```

### 🧠 Memory Trick

```text
NOT
 ↓
AND
 ↓
OR
```

> **Important:** Python does not always evaluate logical expressions simply from left to right. It follows operator precedence.

---

# 🧪 Example 1

```python
True or False and False
```

### Step 1: Evaluate `and` first

```text
False and False
      ↓
    False
```

### Step 2: Evaluate `or`

```text
True or False
     ↓
   True
```

### Final Result

```text
True
```

---

# 🧪 Example 2

```python
not True and False
```

### Step 1: Evaluate `not` first

```text
not True
   ↓
 False
```

### Step 2: Evaluate `and`

```text
False and False
      ↓
    False
```

### Final Result

```text
False
```

---

# 🧪 Example 3

```python
not False or False
```

### Step 1: Evaluate `not` first

```text
not False
    ↓
   True
```

### Step 2: Evaluate `or`

```text
True or False
    ↓
  True
```

### Final Result

```text
True
```

---

# 🧠 One-Table Revision

| Priority | Operator | Meaning |
|---|---|---|
| 1️⃣ | `not` | Reverse truthiness |
| 2️⃣ | `and` | Find the first falsy value |
| 3️⃣ | `or` | Find the first truthy value |

---

# ⭐ The Golden Rule

```text
NOT → AND → OR
```

Python evaluates logical operators in this order:

```text
not
 ↓
and
 ↓
or
```

---

# 🟡 Parentheses Come First

Parentheses have the highest priority.

## Example

```python
(True or False) and False
```

### Step 1: Evaluate the parentheses

```text
True or False
    ↓
  True
```

### Step 2: Evaluate `and`

```text
True and False
     ↓
   False
```

### Final Result

```text
False
```

---

# 🔄 Parentheses Can Change the Result

Compare the following expressions:

## Without Parentheses

```python
True or False and False
```

### Order

```text
False and False
      ↓
    False

True or False
    ↓
  True
```

### Result

```text
True
```

---

## With Parentheses

```python
(True or False) and False
```

### Order

```text
True or False
    ↓
  True

True and False
     ↓
   False
```

### Result

```text
False
```

---

# 🏆 Final Revision

| Priority | Operator | Example | Evaluated First |
|---|---|---|---|
| 1️⃣ | Parentheses `()` | `(True or False)` | Always first |
| 2️⃣ | `not` | `not True` | Second |
| 3️⃣ | `and` | `True and False` | Third |
| 4️⃣ | `or` | `True or False` | Last |

## Remember

```text
()
 ↓
not
 ↓
and
 ↓
or
```

> **Parentheses can override the normal operator precedence and change the result of an expression.**  



# 🐍 Identity Operators in Python

We are starting the next operator category:

```python
is
is not
```

This topic is extremely important because many beginners confuse:

```python
==
```

with:

```python
is
```

---

## 1️⃣ What Are Identity Operators?

Python has two identity operators:

| Operator | Meaning                                                  |
| -------- | -------------------------------------------------------- |
| `is`     | Checks whether two variables reference the same object   |
| `is not` | Checks whether two variables reference different objects |

The key concept is:

> **Same object**

Not:

> **Same value**

---

## 2️⃣ First Understand `==`

Suppose:

```python
x = 10
y = 10
```

You ask:

```python
x == y
```

Python asks:

> Do the values of `x` and `y` compare equal?

Step-by-step:

```text
x == y
  ↓
10 == 10
  ↓
True
```

### Result

```text
True
```

So:

```text
== → Value equality
```

---

## 3️⃣ Now Understand `is`

Suppose:

```python
x = 10
y = 10
```

When you write:

```python
x is y
```

Python asks:

> Do `x` and `y` refer to the exact same object in memory?

So:

```text
== → Same value?
is → Same object?
```

This is the most important difference.

---

## 🧠 Memory Model

Consider:

```python
x = 10
y = x
```

Conceptually:

```text
             ┌──────────┐
x ──────────►│          │
             │    10    │
y ──────────►│          │
             └──────────┘
```

Both names point to the same object.

Therefore:

```python
x == y
```

Output:

```text
True
```

And:

```python
x is y
```

Output:

```text
True
```

Because:

```text
Same value?  → Yes
Same object? → Yes
```

---

# 4️⃣ `==` vs `is`

Consider:

```python
x = 10
y = 10
```

Check:

```python
x == y
```

Python asks:

> Does `10` equal `10`?

Answer:

```text
True
```

Now:

```python
x is y
```

Python asks:

> Are `x` and `y` referencing the same exact object?

Depending on Python's object handling for certain immutable values, they may refer to the same object.

However:

> ⚠️ You should never use `is` to compare normal values.

Use:

```python
x == y
```

for value comparison.

---

# 🚨 The Most Important Example: Lists

Consider:

```python
x = [1, 2, 3]
y = [1, 2, 3]
```

Many beginners think:

```python
x == y
```

and:

```python
x is y
```

will both be `True`.

But:

```python
x == y
```

returns:

```text
True
```

Why?

Because both lists contain the same values:

```python
[1, 2, 3] == [1, 2, 3]
```

But:

```python
x is y
```

returns:

```text
False
```

Why?

Because Python created two different list objects:

```text
       ┌──────────────┐
x ────►│ [1, 2, 3]    │
       └──────────────┘


       ┌──────────────┐
y ────►│ [1, 2, 3]    │
       └──────────────┘
```

The values are equal.

But the objects are different.

Therefore:

```python
x == y    # True
x is y    # False
```

---

## 🧠 Remember This

```text
┌──────────────────────────────┐
│ ==                           │
│                              │
│ "Do they have equal values?" │
└──────────────────────────────┘
```

```text
┌──────────────────────────────┐
│ is                           │
│                              │
│ "Are they the same object?"  │
└──────────────────────────────┘
```

---

# 5️⃣ Same Object Example

Consider:

```python
x = [1, 2, 3]
y = x
```

Now:

```text
       ┌──────────────┐
x ────►│              │
       │ [1, 2, 3]    │
y ────►│              │
       └──────────────┘
```

Both variables reference one list object.

Therefore:

```python
x == y
```

Output:

```text
True
```

And:

```python
x is y
```

Output:

```text
True
```

Because:

```text
Same values?  → True
Same object?  → True
```

---

# 6️⃣ Different Objects, Same Values

Consider:

```python
x = [1, 2, 3]
y = [1, 2, 3]
```

### Memory

```text
x ───► [1, 2, 3]  ← Object A

y ───► [1, 2, 3]  ← Object B
```

Therefore:

```python
x == y
```

Output:

```text
True
```

But:

```python
x is y
```

Output:

```text
False
```

Because:

```text
Same values?  → True
Same object?  → False
```

---

# 🔥 Very Important Rule

## Use `==` for Values

Examples:

```python
age == 18
name == "Gajanand"
marks == 100
```

The question is:

> Do the values match?

---

## Use `is` for Object Identity

The most common use is:

```python
value is None
```

Example:

```python
result = None
```

Later, we can write:

```python
if result is None:
    ...
```

We will learn the `if` syntax later.

For now:

```python
result is None
```

asks:

> Is `result` the exact special `None` object?

---

# 7️⃣ `is not`

`is not` means:

> Are these two variables referencing different objects?

# 🌍 Real-World Python Usage: `None`

This is the most important practical use of:

```python
is not
```

---

## Example

```python
result = None
```

To check whether a value is **not `None`**:

```python
if result is not None:
    print("A result exists")
```

---

## 🤔 Why Do Python Developers Prefer `is not None`?

Python developers prefer:

```python
result is not None
```

instead of:

```python
result != None
```

Because `None` is a special **singleton object** in Python.

---

## 🧠 What Is a Singleton Object?

There is only **one `None` object** in Python:

```text
        None
         ▲
         │
    ┌────┴────┐
    │         │
result      value
```

All references to `None` point to the same special object.

Therefore, identity checking is appropriate:

```python
result is None
```

```python
result is not None
```

---

## 🧠 Memory Trick

| Operator | Question          |
| -------- | ----------------- |
| `==`     | Same value?       |
| `!=`     | Different value?  |
| `is`     | Same object?      |
| `is not` | Different object? |

```text
==       → Same value?
!=       → Different value?
is       → Same object?
is not   → Different object?
```

## Example

```python
x = [1, 2]
y = [1, 2]

x is not y
```

Since they are different list objects:

```text
True
```

---

## Same Object Example

```python
x = [1, 2]
y = x
```

Now:

```python
x is not y
```

returns:

```text
False
```

because they are the same object.

---

## 🧠 Simple Comparison Table

| Code         | Question           | Result         |
| ------------ | ------------------ | -------------- |
| `x == y`     | Same/equal value?  | Value-based    |
| `x is y`     | Same object?       | Identity-based |
| `x != y`     | Different values?  | Value-based    |
| `x is not y` | Different objects? | Identity-based |

---

# 🎯 The Golden Example

Consider:

```python
x = [10, 20]
y = [10, 20]
z = x
```

## Memory

```text
x ───────────────┐
                 ▼
              [10, 20]
                 ▲
z ───────────────┘


y ─────────────► [10, 20]
```

---

## `x == y`

```python
x == y
```

Output:

```text
True
```

Why?

> Same values.

---

## `x is y`

```python
x is y
```

Output:

```text
False
```

Why?

> Different objects.

---

## `x is z`

```python
x is z
```

Output:

```text
True
```

Why?

> Same object.

---

## `x == z`

```python
x == z
```

Output:

```text
True
```

Why?

> Same values too.

---


## 🧠 Simple Quick Revision Table

| Expression   |  Result | Why                      |
| ------------ | ------: | ------------------------ |
| `x == y`     |  `True` | Same values              |
| `x != y`     | `False` | Values are not different |
| `x is y`     | `False` | Different objects        |
| `x is not y` |  `True` | Different objects        |

---

Excellent! Now we start the **last major beginner operator category** before moving into control flow.

# 📚 Membership Operators

```python
in
not in
```

These operators are used **every day** by Python developers.

---

# 1. What are Membership Operators?

Membership operators check **whether a value exists inside a collection**.

A collection can be:

* String
* List
* Tuple
* Set
* Dictionary

Python asks:

> **"Is this value present inside that collection?"**

The answer is always a Boolean:

```python
True
```

or

```python
False
```

---

# 2. Why do we need Membership Operators?

Imagine:

* Is a student's name in the attendance list?
* Is a product in the shopping cart?
* Does a password contain `"@"`?
* Is a city in the supported locations?
* Is `"python"` one of the available courses?

Without membership operators, checking these would be much harder.

---

# 3. Syntax

## `in`

```python
value in collection
```

Python asks:

> "Does this value exist inside this collection?"

---

## `not in`

```python
value not in collection
```

Python asks:

> "Does this value NOT exist inside this collection?"

---

# 4. Internal Working

Example:

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

### Step 1

Python looks at

```text
[10, 20, 30]
```

### Step 2

It starts searching.

```
10 ?
```

Not equal.

↓

```
20 ?
```

Equal!

↓

Stop searching.

Python creates

```python
True
```

and prints it.

---

# Memory Model

```text
numbers
    │
    ▼
+------------------+
| 10 | 20 | 30 |
+------------------+
```

Python checks one element at a time until:

* it finds the value
* or reaches the end

---

# 5. Example with List

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Python thinks

```
Is 20 inside the list?
```

Yes.

Output

```text
True
```

---

Example

```python
numbers = [10, 20, 30]

print(50 in numbers)
```

Python thinks

```
10?

No

20?

No

30?

No

Reached end.
```

Output

```text
False
```

---

# 6. Example with String

```python
name = "Python"

print("P" in name)
```

Python searches

```
P
```

Found.

Output

```text
True
```

---

Example

```python
print("Z" in name)
```

Search

```
P

y

t

h

o

n
```

Not found.

Output

```text
False
```

---

# 7. Example with Tuple

```python
numbers = (10, 20, 30)

print(30 in numbers)
```

Output

```text
True
```

---

# 8. Example with Set

```python
numbers = {10, 20, 30}

print(20 in numbers)
```

Output

```text
True
```

Sets are optimized for very fast membership checks, which is one reason they're useful.

---

# 9. Example with Dictionary

This is very important.

```python
student = {
    "name": "Gajanand",
    "age": 22
}

print("name" in student)
```

Output

```text
True
```

### Why?

Python checks **dictionary keys**, not values.

Keys:

```
name
age
```

---

Example

```python
print("Gajanand" in student)
```

Output

```text
False
```

Even though `"Gajanand"` is stored in the dictionary, it is a **value**, not a key.

Later, when we study dictionaries in depth, we'll learn how to check values as well.

---

# 10. `not in`

Example

```python
numbers = [10, 20, 30]

print(50 not in numbers)
```

Python asks

```
Is 50 NOT inside the list?
```

Yes.

Output

```text
True
```

---

Example

```python
print(20 not in numbers)
```

Python asks

```
Is 20 NOT inside the list?
```

No.

Output

```text
False
```

---

# 11. Real-World Examples

### Login System

```python
allowed_users = ["Alice", "Bob", "Charlie"]

"Bob" in allowed_users
```

Meaning:

```
Is Bob allowed?
```

---

### Shopping Cart

```python
cart = ["Milk", "Bread", "Eggs"]

"Milk" in cart
```

Meaning:

```
Is Milk in the cart?
```

---

### Password Validation

```python
password = "Hello@123"

"@" in password
```

Meaning:

```
Does the password contain @?
```

---

### Course Platform

```python
courses = ["Python", "Java", "C++"]

"Python" in courses
```

Meaning:

```
Is Python available?
```

---

# 🧠 Memory Trick

| Operator | Python asks                |
| -------- | -------------------------- |
| `in`     | Does this value exist?     |
| `not in` | Does this value NOT exist? |

---

# ⚠ Common Beginner Mistakes

### ❌ Mistake 1

Thinking `in` compares object identity.

No.

It checks **membership**, not memory identity.

---

### ❌ Mistake 2

Thinking dictionaries search values.

```python
student = {
    "name": "Gajanand"
}
```

```python
"Gajanand" in student
```

returns

```text
False
```

because Python checks keys by default.

---

### ❌ Mistake 3

Confusing `==` with `in`.

```python
numbers = [10, 20, 30]
```

```python
20 == numbers
```

asks:

```
Is 20 equal to the entire list?
```

Answer:

```text
False
```

Whereas:

```python
20 in numbers
```

asks:

```
Is 20 one of the elements in the list?
```

Answer:

```text
True
```

---

# 📋 Revision Table

| Operator | Python asks                                      | Returns          |
| -------- | ------------------------------------------------ | ---------------- |
| `in`     | Does this value exist inside the collection?     | `True` / `False` |
| `not in` | Does this value NOT exist inside the collection? | `True` / `False` |


# Problem 1

```python
USN = [101, 102, 103, 104]
print(101 in USN)
```

---

## Step 1: Python creates the list

Memory:

```text
USN
 │
 ▼
+------------------------+
| 101 | 102 | 103 | 104 |
+------------------------+
```

`USN` stores a reference to the list object.

---

## Step 2: Python evaluates

```python
101 in USN
```

Python asks:

> "Is **101** one of the elements inside this list?"

---

## Step 3: Search starts

Python checks one element at a time.

```text
101 ?

↓

Found ✅

↓

Stop searching
```

Python doesn't continue because it already found the answer.

---

## Step 4: Python creates a Boolean object

```python
True
```

---

## Output

```text
True
```

---

# Problem 2

```python
name = "PYTHON"
print("P" in name)
```

---

## Step 1

Python creates a string object.

Memory

```text
name
 │
 ▼
+-------------------+
| P | Y | T | H | O | N |
+-------------------+
```

Strings are sequences of characters.

---

## Step 2

Python evaluates

```python
"P" in name
```

Python asks

> "Is the character **P** inside this string?"

---

## Step 3

Search

```text
P ?

↓

Found ✅

↓

Stop
```

---

## Step 4

Creates

```python
True
```

---

## Output

```text
True
```

---

# Problem 3

```python
name = "PYTHON"

print("Z" in name)
```

---

## Memory

```text
P
Y
T
H
O
N
```

---

## Python asks

> "Is Z inside this string?"

---

Search

```text
P ?

No

↓

Y ?

No

↓

T ?

No

↓

H ?

No

↓

O ?

No

↓

N ?

No

↓

Reached end
```

Nothing matched.

Python creates

```python
False
```

---

## Output

```text
False
```

---

# Problem 4

```python
Numbers = [1,2,3,4,5,6,7,8,9,0]

print(1 not in Numbers)
```

---

## Memory

```text
Numbers
 │
 ▼
+------------------------------+
|1|2|3|4|5|6|7|8|9|0|
+------------------------------+
```

---

Python first evaluates

```python
1 in Numbers
```

Search

```text
1 ?

↓

Found
```

So

```python
1 in Numbers
```

becomes

```python
True
```

Now Python applies

```python
not True
```

which becomes

```python
False
```

---

## Output

```text
False
```

---

# Problem 5

```python
Numbers = [0,9,8,7,6,5,4,3,2,1]

print(1 in Numbers)
```

Notice something important.

Many beginners think because **1 is last**, Python returns False.

No.

Python simply searches until it finds it.

---

Memory

```text
0
9
8
7
6
5
4
3
2
1
```

Search

```text
0 ?

No

↓

9 ?

No

↓

8 ?

No

↓

...

↓

1 ?

Yes

↓

Stop
```

---

Output

```text
True
```

---

# Problem 6

```python
Student = {
    "Name": "Gajanand",
    "USN": "1NH23AI406"
}

print("USN" in Student)
```

---

## Memory

```text
Student
 │
 ▼

+----------------------------------+
| "Name" ─────► "Gajanand"         |
| "USN"  ─────► "1NH23AI406"       |
+----------------------------------+
```

Notice there are two parts.

Key

```text
Name
USN
```

Value

```text
Gajanand
1NH23AI406
```

---

Python asks

> "Is **USN** one of the keys?"

Search

```text
Name ?

No

↓

USN ?

Yes
```

Stop.

---

Output

```text
True
```

---

# Problem 7

```python
student = {
    "name": "Gajanand",
    "age": 22
}

print("Gajanand" in student)
```

---

Memory

```text
+------------------------------+
| name ─────► Gajanand         |
| age  ─────► 22               |
+------------------------------+
```

Python asks

> "Is **Gajanand** one of the keys?"

Search

```text
name ?

No

↓

age ?

No

↓

End
```

Notice

Python **never checks the values**.

It only checks

```text
Keys

name
age
```

Therefore

```python
False
```

---

## Output

```text
False
```

---

# 🔥 Universal Membership Evaluation Process

Whenever Python sees:

```python
value in collection
```

it always follows this process:

```text
                value in collection
                       │
                       ▼
         Evaluate the left value
                       │
                       ▼
      Evaluate the right collection
                       │
                       ▼
      What type of collection is it?
                       │
      ┌────────┬────────┬────────┬──────────┐
      ▼        ▼        ▼        ▼
    List    String    Tuple     Set
      │        │        │        │
 Search  Search   Search   Search elements
 elements chars   elements (fast hash lookup)
                       │
                       ▼
                 Dictionary?
                       │
                       ▼
                Search KEYS only
                       │
                       ▼
                 Found?
              ┌──────────┐
          Yes ▼          ▼ No
         Return True   Return False
```

### One-line memory rule

| Collection | What `in` checks |
| ---------- | ---------------- |
| String     | Characters       |
| List       | Elements         |
| Tuple      | Elements         |
| Set        | Elements         |
| Dictionary | **Keys only**    |





# 📚 Bitwise Operators 

---

# 🚨 Before Learning Bitwise Operators


Think of it like this:

```text
Arithmetic Operators
        ↓
Decimal Numbers (0-9)

Bitwise Operators
        ↓
Binary Numbers (0 and 1)
```

Everything in a computer is stored as **0s and 1s**.

---

# What are Bitwise Operators?

Bitwise Operators perform operations on **individual bits** of an integer.

Instead of thinking:

```text
10
20
```

Python thinks:

```text
10

↓

1010
```

and

```text
20

↓

10100
```

Then it compares **each bit**.

---

# Why do we need them?

Normally we work with numbers.

Example

```python
10 + 20
```

Python performs arithmetic.

But sometimes we need to work directly with the bits stored in memory.

Examples:

* Operating Systems
* Device Drivers
* Networking
* File Permissions
* Compression Algorithms
* Encryption
* Graphics Programming
* Embedded Systems
* Game Development
* Performance Optimization

Even if you don't use them daily, interviewers often ask about them.

---

# First We Must Learn Binary Numbers

We normally count like this:

```text
Decimal

0
1
2
3
4
5
6
7
8
9
10
11
12
```

This is called **Base 10** because it uses **10 digits**:

```text
0 1 2 3 4 5 6 7 8 9
```

---

# Computers Count Differently

Computers only understand two states.

```text
OFF

ON
```

or

```text
0

1
```

Therefore computers use **Base 2**, called **Binary**.

Binary has only two digits:

```text
0

1
```

---

# Counting in Binary

```text
Decimal     Binary

0           0
1           1
2           10
3           11
4           100
5           101
6           110
7           111
8           1000
9           1001
10          1010
```

Notice something interesting.

After

```text
1
```

there is no digit

```text
2
```

because binary only has

```text
0

1
```

So it becomes

```text
10
```

---

# Why is Decimal 10 Binary 1010?

Let's understand.

Every position in binary has a value.

```text
Bit Position

8    4    2    1
```

Now write

```text
1010
```

```text
8    4    2    1

1    0    1    0
```

Now multiply.

```text
1 × 8 = 8

0 × 4 = 0

1 × 2 = 2

0 × 1 = 0
```

Total

```text
8 + 2

=

10
```

That's why

```text
1010

=

10
```

---

# Another Example

Binary

```text
1101
```

Positions

```text
8    4    2    1

1    1    0    1
```

Calculation

```text
8

+

4

+

0

+

1

=

13
```

So

```text
1101

=

13
```

---

# Memory Representation

Suppose

```python
x = 10
```

You see

```text
10
```

Python stores it (conceptually) as binary.

```text
1010
```

In memory (using 8 bits for illustration):

```text
00001010
```

```text
x
 │
 ▼

00001010
```

This binary representation is what Bitwise Operators work with.

---

# Important Terminology

## Bit

A single binary digit.

```text
0

or

1
```

One digit = One Bit

---

## Byte

Eight bits together.

```text
00001010
```

This is **8 bits**, which is **1 byte**.

---

# Revision Table

| Term             | Meaning                                         |
| ---------------- | ----------------------------------------------- |
| Decimal          | Base 10 (0–9)                                   |
| Binary           | Base 2 (0 and 1)                                |
| Bit              | One binary digit                                |
| Byte             | 8 bits                                          |
| Bitwise Operator | Works on binary bits instead of decimal numbers |

---

# 🧠 Memory Trick

```text
Arithmetic Operators

↓

Work on Numbers

10

20

30

-------------------------

Bitwise Operators

↓

Work on Bits

1010

1100

0011
```

---

## 📝 Practice (Don't use a calculator)

Convert these decimal numbers to binary.

1. Decimal **2** = ?
2. Decimal **5** = ?
3. Decimal **7** = ?
4. Decimal **9** = ?
5. Decimal **12** = ?
6. Decimal **15** = ?

Once you're comfortable converting between decimal and binary, learning `&`, `|`, `^`, `~`, `<<`, and `>>` becomes much easier because you'll be able to see exactly what Python is doing bit by bit.

Yes! There is a simple algorithm, and it's the one every programmer learns.

There are **three common methods** to find the binary representation of a decimal number.

---

# Method 1 (Most Important) ⭐⭐⭐⭐⭐

## Repeated Division by 2

This is the standard algorithm.

### Steps

1. Divide the number by **2**.
2. Write down the **remainder** (`0` or `1`).
3. Divide the quotient by **2** again.
4. Repeat until the quotient becomes **0**.
5. Read the remainders **from bottom to top**.

---

## Example: Decimal 10

| Division | Quotient | Remainder |
| -------: | -------: | --------: |
|   10 ÷ 2 |        5 |     **0** |
|    5 ÷ 2 |        2 |     **1** |
|    2 ÷ 2 |        1 |     **0** |
|    1 ÷ 2 |        0 |     **1** |

Now read the remainders **bottom → top**:

```text
1 0 1 0
```

So,

```text
Decimal 10 = Binary 1010
```

---

## Example: Decimal 13

| Division | Quotient | Remainder |
| -------: | -------: | --------: |
|   13 ÷ 2 |        6 |     **1** |
|    6 ÷ 2 |        3 |     **0** |
|    3 ÷ 2 |        1 |     **1** |
|    1 ÷ 2 |        0 |     **1** |

Read bottom → top:

```text
1101
```

Therefore,

```text
13 = 1101
```

---

# Why Does This Work?

Every division by 2 extracts one binary digit.

* Remainder `0` means the current bit is `0`.
* Remainder `1` means the current bit is `1`.

Reading from the bottom reconstructs the binary number from the most significant bit to the least significant bit.

---

# Method 2 (Using Powers of 2) ⭐⭐⭐⭐

This is excellent for checking your answer mentally.

Find the largest power of 2 less than or equal to the number.

Example: **13**

Powers of 2:

```text
1   2   4   8   16
```

13 fits into:

```text
8 ✓
```

Remaining:

```text
13 - 8 = 5
```

5 fits into:

```text
4 ✓
```

Remaining:

```text
5 - 4 = 1
```

1 fits into:

```text
1 ✓
```

Now fill the positions:

|  8 |  4 |  2 |  1 |
| -: | -: | -: | -: |
|  1 |  1 |  0 |  1 |

Result:

```text
1101
```

---

# Method 3 (Python)

Python can do it automatically.

```python
print(bin(10))
```

Output:

```text
0b1010
```

The prefix `0b` means:

```text
Binary Number
```

So,

```text
0b1010
```

is simply

```text
1010
```

---

# 🧠 Memory Trick

Whenever you need to convert **Decimal → Binary**:

```text
Divide by 2
↓

Write the remainder

↓

Repeat until quotient = 0

↓

Read remainders from bottom to top
```

This is the algorithm used in schools, colleges, interviews, and computer science courses.

---

# Let's Practice

Without using Python or a calculator, convert these using the **division by 2** method:

1. **6**
2. **11**
3. **18**
4. **25**

Write the division table just like we did above. Once you master this method, understanding `&`, `|`, `^`, `~`, `<<`, and `>>` becomes much easier.

---

| Decimal | Your Binary | Correct |
| ------: | :---------: | :-----: |
|       6 |     110     |    ✅    |
|      11 |     1011    |    ✅    |
|      18 |    10010    |    ✅    |
|      25 |    11001    |    ✅    |

Now let's learn the **power-of-2 method** properly. Most beginners get confused because nobody explains **how to choose the powers**.

---

# Step 1: Memorize the Powers of 2

You **must** memorize this table.

| Power | Value |
| ----: | ----: |
|    2⁰ |     1 |
|    2¹ |     2 |
|    2² |     4 |
|    2³ |     8 |
|    2⁴ |    16 |
|    2⁵ |    32 |
|    2⁶ |    64 |
|    2⁷ |   128 |
|    2⁸ |   256 |
|    2⁹ |   512 |

Don't calculate these every time. Just know them.

---

# Step 2: Find the Largest Power ≤ Number

This is where you were stuck.

Suppose the number is:

```text
25
```

Look at the powers:

```text
1
2
4
8
16
32
```

Ask yourself:

> **Which is the largest power of 2 that is NOT bigger than 25?**

```text
32 ❌ Too big

16 ✅ Yes
```

So we start from **16**.

---

# Example 1: 25

Write the powers from largest to smallest.

| 16 |  8 |  4 |  2 |  1 |
| -: | -: | -: | -: | -: |

Now ask:

### Can I use 16?

```text
25 ≥ 16

Yes
```

Write **1**.

Remaining:

```text
25 - 16 = 9
```

| 16 |  8 |  4 |  2 |  1 |
| -: | -: | -: | -: | -: |
|  1 |    |    |    |    |

---

### Can I use 8?

Remaining is **9**.

```text
9 ≥ 8

Yes
```

Write **1**.

Remaining:

```text
9 - 8 = 1
```

| 16 |  8 |  4 |  2 |  1 |
| -: | -: | -: | -: | -: |
|  1 |  1 |    |    |    |

---

### Can I use 4?

Remaining:

```text
1 ≥ 4 ?

No
```

Write

```text
0
```

---

### Can I use 2?

```text
1 ≥ 2 ?

No
```

Write

```text
0
```

---

### Can I use 1?

```text
1 ≥ 1

Yes
```

Write

```text
1
```

Final answer:

| 16 |  8 |  4 |  2 |  1 |
| -: | -: | -: | -: | -: |
|  1 |  1 |  0 |  0 |  1 |

Binary:

```text
11001
```

---

# Example 2: 18

Largest power ≤ 18?

```text
32 ❌

16 ✅
```

Start.

| 16 |  8 |  4 |  2 |  1 |
| -: | -: | -: | -: | -: |

Remaining = 18

---

Can use 16?

Yes.

Write

```text
1
```

Remaining

```text
2
```

---

Can use 8?

```text
2 ≥ 8 ?

No
```

Write

```text
0
```

---

Can use 4?

No

Write

```text
0
```

---

Can use 2?

Yes

Write

```text
1
```

Remaining

```text
0
```

---

Can use 1?

No

Write

```text
0
```

Final

| 16 |  8 |  4 |  2 |  1 |
| -: | -: | -: | -: | -: |
|  1 |  0 |  0 |  1 |  0 |

Binary

```text
10010
```

---

# Example 3: 11

Largest power ≤ 11?

```text
16 ❌

8 ✅
```

|  8 |  4 |  2 |  1 |
| -: | -: | -: | -: |

Remaining = 11

---

8?

Yes

Remaining = 3

Write

```text
1
```

---

4?

```text
3 ≥ 4 ?

No
```

Write

```text
0
```

---

2?

Yes

Remaining = 1

Write

```text
1
```

---

1?

Yes

Remaining = 0

Write

```text
1
```

Final

```text
1011
```

---

# The Thinking Pattern

Whenever you convert a decimal number:

```text
Step 1

Find largest power of 2 ≤ number

↓

Step 2

Subtract it

↓

Step 3

Move to next smaller power

↓

If remaining ≥ power

↓

Write 1

Else

↓

Write 0

↓

Repeat until 1
```

---

# Why Does This Work?

Each binary digit tells Python:

```text
Should I include this power of 2?
```

Example:

```text
25
```

| Power | 16 |  8 |  4 |  2 |  1 |
| ----: | -: | -: | -: | -: | -: |
|   Bit |  1 |  1 |  0 |  0 |  1 |

This means:

```text
Use 16 ✔

Use 8 ✔

Don't use 4 ✘

Don't use 2 ✘

Use 1 ✔
```

Now add them:

```text
16 + 8 + 1

=

25
```

That's all binary really is—a compact way of saying **which powers of 2 are included**.

---

## 🧠 Memory Trick

Think of the binary digits as **Yes/No switches**:

```text
Power of 2:   16    8    4    2    1
Include it?    ✔    ✔    ✘    ✘    ✔
Bit:           1    1    0    0    1
```

`1` means **"Yes, include this power."**

`0` means **"No, don't include this power."**


