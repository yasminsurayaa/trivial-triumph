"""
Program: menus.py
Author: Trivial Triumph Devs
Provide all functions for menus
"""


import time
from auth import sign_up, log_in
from db import save_users_data, get_users_data
from quiz import quizEasy
from ui import clear, countdown, display_header, center, fill, good_game, prompt, prompt_choice, display_header_cinematic


# Enums for referencing menu number
MAIN_MENU = 0
SIGN_UP = 1
LOGIN = 2
HOME_MENU = 3
QUIZ = 4
STATISTIC = 5
LEADERBOARD = 6
HELP = 7
EXIT = -1


# Global variable storing the username of current user (need log in first)
CurUser = ""

# Global variable containing all user data.
Users: dict[list] = get_users_data()


def main_menu():
  """
  Main menu (parent menu)
  """
  try:
    # Display header of main menu
    display_header_cinematic()

    # Prompt message
    center("Do you want to register or login?\n")
    center("[1] Register    [2] Login\n")

    choice = int(prompt_choice(">", choices=[1, 2]))
    
    if choice == 1:
      return SIGN_UP  # Go to sign up
    elif choice == 2:
      return LOGIN  # Go to login
  except KeyboardInterrupt:
    if exit_modal():
      return EXIT  # Quit the application
    return MAIN_MENU


def sign_up_menu():
  """
  Sign up menu
  """
  # Display header of login menu
  display_header()
  center("Sign Up\n")

  global Users, CurUser
  while True:
    username = prompt("Username: ")
    password = prompt("Password: ", hidden=True)
    repeat_password = prompt("Repeat password: ", hidden=True, input_width=24)

    CurUser = sign_up(username, password, repeat_password, Users)

    if not CurUser: continue

    # Save the updated data
    save_users_data(Users)
    return HOME_MENU  # Go to home menu


def login_menu():
  """
  Log in menu
  """
  # Display header of login menu
  display_header()
  center("Log In\n")

  while True:
    username = prompt("Username: ")
    password = prompt("Password: ", hidden=True)
    
    global CurUser, Users
    CurUser = log_in(username, password, Users)

    if not CurUser: continue

    return HOME_MENU  # Go to home menu


def home_menu():
  """
  Home menu (parent menu)
  """
  try:
    # Display header of home menu
    global CurUser
    display_header(subtitle=f"Welcome {CurUser}!")

    # Prompt message
    center("Home Menu\n")
    center("(1) Play       ")
    center("(2) Stats      ")
    center("(3) Leaderboard")
    center("(4) Help       ")
    center("(5) Logout     ")
    center()

    choice = int(prompt_choice(">", choices=[1, 2, 3, 4, 5]))
    if choice == 1:
      return QUIZ  # Go to quiz menu
    elif choice == 2:
      return STATISTIC  # Go to leaderboard menu
    elif choice == 3:
      return LEADERBOARD  # Go to help menu
    elif choice == 4:
      return HELP
    elif choice == 5:
      CurUser = ""  # Reset current user due to logout
      return MAIN_MENU  # Back to main menu
  except KeyboardInterrupt:
    if exit_modal():
      return EXIT  # Quit the application
    return HOME_MENU
  
  
def quiz_menu():
  """
  Handles Quiz display and flow
  """
  clear()
  center("Trivial Triumph", col="\033[33m")
  fill("*")
  center()
  center("You will answer 15 fun trivial questions.")
  center("If you answer some of the first 9 questions correctly, you stand a chance on doubling marks in HARD MODE.")
  center("There are MCQ, True/False, Matching, Fill The Blanks, and Subjective questions.", end="\n\n")
  prompt("Press Enter when you're ready!", input_width=0, hidden=True)
  countdown()
  display_header(subtitle="Happy Answering!")
  
  start = time.time()  # Record starting time
  score = quizEasy()  # Run the quiz
  end = time.time()  # Record finishing time

  # Result processing
  time_taken = int(end - start)
  if Users[CurUser][1] == -1:
    is_new_high_score = True
  else:
    is_new_high_score = score > max([x[0] for x in Users[CurUser][1:]])

  # Store new score
  if Users[CurUser][1] != -1:
    Users[CurUser].append((score, time_taken))
  else:
    Users[CurUser][1] = (score, time_taken)
  save_users_data(Users)

  fill("*")
  center("END OF QUIZ", col="\033[33m")
  time.sleep(1)
  good_game()
  prompt("Press Enter to see result\n", hidden=True, input_width=0)
  fill("*")
  center()
  center("RESULT", col="\033[33m", end="\n\n")
  center(f"Quiz completed!", end="\n\n")
  if is_new_high_score: center(f"NEW PERSONAL HIGH SCORE!", col="\033[32m")
  center(f"Your score is: {score} / 48")
  center(f"Time taken: {time_taken} seconds", end="\n\n")
  fill("*")
  prompt("Back to Home...\n", hidden=True, input_width=0)
  return HOME_MENU  # Go to home menu


