###encapsulation
#public
#private
#protected

class demo():
    def __init__(self,a,b):
      self.__a=a  #private
      self._b=b   #protected
class demo2(demo):
    def output(self):
     print(self._b)
d=demo2(56,568)
d.output()


##polymorphism
def add(a,b):
   print(a+b)
add(3,6)
add('a','b')
add([4,9],[9,3])
add((74,93),(92,344))
