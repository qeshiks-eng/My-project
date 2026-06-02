#!/usr/bin/env python3
import os
from scapy.all import rdpcap, HSRP, Ether 
import sys 

def analyze_hsrp_pcap(pcap_file, expected_password=None):
    expected_password = expected_password or os.getenv("LAB_HSRP_EXPECTED_AUTH", "<LAB_EXPECTED_AUTH>") 
    print(f"[*] Запуск DFIR-анализа HSRP для дампа: {pcap_file}") 
    try: 
        packets = rdpcap(pcap_file) 
    except FileNotFoundError: 
        print(f"[-] Ошибка: Файл {pcap_file} не найден.") 
        return 
    
    anomalies_found = 0 
    
    for pkt in packets: 
        if pkt.haslayer(HSRP): 
            mac_sender = pkt[Ether].src 
            hsrp_layer = pkt[HSRP]   
            priority = hsrp_layer.priority 
            raw_auth = hsrp_layer.auth 

            # Декодируем пароль и отрезаем нуль-байты 
            try: 
                clear_password = raw_auth.decode('ascii').rstrip('\x00') 
            except UnicodeDecodeError: 
                clear_password = "<BINARY_DATA_OR_MD5>" 

            # Логика детектирования аномалий 
            if priority == 255: 
                print(f"[!!!] АЛЕРТ: Обнаружен HSRP Coup d'état! MAC {mac_sender} форсирует Priority 255.") 
                anomalies_found += 1 
            if clear_password != expected_password and clear_password != "<BINARY_DATA_OR_MD5>": 
                print(f"[!!!] АЛЕРТ: Неверный HSRP-пароль от MAC {mac_sender}. Получено: '{clear_password}'") 
                anomalies_found += 1 

    if anomalies_found == 0: 
        print("[+] Аномалий в HSRP-трафике не обнаружено. Базовая линия в норме.") 
    else: 
        print(f"[-] Расследование завершено. Найдено аномалий: {anomalies_found}") 

if __name__ == "__main__": 

    analyze_hsrp_pcap("hsrp_incident.pcap") 
