
class SpectralSumClassifier(Classifier):
    def _classify(self,im):
        u=0 
        for i in range(len(im.getbands())):
            B=im.getdata(band=i)
            for p in B:
                u+=p
        self.value=u/(len(B)*i) if (len(B)*i)!=0 else 0 
        #print("spectral sum of {} = {}".format(self.name,self.value))

class SpectralDensityClassifier(Classifier):
    def _classify(self,im):
        u=0
        n=len(im.getbands())
        for i in range(n):
            B=im.getdata(band=i)
            for p in B:
                u+=p*(i-(n/2))
        self.value=u/(len(B)*i) if (len(B)*i)!=0 else 0
        #print("spectral density of {} = {}".format(self.name,self.value))

class BandMaximumClassifier(Classifier):
    def _classify(self,im):
        sums=[sum(im.getdata(band=i)) for i in range(len(im.getbands()))]
        for i,s in enumerate(sums):
            if s==max(sums):
                self.value=i
        #print("band maximum of {} = {}".format(self.name,self.value))

class PolynomialBandHashClassifier(Classifier):
    def _classify(self,im):
        def polynomise(b):
            return sum([x*(i**2) for i,x in enumerate(b)])
        self.value=sum([polynomise(im.getdata(band=bn))*bn for bn in range(len(im.getbands()))])
