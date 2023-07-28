# Working


 The idf of various words have been formed using the CNN/Dailymail corpus. IDF is defined as log(Number of documents/Number of documents where the word occurs)
1. Sentences are cleaned ( urls removed, contractions expanded, html tags removed, special and newline characters removed )
2. For each sentence a score is assigned ( average of tfidf of each word in the sentence)
3. Sentences are sorted in decreasing order of scores ( highest to lowest)
4. Sentences are popped and added until the number of words in summary is close to given summary length

   
