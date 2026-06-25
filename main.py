# Project Name: PasswordStrengthChecker
# Purpose: Program to check various aspects of a entered 
#       password to determine the quality of the password's security
# File Name: main.py
# Description: The main Python file
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

import CheckLogic
import getpass

def main():
    print("Program Start")

    while True:
        pswd = getpass.getpass("\nPlease enter password, or type X to exit: ")

        if pswd.strip().lower() == "x":
            print("Program ended.")
            break

        score, reason = CheckLogic.check_strength(pswd)

        if score == -1:
            print("Password failed required checks.")
            print(f"Reason: {reason}")
        else:
            strength = CheckLogic.get_strength(score)

            print(f"Score: {score}")
            print(f"Strength: {strength}")


if __name__ == "__main__":
    main()

 

