import datetime
import json
import os
import csv

class TaskManager:

    def __init__(self):
        self.jsonFile = "task.json"
        self.csvFile = "activity.csv"
        self.tasks = self.task_Loader()

    def task_Loader(self):
        if os.path.exists(self.jsonFile):
            with open(self.jsonFile, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:
                    print('no task in the list')
                    return []
                else:
                    return json.loads(content)

    def main_menu(self):
        while True:
            choice = input("Type your choice: 1 to 5: ")
            if choice == '1':
                self.display_list()
            elif choice == '2':
                self.display_add_task()
            else:
                break
    
    def display_list(self):
        content = self.tasks
        for line in content:
            print(line)

    def display_add_task(self):
        description = input("New task description: ")
        dead_line = "tomorrow"

        self.add_task(description, dead_line)

    def save_task(self):
        with open(self.jsonFile, "w", encoding="utf-8" ) as file:
            json.dump(self.tasks, file, indent=2, ensure_ascii=False)

    def add_task(self, description, dead_line=None):
        new_task = {
            "id" : len(self.tasks) + 1,
            "description" : description,    
            "creation_date" : datetime.datetime.now().isoformat(),
            "deadLine" : dead_line
        }
        self.tasks.append(new_task)
        self.save_task()
        

if __name__ == "__main__":
    taskManagerObject_1 = TaskManager()
    taskManagerObject_1.main_menu()