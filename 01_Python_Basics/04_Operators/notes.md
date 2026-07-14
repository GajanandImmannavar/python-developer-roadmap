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




