Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def check_password_strength(password):
...     """
...     Checks the strength of a password.
... 
...     Args:
...         password (str): The password to check.
... 
...     Returns:
...         int: A strength score between 0 and 5.
...     """
...     strength = 0
... 
...     # Check length
...     if len(password) >= 8:
...         strength += 1
... 
...     # Check for uppercase letters
...     if re.search(r"[A-Z]", password):
...         strength += 1
... 
...     # Check for lowercase letters
...     if re.search(r"[a-z]", password):
...         strength += 1
... 
...     # Check for numbers
...     if re.search(r"\d", password):
...         strength += 1
... 
...     # Check for special characters
...     if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
...         strength += 1
... 
...     return strength
... 
... def main():
...     password = input("Enter a password: ")
    strength = check_password_strength(password)

    print("Password strength:")
    if strength == 5:
        print("Very strong")
    elif strength >= 3:
        print("Strong")
    elif strength >= 2:
        print("Medium")
    else:
        print("Weak")

if __name__ == "__main__":
