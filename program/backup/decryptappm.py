def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as inf:
        while True:
            chunk = inf.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


bytelist = []
for b in bytes_from_file('./outimage.ppm'):
    bytelist.append(b)


if hex(bytelist[0]) == '0x50' and hex(bytelist[1]) == '0x36':
    print('This is ppm.')


ws = ['0xa', '0x20']
magicNumberBytes = []
widthBytes = []
heightBytes = []
maxValueBytes = []
counterWS = 4
for i in range(0, len(bytelist)):
    if hex(bytelist[i]) in ws:
        counterWS -= 1
    elif counterWS == 4:
        magicNumberBytes.append(bytelist[i])
    elif counterWS == 3:
        widthBytes.append(bytelist[i])
    elif counterWS == 2:
        heightBytes.append(bytelist[i])
    elif counterWS == 1:
        maxValueBytes.append(bytelist[i])
    elif counterWS == 0:
        dataIndex = i
        break

magicNumber = ""
for byte in magicNumberBytes:
    magicNumber += str(chr(byte))

widthStr = ""
for byte in widthBytes:
    widthStr += str(chr(byte))
width = int(widthStr)

heightStr = ""
for byte in heightBytes:
    heightStr += str(chr(byte))
height = int(heightStr)

maxValueStr = ""
for byte in maxValueBytes:
    maxValueStr += str(chr(byte))
maxValue = int(maxValueStr)

#print("magicNumber: " + magicNumber)
#print("width: " + str(width))
#print("height: " + str(height))
#print("maxValue: " + str(maxValue))
#print("dataIndex: " + str(dataIndex))


secret = []
for i in range(dataIndex, dataIndex + 32):
    secret.append(bytelist[i] % 2)
print("Secret:")
print(secret)

encodedMessageSize = []
for i in range(dataIndex + 32, dataIndex + 64):
    encodedMessageSize.append(bytelist[i] % 2)
print("EncodedMessageSize:")
print(encodedMessageSize)
messageSize = 0
for bit in encodedMessageSize:
    messageSize = (messageSize << 1) | bit
print("MessageSize:")
print(messageSize)

encodedMessage = []
for i in range(dataIndex + 64, dataIndex + 64 + messageSize):
    encodedMessage.append(bytelist[i] % 2)
#print("Encoded message:")
#print(encodedMessage)

message = frombits(encodedMessage)
print("Message:")
print(message)
