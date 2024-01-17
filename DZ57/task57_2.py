class Book:

    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, name):
        print(f"call __getattr__{name=}")
        if name not in self._attributes:
            raise AttributeError(f"'Book' object has no attribute '{name}'")
        return self._attributes[name]

    def __setattr__(self, name, value):
        print(f"Call __setattr__ with {name=} {value=}")
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            self._attributes[name] = value

    def __str__(self):
        return f"Book {self.title} by {self.author}"

    def __delattr__(self, name):
        if name in self._attributes:
            del self._attributes[name]
        else:
            raise AttributeError(f"Book has no attribute {name}")

    # def __getattribute__(self, name):
    #     print(f"Call __getattribute__ with {name=}")
    #     if name in ("_attributes", "__dict__"):
    #         return super().__getattribute__(name)
    #     else:
    #         raise AttributeError("Error ")

    def __getattribute__(self, name):
        print(f"Виклик __getattribute__ з атрибутом {name=}")
        try:
            if name == "secret":
                raise AttributeError(f"Blocked attribute {name}")
            return super().__getattribute__(name)
        except AttributeError as a:
            return a


if __name__ == "__main__":
    print("1-----------------")
    book = Book("Python Programming", "John Zelle")
    print("2-----------------")
    book.year = 2016
    print("3-----------------")
    print(book.__dict__)
    print("4-----------------")
    print("book.year=", book.year)
    print(book.secret)
