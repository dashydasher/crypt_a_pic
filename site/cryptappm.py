secret_id = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]

def bytes_from_file(filename, chunksize=8192):
    byte_list = []
    with open(filename, "rb") as in_file:
        while True:
            chunk = in_file.read(chunksize)
            if chunk:
                for b in chunk:
                    byte_list.append(b)
            else:
                return byte_list

def bytes_to_file(filename, byte_list):
    with open(filename, "wb") as out_file:
        out_file.write(bytes(byte_list))

def check_ppm(byte_list):
    if byte_list[0] == 80 and byte_list[1] == 54:
        return True
    else:
        return False

def read_non_data_ppm(byte_list):
    white_spaces = [10, 32]
    magic_number_bytes = []
    width_bytes = []
    height_bytes = []
    max_value_bytes = []
    ws_counter = 4
    for i in range(0, len(byte_list)):
        if byte_list[i] in white_spaces:
            ws_counter -= 1
        elif ws_counter == 4:
            magic_number_bytes.append(byte_list[i])
        elif ws_counter == 3:
            width_bytes.append(byte_list[i])
        elif ws_counter == 2:
            height_bytes.append(byte_list[i])
        elif ws_counter == 1:
            max_value_bytes.append(byte_list[i])
        elif ws_counter == 0:
            data_index = i
            break

    magic_number = ""
    for byte in magic_number_bytes:
        magic_number += str(chr(byte))

    width_str = ""
    for byte in width_bytes:
        width_str += str(chr(byte))
    width = int(width_str)

    height_str = ""
    for byte in height_bytes:
        height_str += str(chr(byte))
    height = int(height_str)

    max_value_str = ""
    for byte in max_value_bytes:
        max_value_str += str(chr(byte))
    max_value = int(max_value_str)

    return magic_number, width, height, max_value, data_index

def string_to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def bits_to_string(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def int_to_bits(v):
    result = []
    for bit in bin(v)[2:]:
        result.append(int(bit))
    while len(result) < 32:
        result = [0] + result
    return result

def bits_to_int(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def inject_bit_into_byte(bit, byte):
    if byte % 2 == 1 and bit == 0: # 1 na kraju, treba 0
        injected_byte = byte - 1
    elif byte % 2 == 0 and bit == 1: # 0 na kraju, treba 1
        injected_byte = byte + 1
    else:
        injected_byte = byte
    return injected_byte

def hide_message(byte_list, data_index, secret_id, message_size_in_bits, message_in_bits):
    byte_list_with_message = []
    # non data
    for i in range(0, data_index):
        byte_list_with_message.append(byte_list[i])

    # secret_id
    for i in range(data_index, data_index + 32):
        bit_to_inject = secret_id[i-data_index]
        byte_to_be_injected = byte_list[i]
        injected_byte = inject_bit_into_byte(bit_to_inject, byte_to_be_injected)
        byte_list_with_message.append(injected_byte)

    # message_size_in_bits
    for i in range(data_index + 32, data_index + 64):
        bit_to_inject = message_size_in_bits[i-data_index-32]
        byte_to_be_injected = byte_list[i]
        injected_byte = inject_bit_into_byte(bit_to_inject, byte_to_be_injected)
        byte_list_with_message.append(injected_byte)

    # message_in_bits
    for i in range(data_index + 64, data_index + 64 + len(message_in_bits)):
        bit_to_inject = message_in_bits[i-data_index-64]
        byte_to_be_injected = byte_list[i]
        injected_byte = inject_bit_into_byte(bit_to_inject, byte_to_be_injected)
        byte_list_with_message.append(injected_byte)

    # rest
    for i in range (data_index + 64 + len(message_in_bits), len(byte_list)):
        byte_list_with_message.append(byte_list[i])

    return byte_list_with_message

def find_secret_id(byte_list, data_index):
    secret_id = []
    for i in range(data_index, data_index + 32):
        secret_id.append(byte_list[i] % 2)
    return secret_id

def check_secret_id(secret_id, found_id):
    if secret_id == found_id:
        return True
    else:
        return False

def find_message_size(byte_list, data_index):
    message_size_in_bits = []
    for i in range(data_index + 32, data_index + 64):
        message_size_in_bits.append(byte_list[i] % 2)

    message_size = 0
    for bit in message_size_in_bits:
        message_size = (message_size << 1) | bit
    return message_size

def find_message(byte_list, data_index, message_size):
    message_in_bits = []
    for i in range(data_index + 64, data_index + 64 + message_size):
        message_in_bits.append(byte_list[i] % 2)
    return bits_to_string(message_in_bits)
