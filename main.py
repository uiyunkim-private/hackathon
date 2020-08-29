
from src.parser import extract_resume_info
from src.environment import RESUME_PATH
import os

for file in os.listdir(RESUME_PATH):
    print(extract_resume_info(os.path.join(RESUME_PATH,file)))