# 🐍 Python Functions & Methods — DSA Technical Round Revision Sheet

> **Purpose:** Quick morning revision for Python technical rounds and DSA interviews.
>
> For every important function/method, remember:
>
> **What it does → Syntax → Output → Important variation → DSA use → Time Complexity → Interview trap**

---

# ⭐ PART 1 — PYTHON BUILT-IN FUNCTIONS

| # | Function | What It Does | Basic Example | Output | Important DSA Syntax / Variation | DSA Use | Remember |
|---:|---|---|---|---|---|---|---|
| 1 | `len()` | Returns number of elements | `len([10,20,30])` | `3` | `len(arr)-1` → last index | Array/String length | **HOW MANY?** |
| 2 | `range()` | Generates number sequence | `list(range(5))` | `[0,1,2,3,4]` | `range(1,n+1)` → `1...n`<br>`range(n)` → `0...n-1`<br>`range(n-1,-1,-1)` → reverse | Loops / indexes | **STOP EXCLUDED** |
| 3 | `sum()` | Calculates total | `sum([1,2,3])` | `6` | `sum(arr)` | Array sum | **TOTAL** |
| 4 | `min()` | Finds smallest value | `min([5,2,8])` | `2` | `min(arr)` | Minimum problems | **SMALLEST** |
| 5 | `max()` | Finds largest value | `max([5,2,8])` | `8` | `max(arr)` | Maximum problems | **LARGEST** |
| 6 | `abs()` | Returns absolute value | `abs(-10)` | `10` | `abs(a-b)` → absolute difference | Distance / difference | **REMOVE SIGN** |
| 7 | `sorted()` | Returns sorted copy | `sorted([3,1,2])` | `[1,2,3]` | `sorted(arr, reverse=True)` → descending | Sorting | **NEW LIST** |
| 8 | `reversed()` | Returns reverse iterator | `list(reversed([1,2,3]))` | `[3,2,1]` | `list(reversed(arr))` | Reverse traversal | **REVERSE** |
| 9 | `enumerate()` | Gives index + value | `list(enumerate(['a','b']))` | `[(0,'a'),(1,'b')]` | `enumerate(arr,start=1)` | Index tracking | **INDEX + VALUE** |
| 10 | `zip()` | Combines iterables | `list(zip([1,2],[3,4]))` | `[(1,3),(2,4)]` | `zip(a,b)` / `zip(a,b,c)` | Multiple arrays | **PAIR** |
| 11 | `any()` | True if at least one is true | `any([False,True])` | `True` | `any(x > 0 for x in arr)` | Condition checking | **ONE** |
| 12 | `all()` | True if everything is true | `all([True,True])` | `True` | `all(x > 0 for x in arr)` | Validation | **EVERY** |
| 13 | `ord()` | Character → number | `ord('A')` | `65` | `ord(ch)-ord('a')` → alphabet index | Character problems | **CHAR → NUMBER** |
| 14 | `chr()` | Number → character | `chr(65)` | `'A'` | `chr(ord(ch)+1)` | Character manipulation | **NUMBER → CHAR** |
| 15 | `set()` | Creates unique collection | `set([1,2,2])` | `{1,2}` | `set(arr)` → remove duplicates | Hashing / duplicates | **UNIQUE** |

---

# 🔥 PART 2 — `range()` DSA SPECIAL TABLE

> **Important:** `range(start, stop, step)` does **NOT include the stop value**.

| What You Want | Code | If `n = 5` | Output |
|---|---|---|---|
| `0` to `n-1` | `range(n)` | `range(5)` | `0 1 2 3 4` |
| `1` to `n` | `range(1,n+1)` | `range(1,6)` | `1 2 3 4 5` |
| `1` to `n-1` | `range(1,n)` | `range(1,5)` | `1 2 3 4` |
| `0` to `n` | `range(n+1)` | `range(6)` | `0 1 2 3 4 5` |
| Reverse `n-1` to `0` | `range(n-1,-1,-1)` | `range(4,-1,-1)` | `4 3 2 1 0` |
| Reverse `n` to `1` | `range(n,0,-1)` | `range(5,0,-1)` | `5 4 3 2 1` |
| Even numbers | `range(2,n+1,2)` | `range(2,6,2)` | `2 4` |
| Odd numbers | `range(1,n+1,2)` | `range(1,6,2)` | `1 3 5` |

