MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def morseencode(message,seperator):
    message = message.upper()
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            try:
                cipher += MORSE_CODE_DICT[letter] + ' '
            except:
                raise Exception("Unable to encode '%s'" % letter)
        else: 
            cipher += (seperator+' ')
    return cipher 
  
def morsedecode(message,seperator): 
    message = message.strip()
    words = message.split(" "+seperator+" ")
    text = ''
    for w in words:
        for letter in w.split(" "):
            try:
                text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)] 
            except:
                raise Exception("Invalid morse code '%s'" % letter)
        text += " "
    return text