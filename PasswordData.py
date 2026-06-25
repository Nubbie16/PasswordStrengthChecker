# Project Name: PasswordStrengthChecker
# Purpose: Program to check various aspects of a entered 
#       password to determine the quality of the password's security
# File Name: PasswordData.py
# Description: File contains all lists of flagged and blocked common passwords and sequences
# Programmer: Cody Eckard
# Creation Date: 6/24/2026
# GitHub Repository: https://github.com/Nubbie16/PasswordStrengthChecker 


# AI generated lists to be flagged/auto failed.


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

    "password",
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

KEYBOARD_PATTERNS = {
    # Left-to-right keyboard rows
    "qwerty",
    "qwertyuiop",
    "asdf",
    "asdfgh",
    "asdfghjkl",
    "zxcv",
    "zxcvbn",
    "qaz",
    "wsx",

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