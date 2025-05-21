This is a search engine/indexer written in python that takes a document that we want to perform search on turns them into a concordance(a count of ever word that occurs in a document).

It then uses a vector space to perform the search.

Two concordances are supplied, one the document and the other one the query, and the vector space returns a number from zero to one to show how related they are.

The higher the number, the more relevant the search terms are to the document.

So, every document has its concordance built for it, then compared to the concordance of the user query and the results are sorted by the numbers returned.



Although, it does have a few flaws,
Firstly it doesn’t support boolean searches  

Secondly it has problems with larger documents. 
The way the vector space works is biased towards smaller documents since they are closer to the search term space. 
This can be subverted by breaking down larger documents into smaller ones.

Finally, it is very CPU intensive and thus not suitable for millions of documents, it first makes a key value pair dictionary for every word in every single document, then compares that concordance with the concordance of the user query and sorts according to the number that is provided by the function.

 
