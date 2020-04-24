
class Stack:

    def __init__(self):
        self.stack = []

    def append(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            last_element = self.stack.pop(-1)
            print("Taken from stack: " + str(last_element))
            return last_element
        except IndexError:
            print("Stack is empty")

    def show_content(self):
        print(self.stack)

    def empty(self):
        self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0

if __name__ == '__main__':
    s = Stack()
    s.append(1)
    s.append(3)
    s.empty()
    s.append(4)
    s.append('5')
    s.append('a')
    s.show_content()
    s.pop()
    s.append(10)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
