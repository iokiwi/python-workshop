## Orienting Ourselves in python

python cares about whitespaces

```python
if true:
    
```



---

Python is Strongly typed

This means that Python cares about the types of variables and will not implicitly convert them for us.

---

Basic Python Types

|||
|---|---|
|``str``|``"This is a string literal"``|
|``bool``|``True`` or ``False``|
|``int``|``1``, ``0xF9``, ``0O20``, ``0b0110``|
|``float``|``3.14159265358``|
|``complex``|``3 + 2j``|


https://docs.python.org/3/library/stdtypes.html

---

```python
1 + 2        # 3
1 + "2"      # TypeError: unsupported operand type(s) for +: 'int' and 'str'
1 + int("2") # 3
str(1) + "2" # "12"
```

---

Python is dynamically typed

This means that the type of a variable is not fixed / known at compile time and can change throughout the lifecycle of the programm

---

```python
foo = "this is a string"
type(foo) # <class 'str'>
foo = 9000
type(foo) # <class 'int'>
```

---

In python everything is an object, even functions and primitive types

```python
foo = "a"
type(foo)
# <class 'str'>
```

```python
bar = 6
type(bar)
# <class 'int'>
```

This means that all things in python have a set of both *attributes* and *behaviours* assoicated with them

---

We can inspects the attributes and methods associated with any python object in a couple of ways

```python
dir()
help()
```

https://docs.python.org/3/library/functions.html

---

```python
foo = "this is my string"
dir(foo)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

---

"Dunder methods" or "Magic methods"

```
__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__'
```

We will come back to these and even write our own

---

```python
help(str)
```

```
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
```

---

Builtin functions

<img src="../assets/builtin_functions.PNG" height="500px">

---

Builtin functions

Already seen:

```python
exit(), print(), type(), dir(), help(), str(), int(), 
```

We'll visit more of these as we go

```python
len(), range(), enumerate(), dict(), list(), # + More
```

https://docs.python.org/3/library/functions.html

---

Built In Collection Types

```python
list
tuple
dict
set
```

We'll also visit these in greater detail shortly