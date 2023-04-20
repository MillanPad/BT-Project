import sqlite3
import xml.etree.ElementTree as ET


def createDatabase(tabla):
    tree = ET.parse(f'{tabla}/telecom/pb/mlisting.xml')
    root = tree.getroot()
    conn = sqlite3.connect('bt-project.sqlite')
    c = conn.cursor()

    c.execute('''CREATE  ?
                (id INTEGER PRIMARY KEY, nombre TEXT, telefono TEXT)''',(tabla))

    for card in root.findall('card'):
        handle = card.get('handle')
        name = card.get('name')
        vcard_tree = ET.parse(handle)
        vcard_root = vcard_tree.getroot()
        tel = vcard_root.find("./TEL[@TYPE='CELL']").text
        c.execute("INSERT INTO ? (nombre, telefono) VALUES (?, ?)", (tabla,name, tel))

    conn.commit()
    conn.close()
