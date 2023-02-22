from dao import DAO

class Composant(DAO):
    def __init__(self,idcomposant:str=None,nom:str=None,premiere:str=None,produit:bool=None,prixunitaire:float=None):
        super().__init__("composants")
        self.keylist['primaryKey'] = 'idcomposant'
        self.keylist['foreignKey'].append({'nom':'test','reference':type(self)})
        self.setidComposant(idcomposant)
        self.setNom(nom)
        self.setPremiere(premiere)
        self.setProduit(produit)
        self.setPrixUnitaire(prixunitaire)
        self.attrlist=super().attrlists()


    def setidComposant(self,nom:str):
        if(nom==None):
            self.idcomposant = None
        elif(isinstance(nom,str)==False):
            raise Exception("Idcomposant must be a string")
        self.idcomposant:str= nom

    def setNom(self,nom:str):
        if(nom==None):
            self.nom = None
        elif(isinstance(nom,str)==False):
            raise Exception("Nom must be a string")
        self.nom:str= nom

    def setPremiere(self,premiere:bool):
        if(premiere==None):
            self.premiere = None
        elif(isinstance(premiere,bool)==False):
            raise Exception("Premiere must be a boolean")
        
        self.premiere:bool=premiere

    def setProduit(self,Produit:bool):
        if(Produit==None):
            self.produit = None
        elif(isinstance(Produit,bool)==False):
            raise Exception("Produit must be a boolean")
        self.produit:bool=Produit
    
    def setPrixUnitaire(self,prixunitaire:float):
        if(prixunitaire==None):
            self.prixunitaire = None

        elif(isinstance(prixunitaire,(float,int))==False):
            raise Exception("Prix unitaire must be a string")
        self.prixunitaire:float = prixunitaire

