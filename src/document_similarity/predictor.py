from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize

model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
test_data = word_tokenize("building".lower())
v1 = model.infer_vector(test_data)
print("V1_infer", v1)

# to find most similar doc using tags
similar_doc = model.docvecs.most_similar("NIta Resume.pdf")
print("similar",similar_doc)


# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
print(model.docvecs["Eliza Jones Resume.pdf"])