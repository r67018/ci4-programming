from math import gcd, lcm, sqrt, floor


def generate_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(text, pub_key):
    e, n = pub_key
    encrypted_ints = [pow(ord(char), e, n) for char in text]
    return encrypted_ints

def decrypt(encrypted_ints, priv_key):
    d, n = priv_key
    decrypted_ints = [pow(c, d, n) for c in encrypted_ints]
    decrypted_text = ''.join(chr(m) for m in decrypted_ints)
    return decrypted_text

def attack(encrypted_ints, pub_key):
    e, _ = pub_key
    decrypted_ints = []
    for c in encrypted_ints:
        m =  c ** pow(e, -1)
        m = int(m + 0.5) # 四捨五入
        decrypted_ints.append(int(m))
    decrypted_text = ''.join(chr(m) for m in decrypted_ints)
    return decrypted_text


input_text = 'Hello, World!'
pub_key, priv_key = generate_key(1949, 2111)
print('Public key:', pub_key)
print('Private key:', priv_key)
encrypted_ints = encrypt(input_text, pub_key)
decrypted_text = decrypt(encrypted_ints, priv_key)
attacked_text = attack(encrypted_ints, pub_key)

print('Input text:', input_text)
print('Encrypted ints:', encrypted_ints)
print('Decrypted text:', decrypted_text)
print('Attacked text:', attacked_text)
