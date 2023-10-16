# AirBnB clone - The console


![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T161947Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=72ed89d855877b39da18fcaee0294dc82eb1bdfbe9cb06b4c5ffc99d1ee55ec5)

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

#### 1. Be pycodestyle compliant!
 Write beautiful code that passes the pycodestyle checks.

 **Repo**
 
 - GitHub repository: `AirBnB_clone`

 ####  2. Unittests
 Write beautiful code that passes the pycodestyle checks.

 ```
 guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
 ```
*Note that this is just an example, the number of tests you create can be different from the above example.*

**Warning**

Unit tests must also pass in non-interactive mode:

```
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
**Repo**

- GitHub repository: `AirBnB_clone`
- File: `tests/`

###