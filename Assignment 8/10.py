class MyClass:
    def __init__(self, name):
        self.name = name
    def get_class_name(self):
        return self.__class__.__name__
my_instance = MyClass("MyInstance")
print(my_instance.get_class_name())  