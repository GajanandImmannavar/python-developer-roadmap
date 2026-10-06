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

Yes. Let's complete the **remaining Dictionary methods and operations** systematically. We won't leave gaps.

# 🐍 Dictionary — Remaining Methods & Operations

We already covered:

* Creating dictionaries
* Keys and values
* Accessing with `[]`
* `get()`
* Adding
* Updating
* Basic hashing concept

Now we'll cover the rest.

---

# 1. `del` — Delete a Key-Value Pair

```python
student = {
    "name": "Gajanand",
    "age": 22,
    "city": "Bidar"
}

del student["city"]

print(student)
```

Output:

```text
{'name': 'Gajanand', 'age': 22}
```

### What happened?

Before:

```text
"name" → "Gajanand"
"age"  → 22
"city" → "Bidar"
```

After:

```text
"name" → "Gajanand"
"age"  → 22
```

`del` removes the **entire key-value pair**.

### Important

If the key doesn't exist:

```python
del student["salary"]
```

you get:

```text
KeyError
```

---

# 2. `pop()` — Remove and Return a Value

```python
student = {
    "name": "Gajanand",
    "age": 22,
    "city": "Bidar"
}

result = student.pop("age")

print(result)
print(student)
```

Output:

```text
22
{'name': 'Gajanand', 'city': 'Bidar'}
```

This is different from `del`.

```text
del
 ↓
delete

pop()
 ↓
delete + return removed value
```

### Memory trick

> `pop()` = **take something out**

---

# 3. `pop()` With Default Value

Normally:

```python
student.pop("salary")
```

If `"salary"` doesn't exist:

```text
KeyError
```

But:

```python
student.pop("salary", 0)
```

returns:

```text
0
```

without raising an error.

This is useful when you aren't sure whether the key exists.

---

# 4. `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

Example:

```python
student = {
    "name": "Gajanand",
    "age": 22,
    "city": "Bidar"
}

result = student.popitem()

print(result)
print(student)
```

Output:

```text
('city', 'Bidar')
{'name': 'Gajanand', 'age': 22}
```

The returned value is a tuple:

```text
('city', 'Bidar')
```

### Important

In modern Python, dictionaries preserve insertion order, so `popitem()` removes the **last inserted item**.

---

# 5. `clear()`

Removes **everything** from the dictionary.

```python
student = {
    "name": "Gajanand",
    "age": 22
}

student.clear()

print(student)
```

Output:

```text
{}
```

The dictionary still exists.

It is simply empty.

```text
Before:

student → {"name": "Gajanand", "age": 22}

After:

student → {}
```

---

# 6. `keys()`

Returns a view containing the dictionary's keys.

```python
student = {
    "name": "Gajanand",
    "age": 22
}

print(student.keys())
```

Conceptually:

```text
dict_keys(['name', 'age'])
```

You can iterate over it:

```python
for key in student.keys():
    print(key)
```

Output:

```text
name
age
```

---

# 7. `values()`

Returns a view containing the values.

```python
student = {
    "name": "Gajanand",
    "age": 22
}

print(student.values())
```

Conceptually:

```text
dict_values(['Gajanand', 22])
```

Iteration:

```python
for value in student.values():
    print(value)
```

Output:

```text
Gajanand
22
```

---

# 8. `items()` ⭐⭐⭐

This is **extremely important**.

`items()` gives you both:

```text
key + value
```

Example:

```python
student = {
    "name": "Gajanand",
    "age": 22
}

print(student.items())
```

Conceptually:

```text
dict_items([
    ('name', 'Gajanand'),
    ('age', 22)
])
```

---

## Most common usage

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Gajanand
age 22
```

This pattern is used constantly in Python.

---

# 9. Difference Between `keys()`, `values()`, `items()`

| Method     | Gives       |
| ---------- | ----------- |
| `keys()`   | Keys        |
| `values()` | Values      |
| `items()`  | Key + Value |

Think:

```text
keys()
   ↓
"name", "age"

values()
   ↓
"Gajanand", 22

items()
   ↓
"name" → "Gajanand"
"age"  → 22
```

---

# 10. Membership — `in`

You already learned this, but it is important enough to include in the complete dictionary topic.

```python
student = {
    "name": "Gajanand",
    "age": 22
}

print("name" in student)
```

Output:

```text
True
```

Python checks the **keys**.

```python
print("Gajanand" in student)
```

Output:

```text
False
```

Because `"Gajanand"` is a value.

---

# 11. Checking Values

If you want to check values:

```python
print("Gajanand" in student.values())
```

Output:

```text
True
```

So:

```text
"x" in dictionary
        ↓
     checks keys

"x" in dictionary.values()
        ↓
     checks values
