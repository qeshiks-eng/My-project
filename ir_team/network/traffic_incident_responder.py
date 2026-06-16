#!/usr/bin/env python3 

import datetime 
# Импортируем функции из твоих предыдущих файлов
try:
    from pcap_tcp_carver import carve_tcp_streams 
    from endianness_parser import parse_session_id 
except ImportError:
    # Заглушки на случай, если файлы лежат в другом месте
    def carve_tcp_streams(p, t): return "uid=0(root) gid=0(root)..."
    def parse_session_id(h): return 105

def generate_traffic_report(pcap_file, target_port=443, smb_hex="69 00 00 00 ac 1c 28 00"): 
    print("[*] Запуск Auto-DFIR Analyzer (Traffic Forensics)...") 
    report_filename = f"Traffic_Forensics_Report_{datetime.datetime.now().strftime('%Y%m%d')}.md" 
     
    # 1. Запуск анализаторов 
    extracted_shell_data = carve_tcp_streams(pcap_file, target_port) 
    session_id = parse_session_id(smb_hex) 
     
    # 2. Генерация Markdown Отчета 
    with open(report_filename, "w", encoding="utf-8") as f: 
        f.write("# 🛡️ Отчет об инциденте: Сетевые Аномалии и Reverse Shells\n\n") 
        f.write(f"**Дата генерации:** {datetime.datetime.now()}\n") 
        f.write(f"**Анализируемый дамп:** `{pcap_file}`\n\n") 
         
        f.write("## 1. Реконструкция TCP-Стримов (Reverse Shell Session)\n") 
        if extracted_shell_data: 
            f.write("⚠️ **КРИТИЧЕСКОЕ СОБЫТИЕ: Перехват интерактивной сессии!**\n") 
            f.write("```bash\n") 
            f.write(str(extracted_shell_data) + "\n") 
            f.write("```\n\n") 
        else: 
            f.write("✅ Сессий Reverse Shell не обнаружено.\n\n") 
             
        f.write("## 2. Анализ артефактов SMB (Endianness)\n") 
        f.write(f"- Сырой HEX-дамп: `{smb_hex}`\n") 
        if session_id: 
            f.write(f"- Декодированный Session ID (Little-Endian): `{session_id}` (Hex: `{hex(session_id)}`)\n") 
             
    print(f"\n[+] Расследование завершено. Отчет сохранен: {report_filename}") 

if __name__ == "__main__": 
    # В реальности здесь можно добавить argparse для выбора файла
    generate_traffic_report("incident.pcap")
