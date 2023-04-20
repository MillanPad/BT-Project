import bluetooth

def sendMsg(address,message):
    # Conectamos con el dispositivo Bluetooth
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((address, 3))
    socket.send(f"AT+MAPSND={str(message)}\r\n".encode())
    socket.close()