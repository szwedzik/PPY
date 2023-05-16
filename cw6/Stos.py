class Stos:
    def __init__(self, max_size):
        self.stack = list()
        self.max_size = max_size

    def push(self, e):
        if len(self.stack) < self.max_size:
            self.stack.append(e)
        else:
            raise Exception("Stack overflow")

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise Exception("Stack overflow")

    def __str__(self):
        return str(f"{self.stack}, len:{len(self.stack)}")