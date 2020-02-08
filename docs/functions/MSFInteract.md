# MSFInteract Functions

## Class MSFInteract

To create a `MSFInteract` object, you can use :

```python
MSFInteract(debug=False, debugfilename='debug.log')
```

When this object is created, it automatically starts and connects to the Metasploit Console through the `connect()` function.



### External function : `connect()`

Starts and connect connects to the Metasploit Console in background. This is automatically done when creating a `MSFInteract` object. If Metasploit Console was already started, calling the `connect()` function will restart the Metasploit Console.

**Prototype :**

```python
self.connect()
```

**Exemple :**

```python
m = MSFInteract(debug=True)
# If MSF Console was already started, this restarts MSF Console
m.connect()
m.close()
```




### External function : `execute()`

Executes a command in the Metasploit Console.

**Prototype :**

```python
self.execute(command)
```

**Exemple :**

```python
m = MSFInteract(debug=True)
m.execute(command)
m.close()
```




### External function : `search()`

Search for exploits in the Metasploit database, and returns a list of results as dictionaries.

Here is an exemple of result entry :

```python
[
    {
        "id"              : 5,
        "name"            : "exploit/unix/ftp/proftpd_modcopy_exec",
        "disclosure_date" : "2015-04-22",
        "rank"            : "excellent",
        "description"     : "ProFTPD 1.3.5 Mod_Copy Command Execution",
        "check"           : "Yes"
    }
]
```

**Prototype :**

```python
self.search(text)
```

**Exemple :**

```python
m = MSFInteract(debug=True)
# Search for windows exploits
results = m.search("windows")
print(results)
# Closes the connection
m.close()
```



### External function : `close()`

Closes the Metasploit Console in background

**Prototype :**

```python
self.close()
```

**Exemple :**

```python
m = MSFInteract(debug=True)
# Do stuff here
m.close()
```



### Internal function : `_debug(message)`

Prints a debug message and write this message to the debug file. Debug configuration is set when creating `MSFInteract` object and is stored inside a dictionary named `debugging_infos` :

```python
self.debugging_infos = {
    'status'        : debug,
    'debugfilename' : debugfilename,
    'start_time'    : time.time()
}
```

**Prototype :**

```python
self._debug(message)
```




### Internal function : `_wait_for_prompt()`

After sending a command to the Metasploit Console,

**Prototype :**

```python
self._wait_for_prompt()
```




### Internal function : `_sanitize(text)`

Filters the input text before sending to the Metasploit Console.

**Prototype :**

```python
self._sanitize(text)
```
