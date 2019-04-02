#!/usr/bin/env python

from PIL import Image
import os, sys
from classifiers import *



def extract_features(ifn,classifiers):
    im=Image.open('test_images/{}'.format(ifn))
    for ci in classifiers:
        ci.name=ifn
        ci.classify(im)
    im.close()

def test():
    cursor.execute("drop table imgindex;")
    cursor.execute("create table imgindex(name text, indexvalue float, classifier text);")

    cset=[PolynomialBandHashClassifier(),SpectralSumClassifier(),SpectralDensityClassifier(),BandMaximumClassifier()]
    for f in [fn for fn in os.listdir('test_images') if 'png' in fn]:
        extract_features(f, cset)
    for c in cset:
        pass
        #FIXME
        #print("insert into imgindexers values (name='{}', classifier='{}', indexvalue='{}');".format(c.name,c.__class__,c.value))
    conn.close()

if __name__ == '__main__':
    test()
