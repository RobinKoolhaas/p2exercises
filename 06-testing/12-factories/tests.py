from datetime import date, timedelta

import pytest

from calendars import CalendarStub
from tasks import Task, TaskList


def today():
    return date(2000, 1, 1)


def tomorrow():
    return today() + timedelta(days=1)


def yesterday():
    return today() - timedelta(days=1)


def create_calendar():
    return CalendarStub(today())


def create_task(*, description='default description', due_date=None, finished=False):
    due_date = due_date or date(2000, 1, 1)
    task = Task(description, due_date)

    if finished:
        task.finished = True

    return task


def create_empty_task_list(calendar=None):
    calendar = calendar or create_calendar()
    return TaskList(calendar)


def test_creation():
    sut = create_empty_task_list()

    #assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future():
    #arrange
    sut = create_empty_task_list()
    task = create_task(due_date=tomorrow())

    #act
    sut.add_task(task)

    #assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past():
    #arrange
    sut = create_empty_task_list()
    task = create_task(due_date=yesterday())

    #act/assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)


def test_task_becomes_finished():
    #arrange
    sut = create_empty_task_list()
    task = create_task(due_date=today(), finished=True)
    sut.add_task(task)

    #assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
