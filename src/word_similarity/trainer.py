import gensim, logging
from gensim.models import Word2Vec
import os
from src.environment import RESUME_PATH
from nltk.tokenize import sent_tokenize,word_tokenize
from src.parser.text_extractor import extract_text_from_document

sentences = []
for resume in os.listdir(RESUME_PATH):

    file = os.path.join(RESUME_PATH, resume)

    text = extract_text_from_document(file).lower()

    lines = text.split("\n")


    for each_line in lines:
        each_line_in_token = word_tokenize(each_line)
        sentences.append(each_line_in_token)


sentences = [x for x in sentences if x]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



model = gensim.models.Word2Vec(iter=1)
model.build_vocab(sentences)

model = gensim.models.Word2Vec(
    sentences,
    size=1000,
    window=50,
    min_count=1,
    workers=4,
    iter=200)


model.save('mymodel')