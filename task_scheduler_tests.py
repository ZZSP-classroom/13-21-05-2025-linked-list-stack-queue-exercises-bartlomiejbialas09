import unittest
from task_scheduler_5 import Task, PriorityQueue

class TestTaskScheduler(unittest.TestCase):

    def test_task_priority(self):
        scheduler = PriorityQueue()

        scheduler.add_task(Task("Task 1", 1))
        scheduler.add_task(Task("Task 2", 3))
        scheduler.add_task(Task("Task 3", 2))

        self.assertEqual(scheduler.process_task().task_name, "Task 2")
        self.assertEqual(scheduler.process_task().task_name, "Task 3")
        self.assertEqual(scheduler.process_task().task_name, "Task 1")


if __name__ == "__main__":
    unittest.main()