from http.client import PARTIAL_CONTENT
import numpy as np

from preprocessing import getSentenceData
from rnn import Model


word_dim = 800
hidden_dim = 100
X_train, y_train, word_to_idx, idx_to_word = getSentenceData('data/reddit-comments-2015-08.csv', word_dim)

np.random.seed(10)
rnn = Model(word_dim, hidden_dim)
print(word_to_idx)
#test = [word_to_idx["i"], word_to_idx["think"], word_to_idx["she"], word_to_idx["need"], word_to_idx["your"]]
test = [0, word_to_idx["i"], word_to_idx["love"]]
print(len(X_train))
exit
print(test)
losses = rnn.train(X_train[:100], y_train[:100], learning_rate=0.005, nepoch=10, evaluate_loss_after=1)
res = rnn.predict(test)
print(res)
s = ""
for i in res:
  s += idx_to_word[i]