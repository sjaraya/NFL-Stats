import urllib
from bs4 import BeautifulSoup
import mysql.connector
#------------------------------------------------------------------------------------------------
#Metodo donde se obtiene el contenido de la pagina por medio del url
#------------------------------------------------------------------------------------------------
def makeSoup(url):
    page = urllib.urlopen(url)
    soupData = BeautifulSoup(page,'html.parser')
    return soupData
#------------------------------------------------------------------------------------------------
#Metodo donde se extrae la informacion de la tabla
#------------------------------------------------------------------------------------------------
def dataExtract():

    soup = makeSoup("http://www.espn.com.mx/futbol-americano/nfl/estadisticas/jugador/_/stat/defense/sort/totalTackles/temporada/2016/tipoTemporada/2")

    for record in soup.find_all('tr')[2:]:
        playerData = ""
        for data in record.find_all('td')[0:]:
            playerData = playerData + data.text + "-"
        dataList = playerData.split("-")
        dataToMySql(dataList)

#Metodo que almacena los datos en BD mysql
#------------------------------------------------------------------------------------------------
def dataToMySql(data):

    #no insertar datos del encabezado de la tabla
    if (data[0].isdigit() == True):
        connection = mysql.connector.connect(host="us-cdbr-iron-east-03.cleardb.net", user="b28e625cd4879c", password="aa308484", database="heroku_89813343cbae018")
        # se obtiene el objeto para ejecutar los queries
        cursor = connection.cursor()
        # se ejecuta el query
        cursor.execute(
            "Insert into stats(rank, player, team, ast, total, comb, sck, ydsl, pdef, ints, yds, intlong, itd, ff, rec, ftd) values(" +
            data[0] + ", '" + data[1] + "', '" + data[2] + "', " + data[3] + ", " + data[4] + ", " + data[5] + ", " +
            data[6] + ", " + data[7] + ", " + data[8] + ", " + data[9] + ", " + data[10] + ", " + data[11] + ", " +
            data[12] + ", " + data[13] + ", " + data[14] + ", " + data[15] + ")")
        connection.commit()
        connection.close()
        
#Metodo ver los datos de la tabla stats de la base de datos
#------------------------------------------------------------------------------------------------
def showData():
     
    connection = mysql.connector.connect(host="us-cdbr-iron-east-03.cleardb.net", user="b28e625cd4879c", password="aa308484", database="heroku_89813343cbae018")
    # se obtiene el objeto para ejecutar los queries
    cursor = connection.cursor()
    # se ejecuta el query
    cursor.execute(
            "Select * from stats")
    result = cursor.fetchall()
    for row in result:
        print row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[4] + " " + row[5] + " " + row[6] + " " + row[7] + " " + row[8] + " " + row[9] + " " + row[10] + " " + row[11] + " " + row[12] + " " + row[13] + " " + row[14] + " " + row[15]
    connection.commit()
    connection.close()
#------------------------------------------------------------------------------------------------
#dataExtract()
showData()
