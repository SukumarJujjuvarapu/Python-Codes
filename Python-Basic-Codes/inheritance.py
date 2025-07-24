##multilevel inheritance
class grandfather():
    def outputgf(self):
        print("iam the grand father")
class parent():
    def outputp(self):
        print("iam the parent")
class child(parent):
    def outputc(self):
        print("iam the child")
c=child()
p=parent()
gf=grandfather()
gf.outputgf()
p.outputp()
c.outputc()        

##multiple inheritance
class father():
    def outputf(self):
        print("iam the  father")
class mother():
    def outputm(self):
        print("iam the mother")
class child(father,mother):
    def outputc(self):
        print("iam the child")
c=child()
f=father()  ##creating instance
m=mother()
f.outputf()   ##function calling
m.outputm()
c.outputc()        


## hierarchichal inheritance
class father():
    def outputf(self):
        print("iam the  father")
class child1():
    def outputc1(self):
        print("iam the child 1")
class child2(father):
    def outputc2(self):
        print("iam the child 2")
        

c1=child1()
c2=child2()
c1.outputc1()
c2.outputc2()
        
