try:
    # take path of image as a input
    imgpath = input(r'Enter path of Image : ')

    # taking encryption key as input
    key = int(input('Enter Key for encryption of Image : '))

    # print path of image file and encryption key that
    # we are using

    print('The path of file : ', imgpath)
    print('Key for encryption : ', key)

    # open file for reading purpose
    fin = open(imgpath, 'rb')

    # storing image data in variable "image"
    image = fin.read()
    fin.close()

    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key

    # opening file for writing purpose
    fin = open(imgpath, 'wb')

    # writing encrypted data in image
    fin.write(image)
    fin.close()
    print('Encryption Done...')


except Exception:
    print('Error caught : ', Exception.__name__)

    #code for decryption image

