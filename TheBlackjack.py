import random
import time
jack=10
queen=10
king=10
ace=11
finalscore = 0
stickortwist = "s"
def random_number_choice():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])
def random_suit_choice():
    return random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
def stick_twist_input():
    global stickortwist
    stickortwist = raw_input("stick (s) or twist (t)?")

def half_half():
    card1 = random_number_choice()
    card2 = random_number_choice()

    type1 = random_suit_choice()
    type2 = random_suit_choice()
    type3 = random_suit_choice()
    type4 = random_suit_choice()
    type5 = random_suit_choice()

    print "Your first card is ",card1, type1
    print "Your second card is",card2, type2
    global finalscore
    finalscore = card1+card2
    print "The total of the two is", finalscore
    if finalscore == 21:
        print "Wow, first time!"

    stick_twist_input()
    if stickortwist == "s":
        print"your final score is", finalscore
        return
    card3 = random_number_choice()
    print card3, type3
    finalscore = card1 + card2 + card3
    if finalscore > 21:
        time.sleep(1)
        print "Unlucky, you bust with", finalscore
        if card1 == 11 or card2 == 11 or card3 == 11:   #checking for an ace
            print "Oh wait no you didn't"
            finalscore = finalscore-10  #making an ace that is default an 11 into a 1 as the player is bust
            print "Your current total is: ",finalscore
    else:
        print finalscore

        stick_twist_input()
        if stickortwist == "s":
            print finalscore
            return
        card4 = random_number_choice()
        print card4, type4
        finalscore = card1 + card2 + card3 + card4
        if finalscore > 21:
            time.sleep(1)
            print "Unlucky, you bust with", finalscore
            if card1 == 11 or card2 == 11 or card3 == 11 or card4 ==11:
                print "Oh wait no you didn't, you got an ace!"
                finalscore = finalscore - 10
                print "Your current total is: ", finalscore
        return
        print "your final score is:",finalscore

        stick_twist_input()
        if stickortwist == "s":
            print "Your final score is: ", finalscore
            return
        card5 = random_number_choice()
        print card5, type5
        finalscore = card1 + card2 + card3 + card4 + card5
        if finalscore > 21:
            time.sleep(1)
            print "Unlucky, you bust with", finalscore
            if card1 == 11 or card2 == 11 or card3 == 11 or card4 == 11 or card5 ==11:
                print "Oh wait no you didn't, you got an ace!"
                finalscore = finalscore - 10
                print finalscore
        return
        print "your current score is:", finalscore

        stick_twist_input()
        if stickortwist == "s":
            print "Your final score is: ", finalscore
            return
        card6 = random_number_choice()
        print card6
        finalscore = card1 + card2 + card3 + card4 + card5 + card6
        if finalscore > 21:
            time.sleep(1)
            print"Unlucky, you bust with", finalscore
            if card1 == 11 or card2 == 11 or card3 == 11 or card4 == 11 or card5 == 11 or card6 ==11:
                print "Oh wait no you didn't, you got an ace!"
                finalscore = finalscore - 10
                print finalscore
        return
        print "your final score is:", finalscore
half_half()
if finalscore < 22:
    print "We'll have to see what player 2 gets!"
player1score = finalscore
print "-------------------------------------------------------------------------------------------------"
print "Player 2, now its your go!"
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

half_half()
if player1score > 21:
    print "Player 1 scored",player1score, "but was bust."
else:
    print "Player 1 scored",player1score
if finalscore > 21:
    print "Player 2 scored",finalscore, "but was bust."
else:
    print "Player 2 scored",finalscore
if player1score < 22:
    if player1score > finalscore:
        print "Player 1 wins!"
if finalscore < 22:
    if finalscore > player1score:
        print "Player 2 wins!"
if finalscore > 21:
    if player1score > 21:
        print "You both lose!"
elif player1score > 21:
    if finalscore > 21:
        print "You both lose!"
if finalscore < 22:
    if finalscore == player1score:
        print "It's a draw! Play again!"
