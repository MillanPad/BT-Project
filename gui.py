from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QTabWidget, QLabel, QLineEdit, QListWidget
from bluetooth import *
import subprocess
from pprint import pprint
import pbapclient
import createDatabase
import sendMsg
import updateName
class BluetoothConfigurator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BT-Project")

        # Crear pestañas
        self.tab_widget = QTabWidget()
        self.bluetooth_tab = QWidget()
        self.message_tab = QWidget()
        #self.scan_tab = QWidget()
        #self.agent_tab = QWidget()
        self.agendaTel_tab = QWidget()
        self.conect_tab = QWidget()
        self.tab_widget.addTab(self.conect_tab,"Connect")
        self.tab_widget.addTab(self.bluetooth_tab, "Configuracion")
        self.tab_widget.addTab(self.message_tab, "Enviar mensaje")
        #self.tab_widget.addTab(self.scan_tab,"Escanear")
        #self.tab_widget.addTab(self.agent_tab,"Agente/Bypass")
        self.tab_widget.addTab(self.agendaTel_tab, "Descargar Agenda Telefonica")
        #Organizar widgets de pestaña Connect
        conect_layout = QVBoxLayout()
        self.conect_tab.setLayout(conect_layout)

        target_label = QLabel("Conectarse a:")
        conect_layout.addWidget(target_label)

        self.target_entry = QLineEdit()
        conect_layout.addWidget(self.target_entry)

        conect_button = QPushButton("Conectarse")
        conect_button.clicked.connect(self.conect_device)
        conect_layout.addWidget(conect_button)
        # Organizar widgets de pestaña Bluetooth
        bluetooth_layout = QVBoxLayout()
        self.bluetooth_tab.setLayout(bluetooth_layout)

        name_label = QLabel("Nombre:")
        bluetooth_layout.addWidget(name_label)

        self.name_entry = QLineEdit()
        bluetooth_layout.addWidget(self.name_entry)

        address_label = QLabel("Dirección:")
        bluetooth_layout.addWidget(address_label)

        self.address_entry = QLineEdit()
        bluetooth_layout.addWidget(self.address_entry)

        class_label = QLabel("Class of Device:")
        bluetooth_layout.addWidget(class_label)
        

        self.class_entry = QLineEdit()
        bluetooth_layout.addWidget(self.class_entry)

        update_button = QPushButton("Configurar")
        update_button.clicked.connect(self.update_bluetooth_config)
        bluetooth_layout.addWidget(update_button)

        # Organizar widgets de pestaña Enviar mensaje
        message_layout = QVBoxLayout()
        self.message_tab.setLayout(message_layout)

        address_target_label = QLabel("Objetivo:")
        message_layout.addWidget(address_target_label)

        self.address_target_entry = QLineEdit()
        message_layout.addWidget(self.address_target_entry)

        message_label = QLabel("Mensaje:")
        message_layout.addWidget(message_label)

        self.message_entry = QLineEdit()
        message_layout.addWidget(self.message_entry)

        send_button = QPushButton("Enviar mensaje")
        send_button.clicked.connect(self.send_message)
        message_layout.addWidget(send_button)
        # Organizar pestaña escaneo
        #scan_layout = QVBoxLayout()
        #self.scan_tab.setLayout(scan_layout)

        scan_button = QPushButton("Escanear")
        scan_button.clicked.connect(self.scan_devices)
        conect_layout.addWidget(scan_button)

        self.scan_list = QListWidget()
        conect_layout.addWidget(self.scan_list)

        clon_button = QPushButton("Clonar")
        clon_button.clicked.connect(self.clon_devices)
        conect_layout.addWidget(clon_button)

        # Organizar pestaña del agente/bypass
        #agent_layout = QVBoxLayout()
        #self.agent_tab.setLayout(agent_layout)

        agent_button = QPushButton("Activar agente NoInputNoOutput")
        agent_button.setStyleSheet('background-color: gray')
        agent_button.clicked.connect(self.agent_daemon)
        conect_layout.addWidget(agent_button)
        #Organizar widgets de la ventana de descarga telefonica
        agenda_layout = QVBoxLayout()
        self.agendaTel_tab.setLayout(agenda_layout)

        address_targetTel_label = QLabel("Objetivo:")
        agenda_layout.addWidget(address_targetTel_label)

        self.address_targetTel_entry = QLineEdit()
        agenda_layout.addWidget(self.address_targetTel_entry)

        table_base = QLabel("Nombre de la Tabla:")
        agenda_layout.addWidget(table_base)

        self.table_entry = QLineEdit()
        agenda_layout.addWidget(self.table_entry)

        descarga_button = QPushButton("Descargar Agenda Telefonica:")
        descarga_button.clicked.connect(self.descarga_agenda)
        agenda_layout.addWidget(descarga_button)
        # Organizar pestañas en la ventana principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)

    def conect_device(self):
        print("Connection established")

        # Dirección MAC del dispositivo a conectar
        target_address = self.target_entry.text()

        # Crear un socket Bluetooth
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        # Conectarse al dispositivo
        sock.connect((target_address, 1))


    def update_bluetooth_config(self):
        name = self.name_entry.text()
        address = self.address_entry.text()
        cod = self.class_entry.text()

        updateName.updateName(address=address,name=name,cod=cod)
        subprocess.run(["sudo", "service","bluetooth","restart"])
        print("Nombre:", name)
        print("Dirección:", address)

    def send_message(self):
        address = self.address_target_entry.text()
        message = self.message_entry.text()
        sendMsg.sendMsg(address=address,message=message)
        

    def scan_devices(self):
        devices = discover_devices()
        for bdaddr in devices:
            class_of_device = bluetooth.read_class_of_device(bdaddr)
            device_name = bluetooth.lookup_name(bdaddr)
        text= f"Dispositivo: -{bdaddr}- Nombre: -{device_name}- - Clase: -{class_of_device}-"
        
        self.scan_list.addItem(text)
        
    def clon_devices(self):
        selected_items = [item.text() for item in self.scan_list.selectedItems()]
        palabras = []
        for texto in selected_items:
            # Buscar la cadena "Dispositivo:" en la cadena de texto
            if "Dispositivo:" in texto:
                # Separar los datos del dispositivo en una lista de palabras
                datos_dispositivo = texto.split("-")
                palabras.extend(datos_dispositivo[1:]) # se omite el primer elemento "Dispositivo:"
        print(palabras.pop(0))
        print(palabras.pop(1))
        print(palabras.pop(2))

        #print(selected_items)
    def agent_daemon(self):
        print("Ejecutar agente NoInputNoOutput como daemon")
        subprocess.run(["bt-agent", "-c","NoInputNoOutput","-d"])

    def descarga_agenda(self):
        target = self.address_targetTel_entry.text()
        tabla = self.table_entry.text()
        pbapclient.main(target=target,table=tabla)
        createDatabase.createDatabase(tabla=tabla)

        
if __name__ == "__main__":
    app = QApplication([])
    window = BluetoothConfigurator()
    window.show()
    app.exec_()
