import bluetooth
import classofdevice
import subprocess

def updateName(address,name,cod):
    bluetooth.set_l2cap_name(name)
    # Cambiar el CoD a "Miscellaneous" (valor hexadecimal: 0x000000)
    bluetooth.set_l2cap_class(classofdevice.cod_to_hex(cod_name=cod))

    subprocess.run(['bdaddr','-i','hci0','00:01:E3:64:DD:9B'])


    # Guardar el archivo de configuración
    