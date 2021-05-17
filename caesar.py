def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    for i in range(len(plaintext)):
      char = plaintext[i]
      # uppercase
      if (char.isupper()):
         ciphertext += chr((ord(char) + key - 65) % 26 + 65)
      # lowercase
      else:
         ciphertext += chr((ord(char) + key - 97) % 26 + 97)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    for i in range(len(ciphertext)):
      char = ciphertext[i]
      # uppercase
      if (char.isupper()):
         plaintext += chr((ord(char) - key - 65) % 26 + 65)
      # lowercase
      else:
         plaintext += chr((ord(char) - key - 97) % 26 + 97)
    return plaintext

test_en = encrypt(1, "hello")
print(test_en)

test_de = decrypt(1, "hellow")
print(test_de)