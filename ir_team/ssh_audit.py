import re
from collections import Counter

def audit_ssh_logs(log_file):
    print(f"[*] Запуск аудита SSH логов: {log_file}")
    
    # 1. Твой правильный RegEx паттерн для IPv4
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    
    # Инициализируем счетчик (работает как словарь, но сам ставит 0 для новых ключей)
    brute_force_attempts = Counter()
    
    try:
        with open(log_file, "r") as file:
            # 2. Читаем файл построчно (O(N) сложность, не забиваем оперативную память)
            for line in file:
                
                # 3. Фильтруем строки: нас интересуют только неудачные попытки пароля
                if "Failed password" in line:
                    
                    # 4. Ищем совпадение RegEx в строке
                    match = re.search(ip_pattern, line)
                    if match:
                        ip_address = match.group(0) # Извлекаем найденный IP
                        
                        # 5. Увеличиваем счетчик для данного IP на 1
                        brute_force_attempts[ip_address] += 1
                        
    except FileNotFoundError:
        print("[-] Файл логов не найден!")
        return

    print("\n[*] Анализ завершен. Результаты:")
    # 6. Выводим только те IP, которые пытались подобрать пароль больше 5 раз
    for ip, count in brute_force_attempts.items():
        if count > 5:
            print(f"[!!!] АЛЕРТ: Brute Force атака! IP: {ip} | Попыток: {count}")

if __name__ == "__main__":
    audit_ssh_logs("auth.log")