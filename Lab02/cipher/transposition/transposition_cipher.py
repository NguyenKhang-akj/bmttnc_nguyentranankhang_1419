class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row = 0  # Initialize row variable
        for symbol in text:
            for col in range(key):
                if (col == key - 1 and row == len(text) % key) or col == 0:
                    row += 1
            decrypted_text[col] += symbol
        return ''.join(decrypted_text)