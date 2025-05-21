class Task:
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority

    def __repr__(self):
        return f"Task({self.task_name}, {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)
        self.queue.sort(key=lambda x: x.priority, reverse=True)

    def process_task(self):
        if len(self.queue) == 0:
            raise Exception("No tasks to process")
        return self.queue.pop(0)



if __name__ == "__main__":
    scheduler = PriorityQueue()

    scheduler.add_task(Task("Task 1", 1))
    scheduler.add_task(Task("Task 2", 3))
    scheduler.add_task(Task("Task 3", 2))

    print("Processing tasks:")
    while scheduler.queue:
        print(scheduler.process_task())