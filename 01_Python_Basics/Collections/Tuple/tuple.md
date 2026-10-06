# 🐍 Python Tuple — Complete Learning

We finished the major **List** concepts, so now we move to the next data structure:

```text
Python Basics
│
├── Variables ✅
├── Data Types ✅
├── Type Casting ✅
├── Operators ✅
├── Built-in Functions 🔄
│
├── Lists ✅
│   ├── Methods
│   ├── Indexing
│   ├── Slicing
│   ├── Operators
│   └── Operations
│
└── 🔜 Tuple
```

And as you requested, we won't learn Tuple as only a definition. We'll cover **everything important**.

---

# 1. What Is a Tuple?

A **tuple** is an ordered collection of elements.

Example:

```python
student = ("Gajanand", 22, "AIML")
```

A tuple can contain different data types:

```python
data = ("Python", 100, 10.5, True)
```

---

# 2. Basic Tuple Syntax

```python
numbers = (10, 20, 30, 40)
```

Memory model:

```text
numbers
   │
   ▼
┌─────────────────────┐
│ 10 │ 20 │ 30 │ 40  │
└─────────────────────┘
   0    1    2    3
```

Like a list, a tuple is:

* ordered
* indexed
* allows duplicates
* supports slicing
* supports iteration

But the major difference is:

> **A tuple is immutable.**

---

# 3. Tuple vs List

| Property   | List      | Tuple    |
| ---------- | --------- | -------- |
| Ordered    | ✅         | ✅        |
| Indexed    | ✅         | ✅        |
| Duplicates | ✅         | ✅        |
| Mutable    | ✅         | ❌        |
| Immutable  | ❌         | ✅        |
| Slicing    | ✅         | ✅        |
| `in`       | ✅         | ✅        |
| `+`        | ✅         | ✅        |
| `*`        | ✅         | ✅        |
| Methods    | Many      | Few      |
| Hashable   | Usually ❌ | Can be ✅ |

Example:

```python
numbers = [10, 20, 30]
numbers[0] = 100
```

Works.

But:

```python
numbers = (10, 20, 30)
numbers[0] = 100
```

gives:

```text
TypeError
```

because tuples cannot be modified.

---

# 4. Why Is Tuple Immutable?

Suppose:

```python
data = (10, 20, 30)
```

Conceptually:

```text
data
 │
 ▼
┌─────────────────┐
│ 10 │ 20 │ 30   │
└─────────────────┘
```

After creation, you cannot change which elements the tuple contains.

This is invalid:

```python
data[0] = 100
```

Python protects the tuple's structure.

---

# 5. Tuple Indexing

Tuples support indexing exactly like lists.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
```

Output:

```text
10
```

```python
print(numbers[2])
```

Output:

```text
30
```

---

# 6. Negative Indexing

```python
numbers = (10, 20, 30, 40, 50)
```

Indexes:

```text
Value:       10    20    30    40    50
Positive:     0     1     2     3     4
Negative:    -5    -4    -3    -2    -1
```

Therefore:

```python
numbers[-1]
```

returns:

```text
50
```

---

# 7. Tuple Slicing

Tuple slicing works like list slicing.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

Remember:

```text
[start:stop:step]
```

and:

> start included, stop excluded.

---

# 8. Reverse a Tuple

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])
```

Output:

```text
(50, 40, 30, 20, 10)
```

Notice that the result is still a **tuple**.

---

# 9. Creating a Tuple

The most common syntax is:

```python
numbers = (10, 20, 30)
```

But parentheses are not actually what make it a tuple.

The **comma** is important.

---

# 10. The One-Element Tuple Trap ⭐⭐⭐

This is NOT a tuple:

```python
x = (10)
```

Check:

```python
print(type(x))
```

Output:

```text
<class 'int'>
```

Why?

Because:

```python
(10)
```

is just parentheses around `10`.

---

# 11. Correct One-Element Tuple

You need a comma:

```python
x = (10,)
```

Now:

```python
print(type(x))
```

Output:

```text
<class 'tuple'>
```

Memory trick:

```text
(10)   → int
(10,)  → tuple
```

### ⭐ The comma creates the tuple.

---

# 12. Tuple Without Parentheses

You can also create tuples without parentheses:

```python
numbers = 10, 20, 30
```

Python creates:

```python
(10, 20, 30)
```

This is called **tuple packing**.

---

# 13. Tuple Packing

```python
student = "Gajanand", 22, "AIML"
```

Python interprets this as:

```python
("Gajanand", 22, "AIML")
```

The values are packed into one tuple.

---

# 14. Tuple Unpacking ⭐⭐⭐

You can unpack the tuple into variables.

```python
student = ("Gajanand", 22, "AIML")

name, age, stream = student
```

Now:

```text
name   → "Gajanand"
age    → 22
stream → "AIML"
```

Example:

```python
print(name)
print(age)
print(stream)
```

Output:

```text
Gajanand
22
AIML
```

---

# 15. Number of Variables Must Match

This:

```python
data = (10, 20, 30)

a, b, c = data
```

works.

But:

```python
a, b = data
```

raises:

```text
ValueError
```

because:

```text
3 values
2 variables
```

---

# 16. Extended Unpacking ⭐⭐

Python allows `*`.

```python
numbers = (10, 20, 30, 40, 50)

a, *b = numbers
```

Result conceptually:

