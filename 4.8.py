class LibraryItem:
    def __init__(self, title, item_id, no_copies):
        self.title = title
        self.item_id = item_id
        self.no_copies = no_copies
    def display(self):
        print("\nTitle: ",self.title)
        print("Item ID: ",self.item_id)
        print("Num Copies: ",self.no_copies)
    def checkout(self):
        cho=input("Enter the item ID:")
        if (cho=="B12"):
            ch=int(input("Enter the No of Copies: "))
            if (ch<=self.no_copies):
                self.no_copies-=1
            else:
                print("Insufficient Copies")
        

class Book(LibraryItem):
    def __init__(self, title, item_id, no_copies):
        super().__init__(title, item_id, no_copies)
        self.title = title
    def display(self):
        super().display()

class DVD(LibraryItem):
    def __init__(self, title, item_id, no_copies):
        super().__init__(title, item_id, no_copies)
        self.title = title
    def display(self):
        super().display()


class Journal(LibraryItem):
    def __init__(self, title, item_id, no_copies):
        super().__init__(title, item_id, no_copies)
        self.titler = title
    def display(self):
        super().display()



book = Book("C++ Obj.", "B12", 10)
dvd = DVD("Animal", "D13", 5)
journal = Journal("Indian Journal", "J14",15)

book.display()
dvd.display()
journal.display()