# Complete Concept Guide - Website Blocker Project

## 1. Python Programming Fundamentals

### Classes and Object-Oriented Programming (OOP)
```python
class WebsiteBlocker:
    def __init__(self, root):
        self.root = root
        self.blocked_sites = []
```
**Concepts:**
- **Class**: Blueprint for creating objects (`WebsiteBlocker`)
- **`__init__`**: Constructor method - runs when object is created
- **`self`**: Reference to the instance itself
- **Instance variables**: `self.root`, `self.blocked_sites` - unique to each object
- **Methods**: Functions inside a class that operate on the object

### File I/O (Input/Output)
```python
# Reading
with open(self.config_file, 'r') as f:
    data = json.load(f)

# Writing
with open(self.config_file, 'w') as f:
    json.dump(data, f, indent=4)
```
**Concepts:**
- **`open()`**: Opens a file
- **`'r'` mode**: Read mode
- **`'w'` mode**: Write mode (overwrites file)
- **`with` statement**: Context manager - automatically closes file
- **`as f`**: Assigns file object to variable `f`

### Exception Handling
```python
try:
    # Code that might fail
    with open(self.hosts_path, "r") as f:
        content = f.read()
except PermissionError:
    print("Need admin privileges")
except Exception:
    # Catch any other error
    return False
```
**Concepts:**
- **`try-except`**: Handle errors gracefully without crashing
- **Specific exceptions**: `PermissionError`, `FileNotFoundError`
- **Generic exception**: `Exception` catches all errors
- **Error recovery**: Program continues even if error occurs

### String Operations
```python
url = "https://www.facebook.com/page"
url = url.lower()                    # Convert to lowercase
url = url.replace("https://", "")    # Remove https://
url = url.replace("www.", "")        # Remove www.
url = url.split('/')[0]              # Get domain only
```
**Concepts:**
- **`lower()`**: Converts to lowercase
- **`replace()`**: Substitutes text
- **`split()`**: Breaks string into list
- **String slicing**: `[0]` gets first element
- **f-strings**: `f"127.0.0.1 {domain}"` - formatted strings

### List Operations
```python
blocked_sites = []
blocked_sites.append("facebook.com")    # Add item
blocked_sites.remove("facebook.com")    # Remove item
if "facebook.com" in blocked_sites:     # Check if exists
    pass
```
**Concepts:**
- **Lists**: Ordered, mutable collections
- **`append()`**: Add to end
- **`remove()`**: Remove specific item
- **`in` operator**: Check membership
- **List comprehension**: `[x for x in list if condition]`

### Modules and Imports
```python
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import json
import platform
```
**Concepts:**
- **`import`**: Load external code
- **`as`**: Alias (shorthand)
- **`from ... import`**: Import specific parts
- **Standard library**: Built-in Python modules (json, os, platform)
- **Third-party**: External packages (none used here)

---

## 2. GUI Programming (Tkinter)

### Window Creation
```python
root = tk.Tk()
root.title("Website Blocker")
root.geometry("600x500")
root.resizable(True, True)
```
**Concepts:**
- **`Tk()`**: Main window object
- **`title()`**: Window title bar text
- **`geometry()`**: Window size "width x height"
- **`resizable()`**: Allow/prevent resizing
- **`mainloop()`**: Event loop - keeps window open

### Layout Management
```python
# Pack - stacks widgets
frame.pack(fill=tk.X, pady=10)

# Grid - table layout
label.grid(row=0, column=0, sticky='w')

# Place - absolute positioning (not used here)
```
**Concepts:**
- **Pack**: Automatic stacking (top to bottom)
- **Grid**: Row/column layout
- **`fill`**: Expand to fill space (X=horizontal, Y=vertical, BOTH)
- **`pady`/`padx`**: Padding (spacing)
- **`sticky`**: Alignment (n,s,e,w = north,south,east,west)

### Widgets (UI Components)
```python
# Button
btn = tk.Button(frame, text="Click", command=self.add_website)

# Entry (text input)
entry = tk.Entry(frame, font=("Arial", 12))

# Listbox (scrollable list)
listbox = tk.Listbox(frame, height=10)

# Label (text display)
label = tk.Label(frame, text="Hello")

# Frame (container)
frame = tk.Frame(root, bg="#2c3e50")
```
**Concepts:**
- **Parent**: First argument (where widget goes)
- **`text`**: Display text
- **`command`**: Function to run on click
- **`font`**: Typography settings
- **`bg`/`fg`**: Background/foreground colors
- **Hex colors**: `#2c3e50` (RGB in hexadecimal)

