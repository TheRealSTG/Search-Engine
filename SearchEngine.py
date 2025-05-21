# A concordance is a count fo every word that appears in a document.
# This function takes the document as a string and returns a dictionary 
# where the keys are the words and the values are the number of times the word occurs.


def concordance(document):
    if type(document) != str:
        raise ValueError("Supplied Aguement should be of type string")
    con = {}
    for word in document.split(' '):
        if con.has_key(word):
            con[word] = con[word] + 1

        else:
            con[word] = 1

    return con

