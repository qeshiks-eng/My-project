#!/usr/bin/env python3
import datetime
from pcap_dhcp_hunter import analyze_pcap
from ssh_audit import audit_ssh_logs

def generate_report(pcap_file, log_file):
    print("[*] Запуск Auto-DFIR Analyzer...")
    
    # Предполагаем, что теперь функции возвращают словари с найденными угрозами
    rogue_dhcp_results = analyze_pcap(pcap_file)
    ssh_brute_results = audit_ssh_logs(log_file)
    
    report_filename = f"AitM_Incident_Report_{datetime.datetime.now().strftime('%Y%m%d')}.md"
    
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write("# 🛡️ Отчет об инциденте: Adversary-in-the-Middle (AitM)\n\n")
        f.write(f"**Дата генерации:** {datetime.datetime.now()}\n\n")
        
        f.write("## 1. Анализ сетевого трафика (L2/L3)\n")
        if rogue_dhcp_results:
            f.write("🚨 **КРИТИЧЕСКИЙ АЛЕРТ: Обнаружен Rogue DHCP!**\n")
            f.write(f"- MAC Атакующего: `{rogue_dhcp_results['mac']}`\n")
            f.write(f"- Выданный IP: `{rogue_dhcp_results['ip']}`\n\n")
        else:
            f.write("✅ Аномалий DHCP не обнаружено.\n\n")
            
        f.write("## 2. Анализ системных логов (SSH Brute Force)\n")
        if ssh_brute_results:
            for ip, data in ssh_brute_results.items():
                f.write(f"- **IP:** `{ip}` | **Попыток:** {data['count']} | **Abuse Score:** {data['score']}%\n")
        else:
            f.write("✅ Попыток Brute Force не обнаружено.\n")
            
    print(f"[+] Расследование завершено. Отчет сохранен: {report_filename}")

if __name__ == "__main__":
    generate_report("capture.pcap", "auth.log")