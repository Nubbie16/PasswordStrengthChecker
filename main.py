# Project Name: PasswordStrengthChecker
# Purpose: Program to check various aspects of a entered 
#       password to determine the quality of the password's security
# File Name: main.py
# Description: The main Python file
# Programmer: Cody Eckard
# Creation Date: 6/24/2026
# GitHub Repository: https://github.com/Nubbie16/PasswordStrengthChecker 

import string

def main():
    print("Program Start")

if __name__ == "__main__":
    main()

"""
Provide a "Strength Score that starts at 0

Priority List:
1. Empty password check
1.1 Emoji / non-ASCII check (func already created)
2. Minimum length check
3. Common password check
4. Contains common weak word check
5. Length scoring
6. Lowercase check
7. Uppercase check
8. Number check
9. Special character check
10. Repeating character penalty
11. Sequential number penalty
12. Keyboard pattern penalty
13. All-numeric penalty (< 16 == FAIL, >= 16 == penalty)
14. Final strength rating  

Common Passwords:
    AI generated "common" passwords to be flagged. Rule to flag entered password if any of the 
        COMMON_PASSWORDS is anywhere in the entered password 

                   
"""

WEAK_WORDS = {
    # Account/system words
    "password",
    "pass",
    "admin",
    "administrator",
    "root",
    "user",
    "guest",
    "login",
    "default",
    "test",

    # Common phrases
    "welcome",
    "letmein",
    "access",
    "unlock",
    "signin",
    "logmein",

    # Keyboard patterns
    "qwerty",
    "asdf",
    "zxcv",
    "qaz",
    "wsx",

    # Common emotional/simple words
    "love",
    "iloveyou",
    "secret",
    "master",
    "shadow",
    "sunshine",

    # Common pop culture / hobbies
    "football",
    "baseball",
    "soccer",
    "dragon",
    "monkey",
    "batman",
    "superman",
    "starwars",
    "pokemon"
}

COMMON_PASSWORDS = {
    "abc",
    "abcd",
    "abc123",
    "abc1234",
    "abc12345",
    "abc123456",
    "123abc",
    "a12345",
    "a123456",
    "hello",
    "hello123",

    "password1",
    "password12",
    "password123",
    "password1234",
    "password12345",
    "password!",
    "password!!",
    "password123!",
    "p@ssword",
    "p@ssword1",
    "p@ssword123",

    "admin1",
    "admin12",
    "admin123",
    "admin1234",
    "admin!",
    "admin@123",
    "user1",
    "user123",
    "guest123",
    "welcome1",
    "welcome123",
    "letmein1",
    "letmein123",

    "summer123",
    "winter123",
    "spring123",
    "fall123",
    "january123",
    "june123",
    "july123",
    "money123",
    "family123",
    "friend123",
    "school123",
    "college123",
    "computer123",
    "internet123",
    "coffee123",
    "cookie123",
    "flower123",
    "princess123",
    "whatever123"
}

KEYBOARD_PATTERNS = {
    # Left-to-right keyboard rows
    "qwerty",
    "qwertyuiop",
    "asdf",
    "asdfgh",
    "asdfghjkl",
    "zxcv",
    "zxcvbn",

    # Common keyboard + number patterns
    "qwerty123",
    "asdf123",
    "zxcv123",

    # Vertical / diagonal keyboard patterns
    "1q2w3e4r",
    "1qaz2wsx",
    "qazwsx",
    "zaq12wsx",
    "2wsx3edc",

    # Reverse/simple variants
    "ytrewq",
    "poiuy",
    "lkjhg",
    "mnbvc"
}
# 
# 
# 
#    

def contains_non_ascii(password):   #Blocks spaces and all non-standard keyboard characters
    for char in password:
        value = ord(char)

        if value < 33 or value > 126:
            return True

    return False