```

---

# 12. `not in`

Same concept:

```python
print("salary" not in student)
```

Output:

```text
True
```

Because `"salary"` isn't a key.

---

# 13. `len()` With Dictionary

`len()` tells you the number of **key-value pairs**.

```python
student = {
    "name": "Gajanand",
    "age": 22,
    "city": "Bidar"
}

print(len(student))
```

Output:

```text
3
```

Not 6.

Because there are three entries:

```text
"name" → "Gajanand"
"age"  → 22
"city" → "Bidar"
```

---

# 14. Iterating Through a Dictionary

## Only keys

```python
for key in student:
    print(key)
```

This is equivalent to:

```python
for key in student.keys():
    print(key)
```

Output:

```text
name
age
city
```

### Important

When you directly loop over a dictionary:

```python
for x in student:
```

`x` receives the **keys**.

---

# 15. Only Values

```python
for value in student.values():
    print(value)
```

Output:

```text
Gajanand
22
Bidar
```

---

# 16. Key + Value

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Gajanand
age 22
city Bidar
```

This is the standard way to iterate through both.

---

# 17. `update()`

`update()` adds or changes multiple key-value pairs.

```python
student = {
    "name": "Gajanand",
    "age": 22
}

student.update({
    "age": 23,
    "city": "Bidar"
})

print(student)
```

Result:

```text
{
    "name": "Gajanand",
    "age": 23,
    "city": "Bidar"
}
```

Notice:

```text
age
 ↓
already existed
 ↓
updated
```

and:

```text
city
 ↓
didn't exist
 ↓
added
```

So `update()` can:

> **Add + Update**

---

# 18. `setdefault()`

This one is important, especially for DSA.

```python
student = {
    "name": "Gajanand"
}

student.setdefault("age", 22)

print(student)
```

Result:

```text
{
    "name": "Gajanand",
    "age": 22
}
```

It adds the key **only if the key doesn't already exist**.

---

## Existing key

```python
student = {
    "age": 22
}

student.setdefault("age", 30)

print(student)
```

Result:

```text
{
    "age": 22
}
```

It does **not** replace 22 with 30.

### Memory trick

```text
setdefault()

Does key exist?
     │
 ┌───┴───┐
YES     NO
 │       │
keep    add
existing
value
```

---

# 19. `copy()`

Creates a **shallow copy** of the dictionary.

```python
student = {
    "name": "Gajanand",
    "age": 22
}

new_student = student.copy()
```

Now:

```text
student      → dictionary A

new_student  → dictionary B
```

They are separate dictionary objects.

```python
new_student["age"] = 23

print(student["age"])
print(new_student["age"])
```

Output:

```text
22
23
```

---

# 20. Assignment Is NOT Copying

Very important.

```python
student = {
    "name": "Gajanand"
}

new_student = student
```

Now:

```text
student
   ↘
    same dictionary
   ↗
new_student
```

So:

```python
new_student["age"] = 22
```

also changes `student`.

Because both variables refer to the **same dictionary object**.

This connects directly to what you learned about `is`.

---

# 21. `copy()` vs Assignment

```python
a = {"x": 10}
b = a
```

```text
a ──┐
    ├──→ same object
b ──┘
```

But:

```python
a = {"x": 10}
b = a.copy()
```

```text
a ──→ object A

b ──→ object B
```

Therefore:

```python
a is b
```

### Assignment:

```text
True
```

### `.copy()`:

```text
False
```

---

# 22. Merging Dictionaries

Python supports dictionary merging using `|`.

```python
student1 = {
    "name": "Gajanand",
    "age": 22
}

student2 = {
    "city": "Bidar",
    "course": "AI & ML"
}

result = student1 | student2

print(result)
```

Result:

```text
{
    "name": "Gajanand",
    "age": 22,
    "city": "Bidar",
    "course": "AI & ML"
}
```

The original dictionaries remain unchanged.

---

# 23. Merging With `update()`

You can also:

```python
student1.update(student2)
```

Difference:

```text
| 
↓
creates a new dictionary

update()
↓
modifies existing dictionary
```

---

# 24. Duplicate Keys During Creation

Consider:

```python
student = {
    "age": 22,
    "age": 25
}
```

What happens?

The later value wins.

```text
"age" → 25
```

So:

```python
print(student)
```

gives:

```text
{'age': 25}
```

A dictionary cannot have two separate entries with the same key.

---

# 25. Dictionary Comprehension

This is an important Python topic.

Normal:

```python
numbers = {}

for number in range(1, 6):
    numbers[number] = number * number
```

Result:

