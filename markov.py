"""Generate Markov text from text files."""

from random import choice

import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_data = open(file_path)
    # file object to interact with from our program
    input_text = text_data.read()
    # naming consistent with make_chains() input
    return input_text


def make_chains(input_text):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # empty dictionary to hold tuples (key) & list (values)

    words = input_text.split()
    # creating list out of long string from open_and_read_file()


    for i in range(len(words) - 2):
    # iterate over each item in the list (except the last two)
        a = words[i]
        # assign a to the word when looping
        # this is the 1st part of our key value
        b = words[i + 1]
        # assign b to the word when looping
        # this is the 2nd part of our key value
        pair = (a, b,)
        # put items into a tuple

        if chains.get(pair, False):
        # check to see if chains{} includes the tuple pair
            c = words[i + 2]
            # assign c to the next letter after b
            chains[pair].append(c)
            # append to the values list within the dictionary

        else:
        # if it isn't in the list, create the empty list in the dictionary
        # then follow the same steps above
            c = words[i + 2]
            chains[pair] = []
            chains[pair].append(c)


    return chains


def make_text(chains):
    """Return text from chains."""

    key_selection = choice(chains.keys())
    # randomly select a key from the chains {} as a seed (tuple)

    word_chain = [key_selection[0], key_selection[1]]
    # create list to hold beginning of chain
    # first words are the randomly selected tuple pair

    while key_selection in chains:
    # while loop searches for tuples to chain to
    # stops when tuple is unable to chain
        new_word = choice(chains[key_selection])
        # look for random value in list associated with key

        word_chain.append(new_word)
        # add word to new word chain

        key_selection = (key_selection[1], new_word,)
        # update keep to continue loop with current key's second value
        # and selected value

    return " ".join(word_chain)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string

input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
