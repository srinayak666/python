# As previously defined
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def par_checker_(self,symbol):
        balanced=False
        if len(symbol)%2!=0:
            return False
        for character in symbol:
            print("Character is:--"+character)
            if character in '({[':
                self.push(character)
            else:
                if s.is_empty():
                    balanced=False
                else:
                    top = s.peek()
                    if character in ')}]':
                        s.pop()


        if balanced and s.is_empty():
            balance=True
        else:
            balance=False

        return balanced

# Completed extended par_checker for: [,{,(,),},]



s=Stack()
print(s.par_checker_("{[()]}"))
print(s.par_checker_("{{([][])}()}"))
print(s.par_checker_("[{()]}[]"))