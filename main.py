# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file(filename):
    # [assignment] Add your code here
    open_file = open("./story.txt", "r")
    read_file = open_file.read()
    return read_file()


def countwords():
    text = read_file("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    print(split_text)
    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[1] = 1


print(countwords())