def leaderboard_menu():
  """
  Leaderboard menu
  """
  users = get_users_data()
  display_header(subtitle="Top 10 Players' Highest Marks")
  
  # Filter from player that hasnot played any matches
  remove_list = []
  for k in users.keys():
    if users[k][1] == -1:
      remove_list.append(k)
  
  for k in remove_list:
    users.pop(k)

  # Sort users by their highest score
  sorted_users = sorted(users.items(), key=lambda x: (max([score[0] for score in x[1][1:]]), min([-time[1] for time in x[1][1:]])), reverse=True)
  center("Leaderboard", col="\033[33m", end="\n\n")
  center("Rank    Name            Highest Score    Time Taken")
  for rank, (username, scores) in enumerate(sorted_users[:10], 1):
      sorted_scores = sorted(scores[1:], key=lambda x: (x[0], -x[1]), reverse=True)
      highest_score, lowest_time = sorted_scores[0]
      center("%4d    %-12s    %-2d / 48          %-3ds      " % (rank, username, highest_score, lowest_time))
  
  center(end="\n\n\n")
  fill("*")
  prompt("Press Enter to return to Home...\n", hidden=True, input_width=0)
  return HOME_MENU  # Go to home menu


def help_menu():
  """
  Show helpful controls to navigate through the app
  """
  display_header("")
  center("Controls", end="\n\n")
  center("Navigate       -  [1, 2, 3, 4, 5]   ")
  center("Answer         -  [A..Z, a..z, 0..9]")
  center("Proceed        -  [Enter]           ")
  center("Back/Previous  -  [Ctrl + C]        ")
  center()
  prompt("Back to Home...\n", hidden=True, input_width=1)
  return HOME_MENU  # Go to home menu


def exit_menu():
  """
  Clear the whole application texts when exitted application
  """
  clear()


def exit_modal(message="Are you sure you want to quit?"):
  """
  Prompt confirmation from user whether to exit the application or not.
  """
  try:
    clear()
    center(message, end="\n\n")
    center("[1] No    [2] Yes")
    center()

    choice = int(prompt_choice(">", choices=[1, 2]))
    if choice == 1:
      return False
    elif choice == 2:
      return True
  except KeyboardInterrupt:
    return False


def player_statistics_menu():
  """
  Generate and display statistics about the user performance based on matches, scores, and time.
  """
  # Display header
  clear()
  center("Player Stats", col="\033[33m")
  center()
  fill("*")
  center()
  
  matches_played = 0 if Users[CurUser][1] == -1 else len(Users[CurUser][1:])

  center(f"Username: {CurUser}", col="\033[33m")
  center(f"Matches Played: {matches_played}", end="\n\n")

  if matches_played == 0:
    center("No data available. Play at least one match to see statistics.")
  else:
    center("+-------+-------+------------+-------+")
    center("| Match | Score | Time taken | Speed |")
    center("+-------+-------+------------+-------+")

    count = 0
    total_score = 0
    total_time = 0
    highest_score = 0
    
    for score, time in Users[CurUser][1:]:
      center("|%7d|%4d/48|%10d s| %5.2f |" % (count+1, score, time, time / 15))
      center("+-------+-------+------------+-------+")
      count += 1
      total_score += score
      total_time += time
      if score > highest_score:
        highest_score = score

    center()
    center(f"Average Score: {round(total_score / count, 2)}")
    center(f"Average Time Taken: {round(total_time / count, 2)} s")
    center(f"Best Score: {highest_score}/48", col="\033[32m")
  
  center()
  fill("*")
  center()
  prompt("Back to Home\n", input_width=1, hidden=True)
  return HOME_MENU
