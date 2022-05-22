from secrets import token_bytes


class OneTimePad(object):
    def random_key(self, length):
        bytes = token_bytes(length)
        return int.from_bytes(bytes, "big")

  

class Text(OneTimePad):
    def __init__(self, content):
        self.content = content
        self.key = 0
        self.decrypted = 0

    def encrypt(self):
        self.content = self.content.encode()
        self.key = super().random_key(len(self.content))
        original_key = int.from_bytes(self.content, 'big')
        self.content = original_key ^ self.key
        return self.content

    def decrypt(self):
        self.decrypted = self.content ^ self.key
        bytes = self.decrypted.to_bytes((self.decrypted.bit_length() + 7)   //8,    "big")
        return bytes.decode()
