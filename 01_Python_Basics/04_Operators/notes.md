# Operators

## Goal
Learn how Python performs calculations, comparisons, and logical decisions.

---

## Example

```python
10 + 20
```

Python sees:

```
Integer Object + Integer Object → New Integer Object
```

> **Note:** Operators work on **objects**, not variables. Variables only help Python locate those objects.

---

# Types of Operators

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

---

# 1. Arithmetic Operators

## 1️⃣ Definition

**Operator:** A symbol that tells Python to perform an operation on one or more objects.

### Example

```python
5 + 3
```

Here, `+` is the operator.

### Real-Life Example

```
5 Apples + 3 Apples = 8 Apples
```

The `+` tells you what operation to perform. Python operators work the same way.

---

## 2️⃣ Types of Arithmetic Operators

| Operator | Name |
|----------|------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor Division |
| `%` | Modulus |
| `**` | Exponent |

We'll learn each one in detail.

---

# 3️⃣ Addition (`+`)

### Definition

Adds two numeric objects.

### Syntax

```python
a + b
```

### Example

```python
10 + 20
```

**Output**

```python
30
```

## Internal Working

```python
x = 10
y = 20
z = x + y
```

Python performs these steps:

1. `x = 10` → Creates an Integer Object (`10`)
2. `y = 20` → Creates another Integer Object (`20`)
3. `z = x + y`
   - Finds the object referenced by `x`
   - Finds the object referenced by `y`
   - Performs addition
   - Creates a **new Integer Object** (`30`)

### Memory

```
x ─► 10
y ─► 20
z ─► 30
```

> **Notice:** Objects `10` and `20` are unchanged. Python creates a new object (`30`).

### Example 2

```python
5 + 2.5
```

**Output**

```python
7.5
```

**Type:** `float`

**Why?** Python performs **implicit type conversion**, converting the integer to a float before addition.

---

# 4️⃣ Subtraction (`-`)

### Definition

Subtracts the second object from the first.

### Syntax

```python
a - b
```

### Example

```python
20 - 5
```

**Output**

```python
15
```

Python creates a **new Integer Object**.

---

# 5️⃣ Multiplication (`*`)

### Definition

Multiplies two numeric objects.

### Example

```python
5 * 4
```

**Output**

```python
20
```

Python creates a **new Integer Object**.

---

# 6️⃣ Division (`/`)

> **Important Rule:** `/` always returns a **float**.

### Example

```python
10 / 2
```

**Output**

```python
5.0
```

Even this:

```python
8 / 4
```

returns

```python
2.0
```

### Why?

Division can produce decimal values. Python always returns a float to keep the result consistent.

---

# 7️⃣ Floor Division (`//`)

### Definition

Returns the quotient after removing the fractional part.

### Example

```python
10 // 3
```

```
10 / 3 = 3.333...
Floor Division = 3
```

### Example

```python
17 // 5
```

```
17 / 5 = 3.4
Floor Division = 3
```

> **Important:** Floor division is **not rounding**. It always moves down to the nearest integer.

---

# 8️⃣ Modulus (`%`)

### Definition

Returns the remainder after division.

### Example

```python
10 % 3
```

```
10 = (3 × 3) + 1
```

**Output**

```python
1
```

### Example

```python
20 % 5
```

**Output**

```python
0
```

because there is no remainder.

### Why is `%` Important?

It is heavily used in DSA problems such as:

- Even/Odd Numbers
- Circular Arrays
- Hashing
- Cyclic Problems

---

# 9️⃣ Exponent (`**`)

### Definition

Raises a number to the power of another number.

### Example

```python
2 ** 3
```

means

```
2 × 2 × 2
```

**Output**

```python
8
```

### Example

```python
5 ** 2
```

**Output**

```python
25
```

---

# 📌 Summary Table

| Operator | Name | Example | Output |
|:--------:|----------------|:-------:|:------:|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 3` | `2.0` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus | `7 % 2` | `1` |
| `**` | Exponent | `2 ** 4` | `16` |

---

# 🚫 Common Beginner Mistakes

### Mistake 1

Thinking:

```python
10 / 2
```

returns

```python
5
```

❌ Wrong

It returns

```python
5.0
```

---

### Mistake 2

Confusing `/` and `//`

| Operator | Meaning |
|----------|---------|
| `/` | Normal Division |
| `//` | Floor Division |

---

### Mistake 3

Thinking `%` returns the quotient.

❌ Wrong.

It returns the **remainder**.

---

# 🎤 Interview Question

### Q. Why does `/` always return a float in Python?

### Answer

The `/` operator performs **true division**. Python always returns a float because division can produce fractional values, and using a consistent return type avoids ambiguity.



What does % 100 mean?

Think of it this way:

% 10   → keep last 1 digit

% 100  → keep last 2 digits

% 1000 → keep last 3 digits

