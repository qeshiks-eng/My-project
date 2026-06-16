#!/usr/bin/env python3 

import re 
import requests 
from collections import Counter 

# Конфигурация API 
ABUSEIPDB_API_KEY = "РЕАЛЬНЫЙ_API_КЛЮЧ" 
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check" 

def check_ip_reputation(ip): 
    """Обогащение инцидента через Threat Intelligence API (AbuseIPDB)""" 
    headers = { 
        "Key": ABUSEIPDB_API_KEY, 
        "Accept": "application/json" 
    } 
    params = { 
        "ipAddress": ip, 
        "maxAgeInDays": "90" 
    }      
    try: 
        response = requests.get(ABUSEIPDB_URL, headers=headers, params=params, timeout=5) 
        # Если API-ключ неверный или лимит исчерпан — вылетит ошибка
        response.raise_for_status()   
        data = response.json() 
        abuse_score = data["data"]["abuseConfidenceScore"] 
        return abuse_score     

    except Exception as e: 
        print(f"[-] Ошибка TI API для IP {ip}: {e}") 
        return "N/A" 
 
def audit_ssh_logs(log_file): 
    print(f"[*] Запуск аудита SSH логов: {log_file}") 
    # Регулярка для поиска IP адресов
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" 
    brute_force_attempts = Counter() 

    try: 
        with open(log_file, "r", encoding="utf-8") as file: 
            for line in file: 
                # Ищем только строки с неудачным входом
                if "Failed password" in line: 
                    match = re.search(ip_pattern, line) 
                    if match: 
                        ip_address = match.group(0) 
                        brute_force_attempts[ip_address] += 1 
                         
    except FileNotFoundError: 
        print(f"[-] Файл логов '{log_file}' не найден!") 
        return None 

    print("\n[*] Анализ завершен. Результаты:") 

    results = {} 
    for ip, count in brute_force_attempts.items(): 
        if count > 5: # Порог: больше 5 неудачных попыток
            print(f"[!] Обнаружен Brute Force! IP: {ip} | Попыток: {count}") 
            print(f"    [*] Запрос Threat Intelligence для {ip}…") 

            # Автоматическая проверка репутации
            score = check_ip_reputation(ip) 
            print(f"    [+] Abuse Confidence Score: {score}%\n") 
            results[ip] = {"count": count, "score": score}           

    return results 

if __name__ == "__main__": 
    # Убедись, что файл auth.log лежит рядом со скриптом
    audit_ssh_logs("auth.log")
