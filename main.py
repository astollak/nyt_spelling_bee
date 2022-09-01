
def load_words():
    """
    Reads in a file letters with one word per row, and returns a set of those words, all uppercase
    :return: list of uppercase words
    """
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    valid_words = set(map(lambda w: w.upper(), valid_words))
    return valid_words


def check_words(must, tiles, wiq):
    """
    Check word for NYT Spelling Bee rules
    :param must: the single letter that must be in the word in question
    :param tiles: all of the valid letters that may be in the word in question
    :param wiq: the word in question (what word we're testing)
    :return: True if it passes, False if it doesn't
    """
    # Drop words that don't have the middle tile
    if must not in wiq:
        return False
    # Drop words that are too short
    if len(wiq) < 4:
        return False
    # Drop words with a letter that's not in any of the tiles (middle or otherwise)
    for c in wiq:
        if c not in tiles:
            return False

    return True


def find_words(letters) -> object:
    """
    Find words that contain only the letters passed into the function, but MUST include the first letter.
    :param letters: String of the available letters used to make a word. The first letter is required.
    :return: list of words that match the rules
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'What can we make out of {letters[0]} and {letters[1:]}')  # Press Ctrl+F8 to toggle the breakpoint.
    words = load_words()
    print(f'looking at {len(words)} words')
    wl = list(filter(lambda x: check_words(letters[0], letters, x), words))
    wl = sorted(wl, key=lambda x: (-len(x), x))
    return wl


# Run main function if running this file
if __name__ == '__main__':
    print(find_words('MLEGOTY'))
