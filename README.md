# 0x00. AirBnB clone - The console

A command interpreter to manage your AirBnB objects

## How to start

This is a command interpreter that will be used to:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

Built-in command list to manager the objects:

- `create`

Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`

- `show`

Prints the string representation of an instance based on the class name and `id`

- `destroy`

Deletes an instance based on the class name and `id` (save the change into the JSON file)

- `all`

Prints all string representation of all instances based or not on the class name

- `update`

Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file.
Usage: update `<class name>` `<id>` `<attribute name>` "`<attribute value>`"

## How to use

You can run it from interactive mode `./console.py` and non-interactive mode `echo "help" | ./console.py`

If you want to run `unit tests`, use this command `python3 -m unittest discover tests`, can be ran in non interactive mode too

Have fun !

## Examples

```bash
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

```bash
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
