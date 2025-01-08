def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count = get_word_count(file_contents)
    wordCount = character_count(file_contents)
    report(count,wordCount)

def get_word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    wordCountList = {}
    for character in text:
        if character.isalpha() == True:
            if character.lower() in wordCountList:
                wordCountList[character.lower()] +=  1
            else:
                wordCountList[character.lower()] =  1
    return wordCountList

def report(count,wordCount):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document \n")
    for word in wordCount:
        print(f"The '{word}' character was found {wordCount[word]} times")
    print("--- The end report ---")


main()