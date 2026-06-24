# Project Name: PasswordStrengthChecker
# Purpose: Program to check various aspects of a entered 
#       password to determine the quality of the password's security
# File Name: CheckLogic.py
# Description: File contains all check functions and logic to test password strength
# Programmer: Cody Eckard
# Creation Date: 6/24/2026
# GitHub Repository: https://github.com/Nubbie16/PasswordStrengthChecker 

"""
Rule List:
1. Empty password check                 #Pass/Fail
2. Emoji / non-ASCII check              #Pass/Fail
3. Minimum length check                 #Pass/Fail < 8
4. Common password check                #Pass/Fail for EXACT password in COMMON_PASSWORDS list 
5. Contains common weak word check      #Penalty if word in password is in WEAK_WORDS list  -2
6. Length scoring                       #Add to Score
                                                8-11  = +1
                                                12-15 = +3
                                                16+   = +4
7. Lowercase check                      #Add to Score +1
8. Uppercase check                      #Add to Score +1
9. Number check                         #Add to Score +1
10. Special character check             #Add to Score +1
11. Repeating character penalty         #Penalty for >= 3 repeating characters  -1
12. Sequential number penalty           #Penalty for >= 3 sequential numbers    -1
13. Keyboard pattern penalty            #Penalty if pattern in password is in KEYBOARD_PATTERNS list    -2
14. All-numeric penalty                 #Pass/Fail if < 16 == FAIL. Otherwise >= 16 == penalty) -2
15/16. Final score/strength rating      #0-2 = Weak
                                         3-5 = Average
                                         6-7 = Strong
                                         8   = Very Strong
""" 


from PasswordData import WEAK_WORDS, COMMON_PASSWORDS, KEYBOARD_PATTERNS
import re

# 1. Empty password check               # Pass/Fail
def is_filled(password):
    return password.strip() != ""       #returns the condition directly, simplifing the if statement

# 2. Emoji / non-ASCII check            # Pass/Fail
def contains_only_ascii(password):
    for char in password:
        value = ord(char)

        if value < 33 or value > 126:
            return False
    return True

# 3. Minimum length check               # Pass/Fail
def meets_min_length(password):
    return len(password) >= 8

# 4. Common password check              # Pass/Fail
def not_common(password):
    for common in COMMON_PASSWORDS:
        if common == True:
            return False
    return True

# 5. Contains common weak word check    # -2
def contains_weak_PEN(password):
    for weak in WEAK_WORDS:
        if weak in password:
            return -2
    return 0

# 6. Length scoring                     # 8-11 = +1       12-15 = +3       16 or more = +4
def length_score(password):
    length = len(password)

    if length >= 8 and length < 12:
        return 1
    elif length <= 15:
        return 3
    elif length > 15:
        return 4

# 7. Lowercase check                    # +1
def has_lowercase_score(password):
    if any(char.islower() for char in password):
        return 1
    else:
        return 0

# 8. Uppercase check                    # +1
def has_uppercase_score(password):
    if any(char.isupper() for char in password):
        return 1
    else:
        return 0

# 9. Number check                       # +1
def has_number_score(password):
    if any(char.isdigit() for char in password):
        return 1
    else:
        return 0

# 10. Special character check           # +1
def has_special_score(password):

    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    if any(char in special_chars for char in password):
        return 1
    else:
        return 0

# 11. Repeating character penalty       # -1
def repeating_chars_PEN(password):

    if re.search(r"(.)\1{2,}", password) is not None:
        return 1
    else:
        return 0

# 12. Sequential number penalty         # -1
def seq_number_PEN(password):
    ascending = "0123456789"
    descending = "9876543210"

    for i in range(len(ascending) - 2):
        seq = ascending[i:i + 3]

        if seq in password:
            return 1

    for i in range(len(descending) - 2):
        seq = descending[i:i + 3]
        
        if seq in password:
            return 1

    return 0

# 13. Keyboard pattern penalty          # -2
def contains_key_pattern_PEN(password):
    for key in KEYBOARD_PATTERNS:
        if key in password:
            return -2
    return 0

# 14. All-numeric penalty (< 16 == FAIL, >= 16 == penalty)      # Pass/Fail or -2
def all_nums_length_PEN(password):
    if meets_min_length(password) == False:
        return -1
    
    for char in password:
        value = ord(char)
        if value < 48 or value > 57:
            return -1
        else:
            if len(password) < 16:
                return 2
    return 0

PASS_FAIL_FUNCS = [
    is_filled,               # 1. Empty password check
    contains_only_ascii,     # 2. Emoji / non-ASCII check
    meets_min_length,        # 3. Minimum length check
    not_common               # 4. Common password check
]

def pass_fail_check(password):         # 1.-4. will return False immediately w/o any additional checks 
    
        for check in PASS_FAIL_FUNCS:
            if check(password) != True:
                return False    # checks did not pass. password failed
        return True     
    
# 15. Determines final score
def check_strength(password):

    if pass_fail_check(password) == False:
        return -1
    



    # 5. Contains common weak word check
    # 6. Length scoring
    # 7. Lowercase check
    # 8. Uppercase check
    # 9. Number check
    # 10. Special character check
    # 11. Repeating character penalty
    # 12. Sequential number penalty
    # 13. Keyboard pattern penalty
    # 14. All-numeric penalty (< 16 == FAIL, >= 16 == penalty)
    score = 5   #TEST DATA
    return score


# 16. Final strength rating
def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 5:
        return "Average"
    elif score < 8:
        return "Strong"
    else:
        return "Very Strong"


