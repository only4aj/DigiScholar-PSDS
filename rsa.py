import base64

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


def encry(e, n, message):
    message_encoded = [ord(c) for c in message]
    cipher_text = [mod_exp(c, e, n) for c in message_encoded]

    # Convert the cipher text list to a bytes object
    byte_len = (n.bit_length() + 7) // 8
    cipher_bytes = b"".join(
        [c.to_bytes(byte_len, byteorder="big") for c in cipher_text]
    )
    # Encode the bytes as a base64 string for a more readable format
    cipher_base64 = base64.b64encode(cipher_bytes).decode("utf-8")

    return cipher_base64


def decry(password, pkey, n, cipher_base64):
    d = int.from_bytes(base64.b64decode(password), byteorder="big") + int.from_bytes(
        base64.b64decode(pkey), byteorder="big"
    )
    # Decode the base64 string back to bytes
    cipher_bytes = base64.b64decode(cipher_base64)

    # Split the bytes back into individual encrypted integers
    byte_len = (n.bit_length() + 7) // 8  # Calculate the byte length of each number
    cipher_text = []
    for i in range(0, len(cipher_bytes), byte_len):
        encrypted_num = int.from_bytes(cipher_bytes[i : i + byte_len], byteorder="big")
        cipher_text.append(encrypted_num)

    # Decrypt the cipher text
    message_encoded = [mod_exp(c, d, n) for c in cipher_text]

    # Convert decrypted numbers to bytes and then to a string
    message_bytes = b"".join(
        [
            c.to_bytes((c.bit_length() + 7) // 8, byteorder="big")
            for c in message_encoded
        ]
    )
    try:
        message = message_bytes.decode("utf-8")
    except UnicodeDecodeError:
        # Handle cases where decoding fails
        message = "Decryption failed or message contains non-UTF-8 characters."
    return message


def encryptionData(pubkey, pkey, message):
    e = int.from_bytes(base64.b64decode(pubkey), byteorder="big")
    n = int.from_bytes(base64.b64decode(pkey), byteorder="big")
    cipher_text = encry(e, n, message)
    return cipher_text


def decryptionData(password, pvtkey, pkey, message):
    n = int.from_bytes(base64.b64decode(pkey), byteorder="big")
    decrypted_message = decry(password, pvtkey, n, message)
    return decrypted_message


def passwordUpdate(password,pvtkey,newPassword):
    try:
        if len(newPassword) == 12:
            password = int.from_bytes(base64.b64decode(password), byteorder="big")
            pvtkey = int.from_bytes(base64.b64decode(pvtkey), byteorder="big")
            newKey = password + pvtkey - int.from_bytes(base64.b64decode(newPassword), byteorder="big")
            newKey = base64.b64encode(newPassword.to_bytes((newPassword.bit_length() + 7) // 8, byteorder="big")).decode("utf-8")
        else:
            return "Password contains 12 letters!"
    except ValueError or OverflowError:
        print("Password Generate Problem")
    return newKey