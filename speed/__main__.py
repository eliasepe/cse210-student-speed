from asciimatics.screen import Screen 
from game.director import Director

def main(screen):
    director = Director(screen)
    director.start_game()
    input()

print("Welcome to the speed game:\n\nYou have to see the words and writte them\n")
print("Remember words can hide sometimes! \n")
input("Press ENTER twice to start playing")

Screen.wrapper(main)