from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList


def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('some description', tomorrow)
    tasks = TaskList(calendar)

    tasks.add_task(task)
    calendar.today = next_week

    assert [task] == tasks.overdue_tasks