## 🚨 Off-by-One Error

### Want `1` through `n`?

```python
for i in range(1, n + 1):
    print(i)
```

If:

```python
n = 5
```

Output:

```text
1
2
3
4
5
```

### Wrong:

```python
for i in range(1, n):
    print(i)
```

Output:

```text
1
2
3
4
```

`5` is missing.

### 🧠 Golden Rule

```text
range(start, stop, step)
             ↑
       STOP IS EXCLUDED
```

---

# ⭐ PART 3 — LIST / ARRAY METHODS

| # | Method | What It Does | Example | Output | Important DSA Syntax / Variation | DSA Use | Remember |
|---:|---|---|---|---|---|---|---|
| 1 | `append()` | Adds one element | `a=[1,2]; a.append(3)` | `[1,2,3]` | `stack.append(x)` | Stack / building list | **ONE** |
| 2 | `extend()` | Adds multiple elements | `a=[1,2]; a.extend([3,4])` | `[1,2,3,4]` | `a.extend(other)` | Merge lists | **MANY** |
| 3 | `insert()` | Adds at index | `a=[1,3]; a.insert(1,2)` | `[1,2,3]` | `insert(index,value)` | Insertion | **AT INDEX** |
| 4 | `pop()` | Removes and returns element | `a=[1,2,3]; a.pop()` | `3` | `pop()` → last<br>`pop(i)` → index `i` | Stack | **REMOVE + RETURN** |
| 5 | `remove()` | Removes first matching value | `a=[1,2,3]; a.remove(2)` | `[1,3]` | `remove(value)` | Remove value | **BY VALUE** |
| 6 | `index()` | Finds first index | `[10,20].index(20)` | `1` | `index(value)` | Search position | **WHERE?** |
| 7 | `count()` | Counts occurrences | `[1,2,2].count(2)` | `2` | `count(value)` | Frequency | **HOW MANY?** |
| 8 | `sort()` | Sorts original list | `a=[3,1,2]; a.sort()` | `[1,2,3]` | `sort(reverse=True)` | Sorting | **MODIFY ORIGINAL** |
| 9 | `reverse()` | Reverses original list | `a=[1,2,3]; a.reverse()` | `[3,2,1]` | `reverse()` | Reverse array | **MODIFY ORIGINAL** |
| 10 | `clear()` | Removes everything | `a=[1,2]; a.clear()` | `[]` | `clear()` | Reset list | **EMPTY** |
| 11 | `copy()` | Creates shallow copy | `b=a.copy()` | Same values | `b=a.copy()` | Safe copy | **NEW LIST** |

---

# 🔥 PART 4 — LIST METHOD COMPARISON

| Method | Takes | Returns | Modifies Original? | Example |
|---|---|---|---|---|
| `append(x)` | One object | `None` | ✅ Yes | `a.append(5)` |
| `extend(x)` | Iterable | `None` | ✅ Yes | `a.extend([5,6])` |
| `insert(i,x)` | Index + value | `None` | ✅ Yes | `a.insert(1,5)` |
| `pop()` | Optional index | Removed value | ✅ Yes | `a.pop()` |
| `remove(x)` | Value | `None` | ✅ Yes | `a.remove(5)` |
| `index(x)` | Value | Index | ❌ No | `a.index(5)` |
| `count(x)` | Value | Count | ❌ No | `a.count(5)` |
| `sort()` | Optional options | `None` | ✅ Yes | `a.sort()` |
| `reverse()` | Nothing | `None` | ✅ Yes | `a.reverse()` |
| `copy()` | Nothing | New list | ❌ No | `b=a.copy()` |

---

# ⭐ PART 5 — STRING METHODS

