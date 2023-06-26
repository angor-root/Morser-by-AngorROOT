def encrypt():
    frase = input("Ingrese la frase a cifrar: ")
    palabra_clave = input("Ingrese la palabra clave: ")
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frase = frase.upper()
    palabra_clave = palabra_clave.upper()
    palabra_clave = palabra_clave * (len(frase) // len(palabra_clave) + 1)
    frase_cifrada = ""
    for i in range(len(frase)):
        if frase[i] in alfabeto:
            frase_cifrada += alfabeto[(alfabeto.index(frase[i]) + alfabeto.index(palabra_clave[i])) % len(alfabeto)]
        else:
            frase_cifrada += frase[i]
    print(frase_cifrada)
    return frase_cifrada
def des_encryp(palabra_clave, frase_cifrada):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    palabra_clave = palabra_clave.upper()

    frase_descifrada = ""
    frase_cifrada = frase_cifrada.upper()
    palabra_clave = palabra_clave * (len(frase_cifrada) // len(palabra_clave) + 1)
    for i in range(len(frase_cifrada)):
        if frase_cifrada[i] in alfabeto:
            frase_descifrada += alfabeto[(alfabeto.index(frase_cifrada[i]) - alfabeto.index(palabra_clave[i])) % len(alfabeto)]
        else:
            frase_descifrada += frase_cifrada[i]
    return frase_descifrada
def createDict():
    code = {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----'}
    return code
def to_morse(frase_encriptada):
    words = frase_encriptada.upper()
    codeDict = createDict()
    i = 0
    try:
        while (i < len(words)):
            if (words[i] != " "):
                print(codeDict[words[i]], end = " ")
            else:
                print("/", end = " ")
            i += 1
    except:
        print("\nNo se puede traducir el mensaje")
def from_morse(frase_morse):
    words = frase_morse.split(" ")
    codeDict = createDict()
    i = 0
    frase_traducida = ""
    try:
        while (i < len(words)):
            if (words[i] != "/"):
                frase_traducida += list(codeDict.keys())[list(codeDict.values()).index(words[i])]
            else:
                frase_traducida += " "
            i += 1
    except:
        print("\nNo se puede traducir el mensaje")
    return frase_traducida
def main():
    """This program encrypts and desencrypts a message using the two phases method created by angor_root"""
    print("ENCRYPT_TWO_PHASES")
    print("1. Encrypt")
    print("2. Desencrypt")
    print("3. Exit")
    option = int(input("Ingrese la opcion: "))
    if option == 1:
        frase_encriptada = encrypt()
        print("first_step_encrypt: ",frase_encriptada)
        print("second_step_encrypt: ", end = "")
        to_morse(frase_encriptada)
    elif option == 2:
        frase_morse = input("Ingrese la frase en morse: ")
        palabra_clave = input("Ingrese la palabra clave: ")
        frase_traducida = from_morse(frase_morse)
        print("first_step_desencrypt: ", frase_traducida)
        print("second_step_desencrypt: ", end = "")
        print(des_encryp(palabra_clave, frase_traducida))

    elif option == 3:
        exit()
        
main()
