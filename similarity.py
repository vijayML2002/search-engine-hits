import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import extraction

def vect_cos(vect, text_list):
    query_0 = vect.transform([' '.join(vect.get_feature_names())])
    query_1 = vect.transform(text_list)
    cos_sim = cosine_similarity(query_0.A, query_1.A)  
    return query_1, np.round(cos_sim.squeeze(), 3)

class cos_similarity:
    def __init__(self, mpath):
        self.mpath = mpath
        self.clist = []
        self.e = extraction(self.mpath)

    def stringToList(self, string):
        listRes = list(string.split(" "))
        return listRes
    
    def csim(self, keyword, n):
        keyword = self.e.keyword_clean(keyword)
        klist = self.stringToList(keyword)
        vectoriser = CountVectorizer().fit(klist)
        for file in os.listdir(self.mpath):
            s1 = self.e.html_data(file)
            s1 = self.stringToList(s1)
            lvect, lcos = vect_cos(vectoriser, [' '.join(s1)])
            self.clist.append([file, lcos])
        self.clist = self.rank(self.clist)
        return self.clist[:n]

    def rank(self, slist):
        slist.sort(key = lambda x: x[1])
        return slist[::-1]
        
    def close(self):
        self.clist = []
        
