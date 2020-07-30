class TaxReport(Model):
	# ~ class TaxType(IntegerChoices):
	
	total_invoiced
	amount	
	code
	start_date
	end_date
	taxable_amount_paid 
	taxable_amount_collected 
	net_taxable_amount 
	tax_paid 
	tax_collected 
	net_tax 
	tax_name
	cash_based
	currency_code
	net_profit
class PaymentReport(Model):
	clientsids
	start_date
	end_date
	date_of_payment
	payment_methods
	download_token= (help_text= 'Allows report download to csv file.')
	invoice_number
	method_of_payment

class ExpenseReport():
	start_date
	exclude_personal
	end_date
	owner = User
	vendorid
	authors = User.id
class AgingAccountReport(Model):
	
	client_name = ForeignKey(Users)
	start_date
	end_date
	intervals =("0-30", "31-60", "61-90", "91+",)
	
	date_of_payment
	payment_methods
	download_token= (help_text= 'Allows report download to csv file.')
	invoice_number
	method_of_payment
