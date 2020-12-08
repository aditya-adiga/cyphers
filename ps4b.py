# Problem Set 4B
# Name: <Aditya Adiga>


import string

### HELPER CODE ###
def load_words(file_name):
    '''

    Returns: a list of valid words. Words are strings of lowercase letters.
    

    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story



WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
 
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
      
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
      
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
      

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        if shift>=26 and shift<0:
            print("enter proper input for shift")
            return None
        upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower='abcdefghijklmnopqrstuvwxyz'
        special=" !@#$%^&*()-_+={}[]|\:;'<>?,./\""
        shift_dict={}
        for i in range(26):
            shift_dict[upper[i]]=upper[(i+shift)%26]
            shift_dict[lower[i]]=lower[(i+shift)%26]
        for i in range(len(special)):
            shift_dict[special[i]]=special[i]
        return shift_dict
            
    def apply_shift(self, shift):
        '''
       

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict=self.build_shift_dict(shift)
        new_string=''
        for i in self.get_message_text():
            new_string=new_string+shift_dict[i]
        return new_string

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
       

        '''
        Message.__init__(self,text)
        self.shift=shift
        self.encryption_dict=self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)

    def get_shift(self):
        '''
      
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
       
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
       
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''


        Returns: nothing
        '''
        self.shift=shift
        


class CiphertextMessage(Message):
    def __init__(self, text):

        Message.__init__(self,text)


    def decrypt_message(self):
        '''
   

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        maximum=0
        shift=0
        for i in range(26):
            valid=0
         
            
            for word in self.apply_shift(i).split(' '):
                if word in self.get_valid_words():
                    valid+=1
            if valid>=maximum:
                maximum=valid
                shift=i
                
        return (shift,self.apply_shift(shift))
            
            

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('man hunter', 2)
    print('Expected Output: ocp jwpvgt')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('ocp jwpvgt')
    print('Expected Output:', (24, 'man hunter'))
    print('Actual Output:', ciphertext.decrypt_message())

    #test case to try and read the story document in the folder
    ciphertext = CiphertextMessage(get_story_string())
    print('decrypted text', ciphertext.decrypt_message())

    

 
   
    
    
