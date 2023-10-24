# Conditionals and Flow Control

---

## ``if``

```python
if <expression>:
    <statement>
```


https://realpython.com/python-conditional-statements/

---

## ``if`` ...  ``else``

```python
if <expression>:
    <statement>
else:
    <statement>
```


https://realpython.com/python-conditional-statements/

---

## ``elif``

else + if

```python
if <expression>:
    <statement>
elif <expression>:
    <statement>
```

---

## ``elif``

```python
if <expression>:
    <statement>
elif <expression>:
    <statement>
elif <expression>:
    <statement>
else:
    <statement>
```

---

## ``elif``

```python
def process_event(event):
    if event == "start":
        print("Starting the process...")
    elif event == "run":
        print("Running the process...")
    elif event == "stop":
        print("Stopping the process...")
    else:
        print(f"Unknown event: {event}")
```

https://realpython.com/python-conditional-statements/

---

---

"Truthyness" and "Falseyness" in Python

---

"Falsey" Values

|||
|---|---|
|False|``False``|
|Numbers with a value of 0| e.g ``0``, ``0x0``, ``0O0``, ``0b0`` ``0.0`` |
|Empty Strings|``""``|
|Empty Collections|``[]``, ``{}``, ```()```|
|None||

---

"Truthy" Values

|||
|---|---|
|True|``True``|
|Numbers with a non-zero value| e.g ``-1`` ``1`` ``0.1`` |
|Non-Empty Strings|``"a"``|
|Non-Empty Collections|``[1]``, ``{"a":1}``, ``(2)``|


---

Naive

```python
if x == True:
    # do foo
```

Better

```python
if x is True:
    # do foo
```

Recommended
```python
if x:
    # do foo
```

---

```python
# Will print "<x> is truthy" for: -1, "a", [1], etc
if x:
    print(f"{x} is truthy")


# Will print "<y> is falsey" for: None, 0, [], "", etc
if not y:
    print("{y} is falsey")
```

---

<img src="../assets/false_at_midnight.PNG" height=500px>
<a>https://mail.python.org/pipermail/python-ideas/2014-March/026446.html</a>

---

# Loops

---

### The ``for`` loop

Iterate over elements in a list

---
```python
fruits = ["apple", "banana", "pear"]

for fruit in fruits:
    print(fruits)
```

---

Iterating over the indexes of a list

```python
fruits = ["apple", "banana", "pear"]

for i in range(len(fruits)):
    print(i, fruits[i])

# 0 apple
# 1 banana
# 2 pear
```

---

A more pythonic way:

If we want both the index AND the value of each item, we can use ``enumerate()``

```python
fruits = ["apple", "banana", "pear"]

for i, v in enumerate(fruits):
    print(i, v)

# 0 apple
# 1 banana
# 2 pear
```

---

Iterating over a dictionary

```python
peoples_ages = { "alice": 23, "bob": 22, "eve": 31 }

for k, v in peoples_ages.items():
    print(k, v)

# alice 23
# bob 22
# eve 31
```

Dictionary order guaranteed since 3.7



## Basics
---
PEP 8 – Style Guide for Python Code

https://peps.python.org/pep-0008/

---
## Spaces vs Tabs

Use 4 spaces per indentation level.


Built In Functions

https://docs.python.org/3/library/functions.html



## ``match``
(Python >= 3.10)


```python
match <expression>:
    case <pattern1>:
        <statement1>
    case <pattern2>:
        <statement2>
    case <patternN>:
        <statementN>
```

---

```python
def process_event(event):
    match event:
        case "start":
            print("Starting the process...")
        case "run":
            print("Running the process...")
        case "stop":
            print("Stopping the process...")
        case _:
            print(f"Unknown event: {event}")
```