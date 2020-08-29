import gensim, logging
from gensim.models import Word2Vec
import os
import pickle
from src.environment import RESUME_PATH
from nltk.tokenize import sent_tokenize,word_tokenize
from src.parser.text_extractor import extract_text_from_document
from src.parser.wikipedia_extractor import extract_wikipedia_with_noun_tokenization
import threading

sentences = []
for resume in os.listdir(RESUME_PATH):
    file = os.path.join(RESUME_PATH, resume)
    text = extract_text_from_document(file).lower()
    lines = text.split("\n")


    for each_line in lines:
        each_line_in_token = word_tokenize(each_line)
        sentences.append(each_line_in_token)


sentences = [x for x in sentences if x]

model = gensim.models.Word2Vec(iter=1)
model.build_vocab(sentences)

wiki_sentences = []
vocab_size = len(list(model.wv.vocab.keys()))

wiki_search_threads = []
for i, vocab in enumerate(list(model.wv.vocab.keys())):
    wiki_page = extract_wikipedia_with_noun_tokenization(vocab,)

    if wiki_page is not None:
        tokenized_wiki = sent_tokenize(wiki_page)
        print(vocab,i,"/",vocab_size)
        for line in tokenized_wiki:
            word_tokenized = word_tokenize(line)
            wiki_sentences.append(word_tokenized)



with open('wiki_sentences.pkl', 'wb') as f:
    pickle.dump(wiki_sentences, f)


model = gensim.models.Word2Vec(
    sentences,
    size=1000,
    window=50,
    min_count=1,
    workers=4,
    iter=200)


model.save('mymodel')