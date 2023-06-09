import random
import string
import argparse

# Define the arguments for the command line application
parser = argparse.ArgumentParser(description='Generate a random password')
parser.add_argument('length', type=int, help='Length of password')
parser.add_argument('--uppercase', action='store_true', help='Include uppercase letters')
parser.add_argument('--numbers', action='store_true', help='Include numbers')
parser.add_argument('--symbols', action='store_true', help='Include symbols')

# Parse the arguments
args = parser.parse_args()

# Define the character sets to be used in the password generation
lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
number_chars = string.digits
symbol_chars = string.punctuation

# Create the character set based on user input
chars = lowercase_chars
if args.uppercase:
    chars += uppercase_chars
if args.numbers:
    chars += number_chars
if args.symbols:
    chars += symbol_chars

# Generate the password
password = ''.join(random.choice(chars) for _ in range(args.length))

# Output the password to the terminal
print(password)
