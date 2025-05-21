# A concordance is a count fo every word that appears in a document.
# This function takes the document as a string and returns a dictionary 
# where the keys are the words and the values are the number of times the word occurs.

## Vector Space
## Vector space allows for the calculation of the distance between two points.
# The distance between two points is the square root of the sum of the squares of the differences between the coordinates.

import math




class VectorCompare:
    def magnitude(self, concordance):
        if type(concordance) != dict:
            raise ValueError("Supplied Aguement should be of type dictionary")
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)
    
    def relation(self, concordance1, concordance2):
        if type(concordance1) != dict:
            raise ValueError("Supplied Aguement should be of type dictionary")
        if type(concordance2) != dict:
            raise ValueError("Supplied Aguement should be of type dictionary")
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if concordance2.__contains__(word):
                topvalue += count * concordance2[word]
        if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
            return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
        else:
            return 0
        
    def concordance(self,document):
        if type(document) != str:
            raise ValueError("Supplied Aguement should be of type string")
        con = {}
        for word in document.split(' '):
            if con.__contains__(word):
                con[word] = con[word] + 1

            else:
                con[word] = 1

        return con



## Test
v = VectorCompare()

documents = {
    0: 'This is a test document. This document is a test.',
    1: 'This is another test document. This document is another test.',
    2: 'This is a different test document. This document is a different test.',
    3: 'This is a different test document. This document is a different test.',
}

index = {
0:v.concordance(documents[0].lower()),
1:v.concordance(documents[1].lower()),
2:v.concordance(documents[2].lower()),
3:v.concordance(documents[3].lower()),
}

searchterm = 'test'
matches = []

for i in range(len(index)):
    relation = v.relation(v.concordance(searchterm.lower()), index[i])
    if relation != 0:
        matches.append((relation, documents[i][:100]))


matches.sort(reverse=True)
for i in matches:
    print(i[0], i[1])
