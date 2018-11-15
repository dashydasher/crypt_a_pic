import sys
import cryptappm

input_file_name = sys.argv[1]

print("--------------------------------------------------------")
print("FINDING")
print()
byte_list = cryptappm.bytes_from_file(input_file_name)
print("Is it ppm?", cryptappm.check_ppm(byte_list))
print()
magic_number, width, height, max_value, data_index = cryptappm.read_non_data_ppm(byte_list)
print("Magic number, width, height, max_value, data_index:", magic_number, width, height, max_value, data_index)
print()
found_id = cryptappm.find_secret_id(byte_list, data_index)
print("Found id:", found_id)
print("Is the id correct?", cryptappm.check_secret_id(cryptappm.secret_id, found_id))
print()
message_size = cryptappm.find_message_size(byte_list, data_index)
print("Found message size:", message_size)
print()
message = cryptappm.find_message(byte_list, data_index, message_size)
print("Found message:", message)
print("--------------------------------------------------------")
