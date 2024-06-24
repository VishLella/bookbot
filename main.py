
def main():
    book = "books/frankenstein.txt"
    text = readBook(book)

    print(letterFreq(text))


def readBook(path):
    with open(path) as f:
        file = f.read()
        return file
    
def wordCount(text):
    words = text.split()
    return len(words)

def letterFreq(text):
    letters = {}
    text = text.lower()
    for c in text:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    letters = dict(sorted(letters.items()))
    return letters

main()