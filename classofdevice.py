def cod_to_hex(cod_major_name, cod_minor_name=None):
    cod_values = {
        'Miscellaneous': {
            'Uncategorized': '0000'
        },
        'Computer': {
            'Desktop workstation': '0104',
            'Server-class computer': '0108',
            'Laptop': '010C',
            'Handheld PC/PDA (clamshell)': '0110',
            'Palm sized PC/PDA': '0114',
            'Wearable computer (watch sized)': '0118'
        },
        'Phone': {
            'Cellular': '0204',
            'Cordless': '0208',
            'Smartphone': '020C',
            'Wired modem or voice gateway': '0210',
            'Common ISDN Access': '0214'
        },
        'LAN/Network Access point': {
            'Fully available': '0304',
            '1-17% utilized': '0308',
            '17-33% utilized': '030C',
            '33-50% utilized': '0310',
            '50-67% utilized': '0314',
            '67-83% utilized': '0318',
            '83-99% utilized': '031C'
        },
        'Audio/Video': {
            'Wearable headset device': '0440',
            'Hands-free device': '0444',
            'Microphone': '0448',
            'Loudspeaker': '044C',
            'Headphones': '0458',
            'Portable audio': '045C',
            'Car audio': '0460',
            'Set-top box': '0464',
            'HiFi audio device': '0468',
            'VCR': '046C',
            'Video camera': '0470',
            'Camcorder': '0474',
            'Video monitor': '0478',
            'Video display and loudspeaker': '047C',
            'Video conferencing': '0480'
        },
        'Peripheral': {
            'Joystick': '0504',
            'Gamepad': '0508',
            'Remote control': '050C',
            'Sensing device': '0510',
            'Digitizer tablet': '0520',
            'Card reader': '0524'
        },
        'Imaging': {
            'Display': '0604',
            'Camera': '0608',
            'Scanner': '060C',
            'Printer': '0610'
        },
        'Wearable': {
            'Wristwatch': '0704',
            'Pager': '0708',
            'Jacket': '070C',
            'Helmet': '0710',
            'Glasses': '0714'
        },
        'Toy': {
            'Robot': '0804',
            'Vehicle': '0808',
            'Doll/action figure': '080C',
            'Controller': '0810',
            'Game': '0814'
        },
        'Health': {
            'Blood pressure monitor': '0904',
            'Thermometer': '0908',
            'Weighing scale': '090C',
            'Glucose meter': '0910',
            'Pulse oximeter': '0914',
            'Heart/Pulse rate monitor': '0918',
            'Health data display': '091C',
            'Step Counter': '0920'
        },
        'Uncategorized': {
            'Reserved': '1F00'
        }
    }
    if cod_major_name not in cod_values:  # Comprueba si el nombre de la categoría principal es válido
        raise ValueError(f'Invalid COD major name: {cod_major_name}')

    if cod_minor_name is not None:  # Si se proporciona un nombre de subcategoría, devuelve su valor hexadecimal
        if cod_minor_name not in cod_values[cod_major_name]:
            raise ValueError(f'Invalid COD minor name: {cod_minor_name} for COD major name: {cod_major_name}')
        return cod_values[cod_major_name][cod_minor_name]

    return cod_values[cod_major_name]['Uncategorized']  # Si no se proporciona un nombre de subcategoría, devuelve el valor para "Uncategorized"
