from scapy.all import rdpcap, DHCP, Ether, BOOTP

def analyze_pcap(pcap_file):
    print(f"[*] Анализ дампа: {pcap_file}")
    
    # "Белый список" MAC-адресов легитимных DHCP-серверов (настоящих роутеров)
    LEGIT_MACS =["00:50:56:c0:00:08", "aa:bb:cc:dd:ee:ff"]
    
    try:
        # Читаем все пакеты из PCAP-файла
        packets = rdpcap(pcap_file)
    except FileNotFoundError:
        print("[-] Файл дампа не найден.")
        return

    rogue_found = False

    # Проходим циклом по каждому пакету
    for pkt in packets:
        # 1. Проверяем наличие слоя DHCP
        if pkt.haslayer(DHCP):
            
            # 2. Вытаскиваем тип сообщения. Нас интересует DHCPOFFER (значение 2)
            # В Scapy опции хранятся как список кортежей:[('message-type', 2), ('router', '192...'), ...]
            for opt in pkt[DHCP].options:
                if opt[0] == "message-type" and opt[1] == 2:
                    
                    # 3. Извлекаем MAC-адрес отправителя (уровень L2)
                    mac_sender = pkt[Ether].src
                    
                    # 4. Извлекаем IP-адрес, который этот сервер пытается выдать жертве (уровень BOOTP)
                    offered_ip = pkt[BOOTP].yiaddr
                    
                    # 5. Проверка по белому списку
                    if mac_sender not in LEGIT_MACS:
                        print(f"[!!!] АЛЕРТ: Обнаружен Rogue DHCP Сервер!")
                        print(f"      [-] MAC Атакующего: {mac_sender}")
                        print(f"      [-] Предлагаемый IP жертве: {offered_ip}")
                        rogue_found = True
                    else:
                        print(f"[+] Легитимный DHCPOFFER от {mac_sender} (IP: {offered_ip})")

    if not rogue_found:
        print("[*] Аномалий не обнаружено. Сеть чиста.")

if __name__ == "__main__":
    # Для теста можешь подставить любой pcap файл
    analyze_pcap("capture.pcap")