% 10000 → keep last 4 digits

Examples
583 % 10
Output: 3

583 % 100
Output: 83

583 % 1000
Output: 583

Notice the pattern?

The number after % determines how many digits you keep when it's a power of 10.


🎯 Interview Tip

If an interviewer asks:

"How do you extract the last k digits of a number?"

The general formula is:

number % (10 ** k)

Examples:

number % 10       # Last 1 digit
number % 100      # Last 2 digits
number % 1000     # Last 3 digits
number % 10000    # Last 4 digits

This pattern appears frequently in DSA and number-based interview questions.


# Printing Last Number
number = 987654

last_two_digits = number % 100

print(last_two_digits)

# Remove the Last Two Digits 
N =  987654

Left_No = N // 100

print(f"{Left_No}\n")

# Dry Run Of Code 

 🧠 Dry Run

 # Step 1
 N = 987654

 Python creates an Integer Object.

 Memory:
 N
 │
 ▼
 987654

 # Step 2
 Left_No = N // 100

 Python performs:

 987654 // 100

 Think of it as:
 987654 ÷ 100
 ↓
 9876.54
 ↓
 9876

 Since // is floor division, Python removes the decimal part.

 Python creates a new Integer Object.

 Memory:

 N                 Left_No
 │                    │
 ▼                    ▼
 987654             9876

 # Step 3
 print(Left_No)

 Output: 9876 


# 📖 Theory

Let's make this a rule you can remember forever.

When should you use //?

Use // when the question asks you to:

Remove digits
Find the quotient
Count complete groups

# Examples:

987654

↓

Remove last digit

98765
987654 // 10
987654

↓

Remove last two digits

9876
987654 // 100
987654

↓

Remove last three digits

987
987654 // 1000

# 🧠 Memory Trick
Question says...

REMOVE
↓

Use //

--------------------

Question says...

KEEP / EXTRACT
↓

Use %

# Example:

Number = 987654

Keep last two digits

↓

54

↓

%100
Number = 987654

Remove last two digits

↓

9876

↓

//100
# 📈 Complexity

Your code performs one arithmetic operation.

Time Complexity
O(1)

One operation.

Space Complexity
O(1)

One extra variable.

# 🎯 Interview Question

If the interviewer asks:

How do you remove the last k digits?

General formula:

number // (10 ** k)

# Examples:

number // 10

Remove last digit.

number // 100

Remove last two digits.

number // 1000

Remove last three digits.

This is a very common DSA pattern.

#########################################################################################################
# Assignment Operators
#########################################################################################################

Assignment Operators

This chapter is much shorter, but very important.

1️⃣ Definition
What is an Assignment Operator?
Definition

An assignment operator is used to assign a value to a variable or update the value that a variable refers to.

The simplest assignment operator is:

=

Example:

x = 10

Python creates an integer object 10, and x becomes a reference to it.

2️⃣ Why Do We Need Assignment Operators?

Imagine this code:

x = 10

x = x + 5

It works.

But Python gives us a shorter way:

x += 5

Both produce the same result.

Assignment operators make code:

shorter
easier to read
less repetitive
3️⃣ Types of Assignment Operators
| Operator | Meaning                 |
| -------- | ----------------------- |
| `=`      | Assign                  |
| `+=`     | Add and assign          |
| `-=`     | Subtract and assign     |
| `*=`     | Multiply and assign     |
| `/=`     | Divide and assign       |
| `//=`    | Floor divide and assign |
| `%=`     | Modulus and assign      |
| `**=`    | Exponent and assign     |


We'll learn them one by one.

4️⃣ The = Operator (Revision)

You already know this.

Example:

x = 10

Memory:

x
│
▼
10

Now:

x = 20

Memory:

Old object: 10

New object: 20

x
│
▼
20

Notice:

The integer object 10 is not changed.

x now refers to a new integer object.

This connects to everything we've learned about objects and references.

5️⃣ The += Operator

Example:

x = 10

x += 5

Many beginners think:

"Python changes the integer object 10."

❌ That's not what happens.

Let's dry run it.

Step 1
x = 10

Memory:

x
│
▼
10
Step 2
x += 5

Python internally treats it like:

x = x + 5

It:

Reads the object referenced by x (10)
Creates the result 15
Creates a new integer object 15
Makes x refer to 15

Memory:

Before

x
│
▼
10


After

x
│
▼
15

The object 10 was never modified.

########################################################################################################
# Comparison Operators
########################################################################################################


Lesson 1: Introduction
1️⃣ Definition

What is a Comparison Operator?

A comparison operator compares two objects (values).

After comparing them, Python returns only one of two Boolean values:

True

or

False

Comparison operators never return numbers. They always return a Boolean result.

2️⃣ Why Do We Need Comparison Operators?

Imagine you're building:

