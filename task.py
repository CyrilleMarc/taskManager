import datetime
import json
import os

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
        choice = input("Type your choice: 1 to 5: ")
        if choice == '1':
            self.display_list()

    def display_list(self):
        print(self.tasks)
        

if __name__ == "__main__":
    taskManagerObject_1 = TaskManager()
    taskManagerObject_1.main_menu()