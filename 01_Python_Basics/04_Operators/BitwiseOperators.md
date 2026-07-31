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

| A | B | A | B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 1     |

---

### Q3. What is the difference between `|` and `or`?

Use this **exact Markdown** in your `.md` file:

```md
| `|` (Bitwise OR) | `or` (Logical OR) |
|------------------|-------------------|
| Bitwise operator | Logical operator |
| Works on bits | Works on truth values |
| Evaluates every bit | Evaluates truthiness |
| Used with integers | Used with Boolean expressions |
```

It will render in GitHub as:

| `|` (Bitwise OR) | `or` (Logical OR) |
|------------------|-------------------|
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


