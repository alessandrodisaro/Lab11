from database.DAO import DAO

nodes = DAO.getAllNodes(2015,"red")
print(nodes)

colori = DAO.getAllColori()
print(colori)