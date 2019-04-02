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
    try : 
        cursor.execute("drop table imgindex;")
        cursor.execute("drop table imgindexers;")
    except sql.OperationalError as oe:
        pass
    cursor.execute("create table imgindexers(class text, description text);")
    cursor.execute("create table imgindex(name text, indexvalue float, classifier text);")

    cset=[PolynomialBandHashClassifier(),SpectralSumClassifier(),SpectralDensityClassifier(),BandMaximumClassifier()]
    for f in [fn for fn in os.listdir('test_images') if 'png' in fn]:
        extract_features(f, cset)
    for c in cset:
        cursor.execute("insert into imgindexers values ('{}', '{}');".format(c.classifier_classname,c.classifier_description))
    conn.commit()
    conn.close()

# TODO event (upload) based reindexing
"""
from threading import Thread

class SampleEvent(Thread):
    def __init__(self):
        pass #TODO
    def run(self):
        test()
"""

if __name__ == '__main__':
    test()