Login system
ATM
Online shopping
Student marks calculator
Age verification
Password checker

Questions like these appear:

Is age greater than 18?

Is password correct?

Are two numbers equal?

Does user have enough balance?

A computer must answer these with Yes or No.

In Python:

Yes  → True

No   → False

Comparison operators let Python make these decisions.

Types of Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal to              |
| `!=`     | Not equal to          |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

First Operator — == (Equal To)
Definition

Checks whether two objects have the same value.

Syntax
left == right

Python compares the values of both objects.

If they are equal:

True

Otherwise:

False
5️⃣ Internal Working

Example:

x = 10
y = 10

print(x == y)
Step 1
x = 10

Memory:

x
│
▼
10
Step 2
y = 10

Memory:

x ─┐
   │
   ▼
 10
 ▲
 │
 y

(Both variables may refer to the same integer object.)

Step 3
x == y

Python asks:

Does the value of x equal the value of y?

Answer:

10 == 10

↓

True

Python creates a Boolean object:

True

Then print() displays:

True
⭐ Important Theory

Remember this forever:

=

means

Assign

Example:

x = 10
==

means

Compare

Example:

x == 10

This is one of the most common beginner mistakes.

🧠 Memory Trick
=     → Give / Assign

==    → Ask / Compare

Think of it like this:

Teacher gives marks

↓

=

Teacher asks

"Did you score 90?"

↓

==

###################################################################
# 📝 Revision Notes (Write these in your notebook)
###################################################################

Comparison Operator ==
Definition

== compares the values of two objects.

It does not check whether they are the same object in memory.

Syntax
left == right
Return Type

Always returns a Boolean object.

True

or

False
Examples
10 == 10

↓

True
10 == 20

↓

False
10 == 10.0

↓

True

because both represent the same numeric value.

10 == "10"

↓

False

because one is an integer and the other is a string.

"Python" == "python"

↓

False

because Python is case-sensitive.


# Comparison Operator — != (Not Equal)

1. Definition

The != operator checks whether two values are different.

If the values are different:

True

If the values are the same:

False

Just like ==, it returns a Boolean object.

2. Why Do We Need It?

Imagine a login system.

password = "python123"

user_input = "hello123"

We want to know:

"Is the entered password different from the real password?"

Python can ask:

user_input != password

Result:

True

because the passwords are different.

Real-life uses:

Password validation
Username checking
Detecting changes
Form validation
Comparing old and new values
3. Syntax
left != right

Read it as:

"Left is not equal to right."

4. Internal Working

Example:

x = 50
y = 20

print(x != y)
Step 1

Python creates an integer object:

50

and x refers to it.

Step 2

Python creates another integer object:

20

and y refers to it.

Step 3

Python asks:

Is 50 different from 20?

Answer:

Yes

Python creates a Boolean object:

True

print() displays:

True


5. Compare == and !=
| Expression | Question Python Asks | Result  |
| ---------- | -------------------- | ------- |
| `10 == 10` | Are they equal?      | `True`  |
| `10 != 10` | Are they different?  | `False` |
| `10 == 20` | Are they equal?      | `False` |
| `10 != 20` | Are they different?  | `True`  |

Notice that != is the opposite of ==.


6. Common Beginner Mistake

Some beginners think:

!=

means

"Not"

❌ Incorrect.

It means

Not Equal To

It always compares two values.
#########################################################################################################

# ">" Greater Than  Operator  
1️⃣ Definition

The > operator checks whether the left value is greater than the right value.

If it is greater:

True

Otherwise:

False

Like all comparison operators, it always returns a Boolean object.

2️⃣ Why Do We Need It?

Imagine these situations:

Is age greater than 18?
Is salary greater than ₹50,000?
Is the exam score greater than the passing mark?
Is today's temperature greater than yesterday's?

These are all comparisons.

Example:

age = 21

age > 18

Python asks:

Is 21 greater than 18?

Answer:

True
3️⃣ Syntax
left > right

Read it as:

Left is greater than right.

4️⃣ Internal Working

Example:

x = 15
y = 10

print(x > y)
Step 1

Python creates an integer object:

15

x refers to it.

Step 2

Python creates another integer object:

10

y refers to it.

Step 3

Python asks:

Is 15 greater than 10?

Answer:

Yes

Python creates the Boolean object:

True

print() displays:

True
Another Example
x = 5
y = 20

print(x > y)

Python asks:

Is 5 greater than 20?

Answer:

No

Python creates:

False
5️⃣ Number Line Thinking

This helps a lot.

← Smaller ---------------------------- Greater →

1   2   3   4   5   6   7   8   9   10

Example:

8 > 3

On the number line:

3 --------> 8

8 is to the right of 3.

Result:

True

Example:

2 > 9

2 is to the left of 9.

Result:

False
6️⃣ Strings

Python can also compare strings.

