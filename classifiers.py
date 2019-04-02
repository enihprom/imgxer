
import sqlite3 as sql

conn = sql.connect("imgxer.db")
cursor = conn.cursor()

class Classifier:
    value=0.0
    def __init__(self):
        self.plaindump=False
        self.classifier_classname=str(self.__class__).split("'")[1]
        self.classifier_description=str(''.join([' '+c if str(c).isupper() else str(c) for c in self.classifier_classname][0]).lower()).strip()
        if '.' in self.classifier_description:
            self.classifier_description = self.classifier_description.split('.')[1:]
    def dump(self):
        if not self.plaindump:
            cursor.execute("insert into imgindex values ('{}', '{}', '{}');".format(self.name,self.value,self.classifier_classname))
        else:
            print("insert into imgindex values ('{}', '{}', '{}');".format(self.name,self.value,self.classifier_classname))
    def classify(self,im):
        self._classify(im)
        self.dump() 

class SpectralSumClassifier(Classifier):
    def _classify(self,im):
        u=0 
        for i in range(len(im.getbands())):
            B=im.getdata(band=i)
            for p in B:
                u+=p
        self.value=u/(len(B)*i) if (len(B)*i)!=0 else 0 

class SpectralDensityClassifier(Classifier):
    def _classify(self,im):
        u=0
        n=len(im.getbands())
        for i in range(n):
            B=im.getdata(band=i)
            for p in B:
                u+=p*(i-(n/2))
        self.value=u/(len(B)*i) if (len(B)*i)!=0 else 0

class BandMaximumClassifier(Classifier):
    def _classify(self,im):
        sums=[sum(im.getdata(band=i)) for i in range(len(im.getbands()))]
        for i,s in enumerate(sums):
            if s==max(sums):
                self.value=i

class PolynomialBandHashClassifier(Classifier):
    def _classify(self,im):
        def polynomise(b):
            return sum([x*(i**2) for i,x in enumerate(b)])
        self.value=sum([polynomise(im.getdata(band=bn))*bn for bn in range(len(im.getbands()))])
