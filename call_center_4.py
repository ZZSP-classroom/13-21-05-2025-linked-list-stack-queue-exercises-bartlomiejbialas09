class Call:
    def __init__(self, caller_id, time_received):
        self.caller_id = caller_id
        self.time_received = time_received

    def __repr__(self):
        return f"Call({self.caller_id}, {self.time_received})"


class CallCenter:
    def __init__(self):
        self.incoming_calls = []
        self.processing_calls = []

    def add_call(self, call):
        self.incoming_calls.append(call)

    def process_call(self):
        if not self.incoming_calls:
            raise Exception("No incoming calls to process")
        call = self.incoming_calls.pop(0)
        self.processing_calls.append(call)

    def complete_call(self):
        if not self.processing_calls:
            raise Exception("No calls to complete")
        return self.processing_calls.pop()


if __name__ == "__main__":
    center = CallCenter()

    center.add_call(Call("123", "10:00 AM"))
    center.add_call(Call("456", "10:05 AM"))

    center.process_call()
    center.process_call()

    print("Completed calls:", center.processing_calls)