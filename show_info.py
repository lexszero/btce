#!/usr/bin/python
import btce
from time import strftime, localtime

info = btce.getinfo()

print "Funds:"
for currency in ['BTC', 'USD', 'RUR']:
	print "\t", currency, info['funds'][currency.lower()]
print

if info['open_orders']:
	print "Open orders (" + str(info['open_orders']) + "):"
	print "id\t\tdirection\tamount\t\trate\t\ttime"
	orders = btce.order_list()
	for id, data in orders.items():
		pair = data['pair'].split('_')
		if data['type'] == 'buy':
			pair[0], pair[1] = pair[1], pair[0]
		print str(id) + "\t\t" + pair[0] + '->' + pair[1] + "\t" + str(data['amount']) + "\t\t" + str(data['rate']) + "\t\t" + strftime('%d.%m.%Y %H:%M:%S', localtime(data['timestamp_created']))

