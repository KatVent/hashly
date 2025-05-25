import hashlib

word = input("Give word to hash : ")
encoded_word= word.encode("utf-8")
hash_word = hashlib.sha256(encoded_word).hexdigest()
#print (word)
print (hash_word)