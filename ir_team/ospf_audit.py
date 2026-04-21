#!/usr/bin/env python3 

from scapy.all import rdpcap, IP, load_contrib
# Подгружаем модуль OSPF до импорта заголовков
load_contrib('ospf') 
from scapy.contrib.ospf import OSPF_Hdr 

def analyze_ospf_pcap(pcap_file): 
    print(f"[*] Запуск DFIR-анализа OSPF для дампа: {pcap_file}") 
    try: 
        packets = rdpcap(pcap_file) 
    except FileNotFoundError: 
        print(f"[-] Ошибка: Файл {pcap_file} не найден.") 
        return 

    alerts = 0 

    for pkt in packets: 
        if pkt.haslayer(OSPF_Hdr): 
            # В Scapy поле может называться authtype или auth_type
            auth_type = pkt[OSPF_Hdr].authtype 
            src_ip = pkt[IP].src if pkt.haslayer(IP) else "Unknown" 
            
            if auth_type == 0: 
                print(f"[!!!] АЛЕРТ: OSPF без аутентификации (Null)! Отправитель: {src_ip}") 
                alerts += 1 
            elif auth_type == 1: 
                print(f"[!!!] АЛЕРТ: OSPF с паролем в открытом виде (Plaintext)! Отправитель: {src_ip}") 
                alerts += 1 

    if alerts == 0: 
        print("[+] OSPF-трафик защищен (MD5/SHA). Аномалий не обнаружено.") 
    else: 
        print(f"[-] Расследование завершено. Найдено уязвимых OSPF-пакетов: {alerts}") 

if __name__ == "__main__": 
    analyze_ospf_pcap("routing_incident.pcap")