It compares them alphabetically (lexicographically) based on character values.

For now, we'll focus on numbers only.

We'll learn string comparison in depth when we study strings.

7️⃣ Common Beginner Mistakes
Mistake 1

Thinking:

5 > 5

is

True

❌ Wrong.

Python asks:

Is 5 greater than 5?

No.

They are equal.

Result:

False

Mistake 2

Confusing > with >=.

We'll learn >= later.

For now:

5 > 5

↓

False

#########################################################################################################

#  🐍 Comparison Operator <
1️⃣ Definition

The < operator checks whether the left value is less than the right value.

If yes:

True

Otherwise:

False

Like every comparison operator, it always returns a Boolean object.

2️⃣ Why Do We Need It?

Real-life examples:

Is the temperature below 0°C?
Is the student's age less than 18?
Is the stock price lower than yesterday?
Is the account balance below ₹100?

Example:

balance = 80

balance < 100

Python asks:

Is 80 less than 100?

Answer:

True
3️⃣ Syntax
left < right

Read it as:

Left is less than right.

4️⃣ Internal Working

Example

x = 4
y = 9

print(x < y)
Step 1

Python creates an integer object

4

x refers to it.

Step 2

Python creates another integer object

9

y refers to it.

Step 3

Python asks:

Is 4 less than 9?

Answer:

Yes

Python creates a Boolean object:

True

print() displays:

True
Another Example
x = 20
y = 5

print(x < y)

Python asks:

Is 20 less than 5?

Answer:

No

Result:

False
5️⃣ Number Line Thinking

Remember this forever.

← Smaller ---------------------- Greater →

-5  -4  -3  -2  -1   0   1   2   3   4   5

A number is less than another number if it is to the left.

Example

2 < 8
2 --------> 8

2 is on the left.

Result:

True

Another

8 < 2

8 is on the right.

Result:

False
6️⃣ Negative Numbers

This is where many beginners get confused.

Example

-8 < -3

Number line:

-8 -----> -3

-8 is further left.

So

True
7️⃣ Common Beginner Mistakes
Mistake 1

Thinking

5 < 5

is

True

❌ Wrong.

Python asks:

Is 5 less than 5?

No.

They are equal.

Result

False
Mistake 2

Confusing < with <=.

We'll learn <= after >=.

For now remember:

5 < 5

↓

False

📖 Comparison So Far

| Operator | Question Python Asks        |
| -------- | --------------------------- |
| `==`     | Are they equal?             |
| `!=`     | Are they different?         |
| `>`      | Is left greater than right? |
| `<`      | Is left less than right?    |



⭐ Interview Tip

Many beginners memorize symbols.

A better approach is to translate them into English.

When you see:

a < b

Read it as:

"Is a less than b?"

When you see:

a > b

Read it as:

"Is a greater than b?"

This habit makes it much easier to read complex conditions later in if statements.


#########################################################################################################


# 🐍 Comparison Operator >=


1️⃣ Definition

The operator

>=

means

Greater Than OR Equal To

This is the first comparison operator that has two conditions.

Python asks:

Is the left value greater than the right value OR are they equal?

If either condition is true,

Python returns

True

Otherwise,

False
2️⃣ Why Do We Need It?

Imagine a company hiring people.

Requirement:

Age must be 18 or above.

Notice something.

It doesn't say

Greater than 18

It says

18 OR ABOVE

That means

age >= 18

Examples

Age = 18 ✅

Age = 19 ✅

Age = 25 ✅

Age = 17 ❌

Another example

Bank Account

Minimum balance required:

₹1000

If balance is

₹1000 ✅

₹1500 ✅

₹2000 ✅

₹999 ❌

Python:

balance >= 1000
3️⃣ Syntax
left >= right

Read it as

Left is greater than or equal to right

4️⃣ Internal Working

Example

x = 10
y = 5

print(x >= y)

Python asks

Is 10 greater than 5?

OR

Is 10 equal to 5?

The first question is

Yes

So Python immediately creates

True

Another Example

x = 10
y = 10

print(x >= y)

Python asks

Is 10 greater than 10?

No.

Then asks

Is 10 equal to 10?

Yes.

Result

True

Notice something important.

Although

10 is NOT greater than 10

The answer is still

True

because of

OR EQUAL

This is the new concept in today's lesson.

5️⃣ Number Line
← Smaller ------------------------ Greater →

1   2   3   4   5   6   7   8   9   10

Suppose we ask

5 >= 5

Python thinks

Is it to the right?

OR

Is it exactly here?

It is exactly there.

So

True

Another

8 >= 5

8 is to the right.

Answer

True

Another

2 >= 5

2 is left of 5.

Not equal.

Answer

False
6️⃣ Compare > and >=

This is one of the most important interview concepts.

