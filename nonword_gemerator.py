
import sys
import word_model
import random

class Generator:

    def __init__(self, model):
        self.model = model
        self._max_gram_size = max(model.GRAM_SIZES)
        self._min_length = 5

    def generate(self, **options):
        self.things = options.get('seed') or []
        self.retries = 10
        self._add_thing()
        return self.things

    def _add_thing(self):
        next_thing = self._get_next_thing()
        if self.retries == 0:
            return
        elif next_thing == self.model.END_TOKEN and len(self.things) < self._min_length:
            self.retries -= 1
            self._add_thing()
            return
        elif next_thing == self.model.END_TOKEN:
            return

        self.things.append(next_thing)
        self._add_thing()

    def _get_next_thing(self):
        previous_things = self._get_previous_things()
        stop_at = self._get_stop_at(previous_things)

        for next_thing, count in self.model.distribution(previous_things):
            stop_at -= count
            if stop_at < 0:
                return next_thing[0]

    def _get_stop_at(self, previous_things):
        rand_bound = self.model.count(previous_things)
        return random.randrange(rand_bound)

    def _get_previous_things(self):
        decorated_things = [self.model.BEGIN_TOKEN] * (self._max_gram_size-1) + self.things
        return tuple(decorated_things[-1*(self._max_gram_size-1):])

if __name__ == '__main__':
    # TODO add some argument parser
    text = open(sys.argv[1])
    model = word_model.WordModel(text)
    generator = Generator(model)

    print ''.join(generator.generate())
