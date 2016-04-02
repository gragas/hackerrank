def encrypt(s, k):
    def convert(c):
        offset = 65 if c.isupper() else 97
        return chr((ord(c) - offset + k) % 26 + offset)
    return "".join([convert(c) if c.isalpha() else c for c in s])

n = int(input())
s = input()
k = int(input())
print(encrypt(s, k))
