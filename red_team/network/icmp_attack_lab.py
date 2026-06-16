from scapy.all import IP, ICMP, send

# Отправляем сами себе на локальный адрес (или адрес роутера)
my_packet = IP(dst="127.0.0.1") / ICMP() / "STOLEN_DATA=password123"

print("[*] Отправка ICMP-пакета со скрытой нагрузкой...")
send(my_packet)
print("[+] Пакет успешно отправлен! Ищите пароль в Hex-дампе Wireshark.")