import bluetooth
import classofdevice
import subprocess
import shlex
import fileinput
import re
def clone_device(mac_address,nombre,class_of_device):
    mac_address = ''.join(c for c in mac_address if c.isalnum())

    # Cambiar la dirección MAC con bdaddr
    comando_mac = ["sudo", "./bdaddr", "-r", mac_address]
    subprocess.run(comando_mac, capture_output=True)

    # Cambiar el nombre del dispositivo
    comando_nombre = f"sudo hciconfig -a hci0 name '{nombre}'"
    subprocess.Popen(shlex.split(comando_nombre))

    # Cambiar la clase de dispositivo
    comando_class = f"sudo hciconfig -a hci0 class {class_of_device}"
    subprocess.run(shlex.split(comando_class), capture_output=True)

    # Reiniciar el servicio Bluetooth
   # comando_restart = ['sudo', 'systemctl', 'restart', 'bluetooth.service']
    #subprocess.Popen(comando_restart)
def clone_deviceFile(mac, nombre, clase):
    archivo = '/etc/bluetooth/main.conf'

    # Patrones de búsqueda
    nombre_patron = r'^\s*Name\s*=\s*.*$'
    mac_patron = r'^\s*Device\s*=\s*.*$'
    clase_patron = r'^\s*Class\s*=\s*.*$'

    # Reemplazar el nombre del dispositivo Bluetooth
    nuevo_nombre = 'Name = {}'.format(nombre)
    for linea in fileinput.input(archivo, inplace=True):
        if re.match(nombre_patron, linea):
            print(nuevo_nombre)
        else:
            print(linea.strip())

    # Reemplazar la dirección MAC del dispositivo Bluetooth
    nueva_mac = 'Device = {}'.format(mac)
    for linea in fileinput.input(archivo, inplace=True):
        if re.match(mac_patron, linea):
            print(nueva_mac)
        else:
            print(linea.strip())

    # Reemplazar la clase de dispositivo Bluetooth
    nueva_clase = 'Class = {}'.format(clase)
    for linea in fileinput.input(archivo, inplace=True):
        if re.match(clase_patron, linea):
            print(nueva_clase)
        else:
            print(linea.strip())
