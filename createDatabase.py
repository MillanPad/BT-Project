import sqlite3
import xml.etree.ElementTree as ET
import subprocess
import re
import shutil
from datetime import datetime

def createTableMsg(archivo_xml):
    # Analizar el archivo XML
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    # Crear la conexión a la base de datos y el cursor
    conn = sqlite3.connect('tabla_vc_cards.db')
    c = conn.cursor()

    # Verificar si la tabla ya existe
    c.execute(f'SELECT name FROM sqlite_master WHERE type='table' AND name='vc_cards'')
    table_exists = c.fetchone()

    if not table_exists:
        # Crear la tabla si no existe
        c.execute('''CREATE TABLE vc_cards
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, handle INTEGER, subject TEXT, datetime TEXT, sender_name TEXT, sender_addressing TEXT, recipient_addressing TEXT, type TEXT)''')

    # Obtener el último id insertado
    c.execute("SELECT MAX(id) FROM vc_cards")
    last_id = c.fetchone()[0] or 0

    # Iterar sobre los elementos 'msg'
    for msg in root.findall('msg'):
        handle = msg.get('handle')
        subject = msg.get('subject')
        datetime_str = msg.get('datetime')
        sender_name = msg.get('sender_name')
        sender_addressing = msg.get('sender_addressing')
        recipient_addressing = msg.get('recipient_addressing')
        msg_type = msg.get('type')

        # Convertir el formato de fecha y hora a un objeto datetime
        datetime_obj = datetime.strptime(datetime_str, "%Y%m%dT%H%M%S")

        # Incrementar el id para el nuevo registro
        last_id += 1

        # Insertar los datos en la tabla
        c.execute("INSERT INTO vc_cards (id, handle, subject, datetime, sender_name, sender_addressing, recipient_addressing, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (last_id, handle, subject, datetime_obj, sender_name, sender_addressing, recipient_addressing, msg_type))

    # Confirmar los cambios y cerrar la conexión a la base de datos
    conn.commit()
    conn.close()
def createTableContacts(tabla):
    tree = ET.parse(f'{tabla}/telecom/pb/listing.xml')
    root = tree.getroot()
    conn = sqlite3.connect('bt-project.sqlite')
    c = conn.cursor()

    c.execute(f"CREATE TABLE {tabla} (id INTEGER PRIMARY KEY, nombre TEXT, telefono TEXT)")
    cont = 0
    for card in root.findall('card'):
        handle = card.get('handle')
        name = card.get('name')
        file = open(f'{tabla}/telecom/pb/{handle}', 'r')
        line = file.read()
        match = re.search(r'TEL;CELL:(\d+)',line)
        if match:
            tel = match.group(1)
        else:
            match2 = re.search(r'TEL;CELL:\+34(\d+)',line)
            if match2:
                tel = match2.group(1)
            else:
                tel = None

        c.execute(f"INSERT INTO {tabla} (nombre,telefono) VALUES ('{name}', '{tel}')")
        cont= cont + 1
    conn.commit()
    conn.close()
    shutil.rmtree(tabla)
