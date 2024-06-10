class Task:
    def __init__(self, description: str, due_date):
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
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value) -> None:
        self.__due_date = value


class TaskList:
    def __init__(self, calendar):
        self.__calendar = calendar
        self.__tasks = []

    def add_task(self, task: Task) -> None:
        if task.due_date < self.__calendar.today:
            raise RuntimeError('Task due_date cannot be in the future')
        self.__tasks.append(task)

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
        return [task for task in self.__tasks if not task.finished and task.due_date < self.__calendar.today]