| # | Method | What It Does | Example | Output | Important DSA Syntax / Variation | DSA Use | Remember |
|---:|---|---|---|---|---|---|---|
| 1 | `lower()` | Converts to lowercase | `"PYTHON".lower()` | `"python"` | `s.lower()` | Case normalization | **LOWER** |
| 2 | `upper()` | Converts to uppercase | `"python".upper()` | `"PYTHON"` | `s.upper()` | Case normalization | **UPPER** |
| 3 | `strip()` | Removes outer whitespace | `" hi ".strip()` | `"hi"` | `strip()` / `lstrip()` / `rstrip()` | Input cleaning | **OUTER SPACE** |
| 4 | `split()` | String → list | `"a b c".split()` | `['a','b','c']` | `split()` / `split(",")` | Word problems | **STRING → LIST** |
| 5 | `join()` | Joins strings | `" ".join(['a','b'])` | `"a b"` | `",".join(arr)` | Build strings | **LIST → STRING** |
| 6 | `replace()` | Replaces substring | `"cat".replace("c","b")` | `"bat"` | `replace(old,new)` | String manipulation | **REPLACE** |
| 7 | `find()` | Finds first position | `"python".find("t")` | `2` | Not found → `-1` | Search | **POSITION** |
| 8 | `count()` | Counts occurrence | `"banana".count("a")` | `3` | `count(substring)` | Frequency | **COUNT** |
| 9 | `startswith()` | Checks beginning | `"python".startswith("py")` | `True` | `startswith(prefix)` | Prefix problems | **START** |
| 10 | `endswith()` | Checks ending | `"python".endswith("on")` | `True` | `endswith(suffix)` | Suffix problems | **END** |
| 11 | `isdigit()` | Checks digits | `"123".isdigit()` | `True` | `"123a"` → `False` | Number validation | **DIGIT?** |
| 12 | `isalpha()` | Checks alphabets | `"Python".isalpha()` | `True` | `"Python1"` → `False` | Character validation | **ALPHA?** |
| 13 | `isalnum()` | Checks letters/numbers | `"Python123".isalnum()` | `True` | No spaces/special chars | Validation | **ALPHA + NUMBER** |

---

# ⭐ PART 6 — SET / HASHING

| # | Operation | What It Does | Example | Result | Important DSA Syntax / Variation | DSA Use | Remember |
|---:|---|---|---|---|---|---|---|
| 1 | `set()` | Creates unique set | `set([1,2,2])` | `{1,2}` | `set(arr)` | Remove duplicates | **UNIQUE** |
| 2 | `add()` | Adds one element | `s.add(4)` | Adds `4` | `add(x)` | Build set | **ONE** |
| 3 | `update()` | Adds multiple | `s.update([4,5])` | Adds `4,5` | `update(iterable)` | Merge values | **MANY** |
| 4 | `remove()` | Removes value | `s.remove(2)` | Removes `2` | Error if missing | Deletion | **STRICT** |
| 5 | `discard()` | Safely removes | `s.discard(2)` | Removes if exists | No error if missing | Safe deletion | **SAFE** |
| 6 | `in` | Membership check | `2 in s` | `True/False` | `x in set` | Fast lookup | **EXISTS?** |
| 7 | `|` | Union | `a \| b` | `{1,2,3,4,5}` | `a.union(b)` | Combine unique | **ALL** |
| 8 | `&` | Intersection | `a & b` | `{3}` | `a.intersection(b)` | Common values | **COMMON** |
| 9 | `-` | Difference | `a - b` | `{1,2}` | `a.difference(b)` | A but not B | **A NOT B** |
| 10 | `^` | Symmetric difference | `a ^ b` | `{1,2,4,5}` | `a.symmetric_difference(b)` | Non-common | **NOT BOTH** |

---

# 🔥 SET OPERATIONS

Given:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

| Operation | Code | Result | Meaning |
|---|---|---|---|
| Union | `a \| b` | `{1,2,3,4,5}` | Everything |
| Intersection | `a & b` | `{3}` | Common |
| Difference | `a - b` | `{1,2}` | A but not B |
| Reverse Difference | `b - a` | `{4,5}` | B but not A |
| Symmetric Difference | `a ^ b` | `{1,2,4,5}` | Not common |

---

# ⭐ PART 7 — DICTIONARY / HASHMAP

