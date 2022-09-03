import hashlib
from traceback import print_tb

print ( '''

.==================================================================.
||           Python Hash Maker App - Version : 1.0.0              ||
|'================================================================'|
||                                                                ||
||                                  .::::.                        ||
||                                .::::::::.                      ||
||                                :::::::::::                     ||
||                                ':::::::::::..                  ||
||                                 :::::::::::::::'               ||
||                                  ':::::::::::.                 ||
||                                    .::::::::::::::'            ||
||                                  .:::::::::::...               ||
||                                 ::::::::::::::''               ||
||                     .:::.       '::::::::''::::                ||
||                   .::::::::.      ':::::'  '::::               ||
||                  .::::':::::::.    :::::    '::::.             ||
||                .:::::' ':::::::::. :::::      ':::.            ||
||              .:::::'     ':::::::::.:::::       '::.           ||
||            .::::''         '::::::::::::::       '::.          ||
||           .::''              '::::::::::::         :::...      ||
||        ..::::                  ':::::::::'        .:' ....     ||
||                                                                ||
|'===========================================================LGB=='|
''')

print ("Welcome To The Python Hash Maker App")

print ("---------------------------")

print ("This App Is On Version : 1.0.0")

print ("===========================")

print (" # Application Developer : Mohammad Babaee ")

print ("===========================")

print ("please Choose An Algorithm ")

print ("1 ) sha1 ")
print ("2 ) sha224 ")
print ("3 ) sha256 ")
print ("4 ) sha384 ")
print ("5 ) sha512 ")
print ("6 ) md5 ")

print ("---------------------------")

selector = input("Please Enter The Number Here : ")

if selector == "1":
    h = hashlib.new('sha1')
    algorithm = "The Algoritm That Used For Encryption is : SHA1 "
elif selector == "2":
    h = hashlib.new('sha224')
    algorithm = "The Algoritm That Used For Encryption is : SHA224 "
elif selector == "3":
    h = hashlib.new('sha256')
    algorithm = "The Algoritm That Used For Encryption is : SHA256 "
elif selector == "4":
    h = hashlib.new('sha384')
    algorithm = "The Algoritm That Used For Encryption is : SHA384 "
elif selector == "5":
    h = hashlib.new('sha512')
    algorithm = "The Algoritm That Used For Encryption is : SHA512 "
else:
    h = hashlib.new('md5')
    algorithm = "The Algoritm That Used For Encryption is : MD5 "

text =  str(input("Please Enter Your Text That You Wanna Encrypt That : "))

encoder = text.encode()

h.update(encoder)

result = h.hexdigest()

print ("---------------------------")

print ("The Answer is Ready : ")

print("\n")

print("Your Hash is : " + result)

print("\n")

print(algorithm)

print("\n")

print ("--- This App Is Published Under (MIT License) ---")