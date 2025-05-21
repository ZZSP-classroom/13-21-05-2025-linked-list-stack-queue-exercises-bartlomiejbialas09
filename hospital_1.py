class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Patient({self.name}, {self.appointment_time})"


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def __repr__(self):
        return f"Queue({self.queue})"
    
if __name__ == "__main__":
    q = Queue()

   
    patient1 = Patient("Alice", "10:00 AM")
    patient2 = Patient("Bob", "10:30 AM")
    patient3 = Patient("Charlie", "11:00 AM")

    q.enqueue(patient1)
    q.enqueue(patient2)
    q.enqueue(patient3)

    print("Queue before any dequeue:", q)

    print("Dequeuing patient:", q.dequeue())
    print("Queue after dequeue:", q)

    print("Next patient:", q.peek())