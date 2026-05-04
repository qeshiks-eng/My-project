# 1. Запись SPF (Sender Policy Framework)
# Строгий запрет (-all) на отправку писем с любых IP, кроме авторизованного почтового шлюза (192.168.1.100).
school21.local. IN TXT "v=spf1 ip4:192.168.1.100 -all"

# 2. Запись DMARC
# Установка жесткой политики отклонения (p=reject) для писем, проваливших проверку SPF/DKIM.
_dmarc.school21.local. IN TXT "v=DMARC1; p=reject; rua=mailto:security@school21.local;"