```text
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

Dictionary comprehension:

```python
numbers = {
    number: number * number
    for number in range(1, 6)
}
```

Same result.

### Structure

```text
{
    key: value
    for item in iterable
}
```

We'll practice this separately because comprehension deserves its own deep lesson.

---

# 26. Nested Dictionary

A dictionary can contain another dictionary.

```python
students = {
    "student1": {
        "name": "Gajanand",
        "age": 22
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}
```

Access:

```python
print(students["student1"]["name"])
```

Output:

```text
Gajanand
```

Memory:

```text
students
   │
   ├── student1
   │      ├── name → Gajanand
   │      └── age  → 22
   │
   └── student2
          ├── name → Rahul
          └── age  → 21
```

Nested dictionaries are common in real applications and interview problems.

---

# 27. Dictionary With Lists

Very common in DSA:

```python
data = {
    "numbers": [10, 20, 30],
    "names": ["A", "B", "C"]
}
```

Access:

```python
print(data["numbers"][0])
```

Output:

```text
10
```

Here you're combining:

```text
dictionary key
      ↓
list
      ↓
index
```

---

# 28. Dictionary With Sets

```python
data = {
    "unique_numbers": {1, 2, 3}
}
```

Access:

```python
print(data["unique_numbers"])
```

Again, dictionary values can contain complex structures.

---

# 29. DSA Pattern — Frequency Counting ⭐⭐⭐

This is one of the most important dictionary applications.

```python
numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)
```

Result:

```text
{
    1: 1,
    2: 2,
    3: 3
}
```

The important expression is:

```python
frequency.get(number, 0) + 1
```

Meaning:

```text
Does number exist?
      │
   ┌──┴──┐
  YES    NO
   │      │
current   0
 count
   │      │
   └──┬───┘
      ↓
    + 1
```

This pattern will appear **again and again in DSA**.

---

# 30. DSA Pattern — Character Frequency

```python
text = "banana"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
```

Result:

```text
{'b': 1, 'a': 3, 'n': 2}
```

Used for:

* Anagrams
* Duplicate characters
* Character frequency
* First non-repeating character
* Most frequent character

---

# 31. DSA Pattern — Seen/Lookup

Sometimes we don't need a count.

We just need:

> "Have I already seen this?"

Use a set:

```python
seen = set()
```

But sometimes we need associated information:

```text
number → index
```

Then use a dictionary:

```python
seen = {}
```

Example:

```python
numbers = [2, 7, 11, 15]
```

For Two Sum, we might store:

```text
2  → index 0
7  → index 1
```

This is the beginning of the famous **hash-map pattern**.

---

# 32. Dictionary Method Summary

You should now know these:

| Operation / Method | Purpose                   |
| ------------------ | ------------------------- |
| `{}`               | Create empty dictionary   |
| `dict()`           | Create dictionary         |
| `d[key]`           | Access                    |
| `d[key] = value`   | Add/update                |
| `get()`            | Safe access               |
| `setdefault()`     | Add only if absent        |
| `update()`         | Add/update multiple       |
| `del`              | Delete                    |
| `pop()`            | Remove + return           |
| `popitem()`        | Remove last inserted pair |
| `clear()`          | Remove everything         |
| `keys()`           | Get keys                  |
| `values()`         | Get values                |
| `items()`          | Get key-value pairs       |
| `copy()`           | Shallow copy              |
| `len()`            | Number of pairs           |
| `in`               | Check key                 |
| `not in`           | Check missing key         |
| `\|`               | Merge dictionaries        |

---

# 🧠 Dictionary Mental Model

Remember this:

```text
                 DICTIONARY
                      │
                      ▼
                 KEY → VALUE
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Access       Update      Delete
          │           │           │
       d[key]      d[key]=x      pop()
       get()       update()      del
                                popitem()
                                clear()
```

And for DSA:

```text
             DICTIONARY
                  │
                  ▼
               HASH MAP
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
   Frequency    Lookup    Mapping
    Counting     Table
       │          │
       ▼          ▼
   Anagrams    Two Sum
   Duplicates  Index lookup
```

---

# ⚠️ Important Things You Must Remember

### 1. Dictionary uses keys, not indexes

```python
student["name"]
```

`"name"` is a key.

---

### 2. `in` checks keys

```python
"name" in student
```

not values.

---

### 3. Keys must be hashable

```text
int       ✅
str       ✅
tuple     ✅

list      ❌
dict      ❌
set       ❌
```

---

### 4. `[]` and `get()` behave differently

```python
d["x"]
```

missing key → `KeyError`

```python
d.get("x")
```

missing key → `None`

---

### 5. `d[key] = value` can add OR update

```text
key absent  → ADD
key exists  → UPDATE
```

---

### 6. `pop()` returns what it removes

```python
value = d.pop("age")
```

---

### 7. `popitem()` removes the last inserted pair

---

### 8. `{}` is an empty dictionary

```python
set()
```

is an empty set.

---