### Event Handling
```python
# Button click
btn = tk.Button(text="Add", command=self.add_website)

# Keyboard
entry.bind("<Return>", lambda e: self.add_website())

# Listbox selection
listbox.bind("<Double-Button-1>", self.toggle_website)
```
**Concepts:**
- **Events**: User actions (click, keypress, etc.)
- **`command`**: Button callback
- **`bind()`**: Attach function to event
- **Event names**: `<Return>`, `<Double-Button-1>`
- **Lambda**: Anonymous function `lambda args: expression`

### Scheduled Tasks
```python
# Run after delay
self.root.after(1800000, self.unblock_websites)  # 30 min
```
**Concepts:**
- **`after(milliseconds, function)`**: Schedule future execution
- **1000 ms = 1 second**
- **Non-blocking**: UI remains responsive
- **Timer storage**: `self.timer_id` to track/cancel

---

## 3. Networking Concepts

### IP Addresses
```python
redirect_ip = "127.0.0.1"  # Localhost
```
**Concepts:**
- **127.0.0.1**: Loopback address (your own computer)
- **IPv4**: 4 numbers (0-255) separated by dots
- **Localhost**: Computer talking to itself
- **Port**: Number identifying specific service (80 = HTTP)

### HTTP Protocol
```python
class BlockPageHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))
```
**Concepts:**
- **HTTP**: Hypertext Transfer Protocol (web communication)
- **GET request**: Request to retrieve data
- **POST request**: Send data to server
- **Response code**: 200 = OK, 404 = Not Found
- **Headers**: Metadata about response
- **Content-type**: Format of data being sent

### DNS (Domain Name System)
```python
# Hosts file entry
"127.0.0.1 facebook.com"
```
**Concepts:**
- **DNS**: Converts domain names to IP addresses
- **Hosts file**: Local DNS override
- **DNS cache**: Stored DNS lookups (needs flushing)
- **Domain resolution**: facebook.com → IP address
- **Redirect**: Point domain to different IP

### Socket Programming
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 80))
```
**Concepts:**
- **Socket**: Endpoint for network communication
- **AF_INET**: IPv4 address family
- **SOCK_STREAM**: TCP protocol (reliable)
- **bind()**: Attach to IP:port
- **Port 80**: Standard HTTP port

### HTTP Server
```python
server = http.server.HTTPServer(('127.0.0.1', 80), BlockPageHandler)
server.serve_forever()
```
**Concepts:**
- **HTTPServer**: Built-in Python web server
- **Handler**: Processes incoming requests
- **serve_forever()**: Run continuously
- **Threading**: Run server in background

---

## 4. Operating System Concepts

### File System
```python
# Windows hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Path operations
from pathlib import Path
config_file = Path(__file__).parent / "config" / "blocked_sites.json"
```
**Concepts:**
- **Absolute path**: Full path from root (C:\...)
- **Relative path**: Path from current location
- **Path separators**: Windows `\`, Unix `/`
- **Raw strings**: `r"C:\path"` - backslash not escape character
- **Path object**: Modern way to handle paths
- **`__file__`**: Current script's path

### Process Management
```python
import subprocess
result = subprocess.run(
    ['ipconfig', '/flushdns'],
    capture_output=True,
    text=True,
    timeout=5
)
```
**Concepts:**
- **Process**: Running program
- **subprocess**: Run external commands
- **`run()`**: Execute command and wait
- **`capture_output`**: Get command output
- **`timeout`**: Maximum wait time
- **Return code**: 0 = success, other = error

### Platform Detection
```python
import platform
if platform.system() == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    hosts_path = "/etc/hosts"
```
**Concepts:**
- **Cross-platform**: Works on Windows/Linux/Mac
- **platform.system()**: Returns OS name
- **Conditional logic**: Different behavior per OS
- **System differences**: File paths, commands vary

### Permissions
```python
import ctypes
is_admin = ctypes.windll.shell32.IsUserAnAdmin()
```
**Concepts:**
- **Admin/Root**: Elevated privileges
- **UAC**: User Account Control (Windows)
- **Hosts file**: Requires admin to modify
- **Port 80**: Requires admin on Windows
- **ctypes**: Call Windows DLL functions

---

## 5. Data Formats

### JSON (JavaScript Object Notation)
```python
# Python to JSON
data = {"blocked_sites": ["facebook.com", "twitter.com"]}
json.dump(data, f, indent=4)

