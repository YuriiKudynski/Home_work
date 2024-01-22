import re


class NameDescriptor:

    def __init__(self, prefix="_", min_length=3, max_length=10, only_letters=True):
        self.prefix = prefix
        self.min_length = min_length
        self.max_length = max_length
        self.only_letters = only_letters

    def __set_name__(self, owner, name):
        prefix = self.prefix
        self.var = prefix + name

    def __get__(self, instance, owner):
        return getattr(instance, self.var)

    def __set__(self, instance, value):
        """Set values with some foo"""
        # For first_name and last_name use only letters.
        # For user_name we can use all symbol, first symbol must be letter.
        if self.only_letters and not value.isalpha():
            raise ValueError("First Name and Last Name must have only letters!")
        # Len must be more min_length and lower max_length
        if self.min_length <= len(value) <= self.max_length and value[0].isalpha():
            setattr(instance, self.var, value)
        else:
            raise ValueError(f"Invalid name: {value}")

    def __delete__(self, instance):
        print(f"Delete Name completed!")
        delattr(instance, self.var)


class PasswordDescriptor:
    # Password must have symbols more min_length

    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner, name):
        self.var = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.var)

    def __set__(self, instance, value):
        if len(value) >= self.min_length:
            setattr(instance, self.var, value)
        else:
            raise ValueError(f"Password must have at least {self.min_length} characters")

    def __delete__(self, instance):
        print(f"Delete Password completed!")
        delattr(instance, self.var)


class EmailDescriptor:
    # Use module re for have a true email view

    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        if not re.match(email_pattern, value):
            raise ValueError("Invalid format email!")

        instance._email = value

    def __delete__(self, instance):
        print(f"Delete Email completed!")
        delattr(instance, '_email')


class User:
    username = NameDescriptor("_", 4, 11, only_letters=False)
    first_name = NameDescriptor("_", 4, 11, only_letters=True)
    last_name = NameDescriptor("_", 4, 11, only_letters=True)
    email = EmailDescriptor()
    password = PasswordDescriptor(7)

    def __init__(self, username: str, first_name: str, last_name: str, email: str, password: (str, int)):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Return display_info created user"""
        return (f"User:\nusername={self.username}"
                f"\nfirst_name={self.first_name}"
                f"\nlast_name={self.last_name}"
                f"\nemail={self.email}"
                f"\npassword={self.password}")


user1 = User("username12", "Alice", "Parker", "alo@gmail.com", "123gasea")
print(user1)
user1.password = "aloha102"
del user1.email
user1.email = "test@com.ua"
print(user1)


