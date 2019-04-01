#!/usr/bin/env python -O

from PIL import Image
import os
from classifiers import *
import sqlite3 as sql

class Classifier:
    value=0.0
    def __init__(self):
        self.classifier_text=str(self.__class__).split("'")[1] #TODO insert space before uppercase letters
    def dump(self):
        print("insert into imgindex values ('{}', '{}', '{}');".format(self.name,self.value,self.classifier_text))
    def classify(self,im):
        self._classify(im)
        self.dump()



def extract_features(ifn,classifiers):
    im=Image.open(ifn)
    for ci in classifiers:
        ci.name=ifn
        ci.classify(im)
    im.close()

def test():
    cset=[PolynomialBandHashClassifier(),SpectralSumClassifier(),SpectralDensityClassifier(),BandMaximumClassifier()]
    for f in [fn for fn in os.listdir() if 'png' in fn]:
        extract_features(f, cset)
    for c in cset:
        print("insert into imgindexers values (name='{}', classifier='{}', indexvalue='{}');".format(c.name,c.__class__,c.value))

if __name__ == '__main__':
    test()