```text
a → 10
b → [20, 30, 40, 50]
```

Notice:

> The starred variable receives a **list**, not a tuple.

---

# 17. Another Example

```python
numbers = (10, 20, 30, 40, 50)

a, *middle, e = numbers
```

Result:

```text
a      → 10
middle → [20, 30, 40]
e      → 50
```

This is useful in Python programming and DSA.

---

# 18. Tuple Concatenation `+`

Just like lists:

```python
a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)
```

Output:

```text
(1, 2, 3, 4, 5, 6)
```

It creates a new tuple.

---

# 19. Tuple Repetition `*`

```python
numbers = (1, 2, 3)

print(numbers * 3)
```

Output:

```text
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

---

# 20. Tuple Membership

```python
numbers = (10, 20, 30)

print(20 in numbers)
```

Output:

```text
True
```

And:

```python
print(50 not in numbers)
```

Output:

```text
True
```

---

# 21. Tuple Comparison

Tuples support:

```python
==
!=
<
>
<=
>=
```

Example:

```python
a = (1, 2, 3)
b = (1, 2, 4)

print(a < b)
```

Python compares from left to right:

```text
1 == 1
2 == 2
3 < 4
```

Therefore:

```text
True
```

This is the same lexicographical comparison behavior you just learned with lists.

---

# 22. Tuple Methods

Unlike lists, tuples have only **two primary methods**:

```text
tuple
│
├── count()
└── index()
```

### `count()`

Counts occurrences.

```python
numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))
```

Output:

```text
3
```

### `index()`

Finds the first occurrence.

```python
numbers = (10, 20, 30, 20)

print(numbers.index(20))
```

Output:

```text
1
```

We will later go through these methods deeply.

---

# 23. Why Does Tuple Have Fewer Methods?

Because tuples are immutable.

A list needs methods such as:

```text
append()
extend()
insert()
remove()
pop()
clear()
sort()
reverse()
```

But a tuple cannot perform these operations.

For example:

```python
numbers = (10, 20, 30)

numbers.append(40)
```

gives:

```text
AttributeError
```

because tuples don't have `append()`.

---

# 24. Can a Tuple Contain a List?

Yes! ⭐

This is where **immutability gets subtle**.

```python
data = (10, [20, 30], 40)
```

The tuple itself cannot replace its elements.

This is invalid:

```python
data[0] = 100
```

But the inner list is mutable:

```python
data[1].append(50)
```

Now:

```python
print(data)
```

Output:

```text
(10, [20, 30, 50], 40)
```

Why?

Because:

```text
tuple
 │
 ├──→ 10
 │
 ├──→ list ──→ [20,30]
 │
 └──→ 40
```

The tuple still points to the **same list object**.

The tuple's references didn't change.

The list object itself changed.

This distinction is very important for understanding Python's memory model.

---

# 25. Tuple as Dictionary Key ⭐⭐⭐

A tuple can sometimes be used as a dictionary key.

```python
location = {
    (10, 20): "Point A"
}
```

Why can this work?

Because tuples can be **hashable**, provided their elements are hashable.

This is very useful in DSA.

For example:

```python
visited = set()

visited.add((2, 3))
visited.add((4, 5))
```

You can represent coordinates as:

```text
(row, column)
```

or:

```text
(x, y)
```

This is extremely common in:

* grids
* graphs
* BFS
* DFS
* coordinate problems

---

# 26. But This Tuple Cannot Be a Dictionary Key

```python
data = ([1, 2], 3)
```

You cannot use it as a dictionary key:

```python
d = {
    data: "value"
}
```

because the tuple contains a list, and lists are unhashable.

So:

```text
(1, 2)       → hashable
([1, 2], 3)  → not hashable
```

---

# 27. Tuple Memory Advantage

A tuple is generally more compact than a list for the same references because it is immutable and doesn't need list-style resizing machinery.

Conceptually:

```text
LIST

data
 ↓
[ references + dynamic capacity ]
```

while:

```text
TUPLE

data
 ↓
( references )
```

Don't interpret this as "tuples are always dramatically faster." The practical difference depends on the operation and data.

---

# 28. When Should You Use a Tuple?

Use a tuple when the collection represents data that should **not be structurally changed**.

Examples:

### Coordinates

```python
point = (10, 20)
```

### RGB color

```python
color = (255, 0, 0)
```

### Database record

```python
user = ("Gajanand", 22, "AIML")
```

### Function return values

```python
def get_user():
    return "Gajanand", 22
```

Then:

```python
name, age = get_user()
```

---

# 29. Tuple in DSA

Tuples are especially useful for representing **fixed groups of values**.

Example:

```python
edges = [
    (1, 2),
    (2, 3),
    (3, 4)
]
```

Each tuple represents:

```text
(source, destination)
```

Another example:

```python
points = [
    (2, 3),
    (5, 7),
    (8, 1)
]
```

Each tuple represents:

```text
(x, y)
```

This is very common in DSA.

---

# 30. Tuple vs List — DSA Decision

Think:

```text
Need to MODIFY collection?
        │
       YES
        ↓
      LIST

Need FIXED collection?
        │
       YES
        ↓
     TUPLE
```

Examples:

```text
Dynamic result array → List

Stack → List

Queue implementation → usually List/deque depending on operation

Coordinates → Tuple

Graph edge (u, v) → Tuple

Fixed record → Tuple
```

---
