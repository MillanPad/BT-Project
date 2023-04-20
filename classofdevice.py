def cod_to_hex(cod_name):
   cod_values = {
        'Miscellaneous': '0x000000',
        'Computer': '0x000100',
        'Phone': '0x000200',
        'LAN/Network Access point': '0x000300',
        'Audio/Video': '0x000400',
        'Peripheral': '0x000500',
        'Imaging': '0x000600',
        'Wearable': '0x000700',
        'Toy': '0x000800',
        'Health': '0x000900',
        'Uncategorized': '0x1F0000'
    } 
   return cod_values.get(cod_name, None)
