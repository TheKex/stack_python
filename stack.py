class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def check_brackets(brackets_string):
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = Stack()
    for bracket in brackets_string:
        if stack.size() == 0:
            stack.push(bracket)
            continue
        if bracket in brackets and stack.peek() == brackets[bracket]:
            stack.pop()
        else:
            stack.push(bracket)

    return stack.size() == 0


if __name__ == '__main__':
    brackets = input('Введите строку со скобками:')
    is_correct_input = True
    for i in brackets:
        if i not in '{}[]()':
            is_correct_input = False
            break

    if not is_correct_input:
        print('Ошибка ввода')
        exit()

    print("Сбалансированно" if check_brackets(brackets) else "Несбалансированно")