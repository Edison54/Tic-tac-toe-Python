##Edison CV##
#Milestone Project - 1#
#Make a tic tac toe wit lists!#
import random
Boardfinal = ['#','X','O','X','O','X','O','X','O','X']
def display_board(Board):
    
    print(Board[1]+'|'+Board[2]+'|'+Board[3]+'------'+'1'+'|'+'2'+'|'+'3')
    print(Board[4]+'|'+Board[5]+'|'+Board[6]+'------'+'4'+'|'+'5'+'|'+'6')
    print(Board[7]+'|'+Board[8]+'|'+Board[9]+'------'+'7'+'|'+'8'+'|'+'9')
       
    pass

def player_choose():
    
    choose= ''
    
    while choose != 'X' and choose != 'x' and choose != 'O'  and choose != 'o':
        choose = input('Player 1 , pleace choose X or O: ').upper()
        
  
    if choose =='X':
        return('X','O')
    else: 
       return('X','O')
    

        
 
def place_marker(Board, choose, position):
  
    Board[position] = choose 
   
 
  
def win(Board,choose):
    
    return ((Board[1] == choose and Board[2] == choose and Board[3] == choose ) or 
    (Board[4] == choose and Board[5] == choose and Board[6] == choose ) or
    (Board[7] == choose and Board[8] == choose and Board[9] == choose ) or
    (Board[1] == choose and Board[4] == choose and Board[7] == choose) or
    (Board[2] == choose and Board[5] == choose and Board[8] == choose) or
    (Board[3] == choose and Board[6] == choose and Board[9] == choose) or
    (Board[1] == choose and Board[5] == choose and Board[9] == choose) or
    (Board[7] == choose and Board[5] == choose and Board[3] == choose))
    
    
    pass
        
def choose_first():
    flip =random.randint(0,1)  
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'      
        
def check_spaces(Board , position):
    
    return Board[position] == ' '    
    
def full_spaces(Board):
    for a in range(1,10):
        if check_spaces(Board,a):
            return False
    return True
def player_choice(Board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not check_spaces(Board,position):
        position= int(input('Choose one position (1-9) '))
        
    return position

def replay():
  
    return  input("Want to play again? say yes or no " ).lower().startswith('y')



#Call all the defs!
print("Hi welcome to our tic tac toe game! ")

while True:
    
    #here que run the game
    Boardfinal = [' ']*10
    player1_marker,player2_marker = player_choose()
    
    turn = choose_first()
    
    print(turn+' You will go first!')
    
    play = input('Ready to play? Enter yes or no! ')
    
    if play.lower()[0] == 'y':
        game_on =True
    else:
        game_on =False
    
    while game_on:
        if  turn == 'Player 1':  
            
            display_board(Boardfinal)
            
            position = player_choice(Boardfinal)
            
            place_marker(Boardfinal,player1_marker,position)
            
            
            if win(Boardfinal,player1_marker):
                display_board(Boardfinal)
                print('Congratulations! player 1 you won! ')
                game_on= False
            else:
                if full_spaces(Boardfinal):
                    display_board(Boardfinal)
                    print("Its a tie!")
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(Boardfinal)
            
            position = player_choice(Boardfinal)
    
            place_marker(Boardfinal, player2_marker ,position)
            
            
            if win(Boardfinal,player2_marker):
                display_board(Boardfinal)
                print('Congratulations! player 2 you won! ')
                game_on = False
            else:
                if full_spaces(Boardfinal):
                    display_board(Boardfinal)
                    print("Its a tie!")
                    break
                else:
                    turn = 'Player 1'
           
        
    if not replay():
        break

