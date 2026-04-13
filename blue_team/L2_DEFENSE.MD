! Глобальное включение DHCP Snooping для защиты от поддельных DHCP-серверов
ip dhcp snooping
ip dhcp snooping vlan 1

! Настройка порта пользователя (Untrusted)
interface FastEthernet 0/1
 description USER_ACCESS_PORT
 switchport mode access
 
 ! Включение Port Security для защиты от MAC Flooding (генерации фейковых MAC)
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation shutdown
 
 ! Rate Limiting: Блокировка порта при аномальном количестве DHCP-запросов (защита от DHCP Starvation)
 ip dhcp snooping limit rate 5
exit

! Настройка порта магистрали (Trusted)
interface FastEthernet 0/24
 description UPLINK_TO_ROUTER
 ! Разрешаем ответы DHCP (Offer) только с этого порта
 ip dhcp snooping trust
exit