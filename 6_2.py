tablitsa_kodov = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                  'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                  'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                  'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
def perevod(text_1):
    perevod_1 = []
    for i in text_1:
        perevod_1.append(tablitsa_kodov.get(i))#убрать пробелы и символы - сделать проверку
    print(perevod_1)

perevod(input('введи текст на английском '))
