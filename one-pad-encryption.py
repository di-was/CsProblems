from secrets import token_bytes

def random_key(length):
    bytes = token_bytes(length)
    return int.from_bytes(bytes, "big")

def encrypt(original):
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, 'big')
    encrypted = original_key ^ dummy
    return dummy, encrypted