Expression	Result	Why
5 > 5	False	Equal is not greater
5 >= 5	True	Equal is allowed
8 > 5	True	Greater
8 >= 5	True	Greater
2 > 5	False	Smaller
2 >= 5	False	Smaller

⭐ Golden Rule

>= means

Greater

OR

Equal

If either is true, the answer is True.

7️⃣ Common Beginner Mistakes
Mistake 1

Thinking

5 >= 5

is

False

❌ Wrong.

Equal is included.

Mistake 2

Confusing

>

with

>=

Remember

5 > 5

↓

False
5 >= 5

↓

True

One tiny = changes everything.



# This difference is worth remembering:

| Expression   | Result      |
| ------------ | ----------- |
| `10 == "10"` | `False`     |
| `10 != "10"` | `True`      |
| `10 > "10"`  | `TypeError` |
| `10 < "10"`  | `TypeError` |
| `10 >= "10"` | `TypeError` |
| `10 <= "10"` | `TypeError` |


########################################################################################################

# 🐍 Comparison Operator <=
1️⃣ Definition

The operator

<=

means

Less Than OR Equal To

It checks two conditions:

Is the left value less than the right value?
OR are both values equal?

If either condition is true,

Python returns

True

Otherwise,

False

Like every comparison operator, it returns a Boolean object.

2️⃣ Why Do We Need It?

Imagine these real-world situations.

Example 1: Speed Limit

The maximum speed allowed is 80 km/h.

That means:

60 ✅
75 ✅
80 ✅
81 ❌

Python:

speed <= 80

Notice something.

The rule is 80 or below.

Not just below.

Example 2: Age Requirement

A children's ticket is available for ages 12 or younger.

age <= 12

Examples:

Age = 8 ✅

Age = 12 ✅

Age = 13 ❌

3️⃣ Syntax
left <= right

Read it as:

Left is less than or equal to right.

4️⃣ Internal Working

Example

x = 5
y = 10

print(x <= y)

Python asks:

Question 1

Is 5 less than 10?

✅ Yes.

Python immediately creates

True

Another example

x = 10
y = 10

print(x <= y)

Python asks

Is 10 less than 10?

No.

Then asks

Is 10 equal to 10?

Yes.

Result

True

Another

x = 15
y = 10

print(x <= y)

Python asks

Is 15 less than 10?

No.

Is 15 equal to 10?

No.

Result

False
5️⃣ Number Line Thinking
← Smaller ------------------------- Greater →

1   2   3   4   5   6   7   8   9   10

Suppose we ask

5 <= 5

Python thinks

Is it on the left?

OR

Is it exactly here?

It is exactly there.

Therefore

True

Another

3 <= 5

3 is left of 5.

Answer

True

Another

8 <= 5

8 is right of 5.

Not equal.

Answer

False


#  Compare < and <=


| Expression | Result  | Why                   |
| ---------- | ------- | --------------------- |
| `5 < 5`    | `False` | Equal is **not** less |
| `5 <= 5`   | `True`  | Equal is allowed      |
| `3 < 5`    | `True`  | Smaller               |
| `3 <= 5`   | `True`  | Smaller               |
| `8 < 5`    | `False` | Greater               |
| `8 <= 5`   | `False` | Greater               |





Logical Operators

Before learning them, remember this:

Arithmetic Operators work on numbers.

Example:

10 + 5

↓

Result

15

Comparison Operators work on values.

Example:

10 > 5

↓

Result

True

Now ask yourself:

What if I have two comparison results?

Example:

10 > 5

↓

True

and

20 > 15

↓

True

How do we combine these two Boolean values?

That's why Logical Operators exist.

1. Definition

A Logical Operator is an operator that works with Boolean values (True and False) and produces a Boolean result.

They are used to combine or modify Boolean expressions.

2. Why do we need Logical Operators?

Imagine a real-world rule.

A student passes only if:

Marks are 35 or more
Attendance is 75% or more

These are two conditions.

Without logical operators, Python would have no way to combine them.

Logical operators answer questions like:

Are both conditions true?
Is at least one condition true?
Is a condition not true?
3. Types of Logical Operators

Python has three logical operators.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be True        |
| `or`     | At least one condition must be True |
| `not`    | Reverses a Boolean value            |


The and Operator
Definition

The and operator returns True only if both operands are True.

If either operand is False, the result is False.

5. Think Like Python

Example:

True and True

Python asks:

Is the left operand True?

✅ Yes.

Then asks:

Is the right operand True?

✅ Yes.

Both are True.

Python creates a new Boolean object:

True

Another example:

True and False

Python asks:

Left?

✅ True.

Right?

❌ False.

Since both are not True:

Python creates:

False


Truth Table

This table is the foundation of logical operators.

| Left  | Right | Left `and` Right |
| ----- | ----- | ---------------- |
| True  | True  | True             |
| True  | False | False            |
| False | True  | False            |
| False | False | False            |


