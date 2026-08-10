print("Scramble project!")
print("There will be six jumbled words, pick one!")
print("1. Each jumbled word will make 3 words!")
print("2. When ur typing in an unscrambled word, use only small letters or it causes errors!")
print("3. Lastly, if u enter an incorrect word, just to make it harder, RESTART.")
choice = input("Choose from ARTP, ERAD, WOLEB, ARBED, ESATT or EATS!: ")
play = True
attempt = 1

while play:
    if choice == "ARTP" or choice == "artp" or choice == "Artp":
        print(f"Attempt {attempt}")
        first = input("Okay! Unscramble and type in da first word!: ")
        if first == "part" or first == "trap" or first == "tarp":
            word = first
            second = input("Correct! Second word!: ")
            if second == "part" or second == "trap" or second == "tarp":
                word1 = second
                if second == word:
                    print("Don't enter wot u entered already again! Restart!")
                    attempt += 1
                else:
                    third = input("Correct! Enter da last word!: ")
                    if third == "part" or third == "trap" or third == "tarp":
                        if third == word1:
                            print("Oh oh! U entered something dat u have already entered! Restart!")
                            attempt += 1
                        else:
                            print("Correct! U win!")
                            if attempt == 1:
                                print("It took u 1 attempt!")
                            else:
                                print(f"It took u {attempt} attempts!")
                            break
                    else:
                        print("Dat iz not a word! Restart!")
                        attempt += 1
            else:
                print("Dat iz not a word! Restart!")
                attempt += 1
        else:
            print("Dat iz not a word! Restart!")
            attempt += 1

    elif choice == "ERAD" or choice == "erad" or choice == "Erad":
        print(f"Attempt {attempt}")
        first = input("Okay! Unscramble and type in da first word!: ")
        if first == "dare" or first == "dear" or first == "read":
            word = first
            second = input("Correct! Second word!: ")
            if second == "dare" or second == "dear" or second == "read":
                word1 = second
                if second == word:
                    print("Don't enter wot u entered already again! Restart!")
                    attempt += 1
                else:
                    third = input("Correct! Enter da last word!: ")
                    if third == "dare" or third == "dear" or third == "read":
                        if third == word1:
                            print("Oh oh! U entered something dat u have already entered! Restart!")
                            attempt += 1
                        else:
                            print("Correct! U win!")
                            if attempt == 1:
                                print("It took u 1 attempt!")
                            else:
                                print(f"It took u {attempt} attempts!")
                            break
                    else:
                        print("Dat iz not a word! Restart!")
                        attempt += 1
            else:
                print("Dat iz not a word! Restart!")
                attempt += 1
        else:
            print("Dat iz not a word! Restart!")
            attempt += 1

    elif choice == "WOLEB" or choice == "woleb" or choice == "Woleb":
        print(f"Attempt {attempt}")
        first = input("Okay! Unscramble and type in da first word!: ")
        if first == "below" or first == "elbow" or first == "bowel":
            word = first
            second = input("Correct! Second word!: ")
            if second == "below" or second == "elbow" or second == "bowel":
                word1 = second
                if second == word:
                    print("Don't enter wot u entered already again! Restart!")
                    attempt += 1
                else:
                    third = input("Correct! Enter da last word!: ")
                    if third == "below" or third == "elbow" or third == "bowel":
                        if third == word1:
                            print("Oh oh! U entered something dat u have already entered! Restart!")
                            attempt += 1
                        else:
                            print("Correct! U win!")
                            if attempt == 1:
                                print("It took u 1 attempt!")
                            else:
                                print(f"It took u {attempt} attempts!")
                            break
                    else:
                        print("Dat iz not a word! Restart!")
                        attempt += 1
            else:
                print("Dat iz not a word! Restart!")
                attempt += 1
        else:
            print("Dat iz not a word! Restart!")
            attempt += 1

    elif choice == "ARBED" or choice == "arbed" or choice == "Arbed":
        print(f"Attempt {attempt}")
        first = input("Okay! Unscramble and type in da first word!: ")
        if first == "bared" or first == "beard" or first == "bread":
            word = first
            second = input("Correct! Second word!: ")
            if second == "bared" or second == "beard" or second == "bread":
                word1 = second
                if second == word:
                    print("Don't enter wot u entered already again! Restart!")
                    attempt += 1
                else:
                    third = input("Correct! Enter da last word!: ")
                    if third == "bared" or third == "beard" or third == "bread":
                        if third == word1:
                            print("Oh oh! U entered something dat u have already entered! Restart!")
                            attempt += 1
                        else:
                            print("Correct! U win!")
                            if attempt == 1:
                                print("It took u 1 attempt!")
                            else:
                                print(f"It took u {attempt} attempts!")
                            break
                    else:
                        print("Dat iz not a word! Restart!")
                        attempt += 1
            else:
                print("Dat iz not a word! Restart!")
                attempt += 1
        else:
            print("Dat iz not a word! Restart!")
            attempt += 1

    elif choice == "ESATT" or choice == "esatt" or choice == "esatt":
        print(f"Attempt {attempt}")
        first = input("Okay! Unscramble and type in da first word!: ")
        if first == "state" or first == "taste" or first == "teats":
            word = first
            second = input("Correct! Second word!: ")
            if second == "state" or second == "taste" or second == "teats":
                word1 = second
                if second == word:
                    print("Don't enter wot u entered already again! Restart!")
                    attempt += 1
                else:
                    third = input("Correct! Enter da last word!: ")
                    if third == "state" or third == "taste" or third == "teats":
                        if third == word1:
                            print("Oh oh! U entered something dat u have already entered! Restart!")
                            attempt += 1
                        else:
                            print("Correct! U win!")
                            if attempt == 1:
                                print("It took u 1 attempt!")
                            else:
                                print(f"It took u {attempt} attempts!")
                            break
                    else:
                        print("Dat iz not a word! Restart!")
                        attempt += 1
            else:
                print("Dat iz not a word! Restart!")
                attempt += 1
        else:
            print("Dat iz not a word! Restart!")
            attempt += 1

    elif choice == "EATS" or choice == "eats" or choice == "Eats":
        print(f"Attempt {attempt}")
        first = input("Okay! Unscramble and type in da first word!: ")
        if first == "seat" or first == "east" or first == "sate":
            word = first
            second = input("Correct! Second word!: ")
            if second == "seat" or second == "east" or second == "sate":
                word1 = second
                if second == word:
                    print("Don't enter wot u entered already again! Restart!")
                    attempt += 1
                else:
                    third = input("Correct! Enter da last word!: ")
                    if third == "seat" or third == "east" or third == "sate":
                        if third == word1:
                            print("Oh oh! U entered something dat u have already entered! Restart!")
                            attempt += 1
                        else:
                            print("Correct! U win!")
                            if attempt == 1:
                                print("It took u 1 attempt!")
                            else:
                                print(f"It took u {attempt} attempts!")
                            break
                    else:
                        print("Dat iz not a word! Restart!")
                        attempt += 1
            else:
                print("Dat iz not a word! Restart!")
                attempt += 1
        else:
            print("Dat iz not a word! Restart!")
            attempt += 1
