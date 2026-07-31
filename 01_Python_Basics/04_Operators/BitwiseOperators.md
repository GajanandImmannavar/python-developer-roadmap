Perfect. We'll learn this like you're preparing for coding interviews—not just to memorize syntax, but to **understand what's happening inside the CPU**.

# Bitwise Operators Roadmap

We will go one by one:

1. ✅ `&` (Bitwise AND) ← **Today**
2. `|` (Bitwise OR)
3. `^` (Bitwise XOR)
4. `~` (Bitwise NOT)
5. `<<` (Left Shift)
6. `>>` (Right Shift)

---

# Rule No. 1

**Bitwise operators never work on decimal numbers directly.**

Whenever you write:

```python
a = 10
b = 12

print(a & b)
```

Python internally thinks:

```
10 → 1010
12 → 1100
```

It converts them to binary first.

---

# Today's Topic: Bitwise AND (`&`)

The AND operator asks a very simple question for **each bit**:

> **"Are both bits 1?"**

If **YES** → output `1`

If **NO** → output `0`

That's all.

---

# Real-Life Analogy

Imagine two security guards.

A door opens **only if both guards say YES**.

| Guard A | Guard B | Door Opens? |
| ------- | ------- | ----------- |
| Yes     | Yes     | ✅ Yes       |
| Yes     | No      | ❌ No        |
| No      | Yes     | ❌ No        |
| No      | No      | ❌ No        |

This is exactly how **AND** works.

---

# Truth Table

This table is the heart of the AND operator.

| Bit A | Bit B | A & B |
| :---: | :---: | :---: |
|   0   |   0   |   0   |
|   0   |   1   |   0   |
|   1   |   0   |   0   |
|   1   |   1   |   1   |

**Memorize this table.** Every AND operation is just this rule repeated for each bit.

---

# Example 1

Let's calculate:

```python
10 & 12
```

## Step 1: Convert to Binary

```
10 = 1010

12 = 1100
```

Write them one below the other:

```
   1010
&  1100
-------
```

Now compare **column by column**.

---

## First Column (leftmost)

```
1 & 1
```

Look at the truth table.

```
1 & 1 = 1
```

Answer so far:

```
1
```

---

## Second Column

```
0 & 1
```

Truth table:

```
0 & 1 = 0
```

Now answer becomes:

```
10
```

---

## Third Column

```
1 & 0
```

Truth table:

```
1 & 0 = 0
```

Answer:

```
100
```

---

## Fourth Column

```
0 & 0
```

Truth table:

```
0 & 0 = 0
```

Final binary answer:

```
1000
```

Convert back to decimal.

```
1000₂

8 4 2 1
1 0 0 0

= 8
```

Therefore,

```python
10 & 12
```

returns

```python
8
```

---

# Verify in Python

```python
print(10 & 12)
```

Output

```python
8
```

---

# Example 2

```python
5 & 3
```

Convert:

```
5 = 0101

3 = 0011
```

Arrange them:

```
0101
0011
----
```

Compare each bit:

```
0 & 0 = 0

1 & 0 = 0

0 & 1 = 0

1 & 1 = 1
```

Result:

```
0001
```

Decimal:

```
1
```

Python:

```python
print(5 & 3)
```

Output

```python
1
```

---

# Example 3

```python
7 & 15
```

Convert:

```
7  = 0111

15 =1111
```

Compare:

```
0111
1111
----
0111
```

Binary

```
0111
```

Decimal

```
7
```

Output

```python
7
```

---

# Why?

Because every bit in 7 is already `1`, and 15 has `1` in all four positions, so every bit stays `1`.

---

# Example 4

```python
4 & 2
```

Binary

```
4 = 0100

2 = 0010
```

```
0100
0010
----
0000
```

Answer

```
0
```

---

# A Pattern You'll Notice

Whenever two numbers don't have `1`s in the same bit positions, the result is often `0`.

Example:

```
0100

0010
```

No column has:

```
1 & 1
```

So every column becomes `0`.

---

# Visual Explanation

Think of the bits as switches.

```
Number A

1 0 1 0

Number B

1 1 0 0
```

The AND operator keeps a switch ON **only if both switches are ON**.

```
1 & 1 = ON

0 & 1 = OFF

1 & 0 = OFF

0 & 0 = OFF
```

Result

```
1 0 0 0
```

---

# Where is AND Used?

### 1. Checking Permissions

Imagine file permissions.

```
Read

Write

Execute
```

Each permission is stored as bits.

AND checks whether a permission exists.

---