| # | Method / Operation | What It Does | Example | Result | Important DSA Syntax / Variation | DSA Use | Remember |
|---:|---|---|---|---|---|---|---|
| 1 | `get()` | Safe lookup | `d.get('a',0)` | `0` if missing | `get(key,default)` | Frequency | **SAFE LOOKUP** |
| 2 | `keys()` | Gets keys | `d.keys()` | Keys | `for k in d` | Key traversal | **KEYS** |
| 3 | `values()` | Gets values | `d.values()` | Values | `for v in d.values()` | Value traversal | **VALUES** |
| 4 | `items()` | Gets key + value | `d.items()` | Pairs | `for k,v in d.items()` | HashMap traversal | **BOTH** |
| 5 | `pop()` | Removes key + returns value | `d.pop('a')` | Removed value | `pop(key)` | Delete mapping | **REMOVE + RETURN** |
| 6 | `update()` | Adds/updates mappings | `d.update({'b':2})` | Updated dict | `update(other_dict)` | Merge/update | **UPDATE** |
| 7 | `setdefault()` | Gets or creates key | `d.setdefault('a',[])` | Value | Useful for grouping | Grouping | **GET OR CREATE** |
| 8 | `in` | Checks key | `'a' in d` | `True/False` | Checks keys | Fast lookup | **KEY EXISTS?** |

---

# 🔥 `dict[key]` VS `dict.get()`

| Code | If Key Exists | If Key Does NOT Exist |
|---|---|---|
| `d["a"]` | Returns value | ❌ `KeyError` |
| `d.get("a")` | Returns value | `None` |
| `d.get("a",0)` | Returns value | `0` |
| `d.get("a",[])` | Returns value | `[]` |

---

# ⭐ PART 8 — FREQUENCY COUNTING

## Basic Pattern

```python
arr = [1, 2, 2, 3, 3, 3]

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)
```

### Output

```text
{1: 1, 2: 2, 3: 3}
```

### Step-by-Step

| Step | Code | Meaning |
|---:|---|---|
| 1 | `freq = {}` | Create HashMap |
| 2 | `freq.get(x,0)` | Get current count |
| 3 | `+ 1` | Increase count |
| 4 | `freq[x] = ...` | Store new count |
| 5 | `freq.items()` | Traverse key + frequency |

### Interview Question

**Q: Why use a dictionary for frequency counting?**

**Answer:**

> Dictionary lookup and insertion are **O(1) on average**, so frequency counting can be done in **O(n) average time**.

---

# ⭐ PART 9 — DUPLICATE DETECTION

## Method 1 — Using `set()`

```python
arr = [1, 2, 3, 2]

if len(arr) != len(set(arr)):
    print("Duplicate exists")
```

### Why?

```text
Original:
[1, 2, 3, 2]
length = 4

Set:
{1, 2, 3}
length = 3

4 != 3
↓
Duplicate exists
```

---

## Method 2 — Using `seen`

```python
arr = [1, 2, 3, 2]

seen = set()

for x in arr:

    if x in seen:
        print("Duplicate:", x)
        break

    seen.add(x)
```

### Important Tools

| Tool | Purpose |
|---|---|
| `set()` | Store unique elements |
| `in` | Fast membership check |
| `add()` | Store element |

---

# ⭐ PART 10 — STACK QUICK TABLE

| Stack Operation | Python Code | Meaning |
|---|---|---|
| Create | `stack = []` | Empty stack |
| Push | `stack.append(x)` | Add to top |
| Pop | `stack.pop()` | Remove top |
| Peek | `stack[-1]` | View top |
| Empty check | `not stack` | Check empty |

## Example

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])
print(stack.pop())
```

### Output

```text
30
30
```

### 🧠 Remember

```text
append() → PUSH
pop()    → POP
[-1]     → PEEK
not      → EMPTY?
```

---

# ⭐ PART 11 — TWO POINTER FOUNDATION

```python
arr.sort()

left = 0
right = len(arr) - 1

while left < right:

    # logic

    left += 1
    right -= 1
