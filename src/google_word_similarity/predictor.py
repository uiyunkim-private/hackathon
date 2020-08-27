import gensim.downloader as api

model = api.load("word2vec-google-news-300")
print(model.most_similar(positive=["king", "woman"], negative=["man"]))