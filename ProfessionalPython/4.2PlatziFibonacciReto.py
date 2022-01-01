"""
Suma de los 2 numeros anteriores
0 1 1 2 3 5 8 13 21 34 55 89 144 ...
Iterar en la sucesion hasta que se tope con un maximo, cuando llegue levantar un error stopiteration
"""
import time
class FiboIter():

    def __init__(self, max=100):
        self.max = max
    
    def __iter__(self):
        #primeros valores en la sucesion
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    def __next__(self):
        #primera vuelta
            if self.counter == 0:
                self.counter +=1
                return self.n1
            #segunda vuelta
            elif self.counter == 1:
                self.counter  +=1
                return self.n2
            #tercer vuelta en adelante 
            else:
                if not self.max or self.n2 <= self.max:
                    self.aux = self.n1 + self.n2
                    self.n1, self.n2 = self.n2, self.aux
                    self.counter +=1
                    return self.aux
                else:
                    raise StopIteration

if __name__ == '__main__':
    #Ireacion = Acto de convertir a partir de un plano de una clase, un objeto
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)

        