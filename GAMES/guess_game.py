# principle of single responsibility
    # husband and wife function will do only one task that is guessing their numbers

# husband function generates a random number for wife function to guess and also makes guesses
import random
hturns = 0
wturns = 0
hnum = 40
wnum = 78
wfound = False
hfound = False
newMinWife = 1
newMinHusband = 1;
newMaxWife = 100
newMaxHusband = 100;

def husband(Mini, Maxi):
    ''' This will guess it's number '''
    global hturns 
    hturns += 1
    return random.randint(Mini,Maxi)


def wife(Mini, Maxi):
    ''' This will guess it's number '''
    global wturns 
    wturns += 1
    return random.randint(Mini,Maxi)


def gameLoader():
    global wfound, hfound, newMinWife, newMaxWife, newMinHusband, newMaxHusband
    if(wfound==False):
        wguess = wife(newMinWife, newMaxWife)
        print(f'Guess by Wife : {wguess}')
        if(wguess == wnum):
            print('\n----FOUND----\nWife found her number\n')
            wfound=True
        else:
            if(wnum>wguess): newMinWife = wguess
            else: newMaxWife = wguess
    if(hfound==False):
        hguess = husband(newMinHusband,newMaxHusband)
        print(f'Guess by Husband : {hguess}')
        if(hguess==hnum): 
            print('\n----FOUND----\nHusband found his number\n')
            hfound=True
        else:
            if(hnum>hguess) : newMinHusband=hguess
            else: newMaxHusband = hguess
    
    if(hfound == False or wfound == False):
        gameLoader()
    else:
        print(f'Wife found her number in {wturns}')
        print(f'Husband found her number in {hturns}')

        if(wturns > hturns): 
            print('Husband won!!\nTook less no. of turns')
        elif(wturns < hturns):
            print('Wife won!!\nTook less no. of turns')
        else:
            print("It's a Tie")

print('--------------- GAME STARTS ---------------')
gameLoader()



