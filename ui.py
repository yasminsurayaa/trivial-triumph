"""
Program: ui.py
Author: Trivial Triumph Devs
Provide custom functions to display text beautifully in the terminal
"""


from time import sleep
import os
import getpass  # For password input


# Width of the terminal
WIDTH = os.get_terminal_size().columns
ASCII_ART_WIDTH = 84
LEFT_PADDING = " " * ((WIDTH - ASCII_ART_WIDTH) // 2)

# Source: https://patorjk.com/software/taag/#p=display&v=2&f=Delta%20Corps%20Priest%201&t=TRIVIAL%0ATRIUMPH
TRIVIAL_ASCII_ART = f"""\033[93m
{LEFT_PADDING}           ███        ▄████████  ▄█   ▄█    █▄   ▄█     ▄████████  ▄█                       
{LEFT_PADDING}       ▀█████████▄   ███    ███ ███  ███    ███ ███    ███    ███ ███                       
{LEFT_PADDING}          ▀███▀▀██   ███    ███ ███▌ ███    ███ ███▌   ███    ███ ███                       
{LEFT_PADDING}           ███   ▀  ▄███▄▄▄▄██▀ ███▌ ███    ███ ███▌   ███    ███ ███                       
{LEFT_PADDING}           ███     ▀▀███▀▀▀▀▀   ███▌ ███    ███ ███▌ ▀███████████ ███                       
{LEFT_PADDING}           ███     ▀███████████ ███  ███    ███ ███    ███    ███ ███                       
{LEFT_PADDING}           ███       ███    ███ ███  ███    ███ ███    ███    ███ ███▌    ▄                 
{LEFT_PADDING}          ▄████▀     ███    ███ █▀    ▀██████▀  █▀     ███    █▀  █████▄▄██                 
{LEFT_PADDING}                     ███    ███                                   ▀             
\033[00m"""
TRIUMPH_ASCII_ART = f"""\033[93m
{LEFT_PADDING}    ███        ▄████████  ▄█  ███    █▄    ▄▄▄▄███▄▄▄▄      ▄███████▄    ▄█    █▄    
{LEFT_PADDING}▀█████████▄   ███    ███ ███  ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   
{LEFT_PADDING}   ▀███▀▀██   ███    ███ ███▌ ███    ███ ███   ███   ███   ███    ███   ███    ███   
{LEFT_PADDING}    ███   ▀  ▄███▄▄▄▄██▀ ███▌ ███    ███ ███   ███   ███   ███    ███  ▄███▄▄▄▄███▄▄ 
{LEFT_PADDING}    ███     ▀▀███▀▀▀▀▀   ███▌ ███    ███ ███   ███   ███ ▀█████████▀  ▀▀███▀▀▀▀███▀  
{LEFT_PADDING}    ███     ▀███████████ ███  ███    ███ ███   ███   ███   ███          ███    ███   
{LEFT_PADDING}    ███       ███    ███ ███  ███    ███ ███   ███   ███   ███          ███    ███   
{LEFT_PADDING}   ▄████▀     ███    ███ █▀   ████████▀   ▀█   ███   █▀   ▄████▀        ███    █▀    
{LEFT_PADDING}              ███    ███                                                             
\033[00m"""
TRIVIAL_TRIUMPH_ASCII_ART = TRIVIAL_ASCII_ART + TRIUMPH_ASCII_ART

def clear():
  """
  Clear the terminal
  """
  os.system("clear")
  os.system("cls")


def center(text="", end="\n", col="\033[00m"):
  """
  Print text on the center of the terminal
  """
  print(col, end="")
  print(text.center(WIDTH), end=end)
  print("\033[00m", end="")
  sleep(0.1)


def fill(char):
  """
  Fill the line with the character
  """
  center(char * ASCII_ART_WIDTH)


def prompt(prompt_message="", input_width=18, hidden=False) -> str:
  """
  Prompt user input at the center of the terminal
  """
  if hidden: return getpass.getpass(prompt_message.center(WIDTH - input_width).rstrip()+" ")  # Password input
  else: return input(prompt_message.center(WIDTH - input_width).rstrip()+" ")  # Normal input


def prompt_choice(prompt_message="", choices = [0, 1], input_width=2) -> str:
  """
  Validate choice input
  """
  
  while True:
    choice = prompt(prompt_message, input_width)

    if choice not in [str(choice) for choice in choices]:
      error("Invalid choice")
      continue
    
    return choice


def display_header(subtitle="Welcome to Trivial Triumph!"):
  """
  Display Trivial Triumph remarkable header
  """
  clear()
  print(TRIVIAL_ASCII_ART, end="")
  sleep(0.1)
  print(TRIUMPH_ASCII_ART)
  sleep(0.1)
  center(f"{subtitle}\n")
  fill("*")
  print()


def display_header_cinematic(subtitle="Welcome to Trivial Triumph!"):
  """
  Display Trivial Triumph remarkable header cinematically
  """
  clear()
  sleep(1)
  print(TRIVIAL_ASCII_ART, end="")
  sleep(1.5)
  print(TRIUMPH_ASCII_ART)
  sleep(1.5)
  center(f"{subtitle}\n")
  sleep(1.7)
  fill("*")
  print()


def error(text=""):
  """
  Print error message in red colour
  """
  center(f"{text}", end="", col="\033[91m")
  print("\033[00m\n")


def success(text=""):
  """
  Print success message in green colour
  """
  center(f"{text}", end="", col="\033[32m")
  print("\033[00m\n")


def countdown():
  global WIDTH
  LEFT_PADDING = " " * ((WIDTH - 38) // 2)

  clear()
  print("\033[33m")
  SKIP_ROW = "\n" * 5
  print(f"""{SKIP_ROW}          
{LEFT_PADDING}             .--,-``-.     
{LEFT_PADDING}            /   /     '.   
{LEFT_PADDING}           / ../        ;  
{LEFT_PADDING}           \ ``\  .`-    ' 
{LEFT_PADDING}            \___\/   \   : 
{LEFT_PADDING}                 \   :   | 
{LEFT_PADDING}                 /  /   /  
{LEFT_PADDING}                 \  \   \  
{LEFT_PADDING}             ___ /   :   | 
{LEFT_PADDING}            /   /\   /   : 
{LEFT_PADDING}           / ,,/  ',-    . 
{LEFT_PADDING}           \ ''\        ;  
{LEFT_PADDING}            \   \     .'   
{LEFT_PADDING}            `--`-,,-'          
""")
  sleep(1)
  clear()
  print(f"""{SKIP_ROW}          
{LEFT_PADDING}                 ,----,   
{LEFT_PADDING}               .'   .' \  
{LEFT_PADDING}             ,----,'    | 
{LEFT_PADDING}             |    :  .  ; 
{LEFT_PADDING}             ;    |.'  /  
{LEFT_PADDING}             `----'/  ;   
{LEFT_PADDING}               /  ;  /    
{LEFT_PADDING}              ;  /  /-,   
{LEFT_PADDING}             /  /  /.`|   
{LEFT_PADDING}           ./__;      :   
{LEFT_PADDING}           |   :    .'    
{LEFT_PADDING}           ;   | .'       
{LEFT_PADDING}           `---'              """)
  sleep(1.2)
  clear()
  print(f"""{SKIP_ROW}
{LEFT_PADDING}                ,---, 
{LEFT_PADDING}             ,`--.' | 
{LEFT_PADDING}            /    /  : 
{LEFT_PADDING}           :    |.' ' 
{LEFT_PADDING}           `----':  | 
{LEFT_PADDING}              '   ' ; 
{LEFT_PADDING}              |   | | 
{LEFT_PADDING}              '   : ; 
{LEFT_PADDING}              |   | ' 
{LEFT_PADDING}              '   : | 
{LEFT_PADDING}              ;   |.' 
{LEFT_PADDING}              '---'   """)
  sleep(1.2)
  clear()
  print(f"""{SKIP_ROW}
{LEFT_PADDING}                              ,---,  
{LEFT_PADDING}                ,----..    ,`--.' |  
{LEFT_PADDING}  ,----..       /   /   \   |   :  :  
{LEFT_PADDING}/   /   \     /   .     :  '   '  ;  
{LEFT_PADDING}|   :     :   .   /   ;.  \ |   |  |  
{LEFT_PADDING}.   |  ;. /  .   ;   /  ` ; '   :  ;  
{LEFT_PADDING}.   ; /--`   ;   |  ; \ ; | |   |  '  
{LEFT_PADDING};   | ;  __  |   :  | ; | ' '   :  |  
{LEFT_PADDING}|   : |.' .' .   |  ' ' ' : ;   |  ;  
{LEFT_PADDING}.   | '_.' : '   ;  \; /  | `---'. |  
{LEFT_PADDING}'   ; : \  |  \   \  ',  /   `--..`;  
{LEFT_PADDING}'   | '/  .'   ;   :    /   .--,_     
{LEFT_PADDING}|   :    /      \   \ .'    |    |`.  
{LEFT_PADDING}\   \ .'        `---`      `-- -`, ; 
{LEFT_PADDING}  `---`                       '---`"                              """)
  sleep(1)
  clear()
  print("\033[00m")


def good_game():
  clear()
  SKIP = "\n" * 5
  GG = f"""{SKIP}
        ░▒▓██████▓▒░   ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓███████▓▒░                 
       ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                
       ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                
       ░▒▓█▓▒▒▓███▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                
       ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                
       ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                
        ░▒▓██████▓▒░   ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓███████▓▒░                 
                                                                          
                                                                          
 ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓██████████████▓▒░  ░▒▓████████▓▒░ ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░ 
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░   ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                
 ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░ 
                                                         
  """
  
  for line in GG.split("\n"):
    center(line, col="\033[32m")
  
  sleep(3)
