from database.DB_connect import DBConnect
from model.connessione import Connessione
import model.model
from model.product import Product


class DAO():
    def __init__(self):
        pass



    @staticmethod
    def getAllNodes(anno, colore):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select p.Product_number,p.Product_line, p.Product_type, p.Product, p.Product_brand, p.Product_color, p.Unit_cost, p.Unit_price
                    from go_products p, go_daily_sales gds 
                    where year(gds.Date) = %s
                    and p.Product_color = %s
                    and p.Product_number = gds.Product_number
                    group by p.Product_number,p.Product_line, p.Product_type, p.Product, p.Product_brand, p.Product_color, p.Unit_cost, p.Unit_price"""
        cursor.execute(query,(anno, colore))

        results = []

        for row in cursor:
            results.append(Product(**row))

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def getAllColori():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct(Product_color)
                    from go_products
                    """
        cursor.execute(query, ())

        results = []

        for row in cursor:
            results.append(row["Product_color"])

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def getAllEdges(anno, colore, idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select g1.Product_number as p1, g2.Product_number as p2 , g1.Retailer_code, g1.`Date`,count(g1.Date) as N
                    from go_daily_sales g1, go_daily_sales g2
                    where g1.Retailer_code = g2.Retailer_code 
                    and g1.`Date` = g2.`Date`
                    and g1.Product_number in (select Product_number from go_products gp where gp.Product_color = %s)
                    and g2.Product_number in (select Product_number from go_products gp where gp.Product_color = %s)
                    and g1.Product_number > g2.Product_number 
                    and year(g1.Date)=%s
                    group by g1.Product_number , g2.Product_number 

 """
        cursor.execute(query, (colore, colore, anno))

        results = []

        for row in cursor:
            results.append(Connessione(idMap[row["p1"]],  idMap[row["p2"]], row["N"]))

        cursor.close()
        cnx.close()

        return results



