from datetime import datetime
from functools import reduce
# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

# print('Date:', d10ate_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)

# deferral = 5
# year_payments_begin = 4

illistration_A1 = {
"cash":25000,
"accounts_receivable":35000,
"inventory":122000,
"net_property_plant_and_equipment":205000,
"patents":18000,
"liabilities":-55000
}
class GoodWill:
	def master_valuation(self):
		fair_value_net_identifiable_assets = reduce((lambda accum, currVal: accum+currVal),illistration_A1.values())
		purchase_price = 400000
		goodwill_value = fair_value_net_identifiable_assets - purchase_price
		return goodwill_value


	def journal_entry(self):
		for account, balance in illistration_A1.items():
			print(f"\n{account.replace('_',' ').upper()}\t\t\t{balance}")

goodwill = GoodWill().journal_entry()
print(goodwill)
