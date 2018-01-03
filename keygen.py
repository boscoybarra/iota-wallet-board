import string
import random
import secrets

# Code
alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = (''.join(random.SystemRandom().choice(alphabet) for _ in range(81)))

# Print your random crypto pass for your IOTA Seed
print(x)

# Check that it has 81 characters for strong password. More characters does not make it more secure.
print(len(x))
