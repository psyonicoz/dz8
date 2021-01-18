class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = [(self.a + other.a), (self.b + other.b)]
        return a
        # return f'({self.a};{self.b}i) + ({other.a};{other.b}i) = ({self.a + other.a} + {self.b + other.b}i)'

    def __mul__(self, other):
        a = [self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b]
        return a
        # return f'({self.a};{self.b}i) * ({other.a};{other.b}i) = ' \
        #        f'({self.a * other.a - (self.b * other.b)} + {self.a * other.b + other.a * self.b}i)'


z_1 = ComplexNumber(6, 4)
z_2 = ComplexNumber(-7, 5)
z_3 = z_1 + z_2
print(z_3)
print(z_1 * z_2)
