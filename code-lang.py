import random

def encode(word):
    if len(word) >= 3:
        random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        random_chars_i = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        return random_chars + word[1:] + word[0] + random_chars_i
    else:
        return word[::-1]

def decode(word):
    if len(word) >= 6: 
        random_chars = word[:3]  
        random_chars_i= word[-3:-1]
        return word[-4] + word[3:-4]  
    else:
        return word[::-1]

def main():
    while True:
        print("Enter to Code-lang game: \nHere U can encode or decode any statement u want!!! \n\nSimple chose encode to convert your secrets into code language ..... that u want\n\nAnd chose decode to retrieve it back for code language...")
        choice = input("Enter 1 to encode or 0 to decode: ")
        if choice == '1':
            message = input("Enter message: ")
            encoded_message = ' '.join(encode(word) for word in message.split())
            print("Encoded message:", encoded_message)
        elif choice == '0':
            message = input("Enter message: ")
            decoded_message = ' '.join(decode(word) for word in message.split())
            print("Decoded message:", decoded_message)
        else:
            print("Wrong choice!")
            continue
        choice = input("Enter 1 to start again or 0 to exit: ")
        if choice == '0':
            break

if __name__ == "__main__":
    main()
