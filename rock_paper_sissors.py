from time import sleep
import random
fighters = ["rock","paper","sissors"]
paper_joke = 0
win = 0
loss = 0
while True:
  while True:
    print('Rock, Paper, Sissors - Choose your Fighter!')
    player_selection = input('').lower()
    if player_selection not in fighters:
      print('Please chose a valid fighter.')
      continue
    if player_selection in fighters:
      break
  print("Three...")
  sleep(1)
  print("Two...")
  sleep(1)
  print("One...")
  sleep(1)
  print("SHOOT!")
  sleep(0.5)
  computer_selection = random.choice(fighters)
  print("You throw",player_selection,"!")
  sleep(0.8)
  print("I throw",computer_selection,"!")
  sleep(1)
  if player_selection == computer_selection:
    print("Its a Tie!")
# rock selction
  elif player_selection == "rock":
    if computer_selection == "sissors":
      print("Rock REKTS Sissors! You Win!")
      win = (win + 1)
    elif computer_selection == "paper":
      print("Paper P-...i guess...smothers? Rock? You Lose!")
      loss = (loss + 1)
# sissors selction
  elif player_selection == "sissors":
    if computer_selection == "paper":
      print("Sissors SLICES Paper! You Win!")
      win = (win + 1)
    elif computer_selection == "rock":
      print("Rock REKTS Sissors! You Lose!")
      loss = (loss + 1)
#paper selection
  elif player_selection == "paper":
    if computer_selection == "rock":
      if paper_joke == 0:
        print("HAHAHA you fool! Paper was a HORRIBLE CHOICE!")
        sleep(1.0)
        print("what really? paper beats-...")
        sleep(1.0)
        print("Ugh...fine, paper beats rock...You win...")
        win = (win + 1)
        paper_joke = (paper_joke + 1)
      elif paper_joke == 1:
        print("Come on! There is no way-")
        sleep(0.2)
        print("...")
        sleep(2.0)
        print("I under stand that! I just think it's ridicu-")
        sleep(0.2)
        print("...")
        sleep(2.0)
        print("Ok! Jeez... You win I guess...")
      elif
    elif computer_selection == "sissors":
      print("HA! Sissors SLICES Paper! You Lose!")
      loss = (loss + 1)
  print("Would you like to play again? (Y or N)")
  game_continue = input("")
  if game_continue == "Y":
    continue
  elif game_continue == "N":
    break
print("done")