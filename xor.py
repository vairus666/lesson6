
def write_to_file(data, filename="./text.txt"):
    with open(filename, 'wb') as crip:
        crip.write(data)
        crip.close()


def read_from_file(filename="./text.txt"):
    with open(filename, 'rb') as crip:
        data = crip.read()
        crip.close()
        return data

def read_to_file_key(filename="./key.txt"):
    with open(filename, 'r') as key_pass:
        data = key_pass.read()
        key_pass.close()
        return data

def xor():
    text = read_from_file()
    key = str(read_to_file_key())
    result = bytearray()
    if type(text) == str:
        text = bytearray(text, "utf-8")
    key = bytearray(key, "utf-8")  

    for i in range(len(text)):
        result.append(text[i] ^ key[i % len(key)])
    write_to_file(result)
    

a = input ('Do you want to encrypt?(Yes or No)\n')
if a.lower() == "yes":
    xor()
elif a.lower() == "no":
    a = input('Do you want to decode?(Yes or No)\n')
    if  a.lower() == 'yes':
        xor()
    elif a.lower == 'no':
        print ('Bye Bye')
    else:
        print ("I don't understand you. Bye")
else:
    print ("I don't understand you. Bye")
