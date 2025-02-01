'''
Secret Decoder Ring


October 10th, 2024


Fortune Meya
Yusuke Homma


This program ask user to select encryot or decrypt the message. If the user chooses encrypt, user also chooses the method 
of encryption. Then user enters a message. Encrypted message will be saved to message.txt. If user choose decrypt, user 
chooses the method of decryption. Then read the message from message.txt and decrypt it.
'''
import cipher
import caesar
import check_input

def write_to_file(message):
        '''Open message.txt and write encrypted message to it'''
        with open("message.txt", "w") as file:
            file.write(message)
        file.close()
        print(f"Encrypted message saved to 'message.txt'.")

def read_from_file():
        '''Open message.txt and read encrypted message from it'''
        print("Reading encrypted message from “message.txt”.")
        with open("message.txt", "r") as file:
            message = file.read()
        file.close()
        return message

def main():
    '''Ask encrypt or decrypt, then ask the method. Save encrypted message to txt file and read message from txt file 
    when decrypt'''
    while True:
        en_or_de = str(input("Secret Decoder Ring: \n1. Encrypt\n2. Decrypt\n"))
        if en_or_de == '1':
            encrypt_input = str(input("Enter encryption type:\n1. Atbash\n2. Caesar\n"))
            user_message = str(input("Enter message: "))

            if encrypt_input == '1':
                e_cipher = cipher.Cipher()
            elif encrypt_input == '2':
                user_shift = check_input.get_int("Enter shift value: ")
                e_cipher = caesar.Caesar(user_shift)
            else:
                print("Invalid")
                continue

            message_result = e_cipher.encrypt_message(user_message)
            write_to_file(message_result)
            #print(f'\nEncrypted message that is written to file: {message_result}\n')
            return


        elif en_or_de == '2':
            decrypt_input = str(input("Enter decryption type:\n1. Atbash\n2. Caesar\n"))
            if decrypt_input == '1':
                encrypted_message = read_from_file()
                d_cipher = cipher.Cipher()
            elif decrypt_input == '2':
                user_shift = check_input.get_int("Enter shift value: ")
                encrypted_message = read_from_file()
                d_cipher = caesar.Caesar(user_shift)
            else:
                 print("Invalid")
                 continue
                
            message_result = d_cipher.decrypt_message(encrypted_message)
            print(f"Decrypted message: {message_result}")
            return
        else:
            print("Invalid")
            continue
        
main()

