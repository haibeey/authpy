
import json

class dbHandler(object):
    def __init__(self,name):
        self.name=name
        
    def init(self):
        with open(self.name,'w') as f:
            d={i:[] for i in range(1001)}
            f.write(json.dumps(d))
            
    def insert(self,name,idd):
        with open(self.name,'r+') as f:
            data=json.loads(f.read())
            if self.binarySearch(data[str(idd)],name,0) is not None:
                return False
            data[str(idd)].append(name)
            edit=data[str(idd)]
            i=len(edit)-1
            while edit[i]<edit[i-1]:
                edit[i],edit[i-1]=edit[i-1],edit[i]
                i-=1
            data=json.dumps(data)
        with open(self.name,'w') as f:
            f.write(data)
        return True
    
    def binarySearch(self,array,value,index):
        if not array:return None
        right=array[len(array)/2:]
        left=array[:len(array)/2]
        if len(array)==1 and array[0]==value:
            return index
        elif len(array)==1 and array[0]!=value:
            return None
        elif value==right[0]:
            return index+len(array)/2
        elif value>right[0]:
            return self.binarySearch(right,value,index+len(array)/2)
        else:
            return self.binarySearch(left,value,index)
        
class auth(object):
    def __init__(self,name):
        self.name=name+'.json'
        self.dbHandler=dbHandler(self.name)
        
    def init(self):
        self.dbHandler.init()
        
    def Hash(self,value):
        d={'a':22,'b':25,'c':7,'d':9,'e':18,'f':21,'g':3,'h':5,'i':6,'j':20,'k':11,'l':13,'m':17,\
           'n':4,'o':2,'p':26,'q':16,'r':1,'s':10,'t':14,'u':19,'v':15,'w':23,'x':12,'y':8,'z':24}
        value=sum([d[i]*ord(i) for i in value])
        return value%1001
    
    def insert(self,name):
        return self.dbHandler.insert(name,self.Hash(name))

    def get(self,idd):
        with open(self.name,'r') as f:
            data=json.loads(f.read())
            print(data[str(idd)])
            
                                             


'''
a=auth('ab')
#a.init()
print(a.insert('ab'))
a.get(a.Hash('ab'))
'''
