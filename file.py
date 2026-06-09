import random
import string

print("Password Generator")

length = 8
chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for i in range(length))

print("Generated:", password)