class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @classmethod
    def multiply(cls, x, y):
        print(f"Calculation type: {cls.calculation_type}")
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y