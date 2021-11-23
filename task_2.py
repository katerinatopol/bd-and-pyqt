"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
from task_1 import host_ping
import ipaddress


def host_range_ping(range_cidr):
    try:
        net = ipaddress.ip_network(range_cidr)
        hosts = list(map(str, net.hosts()))
        res = host_ping(hosts)
    except ValueError as err:
        print(f'Возникла ошибка: {err}')
        return

    return res


if __name__ == '__main__':
    res = host_range_ping('127.0.0.0/30')
    for el in res:
        print(f'{el[0]}, адрес: {el[1]}, ip: {el[2]}')
