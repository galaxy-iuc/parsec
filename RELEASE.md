# Making a new release

1. Find newest bioblend version.
  - edit the setup.py
  - requirements.txt, pin to the latest bioblend
  - HISTORY.rst
  - `parsec/__init__.py`
2. run `make`
3. check the `git diff`. Did it do anything odd?
4. `git add docs/ parsec/ requirements.txt setup.py`
5. `git commit -m 'Release for bioblend 0.15.0'`
6. `git tag 1.15.0` # Note the 1!  I screwed up the numbering earlier in the life of this package, we should have followed bioblend from the start, but I was not smart :( so now we bump the major version to bioblend's + 1.
