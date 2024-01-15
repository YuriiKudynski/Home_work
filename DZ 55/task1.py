class Vector:

    def __init__(self, x, y, z):
        """Create Vector with coordinate (x, y, z)"""
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
            raise ValueError("Only int or float type data!")
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """Print data for vectors"""
        return f"Vector - ({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        """Check if 2 vectors are equal"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        """Check if 2 vectors are not equal"""
        return not (self == other)

    def __add__(self, other):
        """Add two vectors and create new with added coord"""
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            # new_coords = (self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            new_x = self.x + other
            new_y = self.y + other
            new_z = self.z + other
        else:
            raise TypeError("Input correct data!")

        return Vector(new_x, new_y, new_z) # or return new_coords

    def __sub__(self, other):
        """Sub 2 vectors and create new with sub coord"""
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            new_z = self.z - other.z
        elif isinstance(other, (int, float)):
            new_x = self.x - other
            new_y = self.y - other
            new_z = self.z - other
        else:
            raise TypeError("Input correct data!")

        return Vector(new_x, new_y, new_z)

    def __iadd__(self, other):
        """In-place addition of two vectors."""
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            self.z += other
        else:
            raise TypeError("Input correct data!")

        return self

    def __isub__(self, other):
        """In-place subtraction of two vectors."""
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        elif isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
            self.z -= other
        else:
            raise TypeError("Input correct data!")

        return self

    def __mul__(self, other):
        """Scalar multiplication two vectors"""
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Input correct data")

    def __rmul__(self, other):
        """Scalar multiplication two vectors"""
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Input correct data")

    def __len__(self):
        """Calculate len vector"""
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __int__(self):
        """Calculate len vector in math"""
        return round((self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5)

    def __neg__(self):
        """Return negative coord in vector"""
        return Vector(-self.x, -self.y, -self.z)

    def __bool__(self):
        """Return True if len vector more zero, False if zero"""
        return bool(self.__len__())


try:
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    v3 = Vector(2, 3, 5)
    v4 = Vector(-1, -2, -3)
    v5 = Vector(0, 0, 0)
    print(v1 * v2)
    print(v1 * 3)
    print(3 * v2)
    print(len(v1))
    print(int(v1))
    print(v1.__neg__())
    print(v4.__neg__())
    print(bool(v1))
    print(bool(v5))
except ValueError as e:
    print(e)