```

| Code | Meaning |
|---|---|
| `arr.sort()` | Sort array |
| `left = 0` | First index |
| `right = len(arr)-1` | Last index |
| `left < right` | Pointers haven't crossed |
| `left += 1` | Move left pointer |
| `right -= 1` | Move right pointer |

### Remember

```text
left  → 0
right → n - 1
```

---

# ⭐ PART 12 — REVERSE TRAVERSAL

| Requirement | Code | Output for `n=5` |
|---|---|---|
| `0 → n-1` | `range(n)` | `0 1 2 3 4` |
| `n-1 → 0` | `range(n-1,-1,-1)` | `4 3 2 1 0` |
| `1 → n` | `range(1,n+1)` | `1 2 3 4 5` |
| `n → 1` | `range(n,0,-1)` | `5 4 3 2 1` |

---

# ⭐ PART 13 — STRING DSA PATTERNS

| Problem | Useful Method | Example |
|---|---|---|
| Get words | `split()` | `"a b c".split()` |
| Join words | `join()` | `" ".join(words)` |
| Count character | `count()` | `s.count('a')` |
| Find character | `find()` | `s.find('a')` |
| Normalize case | `lower()` | `s.lower()` |
| Remove outer spaces | `strip()` | `s.strip()` |
| Replace character | `replace()` | `s.replace('a','b')` |
| Check digit | `isdigit()` | `s.isdigit()` |
| Check alphabet | `isalpha()` | `s.isalpha()` |
| Character → number | `ord()` | `ord(ch)` |
| Number → character | `chr()` | `chr(n)` |

---

# ⭐ PART 14 — DSA PATTERN TABLE

| DSA Problem / Pattern | Python Tool | Typical Code | Complexity |
|---|---|---|---:|
| Array length | `len()` | `len(arr)` | O(1) |
| Array sum | `sum()` | `sum(arr)` | O(n) |
| Maximum | `max()` | `max(arr)` | O(n) |
| Minimum | `min()` | `min(arr)` | O(n) |
| Sorting | `sorted()` | `sorted(arr)` | O(n log n) |
| Stack push | `append()` | `stack.append(x)` | O(1) amortized |
| Stack pop | `pop()` | `stack.pop()` | O(1) |
| Duplicate detection | `set()` | `len(arr) != len(set(arr))` | O(n) average |
| Fast membership | `set` | `x in seen` | O(1) average |
| Frequency counting | `dict.get()` | `freq[x]=freq.get(x,0)+1` | O(n) average |
| Index + value | `enumerate()` | `for i,x in enumerate(arr)` | O(n) |
| Pair arrays | `zip()` | `for a,b in zip(a,b)` | O(n) |
| Reverse traversal | `range()` | `range(n-1,-1,-1)` | O(n) |
| Word extraction | `split()` | `sentence.split()` | O(n) |
| Build sentence | `join()` | `" ".join(words)` | O(n) |
| Character index | `ord()` | `ord(ch)-ord('a')` | O(1) |

---

# ⭐ PART 15 — INTERVIEW TRAPS

| Question | Correct Answer |
|---|---|
| `append()` vs `extend()`? | `append()` adds one object; `extend()` adds elements from an iterable |
| `remove()` vs `pop()`? | `remove()` uses value; `pop()` uses index and returns removed value |
| `sort()` vs `sorted()`? | `sort()` modifies original; `sorted()` returns a new list |
| `reverse()` vs `reversed()`? | `reverse()` modifies list; `reversed()` returns an iterator |
| `split()` vs `join()`? | `split()` → string to list; `join()` → strings to one string |
| `set.remove()` vs `discard()`? | `remove()` errors if absent; `discard()` does not |
| `d[key]` vs `d.get(key)`? | `d[key]` can raise `KeyError`; `get()` safely returns default/`None` |
| `range(n)` output? | `0` through `n-1` |
| Need `1` through `n`? | `range(1,n+1)` |
| `x in list` complexity? | O(n) |
| `x in set` average complexity? | O(1) |
| `x in dict` average complexity? | O(1) |
| Why is `pop(0)` O(n)? | Remaining elements must shift left |
| Why is `append()` amortized O(1)? | Dynamic arrays usually have available space; occasional resizing is amortized |
| Why use a set for duplicate detection? | Fast membership checking, O(1) average |
| Why use a dictionary for frequency? | Fast key lookup and update, O(1) average |

---

# ⭐ PART 16 — TIME COMPLEXITY

| Python Operation | Typical Complexity |
|---|---:|
| `arr[index]` | O(1) |
| `arr.append(x)` | O(1) amortized |
| `arr.pop()` | O(1) |
| `arr.pop(0)` | O(n) |
| `arr.insert(0,x)` | O(n) |
| `arr.remove(x)` | O(n) |
| `arr.index(x)` | O(n) |
| `arr.count(x)` | O(n) |
| `arr.sort()` | O(n log n) |
| `sorted(arr)` | O(n log n) |
| `x in list` | O(n) |
| `x in set` | O(1) average |
| `x in dict` | O(1) average |
| `dict.get()` | O(1) average |
| `sum(arr)` | O(n) |
| `min(arr)` | O(n) |
| `max(arr)` | O(n) |

---

# ⭐ PART 17 — FUNCTION VS METHOD

| Type | Syntax | Examples |
|---|---|---|
| Function | `function(object)` | `len(arr)`, `sum(arr)`, `max(arr)` |
| Method | `object.method()` | `arr.append()`, `arr.sort()`, `text.split()` |

## 🧠 Memory Trick

```text
FUNCTION
function(object)

