import hashlib
import sqlalchemy.exc as E
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey,\
            create_engine
from sqlalchemy.orm import relationship,sessionmaker


class base(declarative_base()):
    __tablename__="base"
    id=Column(Integer,primary_key=True)
    Name=Column(String())
    

class Operation(object):
    def __init__(self):
        engine=create_engine("sqlite:///"+os.getcwd()+"AuthPy")
        Session=sessionmaker()
        Session.configure(bind=engine)
        self.Session=Session()
        base.metadata.create_all(engine)

    def insert(self,name):
        try:
            data=self.Session.query(base).filter(base.Name==Hash(name)).first()
        except E.OperationalError:
            Base=base(Name=Hash(name))
            self.Session.add(Base)
            self.Session.commit()
            return False
        if data:
            return False
        else:
            Base=base(Name=Hash(name))
            self.Session.add(Base)
            self.Session.commit()
            return True

        
def Hash(value):
    baseHash=hashlib.sha1()
    baseHash.update(str(value)) #incase a non string object is passed
    return baseHash.hexdigest()




class auth(object):
    def __init__(self):
        self.operation=Operation()
        
    def insert(self,name):
        return self.operation.insert(name)


#print(type(Hash("a")) )                                           
#a=auth()
#print(a.insert('ab'),Hash("ab"))
#print(a.insert('ab'),Hash('ab'))
#print(a.insert('ab'))
#print(a.insert('s'),Hash("s"))
