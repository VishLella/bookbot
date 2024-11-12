
def main():
    book = "books/frankenstein.txt"
    text = readBook(book)
    wc = wordCount(text)
    letters = letterFreq(text)
    
    print("--- Begin report of " + book + " ---")
    print(f"{wc} words found in the document\n\n")
    parseOutput(letters)
    print("--- End report ---")

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
    #letters = dict(sorted(letters.items()))
    list = []
    for item in letters:
        if item.isalpha():
            list.append({"letter": item, "num": letters[item]})
    list.sort(reverse=True, key=sort_on)   
    return list

def sort_on(dict):
    return dict["num"]

def parseOutput(letters):
    for item in letters:
        print("The '" + item["letter"] + "' character was found" ,  
              item["num"] , "times")
        

main()
