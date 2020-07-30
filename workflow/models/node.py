from uuid import uuid4
from cuid import cuid
class Node:
	"""
	Contains state information related to an instance
	"""
	# ~ collision_resistant_id = uuid()
	# ~ uniqu_id = cuid()
	# ~ combined_id  = f"{collision_resistant_id}_{uniqu_id}"
	class Status:
		DRAFT= "DRFT"
		DELETE = "DEL"
		CANCEL = "CNCL"
		REJECTED = "REJT"
		IN_PROGRESS= "INPR"
		COMPLETED= "CMPT"
	class PageAudit:
		VIEW
		EDIT
	class Type:
		NODE
		ROUTER
	process = ForeignKey('Process', on_delete=CASCADE, verbose_name='Process')
	name = CharField(max_length=50)
	code = CharField(max_length=50)
	node_type = = CharField(max_length=50, choices=Type.choices, default=Type.NODE)
	can_edit = BooleanField()
	can reject = BooleanField()
	can_cancel = BooleanField()
	operators = CharField(max_length=50)
	note = = CharField(max_length=50)
	is_active = BooleanField(default=True)
	ext_data = JSONField(default=dict)
	
	def __str__(self):
		return self.name
	def get_status(self):
		return self.status
	def is_submitted(self):
		return self.status in ['in_progress','completed']
	
