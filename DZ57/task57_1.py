from task1 import Vector


class NewVector(Vector):

    def __getitem__(self, index):
        if 1 <= index <= 3:
            if index == 1:
                return self.x
            elif index == 2:
                return self.y
            elif index == 3:
                return self.z
        else:
            raise IndexError("Out of range")

    def __setitem__(self, index, value):
        if 1 <= index <= 3:
            if index == 1:
                self.x = value
            elif index == 2:
                self.y = value
            elif index == 3:
                self.z = value
        else:
            raise IndexError("Out of range ")

    def __contains__(self, value):
        return value in (self.x, self.y, self.z)

    def __call__(self, numb):
        if isinstance(numb, int):
            new_x = self.x + numb
            new_y = self.y + numb
            new_z = self.z + numb
            return Vector(new_x, new_y, new_z)
        else:
            raise TypeError("Input must be int")


if __name__ == "__main__":
    new_vector = NewVector(6, 2, 7)
    print()
    print(2 in new_vector)
    print(5 in new_vector)
    print()
    print(new_vector(5))
