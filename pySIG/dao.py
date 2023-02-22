from utilities import Utilities
class DAO:
    def __init__(self,table):
        self.keylist = {'primaryKey':None,'foreignKey':[]}
        self.table = table
        #self.attrlists()

    def insert(self,con):
        cursor = con.cursor()
        query = self.insertQuery()
        print(query)
        cursor.execute(query)
        
    def insertQuery(self):
        Utilities.fieldToinsert(self)
        query = "insert into %s values(" % self.table
        i = 0
        self.attrlist.pop(0)
        #print(len(self.attrlist))
        for field in self.attrlist:
            if(str(type(self.__getattribute__(field)))=="<class 'str'>"):
                query+="'"+self.__getattribute__(field)+"'"
            else:
                query+=str(self.__getattribute__(field))
            if(i<len(self.attrlist)-1):
                query+=","
            i+=1
        query+=")"
        return query

        
    def update(self,con):
        pass

    def updateQuery(self) :
        primaryKey = Utilities.getPrimaryKey(self)
        query = "update table %s set " % self.table
        
        pass

    def delete(self,con):
        pass

    
    def select (self,con):
        cursor = con.cursor()
        query = self.selectQuery()
        cursor.execute(query)
        data = cursor.fetchall()
        array = []
        popo = 0.0
        for d in data:
            instance = type(self)
            temp = instance()
            i=1
            for element in d: 
                temp.__setattr__(self.attrlist[i],element)
                i+=1
            array.append(temp)
        return array
    
    
    def selectQuery(self):
        fieldToGet = Utilities.objectNotNullfields(self)
        query = "select * from %s  " % self.table
        #print(fieldToGet)
        if(len(fieldToGet)>0):
            query+=" where "
            for i in range (1,len(fieldToGet)):
                if(str(type(self.__getattribute__(fieldToGet[i])))=="<class 'str'>"):
                    query+=fieldToGet[i]+"='"+self.__getattribute__(fieldToGet[i])+"'"
                else:
                    query+=fieldToGet[i]+"="+str(self.__getattribute__(fieldToGet[i]))
                if(i<len(fieldToGet)-1):
                    query+=' and '
            pass
        return query

    def colnbr(self):
        pass
    
    def attrlists(self):
        return Utilities.getAllAttrName(self)