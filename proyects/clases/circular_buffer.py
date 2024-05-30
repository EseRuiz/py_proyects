class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.result = []

    def read(self):
        if not self.result:
            raise BufferEmptyException("Circular buffer is empty")
        else:
            return self.result.pop(0)


    def write(self, data):
        if len(self.result) < self.capacity:
            self.result.append(data)
        else:
            raise BufferFullException("Circular buffer is full")
        

    def overwrite(self, data):
        if len(self.result) ==  self.capacity:
            self.result.pop(0)
            self.result.append(data)
        else:
            self.result.append(data)


    def clear(self):
        self.result = []

# buf = CircularBuffer(3)
# buf.write("1")
# buf.write("2")
# buf.write("3")
# print(buf.read(), "1")
# buf.write("4")
# buf.overwrite("5")
# print(buf.read(), "3")
# print(buf.read(), "4")
# print(buf.read(), "5")