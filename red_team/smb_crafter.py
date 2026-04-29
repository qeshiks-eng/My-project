#!/usr/bin/env python3 

from scapy.all import IP, TCP, Raw, send, RandShort
import sys 

def craft_smb_negotiate(target_ip): 
    print(f"[*] Крафтинг пакета SMB2 Negotiate Protocol Request для {target_ip}:445...") 
     
    # 1. Формируем L3 и L4 
    ip_layer = IP(dst=target_ip) 
    # Используем случайный эфемерный порт источника 
    tcp_layer = TCP(sport=RandShort(), dport=445, flags="PA")  
     
    # 2. Сырая полезная нагрузка SMB2 Negotiate (NetBIOS Session Service + SMB2 Header + Negotiate Context) 
    # Начинается с \x00 (NetBIOS) и \xfeSMB (Magic Bytes) 
    smb_negotiate_payload = b"\x00\x00\x00\x48\xfeSMB\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x24\x00\x08\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x10\x02\x22\x02\x24\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" 

    # 3. Сборка матрешки 
    packet = ip_layer / tcp_layer / Raw(load=smb_negotiate_payload) 
     
    # 4. Отправка на L3 
    send(packet, verbose=False) 
    print(f"[+] Пакет успешно отправлен! Ожидайте генерации логов на сенсорах IDS.") 

if __name__ == "__main__": 
    if len(sys.argv) != 2: 
        print(f"Использование: python3 {sys.argv[0]} <Target_IP>") 
        sys.exit(1) 
         
    target = sys.argv[1]
    craft_smb_negotiate(target)
