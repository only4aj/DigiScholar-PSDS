import random
import math
import base64

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % phi

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def gen_keys():
    p, q = generate_prime(10000000, 1000000000), generate_prime(10000000, 1000000000)
    while p == q:
        q = generate_prime(10000000, 1000000000)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(3, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)

    d = mod_inverse(e, phi_n)

    # Convert e, d, and n into bytes and then encode to base64 for char/number combination
    e_bytes = e.to_bytes((e.bit_length() + 7) // 8, byteorder='big')
    d_bytes = d.to_bytes((d.bit_length() + 7) // 8, byteorder='big')
    n_bytes = n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
    
    e_base64 = base64.b64encode(e_bytes).decode('utf-8')
    d_base64 = base64.b64encode(d_bytes).decode('utf-8')
    n_base64 = base64.b64encode(n_bytes).decode('utf-8')
    
    print(e_base64)
    print(d_base64)
    print(n_base64)
    
    return e_base64, d_base64, n_base64

def encry(e, n, message):
    message_encoded = [ord(c) for c in message]
    cipher_text = [mod_exp(c, e, n) for c in message_encoded]
    
    # Convert the cipher text list to a bytes object
    byte_len = (n.bit_length() + 7) // 8
    cipher_bytes = b''.join([c.to_bytes(byte_len, byteorder='big') for c in cipher_text])
    # Encode the bytes as a base64 string for a more readable format
    cipher_base64 = base64.b64encode(cipher_bytes).decode('utf-8')
    
    return cipher_base64

def decry(d, n, cipher_base64):
    # Decode the base64 string back to bytes
    cipher_bytes = base64.b64decode(cipher_base64)

    # Split the bytes back into individual encrypted integers
    byte_len = (n.bit_length() + 7) // 8  # Calculate the byte length of each number
    cipher_text = []
    for i in range(0, len(cipher_bytes), byte_len):
        encrypted_num = int.from_bytes(cipher_bytes[i:i + byte_len], byteorder='big')
        cipher_text.append(encrypted_num)
    
    # Decrypt the cipher text
    message_encoded = [mod_exp(c, d, n) for c in cipher_text]

    # Convert decrypted numbers to bytes and then to a string
    message_bytes = b''.join([c.to_bytes((c.bit_length() + 7) // 8, byteorder='big') for c in message_encoded])
    
    try:
        message = message_bytes.decode('utf-8')
    except UnicodeDecodeError:
        # Handle cases where decoding fails
        message = "Decryption failed or message contains non-UTF-8 characters."
    
    return message


def encryptionData(pubkey, pkey, message):
    e = int.from_bytes(base64.b64decode(pubkey), byteorder="big")
    n = int.from_bytes(base64.b64decode(pkey), byteorder="big")
    cipher_text = encry(e, n, message)
    return cipher_text


def decryptionData(pvtKey, pkey, message):
    d = int.from_bytes(base64.b64decode(pvtKey), byteorder="big")
    n = int.from_bytes(base64.b64decode(pkey), byteorder="big")
    decrypted_message = decry(d, n, message)
    return decrypted_message