Read it carefully.

Only one row produces True.

7. Internal Working

Consider:

5 > 3 and 10 > 7

Let's go step by step.

Step 1

Python evaluates the left comparison.

5 > 3

Python creates a Boolean object:

True
Step 2

Python evaluates the right comparison.

10 > 7

Python creates another Boolean object:

True
Step 3

Now Python has:

True and True

It checks the truth table.

Result:

True

Python creates a new Boolean object for the final result.

8. Memory Thinking

Suppose:

print(5 > 3 and 10 > 7)

Conceptually:

5 > 3
   │
   ▼
 True Object

10 > 7
   │
   ▼
 True Object

True and True
      │
      ▼
 Final True Object


Notice:

Python does not change the earlier Boolean objects.

It creates a result based on them.

Just like integers, Boolean values are immutable.

Boolean Objects

Remember:

True

and

False

are actual Python objects.

Their type is:

bool

Example:

print(type(True))

Output:

<class 'bool'>

Real-Life Examples
Example 1

You can enter a movie only if:

Age is 18 or above.
Ticket is valid.

Both must be true.

That is an and situation.

Example 2

You can submit an exam only if:

You finished writing.
Time has not expired.

Again, both conditions are required.

11. Common Beginner Mistake

Many beginners think:

True and False

returns True because one side is True.

That is incorrect.

The word and means:

Both conditions must be satisfied.

Summary

| Operator | Meaning     | Rule                         |
| -------- | ----------- | ---------------------------- |
| `and`    | Logical AND | Both operands must be `True` |

🧠 One Important Concept Before More Practice

Now let's understand the evaluation process more precisely.

Consider:

10 > 5 and 8 > 2

Python conceptually evaluates:

Step 1:
10 > 5
↓
True

Step 2:
8 > 2
↓
True

Step 3:
True and True
↓
True

So the logical operator receives the results of the comparisons.

Conceptually:

Comparison 1 ──► Boolean
                         \
                          AND ──► Boolean result
                         /
Comparison 2 ──► Boolean

This is the basic model you should remember.



🐍 Logical Operator: and — Level 2

So far, you learned:

True and True

Result:

True

and:

False and True

Result:

False

You learned and with Boolean values.

Now we learn an important Python behavior:

Python's and operator does not always return True or False.

This is a very important concept.

1. First Example
x = 10
y = 20

print(x and y)

What do you expect?

Maybe:

True

But Python outputs:

20

Why?

Because Python's and operator works differently from the simple Boolean truth table.

2. Python's Rule for and

The simplified rule is:

A and B

Python checks A.

If A is False-like:
Return A
If A is True-like:
Return B

So:

A and B

means:

"If A is truthy, give me B."

3. Example
10 and 20

Python asks:

Is 10 truthy?

Yes.

So Python returns the second operand:

20

Output:

20
4. Another Example
0 and 20

Python asks:

Is 0 truthy?

No.

So Python immediately returns:

0

Output:

0

It never needs to evaluate the second operand.

5. Truthy and Falsy

Python considers some values as False-like.

Common Falsy Values
False
0
0.0
""
None

Also:

[]
()
{}
set()

These are considered Falsy.

Most other values are Truthy:

True
1
10
-5
"Python"
[1, 2]
6. Internal Working

Consider:

x = 10
y = 20

result = x and y

Conceptually:

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

Therefore:

result → 20

Notice:

result is not True

It contains the actual value:

20
7. Memory Model
x = 10
y = 20
result = x and y

Conceptually:

x ─────────────► [10]

y ─────────────► [20]
                   ▲
                   │
result ────────────┘

and does not create a new Boolean object here.

It returns the second operand:

20

and result refers to that value.

8. Compare With Comparison Operators
Comparison
10 > 5

Result:

True

A comparison operator produces a Boolean result.

Logical and
10 and 20

Result:

20

The and operator can return an actual operand.

This is a very important difference.

9. Short-Circuit Evaluation

This is the technical name for what Python does.

Consider:

0 and 100

Python evaluates:

Is 0 falsy?

Yes.

Therefore, the answer is already known:

0

Python does not need to evaluate the second side.

This is called:

Short-circuit evaluation

10. Why Is This Useful?

Consider:

name = "Gajanand"

print(name and "Name exists")

Since:

"Gajanand"

is truthy, Python returns:

"Name exists"

Output:

Name exists

Another:

name = ""

print(name and "Name exists")

Since an empty string is falsy:

""

is returned.

11. Important Rule

For:

A and B

Think:

If A is falsy → return A
If A is truthy → return B

Examples:

10 and 20

↓

20
0 and 20

↓

0
"Python" and "Developer"

↓

"Developer"
"" and "Developer"

↓

""
🧠 One Important Detail

When we say:

10 is truthy

we are not saying:

10 == True

These are different concepts.

