import random 
def get_word ():
    words = []
    infile= open("D:\Hangman Words.txt", "r")
    
    for line in infile.readlines():
        words.append(line.strip())    
    return random.choice(words).upper()

def check(word, guesses, guess):
    status = ''
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += ' _'
        if letter  == guess:
            matches += 1
            
    if matches > 1:
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print ( "Yes the word contains", matches , "'" + guess + "'" + "s")
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    elif matches == 1:
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print ( "Yes the word contains " + guess + "'")
        print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    else:
        print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print ( " Sorry the word doesnt contains " + guess + "'")
        print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')       
    return status

def main():
    done = False
    while not done:
        word = get_word ()
        guesses = []
        guessed = False
        incorrect = 0
        print ( '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        user_name = input ("Enter player name: ")
        print ( '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ( "Hey ", user_name, ", Lets play Hangman ")
        print ( '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ( 'The word contains ', len(word) , 'letters')
        print ( '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'    )
        while (not guessed) and (incorrect < 5):
            
            guess = input('Please enter one letter ')
            guess = guess.upper()
            
            if guess in guesses:
                
                print ( 'You already guessed ' + guess + "'")
            elif len(guess) == len(word):
                guesses.append(guess)
                if guess == word:
                    guessed = True
                else:
                    incorrect += 1                
                    print ( "Sorry, that is incorrect")
                    
            elif len(guess) == 1:
                guesses.append(guess)
                result = check(word, guesses, guess)
                if result == word:
                    guessed = True
                    
                if guess not in word:
                    incorrect += 1
                    print ( "****Trials used(out of 5) : ", + incorrect , "Trial"  )              
                    
                else:
                    print ( (result))
            else:
                print ( "Invalid Entry")
                
        if guessed == True:
            print ('Yes the word is' ,   word +  ", Congratulations ")
            play_again = input("Do you Want to play again (yes/no) : ")
            if play_again == "YES" or play_again == "yes" :
                print ( "Letssssss Goooo....."     )           
                done = False
            else:   
                print ( "See you Later"             )   
                break
        else:
            print ( "You lost, the word was",   word +  ", Better luck nextime!")
            play_again = input("Do you Want to play again (yes/no) : ")
            if play_again == "NO" or play_again == "no" :
                print ( "See you Later")
                break
            else:
                print ( "Letssssss Goooo.....")
                done = False
                
main()


