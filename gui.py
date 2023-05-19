from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QComboBox, QTabWidget, QLabel, QLineEdit, QListWidget
import bluetooth
import subprocess
from pprint import pprint
import pbapclient
import createDatabase
import shutil
import updateName
import getMac
class BluetoothConfigurator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BT-Project")
        self.resize(800, 600)  # Ajusta el tamaño de la ventana

        # Crear pestañas
        self.tab_widget = QTabWidget()
        self.bluetooth_tab = QWidget()
        self.message_tab = QWidget()
        self.agendaTel_tab = QWidget()
        self.conect_tab = QWidget()

        self.tab_widget.addTab(self.conect_tab, "Connect")
        self.tab_widget.addTab(self.bluetooth_tab, "Configuracion")
        self.tab_widget.addTab(self.message_tab, "Descargar Mensajes")
        self.tab_widget.addTab(self.agendaTel_tab, "Descargar Agenda Telefonica")
      

        # Organizar widgets de la pestaña Connect
        conect_layout = QVBoxLayout()
        self.conect_tab.setLayout(conect_layout)
        scan_button = QPushButton("Escanear")
        conect_button = QPushButton("Conectar")
        clon_button = QPushButton("Clonar")
        conect_layout.addWidget(scan_button)
        self.scan_list = QListWidget()
        conect_layout.addWidget(self.scan_list)
        conect_layout.addWidget(conect_button)
        conect_layout.addWidget(clon_button)


        # Organizar widgets de la pestaña Bluetooth
        bluetooth_layout = QVBoxLayout()
        self.bluetooth_tab.setLayout(bluetooth_layout)

        name_label = QLabel("Nombre:")
        self.name_entry = QLineEdit()

        address_label = QLabel("Direccion:")
        self.address_entry = QLineEdit()

        self.cod_major_combo_box = QComboBox()
        self.cod_major_combo_box.addItems(['Miscellaneous', 'Computer', 'Phone', 'LAN/Network Access point', 'Audio/Video', 'Peripheral', 'Imaging', 'Wearable', 'Toy', 'Health', 'Uncategorized'])

        classm_label = QLabel("Class of Device(Minor):")
        self.classm_entry = QLineEdit()

        update_button = QPushButton("Configurar")

        bluetooth_layout.addWidget(name_label)
        bluetooth_layout.addWidget(self.name_entry)
        bluetooth_layout.addWidget(address_label)
        bluetooth_layout.addWidget(self.address_entry)
        bluetooth_layout.addWidget(self.cod_major_combo_box)
        bluetooth_layout.addWidget(classm_label)
        bluetooth_layout.addWidget(self.classm_entry)
        bluetooth_layout.addWidget(update_button)

        # Organizar widgets de la pestaña Enviar mensaje
        message_layout = QVBoxLayout()
        self.message_tab.setLayout(message_layout)

        address_target_label = QLabel("Objetivo:")
        self.address_target_entry = QLineEdit()

        message_label = QLabel("Mensaje:")
        self.message_entry = QLineEdit()

        send_button = QPushButton("Enviar mensaje")

        message_layout.addWidget(address_target_label)
        message_layout.addWidget(self.address_target_entry)
        message_layout.addWidget(message_label)
        message_layout.addWidget(self.message_entry)
        message_layout.addWidget(send_button)

        # Organizar widgets de la ventana de descarga telefónica
        agenda_layout = QVBoxLayout()
        self.agendaTel_tab.setLayout(agenda_layout)

        address_targetTel_label = QLabel("Objetivo:")
        self.address_targetTel_entry = QLineEdit()

        table_base = QLabel("Nombre de la Tabla:")
        self.table_entry = QLineEdit()

        descarga_button = QPushButton("Descargar Agenda Telefonica:")
        self.bk_list = QListWidget()
        conect_layout.addWidget(self.bk_list)
        agenda_layout.addWidget(address_targetTel_label)
        agenda_layout.addWidget(self.address_targetTel_entry)
        agenda_layout.addWidget(table_base)
        agenda_layout.addWidget(self.table_entry)
        agenda_layout.addWidget(descarga_button)

        # Organizar pestañas en la ventana principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)

        # Conectar señales y slots
        conect_button.clicked.connect(self.conect_device)
        update_button.clicked.connect(self.update_bluetooth_config)
        send_button.clicked.connect(self.send_message)
        scan_button.clicked.connect(self.scan_devices)
        clon_button.clicked.connect(self.clon_devices)
        descarga_button.clicked.connect(self.descarga_agenda)

    def conect_device(self):
        print("Connection established")
        self.agent_daemon
        # Direccion MAC del dispositivo a conectar
        target_address = None
        if target_address is None:
            selected_items = [item.text() for item in self.scan_list.selectedItems()]
            palabras = []
            for texto in selected_items:
                if "Dispositivo:" in texto:
                    datos_dispositivo = texto.split("-")
                    palabras.extend(datos_dispositivo[1:])
                    target_address = palabras.pop(0)

        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_address, 1))

    def update_bluetooth_config(self):
        name = self.name_entry.text()
        address = self.address_entry.text()
        cod = self.classm_entry.text()

        updateName.updateName(address=address, name=name, cod=cod)
        subprocess.run(["sudo", "service", "bluetooth", "restart"])
        print("Nombre:", name)
        print("Direccion:", address)

    def send_message(self):
        address = self.address_target_entry.text()
        message = self.message_entry.text()

    def scan_devices(self):
        devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
        for (addr, name, cl) in devices:
            text = "Dispositivo: -{bdaddr}- Nombre: -{device_name}- Clase: -{class_of_device}-"
            text = text.format(bdaddr=addr, device_name=name, class_of_device=hex(cl))
            self.scan_list.addItem(text)

    def clon_devices(self):
        selected_items = [item.text() for item in self.scan_list.selectedItems()]
        palabras = []
        for texto in selected_items:
            if "Dispositivo:" in texto:
                datos_dispositivo = texto.split("-")
                palabras.extend(datos_dispositivo[1:])
        mac=getMac.obtener_mac_bluetooth()
        mac=mac[:17]
        #shutil.rmtree(f'/var/lib/bluetooth/{mac}')
        updateName.clone_device(palabras.pop(0), palabras.pop(1), palabras.pop(2))
        subprocess.run(["sudo", "service", "bluetooth", "restart"])

    def agent_daemon(self):
        print("Ejecutar agente NoInputNoOutput como daemon")
        subprocess.run(["bt-agent", "-c", "NoInputNoOutput", "-d"])

    def descarga_agenda(self):
        target = self.address_targetTel_entry.text()
        tabla = self.table_entry.text()
        pbapclient(target,tabla)
        createDatabase.createTableContacts(tabla)

if __name__ == "__main__":
    app = QApplication([])
    window = BluetoothConfigurator()
    window.show()
    app.exec_()
