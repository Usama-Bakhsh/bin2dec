def bin2dec(input_str):
    output = 0
    for position, digit in enumerate(input_str):
        if digit not in ['0', '1']:
            raise ValueError("Input skal være en binær streng, der kun indeholder '0' og '1'.")
        output = (output * 2) + int(digit)
    return output

hex_table = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 
                 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 
                 14:'E', 15:'F',}

def dec2hex(input_dec):
    output = ''
    while(input_dec > 0):
        remainder = input_dec % 16
        output = hex_table[remainder] + output
        input_dec = input_dec // 16

    return output

if __name__ == "__main__":
    user_input = input("Indtast et binært tal: ")
    try:
        dec_output = bin2dec(user_input)
        print(f"Decimal værdi: {dec_output}")
        hex_output = dec2hex(dec_output)
        print(f"Hexadecimal værdi: {hex_output}")
    except ValueError as e:
        print(f"Fejl: {e}")