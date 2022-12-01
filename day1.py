import pandas
import requests

cookie = ''
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

x = requests.get('https://adventofcode.com/2022/day/1/input', headers={'Cookie': cookie, 'User-Agent': ua}, verify=False)
sums = [sum([int(x) for x in elf if x != '']) for elf in map(lambda v: v.split('\n'), x.text.split('\n\n'))]
print(max(sums), sum(sorted(sums, reverse=True)[:3]))