METHOD
object.method()
```

---

# ⭐ PART 18 — METHODS THAT RETURN `None`

These methods modify the original object and normally return `None`.

| Method | Returns | Modifies Original? |
|---|---|---|
| `append()` | `None` | ✅ Yes |
| `extend()` | `None` | ✅ Yes |
| `insert()` | `None` | ✅ Yes |
| `remove()` | `None` | ✅ Yes |
| `sort()` | `None` | ✅ Yes |
| `reverse()` | `None` | ✅ Yes |
| `clear()` | `None` | ✅ Yes |

## Example

```python
arr = [3, 1, 2]

result = arr.sort()

print(result)
```

Output:

```text
None
```

Correct:

```python
arr.sort()

print(arr)
```

Output:

```text
[1, 2, 3]
```

---

# ⭐ PART 19 — TOP 30 FUNCTIONS / METHODS

| # | Function / Method | Remember As |
|---:|---|---|
| 1 | `len()` | HOW MANY? |
| 2 | `range()` | LOOP / INDEX |
| 3 | `sum()` | TOTAL |
| 4 | `min()` | SMALLEST |
| 5 | `max()` | LARGEST |
| 6 | `abs()` | DIFFERENCE |
| 7 | `sorted()` | NEW SORTED |
| 8 | `enumerate()` | INDEX + VALUE |
| 9 | `zip()` | PAIR |
| 10 | `any()` | ONE |
| 11 | `all()` | EVERY |
| 12 | `append()` | ADD ONE |
| 13 | `extend()` | ADD MANY |
| 14 | `insert()` | ADD AT INDEX |
| 15 | `pop()` | REMOVE + RETURN |
| 16 | `remove()` | REMOVE VALUE |
| 17 | `index()` | FIND POSITION |
| 18 | `count()` | COUNT |
| 19 | `sort()` | SORT ORIGINAL |
| 20 | `reverse()` | REVERSE ORIGINAL |
| 21 | `split()` | STRING → LIST |
| 22 | `join()` | LIST → STRING |
| 23 | `find()` | FIND POSITION |
| 24 | `replace()` | REPLACE |
| 25 | `set()` | UNIQUE |
| 26 | `add()` | SET ADD |
| 27 | `in` | MEMBERSHIP |
| 28 | `dict.get()` | SAFE LOOKUP |
| 29 | `items()` | KEY + VALUE |
| 30 | `ord()` / `chr()` | CHAR ↔ NUMBER |

---

# 🧠 PART 20 — ONE-MINUTE MORNING REVISION

```text
len()        → HOW MANY?
range()      → LOOP / INDEX
range(1,n+1) → 1 TO n
sum()        → TOTAL
min()        → SMALLEST
max()        → LARGEST
abs()        → ABSOLUTE DIFFERENCE

sorted()     → NEW SORTED LIST
sort()       → ORIGINAL LIST SORTED

append()     → ADD ONE
extend()     → ADD MANY
insert()     → ADD AT INDEX

pop()        → REMOVE + RETURN
remove()     → REMOVE BY VALUE

