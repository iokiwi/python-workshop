## Python Environments

---

...as the joke goes

![](../assets/xkcd_1987.png)

https://xkcd.com/1987/
---

Linux
```bash
$ which python3
/usr/bin/python3
```

macOS
```bash
$ which python3
System/Library/Frameworks/Python.framework
```

Powershell

```powershell
PS C:\> (Get-Command python).Source
C:\Users\smerrick\AppData\Local\Programs\Python\Python312\python.exe
```

---

Global python installation

---

```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/lib/python3.7'
Consider using the `--user` option or check the permissions.
```

---

```
sudo pip install <package-name>
```

---

Don't do that lol

https://opensource.com/article/19/4/managing-python-packages

---

In Linux ``/usr/bin/python3`` is referred to as "system python" and is used by the operating system itself.

---

Do not ever edit or upgrade 'system python' or global Python dependencies.

...

That way lies madness.

---

Asside from not corrupting your OS...

---

What happens if you have more than one python project on the go and they require different versions of the same dependency?
<br><br>
Environment Isolation a.k.a Virtual Environments

---

> There should be one-- and preferably only one --obvious way to do it.

--Zen of Python

---

 * virtualenv
 * pipenv
 * pyenv
 * pyvenv
 * pyenv-virtualenv
 * virtualenvwrapper
 * pyenv-virtualenvwrapper

---

## virtualenv

Part of the standard library since Python 3.3

---

Creating a virtualenv

```bash
# Its customary to call your virtual environment venv or env
python -m venv <env-name>
```

macOS / Linux
```bash
$ python3 -m venv venv
```
Windows
```powershell
PS C:\> python -m venv venv
```

---

Activating a virtual environment

macOS / Linux
```bash
$ source venv/bin/activate
```

Powershell
```powershell
PS C:\> .\venv\Scripts\Activate.ps1
```

---

macOS / Linux
```bash
(venv) $ which python
/home/simon/venv/bin/python
```

Windows
```powershell
(venv) PS C:\> (Get-Command python).Source
C:\Users\smerrick\venv\Scripts\python.exe
```

---

macos / Linux / Windows

```bash
pip install flake8
```

no ``sudo`` required

If you were previously using '``python3``' you can now just use '``python``' to start a shell.

---

Deactivating a virtualenv

macOS / Linux
```bash
(venv) $ deactivate
```
Windows
```powershell
(venv) PS C:\> deactivate
```
---

```bash
$ which python3
/usr/bin/python3
```

```powershell
PS C:\> (Get-Command python).Source
C:\Users\smerrick\AppData\Local\Programs\Python\Python312\python.exe
```
