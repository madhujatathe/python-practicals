class book:
    def details(self):
        self.title = input("Enter the book title: ")
        self.author = input("Enter the author's name: ")
        self.publisher = input("Enter the publisher's name: ")
        self.isbn = input("Enter the ISBN number: ")

    def display(self):
        print("\nTitle:", self.title)
        print("Author:", self.author)
        print("Publisher:", self.publisher)
        print("ISBN number:", self.isbn)


# Creating object
b = book()
b.details()
b.display()
