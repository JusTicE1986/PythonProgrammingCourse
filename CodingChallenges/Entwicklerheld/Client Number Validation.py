class ParityBitPython:
    @staticmethod
    def validate_client_number(client_number: str) -> bool:
        try:
            if client_number.isdigit() and len(client_number) == 10:
                client_number_byte = bin(int(client_number))
                is_valid = client_number_byte.count("1") % 2 == 0
                print(is_valid)
                return is_valid
            else:
                return False
        except ValueError:
            return False

if __name__ == '__main__':
    print(ParityBitPython.validate_client_number("8456894318"))