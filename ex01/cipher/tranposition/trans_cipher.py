class TranspositionCipher:
        def __init__(self):
            pass
        
        def encrypt(self,plain_text,key):
            encrypted_text = ''
            for col in range(key):
                pointer = col
                while pointer < len(plain_text):
                    encrypted_text += plain_text[pointer]
                    pointer += key
            return encrypted_text
        
        
        def decrypt(self,encrypted_text,key):
            decrypted_text = [''] * key
            row,col = 0 , 0 
            for symbol in encrypted_text:
                decrypted_text[row] += symbol
                row += 1
                if row == key or (row == key - 1 and row >= len(decrypted_text) % key):
                    row = 0
                    col += 1
            return ''.join(decrypted_text)