10 == True

↓

False

But:

bool(10)

↓

True

So:
| Expression   | Result  |
| ------------ | ------- |
| `10 == True` | `False` |
| `bool(10)`   | `True`  |
    
🐍 Truthy and Falsy Values
1. What Does "Truthy" Mean?

A value is truthy when Python treats it as:

True

in a Boolean context.

Example:

bool(10)

Output:

True

So:

10 → Truthy

But remember:

10 == True

is:

False

These are different concepts.

Truthy means:

"Python considers this value as logically True."

2. What Does "Falsy" Mean?

A value is falsy when Python treats it as:

False

in a Boolean context.

Example:

bool(0)

Output:

False

So:

0 → Falsy
3. Is There a Fixed List?

Yes. Python has a small set of important falsy values.

🔴 Falsy Values:

| Value   | Type             |
| ------- | ---------------- |
| `False` | bool             |
| `None`  | NoneType         |
| `0`     | int              |
| `0.0`   | float            |
| `0j`    | complex          |
| `""`    | empty string     |
| `[]`    | empty list       |
| `()`    | empty tuple      |
| `{}`    | empty dictionary |
| `set()` | empty set        |

These are the main built-in falsy values.

Everything Else Is Generally Truthy

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

⚠️ Important

Look carefully:

0

is falsy.

But:

[0]

is truthy.

Why?

Because:

0

is the integer zero.

But:

[0]

is a non-empty list.

Python checks whether the container is empty, not whether its contents are zero.

The Main Rule

You can always test a value using:

bool(value)

Example:

bool(10)

Output:

True

Example:

bool(0)

Output:

False
6. Numeric Values
Integer
bool(0)
False
bool(1)
True
bool(-1)
True
Rule:
0 → Falsy
Any non-zero number → Truthy

So:

0       → False
1       → True
-1      → True
100     → True
-999    → True
7. Float Values
bool(0.0)

↓

False
bool(3.14)

↓

True
bool(-2.5)

↓

True
Rule:
0.0 → Falsy
Any non-zero float → Truthy
8. Strings
Empty String
bool("")

↓

False

Because the string contains zero characters.

Non-Empty String
bool("Python")

↓

True

Even:

bool("0")

↓

True

Why?

Because "0" is a string containing one character.

It is not the integer 0.

Compare:

bool(0)      # False
bool("0")    # True

Very important.

9. Spaces
bool(" ")

↓

True

Why?

Because the string contains one space character.

It is not empty.

""   → 0 characters → Falsy
" "  → 1 character  → Truthy
10. Lists
bool([])

↓

False

Empty list = falsy.

But:

bool([1])

↓

True

And:

bool([0])

↓

True

Again:

Python checks whether the list is empty.

11. Tuples
bool(())

↓

False
bool((1,))

↓

True
12. Dictionaries
bool({})

↓

False
bool({"name": "Gajanand"})

↓

True
13. Sets
bool(set())

↓

False
bool({1})

↓

True
14. Memory Model

Consider:

x = 0

Conceptually:

x ─────► [0]
          │
          │
       Falsy

Now:

y = 10
y ─────► [10]
          │
          │
       Truthy

The object itself does not change.

Python simply evaluates the object's Boolean truth value when needed.

15. Truthiness Is Not the Same as Type

This is extremely important.

10

is:

int

and is:

Truthy

But:

"Python"

is:

str

and is also:

Truthy

So truthy/falsy is not a data type.

It is a logical evaluation.

16. The and Connection

Now return to:

10 and 20

Python asks:

Is 10 truthy?

Yes.

So:

Return 20
0 and 20

Python asks:

Is 0 truthy?

No.

So:

Return 0


## Falsy Values in Python

The following values are considered **Falsy** in Python:

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


7. The Easiest Rule for and
A and B

Python asks:

Is A falsy?

If yes:

Return A

If no:

Return B

Examples:

10 and 20

10 is truthy:

→ 20
0 and 20

0 is falsy:

→ 0
"Python" and "Developer"

"Python" is truthy:

→ "Developer"
"" and "Developer"

"" is falsy:

→ ""

Very Important: bool() vs and

These are different:

bool(10)

Output:

True

But:

10 and 20

Output:

20

Why?

bool() asks:

"What is the Boolean value of 10?"

and asks:

"Is the first value falsy? If not, give me the second value."

🧠 Remember This
bool(value)

Converts the truthiness into:

True or False

Example:

bool(10) → True
bool(0)  → False
and

Returns one of the actual operands:

10 and 20 → 20
0 and 20  → 0

## 🧠 The Key Difference

| Expression   | What happens                  | Output  |
| ------------ | ----------------------------- | ------- |
| `bool(0)`    | Convert truthiness to Boolean | `False` |
| `0 and 20`   | Return the falsy operand      | `0`     |
| `bool([])`   | Convert truthiness to Boolean | `False` |
| `[] and [1]` | Return the falsy operand      | `[]`    |


