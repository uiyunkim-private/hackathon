from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from src.environment import RESUME_PATH
import os
from src.parser.text_extractor import extract_text_from_document
from src.parser.name_extractor import extract_name_with_rules
from src.parser.phone_number_extractor import extract_phone_number_with_multiple_expressions
from src.parser.email_extractor import extract_email_with_regular_expression_v1
from src.parser.skills_extractor import extract_skills_with_word_tokenization
from src.parser.education_extractor import extract_education_with_database_search
from src.parser.experience_extractor import extract_experiences_from_sentence_analyzer

files = []
data = []
for resume in os.listdir(RESUME_PATH):

    file = os.path.join(RESUME_PATH, resume)
    text = extract_text_from_document(file)
    files.append(resume)
    data.append(text)


tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=files) for i, _d in enumerate(data)]

print(files)
max_epochs = 100
vec_size = 100
alpha = 0.025

model = Doc2Vec(size=vec_size,
                window=10,
                alpha=alpha,
                min_alpha=0.00025,
                min_count=1,
                dm=1)

model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.save("d2v.model")
print("Model Saved")