from random import randint

class Stack:

    def __init__(self):
        self.stack = []
        self.colors_dict = {}

    def append(self, element):
        self.stack.append(element)
        if not element in self.colors_dict.keys():
            self.colors_dict[element] = (randint(0, 255), randint(0, 255), randint(0, 255))

    def pop(self):
        if len(self.stack) > 0:
            last_element = self.stack.pop(-1)
            print("Taken from stack: " + str(last_element))
            return last_element
        else:
            print("Stack is empty")

    def show_content(self):
        print(self.stack)

    def empty(self):
        self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0

    def get_color(self, num):
        return self.colors_dict[num]

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