### 2. Checking Odd or Even

This is one of the most common interview questions.

```python
if number & 1:
    print("Odd")
else:
    print("Even")
```

Why does this work?

Let's see.

```
6 = 110

1 = 001
```

```
110
001
---
000
```

Result = `0`, so **6 is even**.

Now try:

```
7 = 111

1 = 001
```

```
111
001
---
001
```

Result = `1`, so **7 is odd**.

The last bit (also called the **Least Significant Bit** or **LSB**) tells us whether a number is odd (`1`) or even (`0`).

---

# Interview Tip

The CPU performs bitwise operations directly on bits, making them **extremely fast**. That's why they're used in:

* Operating systems
* Device drivers
* Networking
* Graphics
* Cryptography
* Embedded systems

---

# Common Beginner Mistake

Don't confuse:

```python
and
```

with

```python
&
```

`and` is a **logical operator** that works with Boolean values or truthiness.

```python
True and False
```

`&` is a **bitwise operator** that works on the individual bits of integers.

```python
10 & 12
```

These are different operators with different purposes.

---

# Practice Questions (Don't use Python yet)

Convert to binary, perform the AND operation, then convert back to decimal.

1. `6 & 5`
2. `9 & 3`
3. `15 & 10`
4. `8 & 7`
5. `13 & 11`
6. `14 & 5`
7. `2 & 1`
8. `12 & 4`
9. `11 & 6`
10. `7 & 1`

Perfect. Since you're learning **like a professional Python developer**, let's learn the **Bitwise OR (`|`) Operator** from absolute basics to interview level.

---

# 🐍 Bitwise OR (`|`) Operator in Python

The **Bitwise OR** operator compares the binary representation of two numbers **bit by bit**.

For every pair of bits, it asks:

> **"Is at least one bit 1?"**

If **YES → 1**

If **NO → 0**

---

# 📖 Definition

The Bitwise OR operator performs an **OR operation** on every corresponding bit of two integers.

Operator:

```python
|
```

---

# 🧠 Why is it called Bitwise?

Suppose:

```python
10 | 5
```

Python **does NOT** compare:

```text
10 and 5
```

Instead it converts both numbers into **binary**.

```
10 → 1010

5 → 0101
```

Then Python compares every bit.

---

# 🧠 What is Binary?

Computers understand only:

```text
0
1
```

Every decimal number has a binary representation.

| Decimal | Binary |
| ------: | :----- |
|       0 | 0000   |
|       1 | 0001   |
|       2 | 0010   |
|       3 | 0011   |
|       4 | 0100   |
|       5 | 0101   |
|       6 | 0110   |
|       7 | 0111   |
|       8 | 1000   |
|       9 | 1001   |
|      10 | 1010   |
|      11 | 1011   |
|      12 | 1100   |
|      13 | 1101   |
|      14 | 1110   |
|      15 | 1111   |

---

# 🧠 Truth Table of OR

OR asks:

> **Is at least one bit 1?**

| A | B | A \| B |
|---|---|:------:|
| 0 | 0 |    0   |
| 0 | 1 |    1   |
| 1 | 0 |    1   |
| 1 | 1 |    1   |


Remember:

```text
Only 0 OR 0 gives 0.

Everything else gives 1.
```

---

# 🧠 Memory Trick

Think of OR as being **generous**.

```
Need only ONE person to say YES.
```

Example:

```
Person A : YES

Person B : NO

Result : YES
```

Binary:

```
1 | 0

↓

1
```

---

# 🧪 Example 1

```python
5 | 3
```

Convert to binary.

```
5

0101
```

```
3

0011
```

Now compare.

```
0101
0011
----
0111
```

Result:

```
0111
```

Convert back.

```
0111

=

7
```

Output

```python
print(5 | 3)

# 7
```

---

# 🧪 Dry Run

```
5 → 0101

3 → 0011
```

Bit by bit:

```
0 | 0 = 0

1 | 0 = 1

0 | 1 = 1

1 | 1 = 1
```

Final

```
0111

↓

7
```

---

# 🧪 Example 2

```python
10 | 5
```

Binary

```
10

1010
```

```
5

0101
```

OR

```
1010
0101
----
1111
```

Binary

```
1111
```

Decimal

```
15
```

Output

```python
print(10 | 5)

# 15
```

---

# 🧪 Example 3

```python
8 | 2
```

Binary

```
8

1000
```

```
2

0010
```

OR

```
1000
0010
----
1010
```

Binary

```
1010
```

Decimal

```
10
```

Output

```python
print(8 | 2)

# 10
```

