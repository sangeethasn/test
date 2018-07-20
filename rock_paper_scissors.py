import random
choices=['rock','paper','scissors']
#random.shuffle(choices)
#player1= choices[0]  #choice of system

chances=1            #to indicate the round of the game
player1_score=0
player2_score=0

while chances<11 :

 print 'Round' + str(chances)
 player2 = raw_input('Play')
 player1 = random.choice(choices)
 if player2 in choices:

   if (player1=='rock' and player2=='scissors') :
       player1_score += 1
   if (player1=='scissors' and player2=='paper'):
       player1_score += 1
   if (player1=='paper' and player2=='rock'):
       player1_score += 1
   else:
    player2_score += 1

    chances += 1
    print player1 + "   " + player2

    if   player1_score > player2_score:
         print ('You Lost')
    elif player1_score==player2_score:
          print 'Draw'
    else:
         print('You Won')

print 'Player1 score' + str(player1_score)
print 'Player2 score' + str(player2_score)

