"""
This program takes two Documents and then:
# STEP 1: Split doc into words
# STEP 2: Compute word frequencies and then use them as vector
# STEP 3: Find the Angle between the two Vectors

0 degree shows identical document and 90 degree shows different documents

"""

import string
import math

class DocumentDistance :
    def __init__(self, add1, add2):
        self.add1 = add1
        self.add2 = add2

    def getDoc(self, address):
        """
            Input: Any txt document
            Output: A dictionary with all words with their occurrence Frequency
        """

        word_occurrence = {}
        doc1=open(address, 'r', encoding='utf-8')
        for line in doc1:
            for word in line.split():
                word = word.lower()
                new_word = word.translate(str.maketrans('', '', string.punctuation))
                if new_word in word_occurrence:
                    word_occurrence[new_word]+=1

                else:
                    word_occurrence[new_word] = 1
        doc1.close()

        sort_data = sorted(word_occurrence.items(), key=lambda x: x[1], reverse=True)
        sort_data_dict = dict(sort_data)
        return sort_data_dict

    def dotProduct(self, D1, D2):
        """Take two dictionary as input and returns their dot Product"""

        total = 0
        for key in D1:
            if key in D2:
                total += D1[key]*D2[key]
        return total

    def __removePrep(self, D1):
        #It removes some most used words that have no meaning by themselves. It might improve the result.

        prep = ['the', 'be', 'it', 'of', 'and', 'a', 'to', 'in', 'is', 'that', 'this', 'on', 'as', 'or']
        for word in prep:
            if word in D1:
                D1.pop(word)
        return D1

    def getVectorDistance(self):

        try:
            doc1 = self.getDoc(self.add1)
            doc2 = self.getDoc(self.add2)
        
        except FileNotFoundError:
            print("Enter a valid address")
            return

        doc1 = self.__removePrep(doc1)
        doc2 = self.__removePrep(doc2)
         
        num = self.dotProduct(doc1, doc2)
        den = math.sqrt(self.dotProduct(doc1, doc1) * self.dotProduct(doc2, doc2))

        distance = num/den
        angle = math.degrees(math.acos(distance))
        # print(doc1, "\n\n\n\n\n\n\n")
        # print(doc2)
        # print(len(doc1))
        # print((len(doc2)))
        return angle


    def getDistance(self):
        pass

distance = DocumentDistance("D:\AI.txt", "D:\CTM.txt").getVectorDistance()
print("Angle between documents: ", distance)