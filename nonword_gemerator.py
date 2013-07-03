
import sys
import word_model

class Generator:

    def __init__(self, model):
        self.model = model

    def generate(self):
        self.things = []
        next_thing = self._get_next_thing()
        while next_thing is not self.model.END_TOKEN:
            self.things.append(next_thing)
        return self.things

    def _get_next_thing(self):
        previous_things = self._get_previous_things()
        stop_at = self._get_stop_at()

        for next_thing, count in self.model.distribution(previous_things):
            stop_at -= count
            if stop_at < 0:
                return next_thing

    def _get_stop_at(self):
        rand_bound = self.model.count(previous_things)
        return random.randrange(rand_bound)

if __name__ == '__main__':
    # TODO add some argument parser
    text = open(sys.argv[1])
    model = word_model.WordModel(text)
    generator = Generator(model)
    print generator.generate()
