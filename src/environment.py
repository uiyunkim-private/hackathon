import os



ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(ROOT_PATH, "data")

RESUME_PATH = os.path.join(DATA_PATH,"resume")
print(RESUME_PATH)