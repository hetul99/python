import random
def Rock_Paper_Scissor():
    player_1 = int(input("Player 1 : Enter your input(Rock - 1, Paper - 2", "Scissor - 3)"))
    player_2 = random.randint(1,3)
    print(player_2)

    if(player_1==player_2):
        print("Draw")

    elif(player_1 == '1' and player_2 == '2'):
        print("Player 2 won")

    elif(player_1 == '1' and player_2 == '3'):
        print("Player 1 won")

    
    elif(player_1 == '2' and player_2 == '1'):
        print("Player 1 won")

    
    elif(player_1 == '2' and player_2 == '3'):
        print("Player 2 won")

    
    elif(player_1 == '3' and player_2 == '1'):
        print("Player 2 won")

    
    elif(player_1 == '3' and player_2 == '2'):
        print("Player 1 won")

    else:
        print("Please enter proper input")
#my_input = int(input("Player 1 : Enter your input(Rock - 1, Paper - 2, Scissor - 3)"))
Rock_Paper_Scissor()


