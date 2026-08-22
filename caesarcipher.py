text='Gen-Z are the best'
shift=5
def caesar(message,offset):
    sequence="abcdefghijklmnopqrstuvwxyz123456789+-%$!@#*[]_'"
    encrypted_text=''
    for char in message.lower():
        if char==' ':
            encrypted_text+=char
        else:
            index=sequence.find(char)
            new_index=(index + offset) % len(sequence)
            encrypted_text+=sequence[new_index]
    print('Plain text:',message)
    print('Encrypted text:',encrypted_text)
caesar(text,shift)