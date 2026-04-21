#!/usr/bin/env python3 

import datetime
# Исправлен регистр в import и from
from pcap_hsrp_hunter import analyze_hsrp_pcap 
from ospf_audit import analyze_ospf_pcap 

def generate_routing_report(pcap_file): 
    print("[*] Запуск Auto-DFIR Analyzer (L2/L3 Routing Attacks)…") 
    
    # Генерация имени файла
    report_filename = f"Routing_Incident_Report_{datetime.datetime.now().strftime('%Y%m%d')}.md"

    # Исправлены кавычки и логика записи f-строк
    with open(report_filename, "w", encoding="utf-8") as f: 
        f.write("# 🛡️ Отчет об инциденте: Атаки на протоколы маршрутизации (L2/L3)\n\n") 
        f.write(f"**Дата генерации:** {datetime.datetime.now()}\n") 
        f.write(f"**Анализируемый дамп:** `{pcap_file}`\n\n") 
         
        f.write("## 1. Анализ протоколов резервирования (HSRP)\n") 
        f.write("> *Проверка логов выведена в консоль DFIR-аналитика.* Запуск модуля `pcap_hsrp_hunter`…\n\n") 
        # Вызываем функцию анализа HSRP
        analyze_hsrp_pcap(pcap_file) 
         
        f.write("## 2. Анализ динамической маршрутизации (OSPF)\n") 
        f.write("> *Проверка логов выведена в консоль DFIR-аналитика.* Запуск модуля `ospf_audit`…\n\n") 
        # Вызываем функцию анализа OSPF
        analyze_ospf_pcap(pcap_file) 
             
    print(f"\n[+] Расследование завершено. Отчет сохранен: {report_filename}") 

if __name__ == "__main__": 
    # Исправлен вызов функции (с маленькой буквы)
    generate_routing_report("routing_incident.pcap")
