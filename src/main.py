from src.environment import RESUME_PATH
import os
from src.parser.text_extractor import extract_text_from_document
from src.parser.name_extractor import extract_name_with_rules
from src.parser.phone_number_extractor import extract_phone_number_with_multiple_expressions
from src.parser.email_extractor import extract_email_with_regular_expression_v1
from src.parser.skills_extractor import extract_skills_with_word_tokenization
from src.parser.education_extractor import extract_education_with_database_search
from src.parser.experience_extractor import extract_experiences_from_sentence_analyzer
from src.parser.wikipedia_extractor import extract_wikipedia_with_noun_tokenization
import json
for resume in os.listdir(RESUME_PATH):

    file = os.path.join(RESUME_PATH, resume)
    text = extract_text_from_document(file)

    # name = extract_name_with_rules(text)
    # phone = extract_phone_number_with_multiple_expressions(text)
    # email = extract_email_with_regular_expression_v1(text)
    skills = extract_skills_with_word_tokenization(text)
    # educations = extract_education_with_database_search(text)
    # experiences = extract_experiences_from_sentence_analyzer(file)
    wikipedia = extract_wikipedia_with_noun_tokenization(skills)

    # print("NAME: " ,name)
    # print("PHONE: ", phone)
    # print("EMAIL: ", email)
    # print("SKILLS", skills)
    # print("EDUCATIONS",educations)
    # print("EXPERIENCES",experiences)
    print("WIKIPEDIA",wikipedia)


