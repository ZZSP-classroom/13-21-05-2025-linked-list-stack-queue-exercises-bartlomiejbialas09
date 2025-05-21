import unittest
from call_center_4 import Call, CallCenter


class TestCallCenter(unittest.TestCase):

    def test_process_call(self):
        center = CallCenter()

        center.add_call(Call("123", "10:00 AM"))
        center.add_call(Call("456", "10:05 AM"))

        center.process_call()
        self.assertEqual(len(center.incoming_calls), 1)

        completed_call = center.complete_call()
        self.assertEqual(completed_call.caller_id, "123")


if __name__ == "__main__":
    unittest.main()