class PlayfairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        
        # Remove duplicates but preserve order
        seen = set()
        filtered_key = []
        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                filtered_key.append(char)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is excluded
        for letter in alphabet:
            if letter not in seen:
                filtered_key.append(letter)
        
        # Create 5x5 matrix
        matrix = [filtered_key[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None  # If letter not found (shouldn't happen)

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = ''.join(filter(str.isalpha, plain_text))  # Remove non-alpha chars
        
        # Prepare pairs with 'X' padding and avoid duplicate pairs
        i = 0
        pairs = []
        while i < len(plain_text):
            a = plain_text[i]
            b = ''
            if i + 1 < len(plain_text):
                b = plain_text[i+1]
            else:
                b = 'X'
            
            if a == b:
                pairs.append((a, 'X'))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        
        encrypted_text = ""
        for a, b in pairs:
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return decrypted_text


# Example usage
if __name__ == "__main__":
    cipher = PlayfairCipher()
    key = "KEY"
    matrix = cipher.create_playfair_matrix(key)
    print("Matrix:")
    for row in matrix:
        print(row)

    plain_text = "HELLO"
    encrypted = cipher.playfair_encrypt(plain_text, matrix)
    decrypted = cipher.playfair_decrypt(encrypted, matrix)

    print(f"Plain text: {plain_text}")
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")
