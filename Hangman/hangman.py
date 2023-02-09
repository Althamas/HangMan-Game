import random
import stage
import words
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
words = words.word_list
choosen = random.choice(words)
display = []
for i in range(len(choosen)):
    display.append("_")

lives = 6
end_of_game = False
print(choosen)
while  not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"Already Guessed {guess}. Try Again")
            
    for position in range(len(choosen)):
        letter = choosen[position]
        if letter == guess:
            display[position] = letter
    print(display)

        
    if guess not in choosen:
        lives -= 1
        print(f"{guess} is not in the Word")
        print(stage.stages[lives])
        if lives == 0:
            end_of_game =  True
            print("You lose")
            print('''
  ________                        ________                     
 /  _____/_____    _____   ____   \_____  \___  __ ___________ 
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \\
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   
        \/     \/      \/     \/          \/          \/       
''')
            
    

        
    if "_" not in display:
        end_of_game = True
        print('''
_____.___.               __      __.__        
\__  |   | ____  __ __  /  \    /  \__| ____  
 /   |   |/  _ \|  |  \ \   \/\/   /  |/    \ 
 \____   (  <_> )  |  /  \        /|  |   |  \\
 / ______|\____/|____/    \__/\  / |__|___|  /
 \/                            \/          \/ 
''')
        