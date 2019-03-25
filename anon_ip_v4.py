import sys
import csv
from ipcalc import Network


COUNTER = int(sys.argv[1])  # number of strings


def write_find(raw_row, anon_row):
    result.writerow(
        (
            raw_row[0],  # exchange
            raw_row[1],  # remote_ip
            raw_row[2],  # imps
            raw_row[3],  # clicks
            raw_row[4],  # convs
            raw_row[5],  # CTR
            raw_row[6],  # CR
            raw_row[7],  # spend
            raw_row[8],  # eCPM
            raw_row[9],  # eCPC
            raw_row[10],  # CPI
            anon_row[0],  # network
            anon_row[1],  # is_anonymous
            anon_row[2],  # is_anonymous_vpn
            anon_row[3],  # is_hosting_provider
            anon_row[4],  # is_public_proxy
            anon_row[5],  # is_tor_exit_node
        )
    )
    return 0


""" Opening output CSV and initialising first row"""
out = open('result_3.csv', 'w')
result = csv.writer(out, delimiter=',')
result.writerow(
    (
        'exchange',
        'remote_ip',
        'imps',
        'clicks',
        'convs',
        'CTR',
        'CR',
        'spend',
        'eCPM',
        'eCPC',
        'CPI',
        'network',
        'is_anonymous',
        'is_anonymous_vpn',
        'is_hosting_provider',
        'is_public_proxy',
        'is_tor_exit_node',
    )
)
i = 0
with open('imp.csv', 'r') as raw_db:
    raw_db.readline()
    for raw_row in csv.reader(raw_db, delimiter=','):
        impression_ip = raw_row[1]

        with open(
            'GeoIP2-Anonymous-IP-Blocks-IPv4.csv', 'r'
        ) as anon_db:
            anon_db.readline()
            for anon_row in csv.reader(
                anon_db, delimiter=','
            ):
                anon_row = [
                    '0' if x == '' else x for x in anon_row
                ]  # fill empty row with 0
                anonynous_ip = anon_row[0]
                if impression_ip in Network(anonynous_ip):
                    write_find(raw_row, anon_row)
                    break

        i += 1
        if i > COUNTER:
            out.close()
            break
