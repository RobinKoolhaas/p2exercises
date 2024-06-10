from datetime import date, timedelta

import pytest

from calendars import CalendarStub
from tasks import Task, TaskList


def setup_function():
    global today, tomorrow, yesterday, calendar, task_list
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    task_list = TaskList(calendar)


def test_creation():
    #assert
    assert 0 == len(task_list)
    assert [] == task_list.due_tasks
    assert [] == task_list.overdue_tasks
    assert [] == task_list.finished_tasks


def test_adding_task_with_due_day_in_future():
    #arrange
    task = Task("valid description", tomorrow)

    #act
    task_list.add_task(task)

    #assert
    assert 1 == len(task_list)
    assert [task] == task_list.due_tasks


def test_adding_task_with_due_day_in_past():
    #arrange
    task = Task("valid description", yesterday)

    #act/assert
    with pytest.raises(RuntimeError):
        task_list.add_task(task)
    assert 0 == len(task_list)


def test_task_becomes_finished():
    #arrange
    task = Task("valid description", today)
    task_list.add_task(task)

    #act
    task.finished = True

    #assert
    assert [] == task_list.due_tasks
    assert [task] == task_list.finished_tasks
