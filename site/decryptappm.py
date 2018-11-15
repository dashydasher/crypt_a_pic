import sys
import cryptappm

def main():
    try:
        input_file_name = sys.argv[1]

        byte_list = cryptappm.bytes_from_file(input_file_name)
        magic_number, width, height, max_value, data_index = cryptappm.read_non_data_ppm(byte_list)
        found_id = cryptappm.find_secret_id(byte_list, data_index)
        message_size = cryptappm.find_message_size(byte_list, data_index)
        message = cryptappm.find_message(byte_list, data_index, message_size)

        print(message)

        return 0
    except:
        return 1

if __name__ == '__main__':
    main()
