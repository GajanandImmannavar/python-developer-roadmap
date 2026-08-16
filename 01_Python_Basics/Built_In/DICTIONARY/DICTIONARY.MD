# 📚 Python Dictionary — Complete Learning

We will now **restart Dictionary properly from the beginning** and take it to the level where I can honestly mark it **🟢 Completed**.

We will **not rush**. We'll cover the topic in sections, and you can say **“next”** when you're ready.

---

# 1. What Is a Dictionary?

A **dictionary (`dict`)** is a Python data structure that stores information as:

```text
KEY → VALUE
```

Example:

```python
student = {
    "name": "Gajanand",
    "age": 22,
    "course": "AI & ML"
}
```

Think of it as:

```text
"name"   → "Gajanand"
"age"    → 22
"course" → "AI & ML"
```

Instead of finding data using a **position**, we find it using a **key**.

---

# 2. Why Do We Need Dictionaries?

Compare a list:

```python
student = ["Gajanand", 22, "AI & ML"]
```

What does this mean?

```python
student[0]
student[1]
student[2]
```

You have to remember:

```text
0 → name
1 → age
2 → course
```

That's not very descriptive.

With a dictionary:

```python
student = {
    "name": "Gajanand",
    "age": 22,
    "course": "AI & ML"
}
```

You can directly say:

```python
student["name"]
```

Much clearer.

### 🧠 Memory trick

```text
LIST
index → value

DICTIONARY
key → value
```

---

# 3. Basic Structure

A dictionary looks like:

```python
{
    key: value,
    key: value,
    key: value
}
```

Example:

```python
person = {
    "name": "Gajanand",
    "age": 22
}
```

Each entry is called a **key-value pair**.

```text
"name": "Gajanand"
  ↑          ↑
 key       value
```

---

# 4. Key vs Value

This distinction is extremely important.

```python
student = {
    "name": "Gajanand",
    "age": 22
}
```

Here:

### Keys

```text
"name"
"age"
```

### Values

```text
"Gajanand"
22
```

The key identifies the information.

The value is the information stored.

---

# 5. Dictionary Memory Model

Consider:

```python
student = {
    "name": "Gajanand",
    "age": 22
}
```

Conceptually:

```text
student
   │
   ▼
┌───────────────────────┐
│       Dictionary      │
│                       │
│  "name" ──→ "Gajanand"│
│  "age"  ──→ 22        │
│                       │
└───────────────────────┘
```

When you write:

```python
student["name"]
```

Python uses `"name"` to locate the associated value.

```text
"name"
   ↓
find matching key
   ↓
"Gajanand"
```

---

# 6. Dictionary Uses Hashing

This is one of the most important concepts for DSA.

Python dictionaries are implemented using a **hash table**.

Conceptually:

```text
Key
 ↓
Hash
 ↓
Location
 ↓
Value
```

For example:

```python
student["age"]
```

Conceptually:

```text
"age"
  ↓
hash("age")
  ↓
find appropriate location
  ↓
retrieve 22
```

You don't manually calculate the hash.

Python handles it.

This is why dictionary lookup is **O(1) average case**.

We'll study hashing much more deeply when we reach the DSA/hash-table section.

---

# 7. Creating a Dictionary

## Method 1 — `{}`

```python
student = {}
```

This creates an empty dictionary.

Check:

```python
print(type(student))
```

Output:

```text
<class 'dict'>
```

---

## Method 2 — `dict()`

```python
student = dict()
```

Same result:

```python
print(type(student))
```

```text
<class 'dict'>
```

### Important

```python
{}
```

means:

> Empty dictionary

Whereas:

```python
set()
```

means:

> Empty set

---

# 8. Creating a Dictionary With Data

```python
student = {
    "name": "Gajanand",
    "age": 22,
    "USN": "1NH23AI406"
}
```

We have three key-value pairs:

```text
"name" → "Gajanand"
"age"  → 22
"USN"  → "1NH23AI406"
```

---

# 9. Keys Can Have Different Types

Dictionary keys don't have to be strings.

Example:

```python
data = {
    1: "One",
    2: "Two",
    3: "Three"
}
```

Now:

```python
print(data[1])
```

Output:

```text
One
```

Here:

```text
1 → "One"
```

---

You can also have tuples as keys:

```python
locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}
```

This is particularly useful in DSA for coordinates.

```python
locations[(10, 20)]
```

---

# 10. What Can Be a Dictionary Key?

A dictionary key must be **hashable**.

Common valid keys:

```python
"name"
10
3.14
True
(1, 2)
```

Common invalid key:

```python
[1, 2, 3]
```

because lists are mutable and therefore unhashable.

For example:

```python
data = {
    [1, 2]: "Hello"
}
```

