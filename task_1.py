"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""
import socket
import ipaddress
import os
import subprocess


def host_ping(addresses_lst):
    for address in addresses_lst:
        try:
            try:
                ip = str(ipaddress.ip_address(address))
            except ValueError as err:
                try:
                    ip = socket.gethostbyname(address)
                except socket.gaierror as err:
                    print(f'Возникла ошибка: {err}')
                    continue

            ping = subprocess.call(['ping', address], stdout=open(os.devnull, 'w'))
            if ping == 0:
                print(f"Узел {ip} доступен")
            else:
                print(f'Узел {ip} недоступен')
        except ValueError as err:
            print(f'Возникла ошибка: {err}')


host_ping(['127.0.0.1', 'google.r;u', 'google.com', '1.1.1.1'])
