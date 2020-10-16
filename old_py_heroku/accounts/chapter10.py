class PlantPropertyEquipment(object):
	depreciation_method
	original_cost
	residual_value
	estimated_useful_life
	
	def calculate_accumulated_depreciation(self):
		accumulated_depreciation = {depreciation_expense:None}
		
		
		
	def calculate_depreciation_expenses(self):
		pass

class OperatingExpenses(object):
	COGS
	selling_epenses
	administrative_expenses
class Sales(object):
	sales_revenue
	
OperatingIncome = sales-operating_expenses
ProfitMargin = OperatingIncome/Sales

Average_oeprating_assets:
	current_assets:
		inventories
		accounts_receivable
		cash
	non_current_assets:
		PPE
		other_assets

asset_turnover = sales / Average_oeprating_assets
ROI = profit_margin * asset_turnover

class Assets(object):
	normal_balance = 'debit'
	
class Capital(object):
	source_of_investment = None
	cost_of_investmenet = .06
	
	source_of_investment='debt'
	cost_of_investmenet = .0.6
	share_of_investment = .5
	weighted_average_cost_of_capital

class VariableExpenses():
	pass

class SegmentMarginIncomeStatement(object):
	def __init__(self):
		self.net_operating_income = None

	def calculate_revenues():
		return sales_revenue + service_revenue

	def calculate_variable_expenses():
		return cost_of_goods_sold + sellling_administrative_expenses

		
	def calculate_contribution_margin():
		"""
		 1. demonstrates fixed and variable expenses
		"""
		
		return calculate_variable_expenses() - calculate_revenues()

	def calculate_traceable_fixed_expenses():
		return segment_cost_of_goods_sold + segment_sellling_administrative_expenses

	def calculate_segment_margin():
		return calculate_contribution_margin()-calculate_traceable_fixed_expenses()

	def calculate_common_fixed_expenses():
		return common_fixed_expenses
	
	def calculate_net_operating_income():
		self.net_operating_income = calculate_segment_margin() - calculate_common_fixed_expenses()
		return self.net_operating_income
		
		
def functional_income():
	pass

def operating_income():		
	return contribution_margin - fixed_expenses

def net_operating_profit():
	return operating_income() - income_taxes

def invested_capital():
	return total_asssets - current_liabilities
	
def weighted_average_cost_of_capital():
	return cost_of_investmenet * share_of_investment

def economic_value_added():
	return net_operating_profit - weighted_average_cost_of_capital()

def calculate_retained_earnings():
	pass
	
def calculate_dividends():
	pass
class CashFlowStatment:
	def calculate_operating_income():
		"""
			1. Find net_profit  or net_loss
			2. Add non_cash_expenses
			3. Adjust for working_capital
				increase / decrease in inventory   dr(increase) | cr (decrease)
				increase / decrease in receivables   dr(increase) | cr (decrease)
				increase / decrease in receivables   dr(decrease) | cr (Increase)
				
		"""
		
def profit_center():
	"""
	manager responsibility:
		1. revenues and costs incurred in generating a product or service.
		2. managers cannot commit funds to invest in assets.
	performance measures:
		overall_profit
			vs.
		flexible_budget (profit budgeted to be earned)
	"""
	
def cost_center():
	"""
	manager responsibility:
		1. responsible for cost incurred in the unit:
		2. reduction of costs
		3. acceptable level of serice or product quality
	performance measures:
		acutual_cost
			vs.
		flexible_budget (profit budgeted to be earned)
	
	"""
	
def investment_center():
	"""
	manager responsibility: 
		1. investing in assets to generate profits.
		
	performance measurements:
		return_on_investment
			&& 
		residual_income
	
	"""

def organization_segment():
	"""
	1. Part of organization management wishes to evaluate.
	
	
	"""
	
	headquarters
	managment
	division
	group
	center
