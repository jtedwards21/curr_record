from yahoo_finance import Currency
import csv, time, os

MyCurrencies = []
usd_eur = Currency('USDEUR')
usd_eur.cur_name = 'USDEUR'
MyCurrencies.append(usd_eur)
eur_usd = Currency('EURUSD')
eur_usd.cur_name = 'EURUSD'
MyCurrencies.append(eur_usd)
gbp_usd = Currency('GBPUSD')
gbp_usd.cur_name = 'GBPUSD'
MyCurrencies.append(gbp_usd)
usd_gbp = Currency('USDGBP')
usd_gbp.cur_name = 'USDGBP'
MyCurrencies.append(usd_gbp)
cny_usd = Currency('CNYUSD')
cny_usd.cur_name = 'CNYUSD'
MyCurrencies.append(cny_usd)
usd_cny = Currency('USDCNY')
usd_cny.cur_name = 'USDCNY'
MyCurrencies.append(usd_cny)
jpy_usd = Currency('JPYUSD')
jpy_usd.cur_name = 'JPYUSD'
MyCurrencies.append(jpy_usd)
usd_jpy = Currency('USDJPY')
usd_jpy.cur_name = 'JPYUSD'
MyCurrencies.append(usd_jpy)

def __checkfileexist(currency_name, directory='/home/jedwards/cur_data'):
	if os.path.isfile(directory + '/' + currency_name + '.csv') == False:
		csvfile = open(directory + '/' + currency_name + '.csv', 'wb')
		wr = csv.writer(csvfile)
		wr.writerow(['Bid'] + ['Ask'] + ['Time'])
		csvfile.close()

def __writetocsv(currency_data, currency_name, directory='/home/jedwards/cur_data'):
	csvfile = open(directory + '/' + currency_name + '.csv', 'wb')
	wr = csv.writer(csvfile)
	wr.writerow([currency_data.bid] + [currency_data.ask] + [currency_data.time])
	wr.close()
	
def __getcurrdata(cur_obj):
	ask = cur_obj.get_ask()
	bid = cur_obj.get_bid()
	time = cur_obj.get_trade_datetime()
	return {'time': time, 'bid': bid, 'ask': ask}
    
for curr in MyCurrencies:
	__checkfileexist(curr.cur_name)

while True:
    for curr in MyCurrencies:
		d = __getcurrdata(curr)
		__writetocsv(curr, curr.cur_name)
	time.sleep(60)
	for curr in MyCurrencies:
		curr.refresh()
