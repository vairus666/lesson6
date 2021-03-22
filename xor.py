# XOR шифрование 
from homework import helping

def xor():
    text = helping.read_from_file()
    key = str(helping.read_to_file_key())
    result = bytearray()
    if type(text) == str:
        text = bytearray(text, "utf-8")
    key = bytearray(key, "utf-8")  

    for i in range(len(text)):
        result.append(text[i] ^ key[i % len(key)])
    helping.write_to_file(result)
    
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
