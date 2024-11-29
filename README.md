# Task Tracker

## Introduction

Task tracker is a CLI tool that helps you to keep track of your tasks. You can add, remove, list and mark tasks as done. The tasks are stored in a file in the user's home directory. [source](https://roadmap.sh/projects/task-tracker)

Made in a couple of minutes using Python, with the help of `os`, `sys` and `datetime` modules.

## Usage

```bash
$ python3 todo.py add "Buy milk"
$ python3 todo.py add "Buy eggs"
$ python3 todo.py list
$ python3 todo.py mark-done 1
$ python3 todo.py list done
$ python3 todo.py delete 1
```
### Commands

- `add`: Add a new task
- `list`: List all tasks
- `list todo`: List all todo tasks
- `list in-progress`: List all in-progress tasks
- `list done`: List all done tasks
- `mark-in-progress {id}`: Mark a task as in-progress
- `mark-done {id}`: Mark a task as done
- `update {id} {new task}`: Update a task description
- `delete {id}`: Delete a task