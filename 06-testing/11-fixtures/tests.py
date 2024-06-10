from datetime import date, timedelta

import pytest

from calendars import CalendarStub
from tasks import Task, TaskList


@pytest.fixture
def today():
    return date(2000, 1, 1)


@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)


@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)


@pytest.fixture
def calendar(today):
    return CalendarStub(today)


@pytest.fixture
def task_list(calendar):
    return TaskList(calendar)


def test_creation(task_list):
    #assert
    assert 0 == len(task_list)
    assert [] == task_list.due_tasks
    assert [] == task_list.overdue_tasks
    assert [] == task_list.finished_tasks


def test_adding_task_with_due_day_in_future(task_list, tomorrow):
    #arrange
    task = Task("valid description", tomorrow)

    #act
    task_list.add_task(task)

    #assert
    assert 1 == len(task_list)
    assert [task] == task_list.due_tasks


def test_adding_task_with_due_day_in_past(task_list, yesterday):
    #arrange
    task = Task("valid description", yesterday)

    #act/assert
    with pytest.raises(RuntimeError):
        task_list.add_task(task)
    assert 0 == len(task_list)


def test_task_becomes_finished(task_list, today):
    #arrange
    task = Task("valid description", today)
    task_list.add_task(task)

    #act
    task.finished = True

    #assert
    assert [] == task_list.due_tasks
    assert [task] == task_list.finished_tasks
