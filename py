
# Online Python - IDE, Editor, Compiler, Interpreter

a = [ "oversimplifying", "yield", "words", "to", "iterate", "void "," "," "," "]

def get_letter(i):

    result = ""

    while i > 0:

        for x in a:

            for y in x:

                #print(str(i) + " - " + y)

                i-=1

                if i == 0:

                    return y

               

def print_w(word):

    s = "";

    for letter in word:

        s += letter + " "

    print(s)

   

def do_guess(guessedWord, wordToFind, guess):

    for idx, letter in enumerate(wordToFind):

        if(letter == guess):

            guessedWord[idx] = guess

for x in a:

    print(x)

   

values = [ 97, 145, 195, 203, 198, 19, 16, 11, 26,  ]

guessedWord = [ "_", "_", "_", "_", "_", "_", "_", "_", "_"]

 

wordToFind = [];

for x in values:

    wordToFind += get_letter(x)

#rint(wordToFind)

maxTries = 15

tries = 0

#replace spaces in guessed word with spaces in wordToFind - user doesn't have to guess spaces

for idx, letter in enumerate(wordToFind):

    if(letter == " "):

        guessedWord[idx] = " "

 

inputVal = "";

while(inputVal != "exit"):

    print("Guess a letter or type 'exit' to exit")

    inputVal = input()

   

    if(inputVal == "exit"):

        print("Goodbye")

        break

   

    tries += 1

    do_guess(guessedWord, wordToFind, inputVal)

    print_w(guessedWord)

    if(not("_" in guessedWord)):

       print("You have won")

       break

    if(tries == maxTries):

        print("You have lost")

        break

    print("You have " + str(maxTries - tries) + " left")
