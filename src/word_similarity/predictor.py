import gensim, logging
from gensim.models import Word2Vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



model = gensim.models.Word2Vec.load('mymodel')
print(model.wv.vocab.keys())
similar = model.wv.similar_by_word('javascript', topn=100)
print(similar)
similar = model.wv.similar_by_word('word')
print(similar)
similar = model.wv.similar_by_word('biology')
print(similar)
similar = model.wv.similar_by_word('photoshop')
print(similar)
similar = model.wv.similar_by_word('python')
print(similar)
#model.doesnt_match("breakfast cereal dinner lunch".split())

#model.similarity('woman', 'man')
