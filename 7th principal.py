import code

class flipkart(phone):
    #Add few object's & method's__dir__
    __offer="free headset"
    __emi="6 months"
    __cashback=500

    '__init__method are invoked by intrepreter'
    def __init__(self,inch,brand,price):
        super( ). __init__(inch,brand,price)

    def __repr__(self):
        print("object rep")
        return("sucess")

    def add (self):
        print("add")

    def __It__(self,ref):
        print("less than")

    def __iter__(self):
        print(" hi i am Iterator")
        # Iterators are iterables too.
        # Adding this functions to make them so.
        print( "iterator data",self.i,self.n)
        #raise stopIteration()
        return 1

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    def offers(self):
        print(self.__offers,self.__emi ,self.__cashback)

    def __del__(self):
        super().__del__()

dir(flipkart)
venkatesh = flipkart(14,"iphone",54000)
venkatesh = venkatesh<1
        