produces:

```text
TypeError: unhashable type: 'list'
```

### 🧠 Important rule

> **Dictionary keys must be hashable.**

We'll return to this concept when we study hashing in detail.

---

# 11. Values Can Be Almost Anything

Unlike keys, values don't have the same hashability restriction.

You can have:

```python
data = {
    "name": "Gajanand",
    "marks": [80, 90, 85],
    "address": {
        "city": "Bidar"
    },
    "subjects": ("Python", "SQL")
}
```

So values can be:

```text
string
integer
float
boolean
list
tuple
set
dictionary
etc.
```

---

# 12. Accessing Values

This is the most basic dictionary operation.

```python
student = {
    "name": "Gajanand",
    "age": 22
}
```

Access:

```python
print(student["name"])
```

Output:

```text
Gajanand
```

And:

```python
print(student["age"])
```

Output:

```text
22
```

---

# 13. How Python Evaluates `student["name"]`

Let's understand it deeply.

```python
student["name"]
```

Python conceptually does:

```text
student
 ↓
dictionary object
 ↓
look for key "name"
 ↓
key found
 ↓
retrieve associated value
 ↓
"Gajanand"
```

So `"name"` is **not an index**.

It is a **key**.

This is an important difference from lists.

---

# 14. List vs Dictionary Access

### List

```python
numbers = [10, 20, 30]
```

```python
numbers[0]
```

Here:

```text
0 = index
```

### Dictionary

```python
numbers = {
    "first": 10,
    "second": 20
}
```

```python
numbers["first"]
```

Here:

```text
"first" = key
```

Therefore:

```text
LIST       → index
DICTIONARY → key
```

---

# 15. What Happens If the Key Doesn't Exist?

Consider:

```python
student = {
    "name": "Gajanand",
    "age": 22
}
```

Now:

```python
print(student["salary"])
```

There is no `"salary"` key.

Python raises:

```text
KeyError
```

This is a very important mistake to understand.

---

# 16. `get()` — Safe Access

Instead of:

```python
student["salary"]
```

you can use:

```python
student.get("salary")
```

If the key doesn't exist:

```python
print(student.get("salary"))
```

Output:

```text
None
```

No `KeyError`.

---

# 17. `[]` vs `.get()`

| Code                    | Missing key  |
| ----------------------- | ------------ |
| `student["salary"]`     | ❌ `KeyError` |
| `student.get("salary")` | ✅ `None`     |

This distinction becomes **very important in DSA**.

---

# 18. `get()` With a Default Value

You can also provide a default:

```python
salary = student.get("salary", 0)

print(salary)
```

Output:

```text
0
```

Meaning:

> "Give me salary if it exists; otherwise give me `0`."

This is extremely useful in frequency-counting problems.

For example:

```python
frequency[char] = frequency.get(char, 0) + 1
```

This single line is a **very important DSA pattern**.

We'll break it down carefully later.

---

# 19. Adding a New Key

Suppose:

```python
student = {
    "name": "Gajanand",
    "age": 22
}
```

Add:

```python
student["city"] = "Bidar"
```

Now:

```text
"name" → "Gajanand"
"age"  → 22
"city" → "Bidar"
```

So:

```python
print(student)
```

contains the new key-value pair.

---

# 20. Updating an Existing Key

Suppose:

```python
student = {
    "name": "Gajanand",
    "age": 22
}
```

Now:

```python
student["age"] = 23
```

Python finds `"age"` and changes its value.

```text
Before:

"age" → 22

After:

"age" → 23
```

### Important

The same syntax:

```python
dict[key] = value
```

does **two jobs**:

```text
Key doesn't exist
        ↓
      ADD

Key already exists
        ↓
     UPDATE
```

This is fundamental.

---

# 📝 Practice Before We Continue

Don't just give the final answer. Explain what Python does.

### Problem 1

```python
student = {
    "name": "Gajanand",
    "age": 22
}

print(student["name"])
```

What happens internally?

---

### Problem 2

```python
student = {
    "name": "Gajanand",
    "age": 22
}

student["city"] = "Bidar"

print(student)
```

Did we **add** or **update**?

---

### Problem 3

```python
student = {
    "name": "Gajanand",
    "age": 22
}

student["age"] = 23

print(student)
```

Did we **add** or **update**?

---

### Problem 4

What is the difference between:

```python
student["salary"]
```

and:

```python
student.get("salary")
```

when `"salary"` doesn't exist?

---

### Problem 5 — Memory Model

For:

```python
student = {
    "name": "Gajanand",
    "age": 22
}
```

Identify:

```text
Keys:
Values:
```

And explain why:

```python
student["name"]
```

uses `"name"` as a **key**, not an index.

---


