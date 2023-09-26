class StringReversal:
    def __init__(self):
        self.string = ""
    def get_string(self):
        self.string = input("Enter a string: ")
    def print_string(self):
        print("The reversed string is:", self.string[::-1])