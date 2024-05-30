import random
list=['rock','paper','scissor']
count=1
while count>=1:
    print('rock\npaper\nscissor')
    user = input("Enter your choice: ")
    computer_choice=random.choice(list)
    if user not in list:
        print('Invalid input')
    else:
        print(f"computer choice: {computer_choice}")
        if computer_choice==user:
            print("It's a Tie")
        elif (user=='rock' and computer_choice=='scissor') or (user=='paper' and computer_choice=='rock') or (user=='scissor' and computer_choice=='paper'):
            print("You Won!")
        else:
            print("You Lost!")
        user2=input('Do you want to play again? (yes/no)')
        if user2=='yes':
            count=count+1
        else:
            print('Exited!')
            break