import gensim.downloader as api

model = api.load("word2vec-google-news-300")
print(model.most_similar(positive=["creative","technology"], negative=[]))