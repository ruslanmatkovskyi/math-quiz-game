from random import randint

correct = 0

while True:
    isalpha = False
    print("Mathematic game!")
    print(f"Correct answers: {correct}")
    
    print("\nSelect difficulty:")
    difficulty = int(input("\n1. Easy\n2. Medium\n3. Hard\n4. Exit game"))


    if isalpha == True:
        print("Input must be a number! Restarting...")
        continue


    match difficulty:
        case 1:
            while True:
                num1 = randint(1, 5)
                num2 = randint(1, 10)
                
                result = num1 * num2
                answer = int(input(f"{num1} x {num2} = "))

                for i in answer:
                    if i.isalpha == True:
                        isalpha = True

                if isalpha == True:
                    print("Input must be a number! Restarting...\n")
                    continue

                if answer == result:
                    correct += 1
                
                    print("Correct! Wanna try another one?: ")
                    choice = int(input("1. Yes\n2. To the main menu\n"))
                    match choice:
                        case 2:
                            break
                        case 1:
                            continue
                        case _:
                            print("Wrong answer! Restarting...")
                            continue
                else:
                    print("Incorrect! Wanna try another one?")
                    choice = int(input("1. Yes\n2. Quit to the main menu"))
                    if choice == 1:
                        continue
                    else:
                        break
        case 2:
            while True:
                num1 = randint(4, 12)
                num2 = randint(1, 15)

                result = num1 * num2
                answer = int(input(f"{num1} x {num2} = "))
                if answer == result:
                    correct += 1
                                
                    print("Correct! Wanna try another one?: ")
                    choice = int(input("1. Yes\n2. To the main menu\n"))
                    match choice:
                        case 2:
                            break
                        case 1:
                            continue
                else:
                    print("Incorrect! Wanna try another one?")
                    choice = int(input("1. Yes\n2. Quit to the main menu"))
                    if choice == 1:
                        continue
                    else:
                        break
        case 3:
            while True:
                num1 = randint(4, 25)
                num2 = randint(1, 35)
            
                result = num1 * num2
                answer = int(input(f"{num1} x {num2} = "))
                if answer == result:
                    correct += 1
                                    
                    print("Correct! Wanna try another one?: ")
                    choice = int(input("1. Yes\n2. To the main menu\n"))
                    match choice:
                        case 2:
                            break
                        case 1:
                            continue
                else:
                    print("Incorrect! Wanna try another one?")
                    choice = int(input("1. Yes\n2. Quit to the main menu"))
                    if choice == 1:
                        continue
                    else:
                        break
    if difficulty == 4:
        break

