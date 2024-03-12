# Programming: LaDanien
# Date: 3.12.2024
# Program: Password Generator
# Resources: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import os


def hash_password(password, salt):
    # Combine password and salt
    salted_password = password.encode() + salt.encode()

    # Hash the combined string using SHA-256 algorithm
    hashed_password = hashlib.sha256(salted_password).hexdigest()

    return hashed_password


def generate_salt():
    # Generate a random salt
    return os.urandom(16).hex()


def main():
    # Accept password input from user
    password = input("Enter your password: ")

    # Generate a salt
    salt = generate_salt()

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed Password:", hashed_password)


if __name__ == "__main__":
    main()
