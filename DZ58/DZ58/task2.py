class UsernameDescriptor:

    def __get__(self, instance, owner):
        return instance._username

    def __set__(self, instance, value):
        if not (4 <= len(value) <= 10 and value[0].isalpha() and value.isalnum()):
            raise ValueError("Incorrect username")
        instance._username = value


class PasswordDescriptor:

    def __get__(self, instance, owner):
        return instance._password

    def __set__(self, instance, value):
        if len(value) <= 8:
            raise ValueError("Password must have more 8 symbol. Try again")
        instance._password = value


class User:
    username = UsernameDescriptor()
    password = PasswordDescriptor()

    def __init__(self, username, password):
        self.username = username
        self.password = password


user = User("Frank1", "123456789")
print(user.username)
print(user.password)

