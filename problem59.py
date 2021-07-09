"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; 
for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", 
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using p059_cipher.txt (right click and 'Save Link/Target As...'),
 a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text.
"""
import numpy as np
from operator import xor

ALPHABET = [ord(i) for i in "abcdefghijklmnopqrstuvwxyz"]

STD_FREQS = np.array(
    [
        0.08123838,
        0.01489279,
        0.0271142,
        0.04319183,
        0.1201955,
        0.02303857,
        0.02025748,
        0.0592146,
        0.0730542,
        0.00103125,
        0.00689511,
        0.03978541,
        0.02611586,
        0.06947774,
        0.07681168,
        0.0181895,
        0.0011245,
        0.06021294,
        0.06280752,
        0.09098589,
        0.02877627,
        0.01107497,
        0.02094864,
        0.00172789,
        0.02113514,
        0.00070213,
    ]
)

with open("resources/p059_cipher.txt") as f:
    ciphertext = [int(n) for n in f.read().split(",")]


def letter_distribution(text):
    length = len(text)
    freqs = np.zeros(len(ALPHABET))
    for letter in text:
        try:
            freqs[ALPHABET.index(letter)] += 1 / length
        except ValueError:
            pass
    return freqs


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


maxsim = 0
ans = 0
for l1 in ALPHABET:
    for l2 in ALPHABET:
        for l3 in ALPHABET:
            plaintext = [
                [l1, l2, l3][i % 3] ^ ciphertext[i] for i in range(len(ciphertext))
            ]
            similarity = cosine_similarity(letter_distribution(plaintext), STD_FREQS)
            if similarity > maxsim:
                ans = sum(plaintext)
                maxsim = similarity

print(ans)
