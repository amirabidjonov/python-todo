import json


def read_file() -> list[dict]:
    f = open("db.json")
    content = f.read()
    tasks = json.loads(content)
    return tasks


def write_file(tasks: list[dict]):
    f = open("db.json", "w")
    content = json.dumps(tasks, indent=4)
    f.write(content)


def add_task(title: str, description: str):
    task = {"title": title, "description": description, "status": False}
    tasks = read_file()
    tasks.append(task)
    write_file(tasks)


def mark_task_as_completed():
    pass


def mark_task_as_incompleted():
    pass


def delete_task():
    pass


def get_all_tasks():
    pass
