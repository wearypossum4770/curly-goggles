from
from django.db.models import (
Model, DateTimeField, BooleanField,DecimalField,
)
class Transaction(Model):
	class DebitAsset():
		DEBIT = 1, _("")
		CREDIT = 0, _("")
		__empty__=_("")
		
	class AllocationType():
		AMOUNT
		PERCENT
		
	class StatusDisplay():
		YES=1, = _("")
		NO = 0,= _("")

	effective_date = DateTimeField()
	allocation = DecimalField(max_digits=9,decimal_places=2)
	suspense
	withholding
	valuation = DecimalField(max_digits=9,decimal_places=2, default=0.00)
	fields
	action_events
	math
	spawns

# Create your models here.
class Account (Model):
	
	is_active= BooleanField(default=True)
	in_collections= BooleanField(default=False)
	
	normal_balance_credit = BooleanField() 
	outstanding_balance = DecimalField(max_digits=9,decimal_places=2, default=0.00)
	# ~ credit_balance = DecimalField()
	current_balance = DecimalField(max_digits=9,decimal_places=2, default=0.00)
	
	draft_balance = BooleanField(help_tex="include balance of draft invoices for client")
	overdue_balance = BooleanField(help_tex="include balance of draft invoices for client")
	grand_total_balance = DecimalField(help_text="")
	last_activity = DecimalField()
	late_reminders = DecimalField(help_text="include information about late reminders")
	late_fee = DecimalField(help_text="include information about late fees")
	
	currency_code
	fax_number
	business_number
	last_activity
	last_user_login
	admin_notes
	client_notes
	beginning_balance
	ending_balance
	
	def net_receivables(self, request):
		
		return self
	def has_credit(self, request):
		"""
		1. Checks if account is Accounts Recievables /Payables.
		2. If A/P processes refund to customer after threshold.
		"""
		
		return self

	def has_draft(self, request):
		"""
		1. Looks for accounts not at due date.
		"""
		
		return self

	def has_outstanding(self, request):
		"""
		1. filters to clients with draft invoices
		2. Checks accounts for amounts overdue.
		3. Sends notification to client.
		4. Limits client's access to services.
		"""
		
		return request

	def has_overdue(self, request):
		"""
		1. Checks accounts for amounts overdue.
		2. Sends notification to client.
		"""
		
		return self
		
	def estimate_allowance_for_doubtful(self, request):
		from users.profile import Profile
		"""
		1. Each receivable has its own allowance for doubtful estimation
		"""

		doubtful_allowance = # ~ __mul__(Profile.Rating, 16)- 100
		# ~ doubtful_receivables = Reciveable*(doubtful_allowance/100)

class Invoice(Model):
	email_subject = DecimalField(help_text="")
	email_body  = DecimalField(help_text="")
	action_email = DecimalField(help_text="")
	name = DecimalField(help_text="")
	setup_complete = BooleanField(default=True)
	confirmed_at= DateTimeField()
	redirect_uri = DecimalField(help_text="")
	description = DecimalField(help_text="")
	subscription_statuses = DecimalField(help_text="")
	profession = DecimalField(help_text="")
	links = DecimalField(help_text="")
	integrations = DecimalField(help_text="")
	website_url = DecimalField(help_text="")
	settings_url = DecimalField(help_text="")
	logo_public_id =  = DecimalField(help_text="<jwt returned from post https://api.freshbooks.com/uploads/images>")

# ~ https://api. path("accounting/account/<accountid>/invoices/<invoiceid>")

"Authorization": f"Bearer {BEARER_TOKEN}"
"Content-Type": "application/json"
