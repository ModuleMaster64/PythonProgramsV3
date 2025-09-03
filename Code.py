# String data types

# Subroutine to process a phrase
def Find(Phrase, Word):
    Start = Phrase.find(Word)
    End = Start + len(Word) -1
    return Start, End

# Main program
Phrase = "Code never lies; comments sometimes do. - Ron Jeffries"
Word = "comments"
Start, End = Find(Phrase,Word)
print("'{}' can be found between characters {} and {} in '{}'.".format(Word, Start, End, Phrase))
