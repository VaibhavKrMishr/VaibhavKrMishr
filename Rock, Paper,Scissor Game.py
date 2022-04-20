import random
while True: 
    user_action = input("Enter Your Option(Rock, Paper, Scissor):")
    possible_action = ['Rock', 'paper','Scissor']
    computer_action = random.choice(possible_action)
    print (f"\n Your choice: {user_action} :: Computer choice: {computer_action} \n" )

    if user_action == computer_action:
        print ("Both Player Selected {user_action}. It's a Tie! ")
    
    elif user_action == "Rock":
         if computer_action == "Scissor":
             print("You Win!")
         else:
             print("You Lose")
         
    elif user_action == "Scissor":
         if computer_action == "Paper":
             print("You Win!")
         else:
             print("You Lose")
         
    elif user_action == "Paper":
         if computer_action == "Rock":
             print("You Win!")
         else:
             print("You Lose")
             
    play_again =  input("Play Again? (Y/N):")
    if play_again.upper() == "y":
        break
    
