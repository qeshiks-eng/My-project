#!/usr/bin/env python3 

import struct 
import argparse 

def parse_session_id(hex_string): 
    # Очищаем входную строку от пробелов 
    clean_hex = hex_string.replace(" ", "") 
    print(f"[*] Анализ сырых байтов Session ID: {clean_hex}") 
     
    try: 
        raw_bytes = bytes.fromhex(clean_hex) 
         
        if len(raw_bytes) != 8: 
            print("[-] Ошибка: Session ID должен быть ровно 8 байт (64 бит).") 
            return None 
             
        # Читаем как Little-Endian (Стандарт протокола SMB) 
        # < означает Little-endian, Q означает unsigned long long (8 байт)
        little_endian_val = struct.unpack('<Q', raw_bytes)[0] 
         
        # Читаем как Big-Endian (Сетевой стандарт) 
        # > означает Big-endian
        big_endian_val = struct.unpack('>Q', raw_bytes)[0] 
         
        print(f"[+] Little-Endian (SMB Standard) : {little_endian_val} [Hex: {hex(little_endian_val)}]") 
        print(f"[+] Big-Endian    (Raw Network)  : {big_endian_val} [Hex: {hex(big_endian_val)}]") 
         
        return little_endian_val 
         
    except ValueError as e: 
        print(f"[-] Ошибка конвертации байтов: {e}") 
        return None 

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="SMB Session ID Endianness Converter") 
    parser.add_argument("-x", "--hex", default="69 00 00 00 ac 1c 28 00", help="Сырой HEX дамп Session ID (8 байт)") 
    args = parser.parse_args() 
     
    parse_session_id(args.hex)
