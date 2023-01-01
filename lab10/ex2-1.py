#!/usr/bin/python3

import string 

FILENAME_PREFIX = "text_files/ex2-1"

def main():

    alphabet = string.ascii_uppercase[::-1] 

    key       = input("Key> ")
    operation = input("Encrypt [E] or Decrypt [D]> ")
    filename  = input("Filename> ")
    result    = input("New filename> ")

    """
    Handle the key to create the appropriate character stream for enc/dec.
    """

    # set is used to remove duplicates. BUT, it does not preserve the order.
    # in order to guarantee that this will be the case, we use sorted with sorting
    # key the index function of the string class.
    # 
    # about sorting: https://docs.python.org/3/howto/sorting.html
    key = ''.join(sorted(set(key), key=key.index)).upper()
    
    alphabet = key + alphabet # concatenate with the alphabet stream 

    # once again, same trick to remove duplicates (i.e., 'key' characters) from the alphabet 
    alphabet = ''.join(sorted(set(alphabet), key = alphabet.index))

    encrypt_mapping = {k : v  for k,v in zip(string.ascii_uppercase,alphabet) }
    decrypt_mapping = {k : v  for k,v in zip(alphabet,string.ascii_uppercase) }

    """
    Read the input file while converting each caracter also to uppercase for convenience
    """
    try: 

        with open(f"{FILENAME_PREFIX}/{filename}") as input_file: 

            data = list(map(str.upper, [x.rstrip() for x in input_file]))

    except: 
        
        exit(f"Tried to open file \"{FILENAME_PREFIX}/{filename}\". It's not found!")


    """
    Encrypt or Decrypt
    """
    output_stream = ""
    
    for line in data: 

        for char in line: 

            if   operation == 'E': 
            
                output_stream += encrypt_mapping[char] if char in string.ascii_uppercase else char  
            
            elif operation == 'D': 
            
                output_stream += decrypt_mapping[char] if char in string.ascii_uppercase else char 
            
            else: 
            
                exit("Invalid operation selected. Valid ones are E (encrypt) and D (decrypt)")
        
        output_stream += '\n'


    """
    Write to file
    """
    try: 
        
        with open(f"{FILENAME_PREFIX}/{result}",'w') as output_file:

            output_file.write(output_stream) 

    except OSError: 

        exit(f"Something went wrong while trying to create output file ({FILENAME_PREFIX}/{result}).")
    


if __name__ == "__main__":
    main() 