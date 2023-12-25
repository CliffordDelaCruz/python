#crytography.py
def caesar_decode(message, offset):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decoded_message = ''
    for letter in message:
        if letter not in letters:
            decoded_message += letter
        else:
            start = letters.index(letter)
            letter_index = start
            for ctr in range(offset):
                if ctr == offset:
                    if letter_index == (len(letters) - 1):
                        letter_index = (len(letters) - 1)
                    else:
                        letter_index += 1
                elif ctr < offset:
                    if letter_index == (len(letters) - 1):
                        letter_index = 0
                    else:
                        letter_index += 1
            decoded_message += letters[letter_index]
    return decoded_message

def caesar_encode(message, offset):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encoded_message = ''
    for letter in message:
        if letter not in letters:
            encoded_message += letter
        else:
            start = letters.index(letter)
            letter_index = start
            for ctr in range(offset):
                if ctr == offset:
                    if letter_index == 0:
                        letter_index = (len(letters) - 1)
                    else:
                        letter_index -= 1
                elif ctr < offset:
                    if letter_index == 0:
                        letter_index = (len(letters) - 1)
                    else:
                        letter_index -= 1
            encoded_message += letters[letter_index]
    return encoded_message

print(caesar_decode('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.',10))

print(caesar_decode('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!',14))

#brute force decode (offset = 7)
for goffset in range(1, 11):
    print(goffset)
    print(caesar_decode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",goffset))

#The Vigenère Cipher
def vigenere_encode(message, keyword):
    keyword_list = list(keyword)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    converted_message = ''
    keyword_ind = 0
    #this section translates per word for the keyword.
    for letter in message:
        if letter in letters:
            converted_message += keyword_list[keyword_ind]
            if keyword_ind >= len(keyword_list) - 1:
                keyword_ind = 0
            else:
                keyword_ind += 1
        else:
            converted_message += letter

    #this section is to get the difference between first message to the converted message
    #pass the words in a list
    o_message = list(message)
    c_message = list(converted_message)
    offset = 0
    encoded_message = ''
    #identify the offset by subtracting list index from converted_message to message
    for ctr in range(len(o_message)):
        if o_message[ctr] not in letters:
            encoded_message += o_message[ctr]
        else:
            first_index = letters.index(o_message[ctr])
            second_index = letters.index(c_message[ctr])
            #determine which index is bigger
            if first_index >= second_index:
                offset = first_index - second_index
            elif first_index < second_index:
                offset = ((len(letters)) - second_index) + first_index
            encoded_message += letters[offset]
    return encoded_message

def vigenere_decode(message, keyword):
    keyword_list = list(keyword)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    converted_message = ''
    keyword_ind = 0
    #this section translates per word for the keyword.
    for letter in message:
        if letter in letters:
            converted_message += keyword_list[keyword_ind]
            if keyword_ind >= len(keyword_list) - 1:
                keyword_ind = 0
            else:
                keyword_ind += 1
        else:
            converted_message += letter

    #this section is to get the difference between first message to the converted message
    #pass the words in a list
    o_message = list(message)
    c_message = list(converted_message)
    offset = 0
    decoded_message = ''
    #identify the offset by subtracting list index from converted_message to message
    for ctr in range(len(o_message)):
        if o_message[ctr] not in letters:
            decoded_message += o_message[ctr]
        else:
            first_index = letters.index(o_message[ctr])
            second_index = letters.index(c_message[ctr])
            #determine which index is bigger
            if first_index >= second_index:
                offset = second_index - ((len(letters)) - first_index)
            elif first_index < second_index:
                offset = second_index + first_index
                if offset >= len(letters):
                    offset = offset - len(letters)
            decoded_message += letters[offset]
    return decoded_message

#test
print(vigenere_encode('you were able to decode this? nice work! you are becoming quite the expert at cryptography!','friends'))
print(vigenere_decode('txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!','friends'))