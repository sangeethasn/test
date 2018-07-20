import random

answerlist = ['world', 'look', 'hello', 'goodbye']
random.shuffle(answerlist)
answer = list(answerlist[0])
display = ['_' for _ in answer]
print display
AllowedGuesses=10
count = 0
while (AllowedGuesses != 0 and count < len(answer)):
    print 'You have ' + str(AllowedGuesses) + ' guesses left'
    guess = raw_input('Please guess a letter: ')
    guess = guess.lower()
    for val in range(len(answer)):
        if answer[val] == guess:
            display[val] = guess
            print str(display)
            count += 1
    if(guess not in answer) :
      print ('Wrong guess')
    AllowedGuesses -= 1
    if  ('_' not in display ):
     print 'you won'
     break
if(AllowedGuesses <= 0 ):
  print 'You lost'





