import unittest
from hospital_1 import Queue, Patient


class TestHospitalQueueSystem(unittest.TestCase):

    def test_enqueue_dequeue(self):
        q = Queue()

        patient1 = Patient("Alice", "10:00 AM")
        patient2 = Patient("Bob", "10:30 AM")
        
        q.enqueue(patient1)
        q.enqueue(patient2)

        self.assertEqual(len(q.queue), 2)
        self.assertEqual(q.dequeue().name, "Alice")
        self.assertEqual(len(q.queue), 1)
        self.assertEqual(q.dequeue().name, "Bob")
        self.assertEqual(len(q.queue), 0)

    def test_peek(self):
        q = Queue()
        
        patient1 = Patient("Alice", "10:00 AM")
        q.enqueue(patient1)
        
        self.assertEqual(q.peek().name, "Alice")
        q.dequeue()
        with self.assertRaises(IndexError):
            q.peek()

    def test_dequeue_empty_queue(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()


if __name__ == "__main__":
    unittest.main()