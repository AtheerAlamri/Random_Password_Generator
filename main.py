import string
import random


def randompassword():
    string_punctuation = "@#$%^&_-"
    chars = string.ascii_letters + string.digits + string_punctuation
    size = 3
    return ''.join(random.choice(chars) for x in range(size, 12))


n = 0
while n < 10:
    print(randompassword())
    n += 1
