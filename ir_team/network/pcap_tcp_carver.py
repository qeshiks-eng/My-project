#!/usr/bin/env python3 

import pyshark 
import argparse 

def carve_tcp_streams(pcap_file, target_port): 
    print(f"[*] Запуск DFIR-анализа TCP-стримов. Файл: {pcap_file} | Порт: {target_port}") 
     
    # Используем FileCapture для чтения дампа с применением Display фильтра 
    capture = pyshark.FileCapture(pcap_file, display_filter=f'tcp.port == {target_port}') 
     
    extracted_data = "" 
     
    try: 
        for packet in capture: 
            # Проверяем наличие TCP слоя и полезной нагрузки 
            if hasattr(packet, 'tcp') and hasattr(packet.tcp, 'payload'): 
                # PyShark отдает payload в виде HEX-строки, убираем двоеточия если они есть
                raw_hex = packet.tcp.payload.replace(':', '') 
                 
                try: 
                    # Декодируем байты в строку, игнорируя нечитаемые символы 
                    decoded_text = bytes.fromhex(raw_hex).decode('utf-8', errors='ignore') 
                    extracted_data += decoded_text 
                except Exception: 
                    continue 
                     
        capture.close() 
         
        if extracted_data: 
            print("[+] Восстановленная переписка (Reverse Shell Session):\n") 
            print("=" * 50) 
            print(extracted_data.strip()) 
            print("=" * 50) 
        else: 
            print("[-] Полезная нагрузка в TCP-стримах не найдена.") 
             
    except Exception as e: 
        print(f"[-] Ошибка при анализе дампа: {e}") 

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Automated TCP Stream Carver (Reverse Shell Forensics)") 
    parser.add_argument("-f", "--file", required=True, help="Путь к файлу PCAP") 
    parser.add_argument("-p", "--port", default=443, help="Целевой TCP-порт (По умолчанию: 443)") 
     
    args = parser.parse_args() 
    carve_tcp_streams(args.file, args.port)
