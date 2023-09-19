import pytest
from lib.reminder import *


"""
Given a name and a task
#remind reminds the user to do the task
"""
def test_remind_to_walk_dog():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind() # => "Walk the dog, Kay!"
    assert result == "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
def test_remind_error():
    reminder = Reminder("Kay")
    reminder.remind_me_to("")
    # raises an error with the message "No task set."
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
def test_return_other_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Buy milk")
    result = reminder.remind() # => ", Kay!"
    assert result == "Buy milk, Kay!"