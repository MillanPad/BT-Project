def cod_to_hex(cod_major_name,cod_minor_name):
    cod_values = {
    'Miscellaneous': {
            'Uncategorized': '0x00000000'
        },
        'Computer': {
            'Desktop workstation': '0x00000104',
            'Server-class computer': '0x00000108',
            'Laptop': '0x0000010C',
            'Handheld PC/PDA (clamshell)': '0x00000110',
            'Palm sized PC/PDA': '0x00000114',
            'Wearable computer (watch sized)': '0x00000118'
        },
        'Phone': {
            'Cellular': '0x00000204',
            'Cordless': '0x00000208',
            'Smartphone': '0x0000020C',
            'Wired modem or voice gateway': '0x00000210',
            'Common ISDN Access': '0x00000214'
        },
        'LAN/Network Access point': {
            'Fully available': '0x00000304',
            '1-17% utilized': '0x00000308',
            '17-33% utilized': '0x0000030C',
            '33-50% utilized': '0x00000310',
            '50-67% utilized': '0x00000314',
            '67-83% utilized': '0x00000318',
            '83-99% utilized': '0x0000031C'
        },
        'Audio/Video': {
            'Wearable headset device': '0x00000440',
            'Hands-free device': '0x00000444',
            'Microphone': '0x00000448',
            'Loudspeaker': '0x0000044C',
            'Headphones': '0x00000458',
            'Portable audio': '0x0000045C',
            'Car audio': '0x00000460',
            'Set-top box': '0x00000464',
            'HiFi audio device': '0x00000468',
            'VCR': '0x0000046C',
            'Video camera': '0x00000470',
            'Camcorder': '0x00000474',
            'Video monitor': '0x00000478',
            'Video display and loudspeaker': '0x0000047C',
            'Video conferencing': '0x00000480'
        },
        'Peripheral': {
            'Joystick': '0x00000504',
            'Gamepad': '0x00000508',
            'Remote control': '0x0000050C',
            'Sensing device': '0x00000510',
            'Digitizer tablet': '0x00000520',
            'Card reader': '0x00000524'
        },
        'Imaging': {
            'Display': '0x00000604',
            'Camera': '0x00000608',
            'Scanner': '0x0000060C',
            'Printer': '0x00000610'
        },
        'Wearable': {
            'Wristwatch': '0x00000704',
            'Pager': '0x00000708',
            'Jacket': '0x0000070C',
            'Helmet': '0x00000710',
            'Glasses': '0x00000714'
        },
        'Toy': {
            'Robot': '0x00000804',
            'Vehicle': '0x00000808',
            'Doll/action figure': '0x0000080C',
            'Controller': '0x00000810',
            'Game': '0x00000814'
        },
        'Health': {
            'Blood pressure monitor': '0x00000904',
            'Thermometer': '0x00000908',
            'Weighing scale': '0x0000090C',
            'Glucose meter': '0x00000910',
            'Pulse oximeter': '0x00000914',
            'Heart/Pulse rate monitor': '0x00000918',
            'Health data display': '0x0000091C',
            'Step Counter': '0x00000920'
        },
        'Uncategorized': {
            'Reserved': '0x00001F00'
        }
    }
    if cod_major_name not in cod_values:  # Comprueba si el nombre de la categoría principal es válido
        raise ValueError(f'Invalid COD major name: {cod_major_name}')

    if cod_minor_name is not None:  # Si se proporciona un nombre de subcategoría, devuelve su valor hexadecimal
        if cod_minor_name not in cod_values[cod_major_name]:
            raise ValueError(f'Invalid COD minor name: {cod_minor_name} for COD major name: {cod_major_name}')
        return cod_values[cod_major_name][cod_minor_name]

    return cod_values[cod_major_name]['Uncategorized']  # Si no se proporciona un nombre de subcategoría, devuelve el valor para "Uncategorized"


