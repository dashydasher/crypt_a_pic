import sys
import cryptappm

def main():
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    message = sys.argv[3]

    print("--------------------------------------------------------")
    print("HIDING")
    print()
    print("Input:", input_file_name)
    print("Output:", output_file_name)
    print("Message:", message)
    print()
    byte_list = cryptappm.bytes_from_file(input_file_name)
    print("Is it ppm?", cryptappm.check_ppm(byte_list))
    print()
    magic_number, width, height, max_value, data_index = cryptappm.read_non_data_ppm(byte_list)
    print("Magic number, width, height, max_value, data_index:", magic_number, width, height, max_value, data_index)
    print()
    message_in_bits = cryptappm.string_to_bits(message)
    print("Message in bits:", message_in_bits)
    print()
    message_size_in_bits = cryptappm.int_to_bits(len(message_in_bits))
    print("Message size in bits:", message_size_in_bits)
    print()
    byte_list_with_message = cryptappm.hide_message(byte_list, data_index, cryptappm.secret_id, message_size_in_bits, message_in_bits)
    cryptappm.bytes_to_file(output_file_name, byte_list_with_message)
    print("Message hidden in", output_file_name)
    print("--------------------------------------------------------")

if __name__ == '__main__':
    main()
