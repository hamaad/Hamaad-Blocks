# Hamaad Markhiani
# cPickle highScore interactive editing system
# Today's a beautiful day...yay.
# Go!
# 

import cPickle

print 'Hello! Welcome to the Ham-Blocks System_Files editor!'
option = raw_input("Would you like to\n1:Edit Names\n2:Edit Numbers\n:")
if (option == "1"):
    file = open("System_Files\\sound.hamaad","r")
    highScoreName = cPickle.load(file)
    print highScoreName
    file.close();
    
    secOption = raw_input("Which name would you like to edit?\n")
    if (secOption == "1"):
        thirdOption = raw_input("To what?\n")
        file = open("System_Files\\sound.hamaad","w")
        highScoreName[0] = thirdOption
        cPickle.dump(highScoreName, file)
        print 'Done.'
        file.close();
    elif (secOption == "2"):
        thirdOption = raw_input("To what?\n")
        file = open("System_Files\\sound.hamaad","w")
        highScoreName[1] = thirdOption
        cPickle.dump(highScoreName, file)
        print 'Done.'
        file.close();
    elif (secOption == "3"):
        thirdOption = raw_input("To what?\n")
        file = open("System_Files\\sound.hamaad","w")
        highScoreName[2] = thirdOption
        cPickle.dump(highScoreName, file)
        print 'Done.'
        file.close();
    elif (secOption == "4"):
        thirdOption = raw_input("To what?\n")
        file = open("System_Files\\sound.hamaad","w")
        highScoreName[3] = thirdOption
        cPickle.dump(highScoreName, file)
        print 'Done.'
        file.close();
    elif (secOption == "5"):
        thirdOption = raw_input("To what?\n")
        file = open("System_Files\\sound.hamaad","w")
        highScoreName[4] = thirdOption
        cPickle.dump(highScoreName, file)
        print 'Done.'
        file.close();
    else:
        print 'nope.'
    
    
elif (option == "2"):
    file = open("System_Files\\font.hamaad","r")
    highScore = cPickle.load(file)
    print highScore
    file.close();
    
    secOption = raw_input("Which high score would you like to edit?\n")
    if (secOption == "1"):
        thirdOption = input("To what?\n")
        file = open("System_Files\\font.hamaad","w")
        highScore[0] = thirdOption
        cPickle.dump(highScore, file)
        print 'Done.'
        file.close();
    elif (secOption == "2"):
        thirdOption = input("To what?\n")
        file = open("System_Files\\font.hamaad","w")
        highScore[1] = thirdOption
        cPickle.dump(highScore, file)
        print 'Done.'
        file.close();
    elif (secOption == "3"):
        thirdOption = input("To what?\n")
        file = open("System_Files\\font.hamaad","w")
        highScore[2] = thirdOption
        cPickle.dump(highScore, file)
        print 'Done.'
        file.close();
    elif (secOption == "4"):
        thirdOption = input("To what?\n")
        file = open("System_Files\\font.hamaad","w")
        highScore[3] = thirdOption
        cPickle.dump(highScore, file)
        print 'Done.'
        file.close();
    elif (secOption == "5"):
        thirdOption = input("To what?\n")
        file = open("System_Files\\font.hamaad","w")
        highScore[4] = thirdOption
        cPickle.dump(highScore, file)
        print 'Done.'
        file.close();
    else:
        print 'nope.'
else:
    print 'nope.'
