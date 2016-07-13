import random
import time
jack=10
queen=10
king=10
ace=11


card1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])
card2 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])

type1 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type2 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type3 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type4 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type5 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])

print "Your first card is ",card1, type1

print "Your second card is",card2, type2

finalscore = card1+card2

print "The total of the two is", finalscore
if finalscore == 21:
    print "Wow, first time!"
stickortwist = raw_input("stick (s) or twist (t)?")

if stickortwist == "s":
    print"your final score is", finalscore
else:
    card3 = random.choice([2,3,4,5,6,7,8,9,10,jack,queen,king,ace])
    print card3, type3
    finalscore = card1 + card2 + card3
    if finalscore > 21:
        print "Unlucky, you bust with", finalscore
        if card1 == 11 or card2 == 11 or card3 == 11:   #checking for an ace
            if finalscore>21:
                print "Oh wait no you didn't"
                finalscore = finalscore-10  #making an ace that is default an 11 into a 1 as the player is bust
                print "Your current total is: ",finalscore
    else:
        print finalscore

        stickortwist = raw_input("Would you like to stick (s) or twist (t)?")

        if stickortwist == "s":
            print finalscore
        else:
            card4 = random.choice([2,3,4,5,6,7,8,9,10,jack,queen,king,ace])
            print card4, type4
            finalscore = card1 + card2 + card3 + card4
            if finalscore > 21:
                print "Unlucky, you bust with", finalscore
                if finalscore > 21:
                    if card1 == 11 or card2 == 11 or card3 == 11 or card4 ==11:
                        print "Oh wait no you didn't, you got an ace!"
                        finalscore = finalscore - 10
                        print "Your current total is: ", finalscore
            else:
                print "your final score is:",finalscore

                stickortwist = raw_input("Would you like to stick (s) or twist (t)?")

                if stickortwist == "s":
                    print "Your final score is: ", finalscore
                else:
                    card5 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])
                    print card5, type5
                    finalscore = card1 + card2 + card3 + card4 + card5
                    if finalscore > 21:
                        print "Unlucky, you bust with", finalscore
                        if finalscore > 21:
                            if card1 == 11 or card2 == 11 or card3 == 11 or card4 == 11 or card5 ==11:
                                print "Oh wait no you didn't, you got an ace!"
                                finalscore = finalscore - 10
                                print finalscore
                        else:
                            print "your current score is:", finalscore

                            stickortwist = raw_input("Would you like to stick (s) or twist (t)?")

                            if stickortwist == "s":
                                    print "Your final score is: ", finalscore
                            else:
                                card6 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])
                                print card6
                                finalscore = card1 + card2 + card3 + card4 + card5 + card6
                                if finalscore > 21:
                                    print"Unlucky, you bust with", finalscore
                                    if finalscore > 21:
                                        if card1 == 11 or card2 == 11 or card3 == 11 or card4 == 11 or card5 == 11 or card6 ==11:
                                            print "Oh wait no you didn't, you got an ace!"
                                            finalscore = finalscore - 10
                                            print finalscore
                                else:
                                    print "your final score is:", finalscore



if finalscore < 22:
    print "We'll have to see what player 2 gets!"
player1score = finalscore
print "-------------------------------------------------------------------------------------------------"
print "Player 2, now its your go!"
print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")


card1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])
card2 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])

type1 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type2 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type3 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type4 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])
type5 = random.choice(["of Hearts", "of Diamonds", "of Spades", "of Clubs"])

print "Your first card is ",card1, type1
time.sleep(1)
print "Your second card is",card2, type2

finalscore = card1+card2
time.sleep(1)
print "The total of the two is", finalscore
if finalscore == 21:
    print "Wow, first time!"
stickortwist = raw_input("stick (s) or twist (t)?")

if stickortwist == "s":
    print "your final score is", finalscore
else:
    card3 = random.choice([2,3,4,5,6,7,8,9,10,jack,queen,king,ace])
    print card3, type3
    finalscore = card1 + card2 + card3
    if finalscore > 21:
        print"Unlucky, you bust with", finalscore
        if card1 == 11 or card2 == 11 or card3 == 11:   #checking for an ace
            if finalscore>21:
                print "Oh wait no you didn't"
                finalscore = finalscore-10  #making an ace that is default an 11 into a 1 as the player is bust
                print "Your current total is: ",finalscore
    else:
        print finalscore

        stickortwist = raw_input("Would you like to stick (s) or twist (t)?")

        if stickortwist == "s":
            print finalscore
        else:
            card4 = random.choice([2,3,4,5,6,7,8,9,10,jack,queen,king,ace])
            print card4, type4
            finalscore = card1 + card2 + card3 + card4
            if finalscore > 21:
                print"Unlucky, you bust with", finalscore
                if finalscore > 21:
                    if card1 == 11 or card2 == 11 or card3 == 11 or card4 ==11:
                        print"Oh wait no you didn't, you got an ace!"
                        finalscore = finalscore - 10
                        print "Your current total is: ", finalscore
            else:
                print "your final score is:",finalscore

                stickortwist = raw_input("Would you like to stick (s) or twist (t)?")

                if stickortwist == "s":
                    print "Your final score is: ", finalscore
                else:
                    card5 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])
                    print card5, type5
                    finalscore = card1 + card2 + card3 + card4 + card5
                    if finalscore > 21:
                        print"Unlucky, you bust with", finalscore
                        if finalscore > 21:
                            if card1 == 11 or card2 == 11 or card3 == 11 or card4 == 11 or card5 ==11:
                                print"Oh wait no you didn't, you got an ace!"
                                finalscore = finalscore - 10
                                print finalscore
                        else:
                            print "your current score is:", finalscore

                            stickortwist = raw_input("Would you like to stick (s) or twist (t)?")

                            if stickortwist == "s":
                                    print "Your final score is: ", finalscore
                            else:
                                card6 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace])
                                print card6
                                finalscore = card1 + card2 + card3 + card4 + card5 + card6
                                if finalscore > 21:
                                    print"Unlucky, you bust with", finalscore
                                    if finalscore > 21:
                                        if card1 == 11 or card2 == 11 or card3 == 11 or card4 == 11 or card5 == 11 or card6 ==11:
                                            print"Oh wait no you didn't, you got an ace!"
                                            finalscore = finalscore - 10
                                            print finalscore
                                else:
                                    print "your final score is:", finalscore


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

