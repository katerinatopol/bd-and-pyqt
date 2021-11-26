"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
"""
from tabulate import tabulate

from task_1 import host_ping
import ipaddress


def host_range_ping_tab(range_cidr):
    reachable = []
    unreachable = []

    try:
        net = ipaddress.ip_network(range_cidr)
        hosts = list(map(str, net.hosts()))
        res = host_ping(hosts)

    except ValueError as err:
        print(f'Возникла ошибка: {err}')
        return

    for el in res:
        if el[0] == 'Узел доступен':
            reachable.append(el[2])
        else:
            if el[2] != 'Не определен':
                unreachable.append(el[2])

    all_word = ['Reachable', 'Unreachable']
    sh_ip_int_br = [('\n'.join(reachable), '\n'.join(unreachable))]
    print(tabulate(sh_ip_int_br, headers=all_word))

    return res


if __name__ == '__main__':
    host_range_ping_tab('127.0.0.0/30')
