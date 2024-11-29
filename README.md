# Task Tracker

## Introduction

Task tracker is a CLI tool that helps you to keep track of your tasks. You can add, remove, list and mark tasks as done. The tasks are stored in a JSON file in the user's home directory. [project source](https://roadmap.sh/projects/task-tracker)

Made in a couple of minutes using Python, with the help of `os`, `sys` and `datetime` modules.

## Usage

Move to the project directory and run any command listed down below.

> Example:
>
>    ```bash
>    $ python3 todo.py add "Buy milk"
>    ```

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