import sys
import json
import datetime


try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []

match sys.argv[1]:
    case "add":  # add
        if len(sys.argv) == 3:
            task = {
                "id": len(tasks) + 1,
                "description": sys.argv[2],
                "status": "todo",
                "createdAt": str(datetime.date.today()),
                "updatedAt": "",
            }
            tasks.append(task)
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
                print("Task added successfully")

    case "list":
        with open("tasks.json", "r") as file:
            if len(sys.argv) == 2:  # list all
                for task in file:
                    print(task)
            elif len(sys.argv) == 3:  # list by status
                for task in list(
                    filter(lambda task: task["status"] == sys.argv[2], tasks)
                ):
                    print(task)

    case "update":
        with open("tasks.json", "r") as file:
            if len(sys.argv) == 4:
                for task in tasks:
                    if task["id"] == int(sys.argv[2]):
                        task["description"] = sys.argv[3]
                        task["updatedAt"] = str(datetime.date.today())
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)

    case "delete":
        for task in tasks:
            if task["id"] == int(sys.argv[2]):
                tasks.remove(task)
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)

    case status if status.startswith("mark-"):
        for task in tasks:
            if task["id"] == int(sys.argv[2]):
                task["status"] = status[5:]
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)

file.close()