# JSON to Python
data = json.load(f)
sites = data.get('blocked_sites', [])
```
**Concepts:**
- **JSON**: Human-readable data format
- **Dictionary**: Python object `{key: value}`
- **List**: Array `[item1, item2]`
- **Serialization**: Convert Python → JSON
- **Deserialization**: Convert JSON → Python
- **`indent=4`**: Pretty printing (readable)

### HTML (HyperText Markup Language)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Site Blocked</title>
    <style>
        body { background: #667eea; }
    </style>
</head>
<body>
    <h1>This site is blocked</h1>
</body>
</html>
```
**Concepts:**
- **Tags**: `<tag>content</tag>`
- **Attributes**: `<tag attribute="value">`
- **Head**: Metadata, CSS, title
- **Body**: Visible content
- **CSS**: Styling (colors, fonts, layout)
- **UTF-8**: Character encoding

---

## 6. Testing Concepts

### Unit Testing
```python
import unittest

class TestWebsiteBlocker(unittest.TestCase):
    def test_sanitize_url(self):
        result = blocker.sanitize_url("https://www.facebook.com")
        self.assertEqual(result, "facebook.com")
```
**Concepts:**
- **Unit test**: Test individual function
- **TestCase**: Base class for tests
- **`test_*`**: Method names must start with "test"
- **Assertions**: `assertEqual`, `assertTrue`, `assertIn`
- **Test isolation**: Each test independent

### Mocking
```python
from unittest.mock import Mock, patch

@patch('tkinter.Tk')
def test_init(self, mock_tk):
    blocker = WebsiteBlocker(Mock())
```
**Concepts:**
- **Mock**: Fake object for testing
- **`@patch`**: Replace real code with mock
- **Decorator**: `@` syntax - wraps function
- **Dependency injection**: Pass mocks instead of real objects
- **Avoid side effects**: Don't actually modify system

### Test Categories
```python
# Unit: Individual functions
# Integration: Multiple components together
# E2E: Full user workflow
# System: Real system validation
```
**Concepts:**
- **Unit**: Smallest testable parts
- **Integration**: Components working together
- **End-to-end**: Complete user scenarios
- **System**: Real environment testing
- **Test pyramid**: More unit, fewer integration/E2E

### Coverage
```python
coverage run -m pytest tests/
coverage report
```
**Concepts:**
- **Code coverage**: % of code executed by tests
- **Line coverage**: Which lines run
- **Branch coverage**: Which if/else paths taken
- **40% coverage**: 40% of code tested
- **Coverage report**: Shows untested lines

---

## 7. Code Quality Tools

### Pylint (Code Quality)
```python
# Checks for:
# - Code smells
# - Bad practices
# - Style violations
# Score: 9.15/10
```
**Concepts:**
- **Linting**: Automated code analysis
- **Code smell**: Suspicious patterns
- **Best practices**: Recommended patterns
- **Scoring**: 0-10 quality rating
- **Configuration**: `.pylintrc` file

### Flake8 (Style Guide)
```python
# PEP 8 compliance
# - Line length (max 100)
# - Spacing
# - Import order
# - Naming conventions
```
**Concepts:**
- **PEP 8**: Python style guide
- **Conventions**: Agreed-upon standards
- **Readability**: Consistent formatting
- **E/W codes**: Error/Warning identifiers
- **Ignore list**: Skip certain checks

### Bandit (Security)
```python
# Scans for:
# - SQL injection
# - Shell injection
# - Hardcoded passwords
# - Insecure functions
```
**Concepts:**
- **Security scanning**: Find vulnerabilities
- **Static analysis**: Check code without running
- **B-codes**: Security issue identifiers
- **Confidence levels**: LOW/MEDIUM/HIGH
- **False positives**: Safe code flagged as risky

### MyPy (Type Checking)
```python
def sanitize_url(self, url: str) -> str:
    return url.lower()
```
**Concepts:**
- **Type hints**: `variable: type`
- **Return type**: `-> type`
- **Type safety**: Catch type errors before runtime
- **Static typing**: Check types without running
- **`# type: ignore`**: Skip type check

