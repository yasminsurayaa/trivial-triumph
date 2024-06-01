"""
Program: db.py
Author: Trivial Triumph Devs
Provide interface for database operations in Trivial Triumph
"""

from os import getcwd


# Store current working directory for file reference
CWD = getcwd()

# Path to file where the users data are stored
USER_DATA_FILE = "users.txt"

# Path to folder containing all questions
QUESTIONS_FOLDER = f"{CWD}\questions"


def get_users_data():
  """
  Read users data from users.txt
  """
  try:
    # Open the database file
    f = open(USER_DATA_FILE, "r")

  except FileNotFoundError:

    # When file is not found, create new file
    
    new_f = open(USER_DATA_FILE, "w")
    new_f.write("username,password,scores-time\n")
    new_f.close()
    f = open(USER_DATA_FILE, "r")

  next(f)  # Skip the 1st line, which is the data header (see users.txt file for reference)
  
  users = {}
  # Parse data into dictionary
  for line in f:
    raw = line.strip()
    username, password, *scores_time = raw.split(",")
    if scores_time[0] == "-1":
        users[username] = [password, -1]
    else:
        scores_time = [s.split("-") for s in scores_time]
        scores_time = [tuple([int(s[0]),int(s[1])]) for s in scores_time]
        users[username] = [password] + scores_time
  return users


def save_users_data(users: dict):
  """
  Write users data into users.txt file
  """
  f = open(USER_DATA_FILE, "w")

  raw = "username,password,scores-time\n"

  # Parse dictionary data into string
  for username, data in users.items():
    if data[1] == -1:
        raw += f"{username},{data[0]},-1\n"
    else:
        raw += f"{username},{data[0]},{','.join([f'{d[0]}-{d[1]}' for d in data[1:]])}\n"

  f.write(raw)


def load_mcq_questions():
    """
    Read MCQ questions and answers in mcq.txt
    """
    f = open(f"{QUESTIONS_FOLDER}\mcq.txt")

    # Skip the first 6 lines which are the sample questions of the file
    for _ in range(6):
        next(f)  # Skip the line

    mcq = []
    for _ in f:
        question = next(f).strip()
        answers = []
        answers.append(f"A. {next(f).strip()}")
        answers.append(f"B. {next(f).strip()}")
        answers.append(f"C. {next(f).strip()}")
        answers.append(f"D. {next(f).strip()}")
        correct_answer = next(f).strip().lower()
        mcq.append((question, answers, correct_answer))

    return mcq


def load_tf_questions():
    """
    Read True/False questions and answers in tf.txt
    """
    f = open(f"{QUESTIONS_FOLDER}\\tf.txt")

    # Skip the first 2 lines which are the sample questions of the file
    for _ in range(2):
        next(f)  # Skip the line

    tf = []
    for _ in f:
        question = next(f).strip()
        correct_answer = next(f).strip().lower()
        tf.append((question, correct_answer))

    return tf


def load_matching_questions():
    """
    Read matching questions in matching.txt
    """
    f = open(f"{QUESTIONS_FOLDER}\matching.txt")
        
    for _ in range(3):
        next(f)

    matchings = []
    for _ in f:  # Read three questions and answers
        m = []
        for _ in range(3):
            question, correct_answer = next(f).strip().split(" -> ")
            m.append((question, correct_answer))
        matchings.append(m)

    return matchings


def load_FIB_questions():
    """
    Read fill in the blank questions in FIB.txt
    """
    f = open(f"{QUESTIONS_FOLDER}\FIB.txt")

    for _ in range (2):
        next(f)

    FIB = []
    for _ in f:
        question = next(f).strip()
        correct_answer = next(f).strip().lower()
        FIB.append((question, correct_answer))

    return FIB


def load_sub_questions():
    """
    Read subjective questions in sub.txt
    """
    f = open(f"{QUESTIONS_FOLDER}\sub.txt")

    for _ in range (2):
        next(f)

    sub = []
    for _ in f:
        question = next(f).strip()
        correct_answer = next(f).strip().lower()
        sub.append((question, correct_answer))

    return sub


if __name__ == "__main__":
  save_users_data({'yasmin': ['yasmin', (67,100), (100,60)], 'khilfi': ['khilfi', -1], 'irfan': ['izerith', -1]})
  print(get_users_data(), end="\n\n\n")
  print(load_mcq_questions(), end="\n\n\n")
  print(load_tf_questions(), end="\n\n\n")
  print(load_matching_questions(), end="\n\n\n")
  print(load_FIB_questions(), end="\n\n\n")
  print(load_sub_questions(), end="\n\n\n")