---

# 🧪 Example 4

```python
6 | 9
```

Binary

```
6

0110
```

```
9

1001
```

OR

```
0110
1001
----
1111
```

Decimal

```
15
```

Output

```python
15
```

---

# 🧠 Visual Explanation

Imagine electricity.

```
Switch A

ON
```

```
Switch B

OFF
```

Will the bulb glow?

YES

Because one switch is ON.

Binary

```
1 | 0

↓

1
```

---

Another

```
OFF

OFF
```

Bulb?

NO

```
0 | 0

↓

0
```

---

# 🔍 Step-by-Step Algorithm

For

```python
a | b
```

Python performs:

```
Convert a into binary

↓

Convert b into binary

↓

Compare every bit

↓

Apply OR truth table

↓

Create new binary number

↓

Convert binary back to decimal

↓

Return result
```

---

# 🧪 Large Example

```python
12 | 10
```

Binary

```
12

1100
```

```
10

1010
```

OR

```
1100
1010
----
1110
```

Binary

```
1110
```

Decimal

```
14
```

Output

```python
14
```

---

# 🧠 Why Does OR Often Produce a Larger Number?

OR turns **more bits into 1**.

Example

```
1000

0010

↓

1010
```

There are now **more set bits (1s)**.

That usually increases the decimal value.

---

# 🧠 Relationship with AND

Suppose

```
1100

1010
```

AND

```
1100

1010

----

1000
```

Keeps only common 1s.

OR

```
1100

1010

----

1110
```

Keeps every 1.

---

# 🧠 Easy Memory Trick

AND

```
Both must be 1
```

OR

```
At least one must be 1
```

---

# 📊 Comparison Table

| Operator | Rule                | Result                |          |
| -------- | ------------------- | --------------------- | -------- |
| `&`      | Both bits must be 1 | Strict                |          |
| `        | `                   | At least one bit is 1 | Generous |

---

# 🧪 Practice Problems

Predict the output **without running the code**.

### Problem 1

```python
print(5 | 1)
```

---

### Problem 2

```python
print(7 | 8)
```

---

### Problem 3

```python
print(15 | 0)
```

---

### Problem 4

```python
print(2 | 4)
```

---

### Problem 5

```python
print(9 | 6)
```

---

# 🎯 Interview Questions

### Q1. What is the Bitwise OR operator?

**Answer:**

The Bitwise OR (`|`) operator compares two integers bit by bit. It returns `1` for each bit position where **at least one** of the corresponding bits is `1`.

---

### Q2. What is the truth table of OR?

| A | B | A \| B |
|---|---|:------:|
| 0 | 0 |    0   |
| 0 | 1 |    1   |
| 1 | 0 |    1   |
| 1 | 1 |    1   |

---

### Q3. What is the difference between `|` and `or`?

| Bitwise OR (`\|`) | Logical OR (`or`) |
|------------------------|-------------------|
| Bitwise operator | Logical operator |
| Works on bits | Works on truth values |
| Evaluates every bit | Evaluates truthiness |
| Used with integers | Used with Boolean expressions |

Example:

```python
5 | 3      # 7

True or False    # True
```

---

### Q4. Why is Bitwise OR useful?

**Answer:**

It is commonly used for:

* Setting specific bits
* Bit masks
* Permissions and flags
* Graphics programming
* Networking protocols
* Embedded systems
* Low-level system programming

---

# 🏆 Final Mental Model

```text
Bitwise OR (|)
        ↓
Convert both numbers to binary
        ↓
Compare each pair of bits
        ↓
If at least one bit is 1 → Result is 1
        ↓
If both bits are 0 → Result is 0
        ↓
Convert the final binary back to decimal
```

---

# 📌 Revision Summary

| Operator | Name | Rule       |                              |
| -------- | ---- | ---------- | ---------------------------- |
| `        | `    | Bitwise OR | At least one bit must be `1` |

### Golden Rule

```text
0 | 0 = 0

0 | 1 = 1

1 | 0 = 1

1 | 1 = 1
```

### Memory Trick

```text
AND → Both must be 1

OR → At least one must be 1
```


# Bitwise XOR (`^`) (Exclusive OR)

Many interview questions use XOR because of its unique properties.

---

# What does XOR ask?

XOR asks one question:

> **"Are the two bits different?"**

* If **YES** → `1`
* If **NO** → `0`

Notice how it's different from AND and OR.

---

# Real-Life Analogy

Imagine two light switches controlling a bulb.

The bulb is **ON only if exactly one switch is ON**.

