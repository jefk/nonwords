
import sys
import itertools
import collections
import nltk

class WordModel:
    GRAM_SIZES = [1, 2, 3]
    BEGIN_TOKEN = '<begin>'
    END_TOKEN = '<end>'

    def __init__(self, stream):
        self.text = self._set_text(stream)
        self.model = collections.Counter()
        self._generate_model()

    def all_words(self):
        return nltk.tokenize.wordpunct_tokenize(self.text)

    def filtered_words(self):
        return ( word for word in self.all_words() if len(word) > 3 )

    def _generate_model(self):
        for word in self.filtered_words():
            chars = list(word)
            for gram in self._all_grams(chars):
                self.model[gram] += 1

    def _all_grams(self, ls):
        flattenable = ( self._golden_grams(ls, size) for size in self.GRAM_SIZES )
        return itertools.chain.from_iterable(flattenable)

    def _golden_grams(self, ls, n):
        decorated_ls = (n-1) * [self.BEGIN_TOKEN] + ls + (n-1) * [self.END_TOKEN]
        indexes = xrange(len(ls) + n - 1)
        return ( tuple(decorated_ls[i:i+n]) for i in indexes )

    def _set_text(self, stream):
        return ' '.join( line.strip() for line in stream )

if __name__ == '__main__':
    print 'word model main'
