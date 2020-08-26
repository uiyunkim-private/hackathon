from pyresparser import ResumeParser
import os
import json
from src.environment import DATA_PATH


resume_path = os.path.join(DATA_PATH,"resume")

for file in os.listdir(resume_path):
    filePath = os.path.join(resume_path,file)
    data = ResumeParser(filePath,skills_file=os.path.join(DATA_PATH,"skills.csv")).get_extracted_data()

    print(json.dumps(data["skills"]))