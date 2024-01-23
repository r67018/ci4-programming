from math import gcd, lcm, sqrt


def generate_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    print('phi:', phi)
    e = 7
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(text, pub_key):
    e, n = pub_key
    encrypted_ints = [pow(ord(char), e, n) for char in text]
    encrypted_text = ''.join(chr(i) for i in encrypted_ints)
    return encrypted_text

def decrypt(encrypted_text, priv_key):
    d, n = priv_key
    decrypted_ints = [pow(ord(char), d, n) for char in encrypted_text]
    decrypted_text = ''.join(chr(i) for i in decrypted_ints)
    return decrypted_text

def attack(encrypted_text, pub_key):
    e, n = pub_key
    decrypted_ints = []
    for char in encrypted_text:
        i = ord(char)
        m = i ** (1 / e)
        print('i:', i)
        print('m:', m)
        decrypted_ints.append(int(m))
    decrypted_text = ''.join(chr(i) for i in decrypted_ints)
    return decrypted_text


input_text = 'H'
pub_key, priv_key = generate_key(101, 3259)
print('Public key:', pub_key)
print('Private key:', priv_key)
encrypted_text = encrypt(input_text, pub_key)
decrypted_text = decrypt(encrypted_text, priv_key)
attacked_text = attack(encrypted_text, pub_key)

print('Input text:', input_text)
print('Encrypted text:', encrypted_text)
print('Decrypted text:', decrypted_text)
print('Attacked text:', attacked_text)
