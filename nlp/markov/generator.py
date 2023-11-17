import markovify
import sys

"""
pip install markovify
https://github.com/jsvine/markovify

https://cs50.harvard.edu/ai/2023/
https://www.youtube.com/watch?v=5NgNicANyqM
"""


# Read text from file
if len(sys.argv) != 2:
    sys.exit("Usage: python generator.py sample.txt")
with open(sys.argv[1]) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text)

# Generate sentences
print()
for i in range(5):
    print(text_model.make_sentence())
    print()

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))