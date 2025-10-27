"""""
Task:
Implement the following class hierarchy using Python: 
A publication can be either a book or a magazine. 
Each publication has a name. 
Each book also has an author and a page count, whereas each magazine has a chief editor. 
Also write the required initializers to both classes. 
Create a print_information method to both subclasses for printing out all information of the publication in question.

Requirements:

Create a Publication base class with a name property and initializer
Create a Book subclass with author and page_count properties
Create a Magazine subclass with a chief_editor property
Both subclasses must have a print_information method
"""""

class Publication():
    def __init__(self, name):
        self.name = name
    def print_information(self):
        print(f"Publication: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        #super() gives you access to methods from the parent (superclass) of the current class (Book).
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name} by {self.author}, Page_count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name} by {self.chief_editor}")