### Black (Formatter)
```python
# Auto-formats code
# - Consistent style
# - 88 char line limit
# - Double quotes
# - No configuration needed
```
**Concepts:**
- **Auto-formatting**: Automatic code styling
- **Opinionated**: Limited customization
- **Consistent**: Same style everywhere
- **PEP 8 compliant**: Follows Python style
- **Git-friendly**: Minimal diffs

---

## 8. Design Patterns

### MVC Pattern (Model-View-Controller)
```python
# Model: Data (blocked_sites list)
# View: GUI (tkinter widgets)
# Controller: Logic (add_website, block_website methods)
```
**Concepts:**
- **Separation of concerns**: Each part has one job
- **Model**: Data and business logic
- **View**: User interface
- **Controller**: Connects model and view
- **Maintainability**: Easy to change one part

### Singleton Pattern
```python
# Only one ProxyServer instance
class ProxyServer:
    _instance = None
```
**Concepts:**
- **Single instance**: Only one object exists
- **Global access**: Available everywhere
- **Resource management**: One server, not many
- **State sharing**: Common data across app

### Observer Pattern (Events)
```python
# Button click → callback function
btn = tk.Button(command=self.add_website)
```
**Concepts:**
- **Event-driven**: React to user actions
- **Callbacks**: Functions called when event occurs
- **Loose coupling**: Components don't need to know each other
- **Asynchronous**: Events happen anytime

---

## 9. Threading and Concurrency

### Background Threads
```python
import threading
server_thread = threading.Thread(target=self.server.serve_forever)
server_thread.daemon = True
server_thread.start()
```
**Concepts:**
- **Thread**: Separate execution path
- **Daemon thread**: Dies when main program exits
- **`target`**: Function to run in thread
- **Non-blocking**: UI stays responsive
- **Concurrency**: Multiple things at once

---

## 10. Version Control (Git)

### .gitignore
```
__pycache__/
*.pyc
.coverage
htmlcov/
```
**Concepts:**
- **Ignore files**: Don't track generated files
- **Patterns**: `*` matches anything
- **Cache files**: Build artifacts, temporary files
- **Clean repo**: Only source code tracked

### CI/CD (GitHub Actions)
```yaml
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: python -m pytest
```
**Concepts:**
- **Continuous Integration**: Auto-test on commit
- **Pipeline**: Automated workflow
- **Triggers**: Run on push/PR
- **Jobs**: Units of work
- **Steps**: Individual commands

---

## 11. Configuration Management

### Configuration Files
```python
# .pylintrc, .flake8, .bandit, mypy.ini
# INI format: [section] key=value
# YAML format: key: value
```
**Concepts:**
- **Configuration**: Settings separate from code
- **Externalized**: Easy to change without editing code
- **Tool-specific**: Each tool has own config
- **Format variations**: INI, YAML, JSON

---

## 12. Software Architecture Principles

### DRY (Don't Repeat Yourself)
```python
# Bad: Repeat code
# Good: Create function, call multiple times
def get_domain_variations(domain):
    return [domain, f"www.{domain}", f"m.{domain}"]
```

### SOLID Principles
- **S**ingle Responsibility: Each class/function does one thing
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subclasses work like parent
- **I**nterface Segregation: Small, specific interfaces
- **D**ependency Inversion: Depend on abstractions

### Error Handling
```python
# Fail gracefully
try:
    risky_operation()
except Exception:
    # Log error, use default, notify user
    return default_value
```

---

## 13. Best Practices Applied

1. **Type hints**: Document expected types
2. **Docstrings**: Explain what functions do
3. **Meaningful names**: `sanitize_url` not `process`
4. **Small functions**: Do one thing well
5. **Constants**: `REDIRECT_IP = "127.0.0.1"`
6. **Error handling**: Try-except blocks
7. **Testing**: Comprehensive test suite
8. **Documentation**: README, code comments
9. **Version control**: Git for history
10. **Code review**: Quality checks before merge

---

## Key Takeaways

- **Python**: OOP, file I/O, exceptions, strings, lists
- **GUI**: Tkinter widgets, layouts, events
- **Networking**: HTTP, DNS, sockets, servers
- **OS**: Files, processes, permissions, cross-platform
- **Data**: JSON, HTML
- **Testing**: Unit, integration, mocking, coverage
- **Quality**: Linting, security, types, formatting
- **Patterns**: MVC, events, threading
- **Best practices**: DRY, SOLID, error handling

This project demonstrates **professional software engineering** with proper structure, testing, documentation, and quality assurance! 🚀
