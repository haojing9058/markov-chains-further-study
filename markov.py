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


def make_chains(input_text, n): # adding second parameter (n) to handle more -grams
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

    for index in range(len(words) - n):
    # iterate over each item in the list (except the last n)
    # changed 2 to "n" to allow more grams
        grouping = []
        # empty list created to hold n-gram
        # included in loop as each word needs a grouping

        grouping.extend(words[index:index+n])
        grouping_key = tuple(grouping)

        if chains.get(grouping_key, False):
        # check to see if chains{} includes the tuple group
            value_for_grouping = words[index + n]
            # assign value based on grouping_key index (i) in original list
            chains[grouping_key].append(value_for_grouping)
            # append to the values list within the dictionary

        else:
        # if it isn't in the list, create the empty list in the dictionary
        # then follow the same steps above
            value_for_grouping = words[index + n]
            chains[grouping_key] = []
            chains[grouping_key].append(value_for_grouping)


    return chains


def make_text(chains):
    """Return text from chains."""

    key_selection = choice(chains.keys())
    # randomly select a key from the chains {} as a seed (tuple)

    word_chain = list(key_selection)
    # create list to hold beginning of chain
    # first words are the randomly selected tuple group

    while key_selection in chains:
    # while loop searches for tuples to chain to
    # stops when tuple is unable to chain
        new_word = choice(chains[key_selection])
        # look for random value in list associated with key
        # leaving word chain as a tuple so it can be searched in chains{}

        word_chain.append(new_word)
        # add word to new word chain

        key_selection = key_selection[1:] + (new_word,)
        # update keep to continue loop with current key's second value
        # and selected value

    return " ".join(word_chain)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string

input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text, 3)

# Produce random text
random_text = make_text(chains)

print random_text
