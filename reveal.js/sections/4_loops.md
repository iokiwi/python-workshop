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
```

---

A more pythonic way:

If we want both the index AND the value of each item, we can use ``enumerate()``

```python
fruits = ["apple", "banana", "pear"]

for i, v in enumerate(fruits):
    print(i, v)
```

---

## List comprehension

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perfect_squares = [x**2 for x in numbers]
```

```python
even_numbers = [n if n % 2 == 0 for n in numbers]
```

---

Iterating over a dictionary

```python
peoples_ages = { "alice": 23, "bob": 22, "eve": 31 }

for k, v in peoples_ages.items():
    print(k, v)
```

Dictionary order guaranteed since Python 3.7

---

## Dictionary comprehension

```python
words = ['apple', 'banana', 'cherry', 'date']
word_lengths = {word: len(word) for word in words}
```

```
people = {'Alice': 22, 'Bob': 20, 'Charlie': 25, 'Dave': 18}
can_go_to_casino = {name: age for name, age in people.items() if age > 21}
```
