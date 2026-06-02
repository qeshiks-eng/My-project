import os
#!/usr/bin/env python3 

import re 
import requests 
from collections import Counter 

# РљРѕРЅС„РёРіСѓСЂР°С†РёСЏ API 
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY", "") 
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check" 

def check_ip_reputation(ip): 
    """РћР±РѕРіР°С‰РµРЅРёРµ РёРЅС†РёРґРµРЅС‚Р° С‡РµСЂРµР· Threat Intelligence API (AbuseIPDB)""" 
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
        # Р•СЃР»Рё API-РєР»СЋС‡ РЅРµРІРµСЂРЅС‹Р№ РёР»Рё Р»РёРјРёС‚ РёСЃС‡РµСЂРїР°РЅ вЂ” РІС‹Р»РµС‚РёС‚ РѕС€РёР±РєР°
        response.raise_for_status()   
        data = response.json() 
        abuse_score = data["data"]["abuseConfidenceScore"] 
        return abuse_score     

    except Exception as e: 
        print(f"[-] РћС€РёР±РєР° TI API РґР»СЏ IP {ip}: {e}") 
        return "N/A" 
 
def audit_ssh_logs(log_file): 
    print(f"[*] Р—Р°РїСѓСЃРє Р°СѓРґРёС‚Р° SSH Р»РѕРіРѕРІ: {log_file}") 
    # Р РµРіСѓР»СЏСЂРєР° РґР»СЏ РїРѕРёСЃРєР° IP Р°РґСЂРµСЃРѕРІ
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" 
    brute_force_attempts = Counter() 

    try: 
        with open(log_file, "r", encoding="utf-8") as file: 
            for line in file: 
                # РС‰РµРј С‚РѕР»СЊРєРѕ СЃС‚СЂРѕРєРё СЃ РЅРµСѓРґР°С‡РЅС‹Рј РІС…РѕРґРѕРј
                if "Failed password" in line: 
                    match = re.search(ip_pattern, line) 
                    if match: 
                        ip_address = match.group(0) 
                        brute_force_attempts[ip_address] += 1 
                         
    except FileNotFoundError: 
        print(f"[-] Р¤Р°Р№Р» Р»РѕРіРѕРІ '{log_file}' РЅРµ РЅР°Р№РґРµРЅ!") 
        return None 

    print("\n[*] РђРЅР°Р»РёР· Р·Р°РІРµСЂС€РµРЅ. Р РµР·СѓР»СЊС‚Р°С‚С‹:") 

    results = {} 
    for ip, count in brute_force_attempts.items(): 
        if count > 5: # РџРѕСЂРѕРі: Р±РѕР»СЊС€Рµ 5 РЅРµСѓРґР°С‡РЅС‹С… РїРѕРїС‹С‚РѕРє
            print(f"[!] РћР±РЅР°СЂСѓР¶РµРЅ Brute Force! IP: {ip} | РџРѕРїС‹С‚РѕРє: {count}") 
            print(f"    [*] Р—Р°РїСЂРѕСЃ Threat Intelligence РґР»СЏ {ip}вЂ¦") 

            # РђРІС‚РѕРјР°С‚РёС‡РµСЃРєР°СЏ РїСЂРѕРІРµСЂРєР° СЂРµРїСѓС‚Р°С†РёРё
            score = check_ip_reputation(ip) 
            print(f"    [+] Abuse Confidence Score: {score}%\n") 
            results[ip] = {"count": count, "score": score}           

    return results 

if __name__ == "__main__": 
    # РЈР±РµРґРёСЃСЊ, С‡С‚Рѕ С„Р°Р№Р» auth.log Р»РµР¶РёС‚ СЂСЏРґРѕРј СЃРѕ СЃРєСЂРёРїС‚РѕРј
    audit_ssh_logs("auth.log")

