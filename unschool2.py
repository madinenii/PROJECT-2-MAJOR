def treasure_room():
  
  print("\nYou are now in a room filled with treasure!")
  print("And there is a door too!")
  print("What would you do? (1 or 2)")
  print("1). Take some treasure and go through the door.")
  print("2). Just go through the door.")

  
  answer = input(">")
  
  if answer == "1":
    
    game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
  elif answer == "2":
   
    print("\nNice, you're are an honest man! Congrats you win the game!")
    
    play_again()
  else:
    
    game_over("Go and learn how to type a number.")



def snake_room():
 
  print("\nThere is a snake here.")
  print("Behind the snake is another door.")
  print("The snake is eating tasty rats!")
  print("What would you do? (1 or 2)")
  print("1). Take the rat.")
  print("2). Taunt the snake.")

 
  answer = input(">")
  
  if answer == "1":
    
    game_over("The snake killed you.")
  elif answer == "2":
   
    print("\nYour Good time, the snake moved from the door. You can go through it now!")
    treasure_room()
  else:
    
    game_over("Don't you know how to type a number?")



def monster_room():
  
  print("\nNow you entered the room of a monster!")
  print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Kill the monster and show your courage!")

  
  answer = input(">")

  if answer == "1":
   
    treasure_room()
  elif answer == "2":
    
    game_over("The monster was hungry, he/it ate you.")
  else:
    
    game_over("Go and learn how to type a number.")



def play_again():
  print("\nDo you want to play again? (y or n)")
  
  
  answer = input(">").lower()

  if "y" in answer:
    
    start()
  else:
   
    exit()



def game_over(reason):
 
  print("\n" + reason)
  print("Game Over!")
  
  play_again()


def start():
  
  print("\nYou are standing in a dark room.")
  print("There is a door to your left and right, which one do you take? (l or r)")
  
  
  answer = input(">").lower()

  if "l" in answer:
    
    snake_room()
  elif "r" in answer:
    
    monster_room()
  else:
    
    game_over("Don't you know how to type something properly?")



start()