################################################################################################

🐍 Logical Operator 2: or

Python has three main logical operators:

1. and
2. or
3. not

We have completed the basic and concept. Now let's start or from the beginner level.

1. What Is or?

or means:

At least one condition must be True.

Example:

True or False

Output:

True

Why?

Because one side is True.

Truth Table

| A       | B       | `A or B` |
| ------- | ------- | -------- |
| `True`  | `True`  | `True`   |
| `True`  | `False` | `True`   |
| `False` | `True`  | `True`   |
| `False` | `False` | `False`  |

The main rule:

and → Both must be True
or  → At least one must be True

3. Simple Examples
print(True or True)

Output:

True

Both are True.

print(True or False)

Output:

True

The first condition is already True.

print(False or True)

Output:

True

The second condition is True.

print(False or False)

Output:

False

Neither condition is True.

4. With Comparisons
print(10 > 5 or 10 < 2)

Python first evaluates the comparisons:

10 > 5 → True
10 < 2 → False

Then:

True or False

Result:

True
5. Internal Evaluation

Consider:

x = 10
y = 20

print(x > 5 or y < 10)

Conceptually:

Step 1:
x > 5
↓
10 > 5
↓
True

Then:

Step 2:
True or ?

Since or already has one True value, the final Boolean result is:

True
6. Important Difference from and

For Boolean values:

True and False

↓

False

But:

True or False

↓

True

Remember:

AND:
True + False → False

OR:
True + False → True
7. or Also Uses Truthy and Falsy Values

Just like and, or does not always return True or False.

Example:

print(10 or 20)

Output:

10

Why?

10 is truthy.

Python sees that the first value is already truthy, so it returns the first value.

Example
print(0 or 20)

Python checks:

0 → Falsy

So Python goes to the second value:

20 → Truthy

Result:

20

So:

0 or 20 → 20
8. Exact Rule for or

For:

A or B

Python conceptually does:

If A is truthy:
    return A

Otherwise:
    return B

Compare with and:

A and B

If A is falsy:
    return A

Otherwise:
    return B

This is the key difference.

9. Examples
10 or 20

First value is truthy:

10 → Truthy

Return:

10


0 or 20

First value is falsy:

0 → Falsy

Return second:

20


"" or "Python"

First value is falsy:

"" → Falsy

Return:

"Python"


"Python" or "Developer"

First value is truthy:

"Python" → Truthy

Return:

"Python"

## 🧠 Compare and and or  

| Expression  | Result |
| ----------- | ------ |
| `10 and 20` | `20`   |
| `0 and 20`  | `0`    |
| `10 or 20`  | `10`   |
| `0 or 20`   | `20`   |


Simple memory trick:

AND → Find the first Falsy value
OR  → Find the first Truthy value

If no such value exists, Python returns the last value.



# Logical Operator 3: not

1. What Is not?

not means:

Reverse the Boolean result.

If something is:

True

then:

not True

becomes:

False

If something is:

False

then:

not False

becomes:

True

Basic Truth Table 

| Value   | `not value` |
| ------- | ----------- |
| `True`  | `False`     |
| `False` | `True`      |


So:

not True

↓

False

And:

not False

↓

True
3. not With Comparisons

Consider:

x = 10

print(not x > 5)

First Python evaluates the comparison:

x > 5

Substitute:

10 > 5

Result:

True

Then not reverses it:

not True

Final result:

False

So:

not (10 > 5) → False


4. Another Example
x = 10

print(not x < 5)

First:

10 < 5 → False

Then:

not False → True

Output:

True
5. not With Truthy and Falsy Values

This is where your previous learning becomes useful.

Example
print(not 10)

Python checks:

10 → Truthy

Then:

not Truthy → False

Output:

False
Example
print(not 0)

Python checks:

0 → Falsy

Then:

not Falsy → True

Output:

True
6. not With Strings
print(not "")

Empty string:

"" → Falsy

Therefore:

not False → True

Output:

True
print(not "Python")

"Python" is non-empty:

"Python" → Truthy

Therefore:

not True → False

Output:

False

7. not Always Returns a Boolean

This is different from and and or.

Compare:

10 and 20

Output:

20
10 or 20

Output:

10

But:

not 10

Output:

False

So:

and → Can return an actual operand
or  → Can return an actual operand
not → Always returns True or False
8. Internal Working

Consider:

x = 10

result = not x

Conceptually:

x
↓
10
↓
Is 10 truthy?
↓
Yes
↓
not True
↓
False

So:

result → False
9. Important Difference

This:

not 10

does not mean:

10 → False

Python does not change the integer object 10.

Instead:

10 is truthy
↓
not reverses that logical result
↓
False

The original object remains:

10


10. Basic Examples

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