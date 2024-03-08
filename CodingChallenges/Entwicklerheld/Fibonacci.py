class FibonacciPython:

    @staticmethod
    def fibonacci(number: int) -> int:
        # implement me
        if number == 0: return number
        letzte_nummer: int = 0
        naechste_nummer: int = 1
        for i in range(1, number):
            letzte_nummer, naechste_nummer = naechste_nummer, letzte_nummer + naechste_nummer
        return naechste_nummer


if __name__ == "__main__":
    print(FibonacciPython.fibonacci(1))