| Switch A | Switch B | Bulb |
| -------- | -------- | ---- |
| OFF      | OFF      | OFF  |
| OFF      | ON       | ON   |
| ON       | OFF      | ON   |
| ON       | ON       | OFF  |

Both ON? → OFF

Both OFF? → OFF

Different? → ON

This is exactly XOR.

---

# Truth Table

This table is the heart of XOR.

|  A  |  B  | A ^ B |
| :-: | :-: | :---: |
|  0  |  0  |   0   |
|  0  |  1  |   1   |
|  1  |  0  |   1   |
|  1  |  1  |   0   |

## Compare all three

|  A  |  B  | AND `&` | OR `\|` | XOR `^` |
| :-: | :-: | :-----: | :-----: | :-----: |
|  0  |  0  |    0    |    0    |    0    |
|  0  |  1  |    0    |    1    |    1    |
|  1  |  0  |    0    |    1    |    1    |
|  1  |  1  |    1    |    1    |    0    |

Look at the last row:

```text
1 & 1 = 1
1 | 1 = 1
1 ^ 1 = 0   ← Different!
```

That's why XOR is called **Exclusive OR**.

---

# Example 1

Calculate:

```python
10 ^ 12
```

Convert to binary.

```text
10 = 1010
12 = 1100
```

```
 1010
^1100
-----
```

Compare bit by bit.

```
1 ^ 1 = 0

0 ^ 1 = 1

1 ^ 0 = 1

0 ^ 0 = 0
```

Result

```text
0110
```

Convert back.

```
0110 = 6
```

Therefore

```python
10 ^ 12 = 6
```

---

# Example 2

```python
5 ^ 3
```

```
5 = 0101
3 = 0011
```

```
0101
0011
----
0110
```

```
0110 = 6
```

Answer

```python
5 ^ 3 = 6
```

---

# Example 3

```python
7 ^ 7
```

```
0111
0111
----
0000
```

Answer

```python
7 ^ 7 = 0
```

---

# The Most Important XOR Property

## Property 1

```python
x ^ x = 0
```

Examples

```python
5 ^ 5 = 0

100 ^ 100 = 0

999 ^ 999 = 0
```

### Why?

Every bit compares with itself.

Each comparison is either

```
0 ^ 0 = 0

or

1 ^ 1 = 0
```

Every bit becomes zero.

---

# Property 2

```python
x ^ 0 = x
```

Example

```python
25 ^ 0 = 25
```

Why?

```
1 ^ 0 = 1

0 ^ 0 = 0
```

Nothing changes.

---

# Property 3 (Very Famous)

```python
x ^ y ^ y = x
```

Why?

Because

```
y ^ y = 0
```

Then

```
x ^ 0 = x
```

This property is used in many interview problems.

---

# Interview Problem 1

Suppose every number appears **twice** except one.

Find the unique number.

Example

```python
[5, 3, 2, 3, 5]
```

Normal thinking:

* Use a dictionary
* Count frequencies

Bitwise thinking:

```
5 ^ 3 ^ 2 ^ 3 ^ 5
```

Group equal numbers.

```
(5 ^ 5)

^

(3 ^ 3)

^

2
```

```
0 ^ 0 ^ 2
```

```
2
```

Answer:

```
2
```

This is one of the most common coding interview questions.

---

# AND vs OR vs XOR

Think like this:

### AND

> Keep only common 1s.

```
1101

1011

↓

1001
```

---

### OR

> Keep all 1s.

```
1101

1011

↓

1111
```

---

### XOR

> Keep only different bits.

```
1101

1011

↓

0110
```

---

# Easy Way to Remember

Imagine two friends answering a yes/no question.

### AND

Both must say **YES**.

### OR

At least one says **YES**.

### XOR

Exactly one says **YES**.

---


Awesome! 🔥 This is the only bitwise operator where almost every beginner gets confused.

Take your time with this lesson. Once you understand it, **left shift (`<<`)** and **right shift (`>>`)** become much easier.

---

# Bitwise NOT (`~`)

Unlike the other operators:

```python
&
|
^
```

which need **two numbers**, NOT needs only **one**.

```python
~5
```

---

# What does NOT do?

It simply **flips every bit**.

```
0 → 1
1 → 0
```

That's all.

---

## Example

Suppose we use **4 bits** (just for understanding).

```
5 = 0101
```

Apply NOT.

```
0101

↓

1010
```

Every bit changed.

```
0 → 1
1 → 0
1 → 0
0 → 1
```

So far, this is easy.

---

# But Wait...

