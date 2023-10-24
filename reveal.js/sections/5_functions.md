## Functions and Arguments

---

Note we can use ``pass`` as the placeholder for any block of code.

```python
# A basic function with no arguments, return value or body
def greet():
    pass
```

---

Arguments

```python
def greet(name):
    print(f"Hello, {name}!")
```

---

Return Values with the ``return`` keyword

```python
def greet(name):
    return f"Hello, {name}!"

greeting = greet("Simon")
print(greeting)
# Hello, Simon!
```


---

Default arguments

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
```

```python
greet("Simon")                        #  Hello, Simon!
greet("Simon", "Guten Tag")           #  Guten Tag, Simon!
greet("Simon", greeting="Guten Tag")  #  Guten Tag, Simon!
```

---

Gotchas!

---

Mutable default arguments

Never do this!

```python
def foo(a, b=[]):
    pass
```

```python
def foo(a, b={})
    pass
```

---

## ``*args`` and ``**kwargs``


https://realpython.com/python-kwargs-and-args/
