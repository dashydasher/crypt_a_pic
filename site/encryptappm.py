import sys
import cryptappm

def main():
    try:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        message = sys.argv[3]

        byte_list = cryptappm.bytes_from_file(input_file_name)
        magic_number, width, height, max_value, data_index = cryptappm.read_non_data_ppm(byte_list)
        message_in_bits = cryptappm.string_to_bits(message)
        message_size_in_bits = cryptappm.int_to_bits(len(message_in_bits))
        byte_list_with_message = cryptappm.hide_message(byte_list, data_index, cryptappm.secret_id, message_size_in_bits, message_in_bits)
        cryptappm.bytes_to_file(output_file_name, byte_list_with_message)

        print("True")
        return 0
    except Exception as e:



        print("False")
        return 1

if __name__ == '__main__':
    main()
