import os

MAX_ATTEMPTS = 5
HIGHSCORE_FILE = os.environ.get('HANGMAN_HIGHSCORE_FILE', 'score.json')
