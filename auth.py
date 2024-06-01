"""
Program: auth.py
Author: Trivial Triumph Devs
Provide interface for user authentications in Trivial Triumph
"""


from ui import error


MIN_CHAR_USERNAME = 3
MAX_CHAR_USERNAME = 12

MIN_CHAR_PASSWORD = 3
MAX_CHAR_PASSWORD = 20


def sign_up(new_username: str, new_password: str, repeat_new_password: str, users: dict) -> str:
  """
  Register a new user. Returns username if authorized, else return empty string. This function automatically assigns the new user data into `users` variable if authorization successful.
  """

  # Make sure username is at least 3 characters long and maximum 12 characters long
  if len(new_username) < MIN_CHAR_USERNAME or len(new_username) > MAX_CHAR_USERNAME:
    error(f"Username must contain at least {MIN_CHAR_USERNAME} characters and maximum of {MAX_CHAR_USERNAME} characters")
    return ''

  # Make sure username is unique
  if new_username in users.keys():
    error("Username already exists")
    return ''

  # Allow underscores
  temp = new_username.replace("_", "")

  # Make sure username only contains alphanumeric characters without space
  if not temp.isalnum():
    error("Username must consists of only alphanumeric characters")
    return ''

  # Make sure password is at least 3 characters long and maximum 20 characters long
  if len(new_password) < MIN_CHAR_PASSWORD or len(new_password) > MAX_CHAR_PASSWORD:
    error(f"Password must contain at least {MIN_CHAR_PASSWORD} characters and maximum of {MAX_CHAR_PASSWORD} characters")
    return ''

  if repeat_new_password != new_password:
    error("Password does not match the repeated password")
    return ''
  
  # Add the new user
  users[new_username] = [new_password, -1]

  return new_username


def log_in(username: str, password: str, users: dict) -> str:
  """
  Authenticate existing user. Returns username if authorized, else return empty string.
  """
  # Check username existence
  if username not in users.keys():
    error("Username does not exist")
    return ''

  # Verify password
  if users[username][0] != password:
    error("Username or password is false")
    return ''
  
  return username


if __name__ == "__main__":
  users = {
  # "username": ["password", score1, score2, ..., scoreN],
    "khilfi": ["khilfi", -1],  # Score -1 indicates the player hasn't played the quiz yet
    "yasmin": ["yasmin", 67, 100]
  }
  sign_up("hello", "hello", "hello", users)
  print(users)
  log_in("hello", "hello", users)
