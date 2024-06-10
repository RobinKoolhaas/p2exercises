from datetime import date


class Task:
    def __init__(self, description: str, due_date: date):
        self.description = description
        self.due_date = due_date
        self.finished = False

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value

    @property
    def due_date(self) -> date:
        return self.__due_date

    @due_date.setter
    def due_date(self, value: date) -> None:
        self.__due_date = value


class TaskList:
    def __init__(self):
        self.__tasks = []
        
    def add_task(self, task: Task) -> None:
        if task.due_date > date.today():
            raise RuntimeError('Task due_date cannot be in the future')

    def __len__(self):
        return len(self.__tasks)

    @property
    def finished_tasks(self) -> list:
        return [task for task in self.__tasks if task.finished]

    @property
    def due_tasks(self) -> list:
        return [task for task in self.__tasks if not task.finished]

    @property
    def overdue_tasks(self) -> list:
        return [task for task in self.__tasks if not task.finished and task.due_date < date.today()]
