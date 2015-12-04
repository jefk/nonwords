# nonword generator

This is a simple character n-gram model that can generate words that look like english words, but they are not english words. The generated words are pronounceable (mostly), which makes them good for including in passwords.

To run the script:
```
./generate [word_model.txt]
```
The words generated will use words in [word_model.txt] to make new words.

There is some text included in this repo, so you can clone and run with:
```
./generate jabber.txt
```
