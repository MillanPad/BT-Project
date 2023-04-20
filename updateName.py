import bluetooth
import configparser
import classofdevice


def updateName(address,name,cod):
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((address, 1))
    # Abrir el archivo de configuración
    config = configparser.ConfigParser()
    config.read('/etc/bluetooth/main.conf')

    # Cambiar el CoD a "Miscellaneous" (valor hexadecimal: 0x000000)
    config['General']['Class'] = classofdevice.cod_to_hex('Audio/Video', 'Headphones')


    # Guardar el archivo de configuración
    with open('/etc/bluetooth/main.conf', 'w') as configfile:
        config.write(configfile)

    socket.send(f"AT+NAME{str(name)}\r\n".encode())
    socket.send(f"AT+ADDR{str(address)}\r\n".encode())
    socket.close()