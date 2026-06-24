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
5. Contains common weak word check      #Penalty if word in password is in WEAK_WORDS list
6. Length scoring                       #Add to Score
                                                8-11  = +1
                                                12-15 = +3
                                                16+   = +4
7. Lowercase check                      #Add to Score +1
8. Uppercase check                      #Add to Score +1
9. Number check                         #Add to Score +1
10. Special character check             #Add to Score +1
11. Repeating character penalty         #Penalty for >= 3 repeating characters
12. Sequential number penalty           #Penalty for >= 3 sequential numbers
13. Keyboard pattern penalty            #Penalty if pattern in password is in KEYBOARD_PATTERNS list
14. All-numeric penalty                 #Pass/Fail if < 16 == FAIL. Otherwise >= 16 == penalty)
15. Final strength rating               #0-2 = Weak
                                         3-5 = Average
                                         6-7 = Strong
                                         8   = Very Strong
""" 


from PasswordData import WEAK_WORDS, COMMON_PASSWORDS, KEYBOARD_PATTERNS

score = 0   #initial password strength score

# 1. Empty password check


# 2. Emoji / non-ASCII check
def contains_non_ascii(password):
    for char in password:
        value = ord(char)

        if value < 33 or value > 126:
            return True

    return False

# 3. Minimum length check


# 4. Common password check


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



# 15. Final strength rating
def check_strength(password):


    return score