enumerate()  → INDEX + VALUE
zip()        → PAIR

split()      → STRING → LIST
join()       → LIST → STRING

set()        → UNIQUE
add()        → ADD ONE
discard()    → SAFE REMOVE
in           → MEMBERSHIP

dict.get()   → SAFE LOOKUP
keys()       → KEYS
values()     → VALUES
items()      → KEY + VALUE

ord()        → CHAR → NUMBER
chr()        → NUMBER → CHAR

any()        → AT LEAST ONE
all()        → EVERY ONE
```

---

# 🏆 PART 21 — GOLDEN DSA MAP

```text
                         PYTHON DSA
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
      ARRAY                STRING                HASHING
       │                     │                     │
    len()                 split()               set()
    range()               join()                add()
    sum()                 find()                in
    min()                 count()               discard()
    max()                 replace()             dict
    sorted()              lower()               get()
    append()              upper()               items()
    pop()                                       keys()
    sort()                                      values()
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             │
                         TRAVERSAL
                             │
                    enumerate() / zip()
                             │
                           STACK
                             │
                    append() + pop()
```

---

# 🎯 PART 22 — FINAL INTERVIEW CHECK

Before your technical round, make sure you can answer these immediately:

| Question | Immediate Answer |
|---|---|
| How do I get array length? | `len(arr)` |
| How do I loop `0` to `n-1`? | `range(n)` |
| How do I loop `1` to `n`? | `range(1,n+1)` |
| Why `n+1`? | Because `range()` excludes the stop value |
| How do I reverse loop? | `range(n-1,-1,-1)` |
| How do I sort? | `sorted(arr)` or `arr.sort()` |
| Difference? | New list vs modify original |
| How do I implement Stack? | `append()` + `pop()` |
| How do I check duplicates? | `set()` / `seen` |
| How do I count frequency? | `dict.get()` |
| How do I perform fast lookup? | `set` / `dict` |
| How do I get index + value? | `enumerate()` |
| How do I process two arrays together? | `zip()` |
| How do I convert string to words? | `split()` |
| How do I convert words to string? | `join()` |
| How do I convert character to number? | `ord()` |
| How do I convert number to character? | `chr()` |
| Why use set instead of list for lookup? | O(1) average vs O(n) |
| Why dictionary for frequency? | O(1) average lookup/update |
| Why is `pop(0)` slow? | Remaining elements shift left |

---

# 🧠 PART 23 — THE 6 QUESTIONS FOR EVERY FUNCTION

For every important Python function/method, ask yourself:

```text
1. WHAT does it do?
        ↓
2. WHAT is the syntax?
        ↓
3. WHAT does it return?
        ↓
4. DOES it modify the original?
        ↓
5. WHAT is the time complexity?
        ↓
6. WHERE is it used in DSA?
```

---

# 🔥 FINAL GOLDEN RULES

```text
range(n)
→ 0 to n-1

range(1,n+1)
→ 1 to n

range(n-1,-1,-1)
→ reverse indexes

len(arr)-1
→ last index

append()
→ PUSH

pop()
→ POP

stack[-1]
→ PEEK

set()
→ UNIQUE

x in set
→ FAST LOOKUP

dict.get()
→ SAFE LOOKUP

freq[x] = freq.get(x,0) + 1
→ FREQUENCY COUNT

enumerate()
→ INDEX + VALUE

zip()
→ PAIR

split()
→ STRING → LIST

join()
→ LIST → STRING

sorted()
→ NEW SORTED LIST

sort()
→ MODIFY ORIGINAL

remove()
→ REMOVE BY VALUE

pop(i)
→ REMOVE BY INDEX

ord()
→ CHAR → NUMBER

chr()
→ NUMBER → CHAR
```

---

# 🏁 FINAL REVISION FORMULA

```text
Python Function
      ↓
Syntax
      ↓
Example
      ↓
Output
      ↓
Variation
      ↓
DSA Use
      ↓
Time Complexity
      ↓
Interview Trap
```

> ## 🎯 Goal
>
> You should be able to look at any function in this sheet and immediately know:
>
> **"What does it do, how do I write it, what does it return, when do I use it in DSA, and what mistake should I avoid?"**