def bin2dec(input_str):
    output = 0
    for position, digit in enumerate(input_str[::-1]):
        if digit not in ['0', '1']:
            raise ValueError("Input skal være en binær streng, der kun indeholder '0' og '1'.")
        output += int(digit) * (2 ** position)
    return output


if __name__ == "__main__":
    user_input = input("Indtast et binært tal: ")
    try:
        result = bin2dec(user_input)
        print(f"Decimal værdi: {result}")
    except ValueError as e:
        print(f"Fejl: {e}")