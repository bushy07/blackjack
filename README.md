# Black Jack written in Python
This is a simulation of a game of blackjack. It involves features such as choosing to pick up another card, deciding not to pick up a card and end your turn, (both using input). A winner is recognised and an ace being either a 1 or an 11 is there but doesn't work very well. 
I am hoping to simplify the code using functions and alter it so that the ace feature works properly.
Here is an example of the code:
```bash
python TheBlackjack.py 
Your first card is  8 of Spades
Your second card is 4 of Clubs
The total of the two is 12
stick (s) or twist (t)?t
10 of Spades
Unlucky, you bust with 22
-------------------------------------------------------------------------------------------------
Player 2, now its your go!
5...
4...
3...
2...
1...
Your first card is  2 of Spades
Your second card is 11 of Diamonds
The total of the two is 13
stick (s) or twist (t)?t
5 of Clubs
18
Would you like to stick (s) or twist (t)?s
18
Player 1 scored 22 but was bust.
Player 2 scored 18
```
 
When run, the code should randomise and print two random numbers and two random card suits. 
Next it should add up the two and print the current score. 
If you got an 11 and a 10 it will print ```"Wow, first time!"```
Then it will ask you whether you would like to stick or twist using:
```
stickortwist = raw_input("stick (s) or twist (t)?")
```
You should then type either "s" (meaning to stick and end your turn) or "t" (to twist and pick up another card)
"s" will result in the end of your turn: ```print ("your final score is", finalscore)``` finalscore being your total score.
If you input "t", it should randomise another card and output it.
This should be added to the score and if it is over 21 it will be the end of the turn. 

This process is repeated until you pick to stick or the total is over 21.
Then the code calculates who wins and prints it:
```
if player1score > 21:
    print "Player 1 scored",player1score, "but was bust."
else:
    print "Player 1 scored",player1score
if finalscore > 21:
    print "Player 2 scored",finalscore, "but was bust."
else:
    print "Player 2 scored",finalscore



if player1score < 21:
    if player1score > finalscore:
        print "Player 1 wins!"

if finalscore < 21:
    if finalscore > player1score:
        print "Player 2 wins!"

if finalscore > 21:
    if player1score > 21:
        print "You both lose!"
elif player1score > 21:
    if finalscore > 21:
        print "You both lose!"
```
