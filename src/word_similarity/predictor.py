import gensim, logging
from gensim.models import Word2Vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



model = gensim.models.Word2Vec.load('mymodel')
print(model.wv.vocab.keys())
similar = model.similar_by_word('javascript')
print(similar)
similar = model.similar_by_word('word')
print(similar)
similar = model.similar_by_word('biology')
print(similar)
#model.doesnt_match("breakfast cereal dinner lunch".split())

#model.similarity('woman', 'man')
