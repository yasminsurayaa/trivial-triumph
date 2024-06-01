# TODO Small Report about quiz app

from menus import STATISTIC, exit_menu, help_menu, main_menu, player_statistics_menu, sign_up_menu, login_menu, home_menu, quiz_menu, leaderboard_menu, \
                             MAIN_MENU, SIGN_UP, LOGIN, HOME_MENU, QUIZ, LEADERBOARD, HELP, EXIT


def main():
  """
  Starting point of the application. This function manages the state of the application.
  """
  parent_menu = EXIT
  cur_menu = MAIN_MENU

  while True:
    try:
        if cur_menu == MAIN_MENU:
          cur_menu = main_menu()  # Parent menu 1
        
        elif cur_menu == SIGN_UP:
          parent_menu = MAIN_MENU
          cur_menu = sign_up_menu()
        
        elif cur_menu == LOGIN:
          parent_menu = MAIN_MENU
          cur_menu = login_menu()

        elif cur_menu == HOME_MENU:
          cur_menu = home_menu()  # Parent menu 2

        elif cur_menu == QUIZ:
          parent_menu = HOME_MENU
          cur_menu = quiz_menu()

        elif cur_menu == LEADERBOARD:
          parent_menu = HOME_MENU
          cur_menu = leaderboard_menu()

        elif cur_menu == STATISTIC:
          parent_menu = HOME_MENU
          cur_menu = player_statistics_menu()

        elif cur_menu == HELP:
          parent_menu = HOME_MENU
          cur_menu = help_menu()

        elif cur_menu == EXIT:
          exit_menu()
          break

    # If user press Ctrl+C, go back to parent menu
    except KeyboardInterrupt:
      cur_menu = parent_menu


if __name__ == "__main__":
  main()
