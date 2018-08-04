#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import socket

REPUTATION_URL = "score.senderscore.com"


def reverse_ip(ip):
    octets = ip.split(".")
    octets.reverse()
    return ".".join(octets)


def read_ip_list():
    pass


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='SMTP IP reputation checker')
    parser.add_argument(
        '-i', '--ip', required=True,
        default=False, help="Single IP to be checked"
    )
    parser.add_argument(
        '-d', '--detailed', required=False, action='store_true',
        help="Report reputation score on each RBL"
    )
    options = parser.parse_args()
    return options


def check_ip_on_rbl(ip, rbl):
    query = '{}.{}'.format(reverse_ip(ip), rbl)
    try:
        result = socket.gethostbyname(query)
        score = result.split(".")[3]
        return score
    except socket.error:
        return 0


def main():
    options = parse_arguments()
    rbl = REPUTATION_URL
    result = check_ip_on_rbl(options.ip, rbl)
    if options.detailed:
        print("{} {}".format(rbl, result))
    else:
        print("{}".format(result))


if __name__ == '__main__':
    main()
