# Problem Set 4C
# Name: <aditya adiga>


import string
from ps4a import get_permutations


def load_words(file_name):

    
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




WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

 '''
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''


        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        consonant_upper='BCDFGHJKLMNPQRSTVWXYZ'
        consonant_lower='bcdfghjklmnpqrstvwxyz'
        vowel_upper='AEIOU'
        vowel_lower='aeiou'
        special=" !@#$%^&*()-_+={}[]|\:;'<>?,./\""
        transpose_dict={}
        for i in range(21):
            transpose_dict[consonant_upper[i]]=consonant_upper[i]
            transpose_dict[consonant_lower[i]]=consonant_lower[i]
            
            transpose_dict[special[i]]=special[i]
        for i in range(5):
            transpose_dict[vowel_upper[i]]=vowels_permutation.upper()[i]
            transpose_dict[vowel_lower[i]]=vowels_permutation[i]
        
        return transpose_dict
            
            
            
    
    def apply_transpose(self, transpose_dict):
 
        encrypted_message=''
        for i in self.get_message_text():
            encrypted_message=encrypted_message+transpose_dict[i]
        return encrypted_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):

        SubMessage.__init__(self,text)
        

    def decrypt_message(self):
        '''


        Returns: the best decrypted message    
        

        '''
        permutation_list=get_permutations('aeiou')
        maximum=0
        decrypt=''
        
        for code in permutation_list:
            dictionary=self.build_transpose_dict(code)
            text=self.apply_transpose( dictionary).strip("!@#$%^&*()-_+={}[]|\:;'<>?,./\"")
            valid=0
            for i in text.split(" "):
                
                if i.lower() in self.valid_words:
                    valid+=1
                    
            if valid>=maximum:
                maximum=valid
                decrypt=code
        
        dictionary=self.build_transpose_dict(decrypt)
        
        return self.apply_transpose( dictionary)
            
                
                
            

                
        
                
                
            

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    
