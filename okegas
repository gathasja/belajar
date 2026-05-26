def is_prima(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prima(n, i + 1)

# Test
print(is_prima(7))   # True
print(is_prima(10))  # False
print(is_prima(13))  # True



=====

def is_palindrom(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])

# Test
print(is_palindrom("katak"))   # True
print(is_palindrom("radar"))   # True
print(is_palindrom("hello"))   # False


====
def deret_ganjil(k):
    if k == 1:
        return 1
    return (2**k - 1) + deret_ganjil(k - 1)

# Test: 1 + 3 + 7 + 15 (k=1 sampai k=4)
print(deret_ganjil(4))  # 26

==


def jumlah_digit(s):
    if len(s) == 0:
        return 0
    return int(s[0]) + jumlah_digit(s[1:])

# Test
print(jumlah_digit("234"))  # 9  (2+3+4)
print(jumlah_digit("159"))  # 15 (1+5+9)

===
def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

# Test
print(kombinasi(5, 2))  # 10
print(kombinasi(6, 3))  # 20
print(kombinasi(4, 1))  # 4
