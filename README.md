# AirBnB clone - The console
The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

<p align="center"><img src= "https://media.itsnicethat.com/original_images/563b97a87fa44cff9d001760.gif" width="600" height="400"/></p>

### Concepts

- [Python Packages](https://intranet.alxswe.com/concepts/66)
- [Airbnb Clone](#)

### Resources
Read or watch:

- [cmd module]()
- cmd module in depth
- packages concept page
- uuid module
- datetime
- unittest module
- args/kwargs
- Python test cheatsheet
- cmd module wiki page
- python unittest

## More Info

**Execution**

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

### Tasks

#### 0. README, AUTHORS

Write a `README.md`:
- description of the project
- description of the command interpreter:
    - how to start it
    - how to use it
    - examples
- You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s](https://intranet.alxswe.com/rltoken/_8n_z3pf5HWi1l7uv1E9iA) AUTHORS page
- You should use branches and pull requests on GitHub - it will help you as team to organize your work

**Repo:**

- GitHub repository: `AirBnB_clone`
- File: `README.md, AUTHORS`