Let's try it in Python.

```python
print(~5)
```

Output:

```python
-6
```

😲

Most beginners expect:

```
1010 = 10
```

or maybe

```
-5
```

But Python prints:

```
-6
```

**Why?**

This is the question we need to answer.

---

# The Secret: Computers Store Negative Numbers Differently

Computers don't store:

```
-5
```

by putting a minus sign in front.

Instead, they use a method called:

> **Two's Complement**

Don't worry about the name yet.

We'll understand it with a simple trick.

---

# The Golden Formula

In Python:

```python
~x = -(x + 1)
```

This is the formula you should remember.

Examples:

```python
~5

= -(5 + 1)

= -6
```

---

```python
~10

= -(10 + 1)

= -11
```

---

```python
~0

= -(0 + 1)

= -1
```

---

```python
~7

= -(7 + 1)

= -8
```

---

# Verify

```python
print(~5)
```

Output

```
-6
```

```python
print(~10)
```

Output

```
-11
```

Works every time.

---

# But WHY?

This is where many tutorials stop.

I don't want you to memorize the formula.

I want you to understand it.

---

# Imagine We Have Only 4 Bits

Let's use **4 bits only**.

```
5 = 0101
```

Flip every bit.

```
0101

↓

1010
```

Now here's the important part.

In a fixed-width binary system, a number that starts with `1` is interpreted as a **negative number** using two's complement.

So `1010` is **not** interpreted as positive `10` in that system.

Instead, it's interpreted as **-6**.

That's why Python returns:

```
-6
```

Python internally behaves as if integers have infinitely many leading bits, which still follows the same mathematical rule:

```python
~x = -(x + 1)
```

---

# Easy Way to Remember

Don't think:

```
NOT gives negative.
```

❌ That's not the rule.

Think:

1. Flip all bits.
2. Python's representation of negative numbers makes the result equal to:

```python
-(x + 1)
```

---

# Practice (No Binary Needed)

Using the formula:

```
~x = -(x + 1)
```

Calculate:

1.

```python
~3
```

2.

```python
~8
```

3.

```python
~15
```

4.

```python
~0
```

5.

```python
~24
```

---

# One Conceptual Question

If

```python
~9 = -10
```

What will be

```python
~-10
```

Don't guess.

Think about the formula carefully.

---

## After This

Once you're comfortable with `~`, we'll move to **Left Shift (`<<`)**, where you'll discover a beautiful shortcut:

```python
x << 1
```

is the same as

```python
x × 2
```

and

```python
x << 3
```

is the same as

```python
x × 8
```


# ⭐ One Amazing Property of Bitwise NOT (`~`)

The Bitwise NOT operator has an interesting mathematical property.

If you apply the `~` operator **twice**, you always get back the original number.

## Example 1

```python
print(~5)
print(~~5)
```

### Step 1

```text
~5

= -6
```

### Step 2

```text
~-6

= 5
```

Therefore,

```text
~~5 = 5
```

---

## Example 2

```python
print(~~20)
```

### Step 1

```text
~20

= -21
```

### Step 2

```text
~-21

= 20
```

Therefore,

```text
~~20 = 20
```

---

## Example 3

```python
print(~~-8)
```

### Step 1

```text
~-8

= 7
```

### Step 2

```text
~7

= -8
```

Therefore,

```text
~~-8 = -8
```

---

# 🧠 Why Does This Happen?

The Bitwise NOT operator follows the formula:

```text
~x = -(x + 1)
```

Applying it twice:

```text
~~x

= ~(-(x + 1))

= x
```

So the second `~` reverses the effect of the first one and returns the original value.

---

# 📌 General Rule

```text
~~x = x
```

No matter whether `x` is:

- Positive
- Negative
- Zero

Applying `~` twice always returns the original number.

---

# 🧪 Examples

```python
print(~~0)      # 0
print(~~7)      # 7
print(~~100)    # 100
print(~~-15)    # -15
```

---

# 🎯 Interview Question

## Q. What is the result of applying the Bitwise NOT operator twice?

### Answer

Applying the Bitwise NOT operator twice always returns the original number.

```text
~~x = x
```

This happens because the first `~` inverts the bits and the second `~` inverts them again, restoring the original bit pattern.

---

# 🏆 Final Mental Model

```text
First ~

Original Number
      ↓
Invert all bits
      ↓
New Number

Second ~

Invert all bits again
      ↓
Original Number
```

## ✅ Golden Rule

```text
~~x = x
```

> **Applying the Bitwise NOT (`~`) operator twice always returns the original number.**