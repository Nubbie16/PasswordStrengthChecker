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

   #initial password strength score



# 1. Empty password check
def is_filled(password):
    return password.strip() != ""       #returns the condition directly, simplifing the if statement

# 2. Emoji / non-ASCII check
def contains_only_ascii(password):
    for char in password:
        value = ord(char)

        if value < 33 or value > 126:
            return False
    return True

# 3. Minimum length check
def meets_min_length(password):
    return len(password) >= 8

# 4. Common password check
def not_common(password):
    for common in COMMON_PASSWORDS:
        if common == True:
            return False
    return True

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
def all_nums_length(password):
    if meets_min_length(password) == False:
        return -1
    
    for char in password:
        value = ord(char)
        if value < 48 or value > 57:
            return -1
        else:
            if len(password) < 16:
                return 
        

    return True



PASS_FAIL_FUNCS = [
    is_filled,               # 1. Empty password check
    contains_only_ascii,     # 2. Emoji / non-ASCII check
    meets_min_length,        # 3. Minimum length check
    not_common,              # 4. Common password check
    
]

def pass_fail_check(password):         # 1.-4. will return False immediately w/o any additional checks 
    
        for check in PASS_FAIL_FUNCS:
            if check(password) == True:
                return False
            
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


