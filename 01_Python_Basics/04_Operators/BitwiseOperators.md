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


