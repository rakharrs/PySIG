from person import Person
from psycopg2 import connect
from composant import Composant
from utilities import Utilities

conn = connect(host='localhost',user='postgres',password='pixel',dbname='postgres')
cursor = conn.cursor()
data = []
cursor.execute("select * from olona")
result = cursor.fetchone()
i = 0
comp = Composant(idcomposant='CR0013',nom='Dolph',premiere=False,produit=True,prixunitaire=369.0)
pk = Utilities.getPrimaryKey(comp)
fkS = Utilities.getForeignKey(comp)
test =fkS[0]['reference']

new_obj = test()
print()
print(type(comp))