from django.contrib.postgres.fields import ArrayField
from django.db.models import(
 Model, CharField,BooleanField,DateTimeField,ForeignKey, CASCADE,JSONField,TextChoices,
)
# ~ from lbworkflow.models import BaseWFObj

class SimpleWorkFlow:
	title = CharField(max_length=50)
	start_date = DateField()
	end_date = DateField()
	comments = JSONField()
	manager_comments = JSONField()
	is_apporved = BooleanField(default=False)
	date_modified = DateTimeField(auto_now_add=True)
	date_created = DateTimeField(auto_now_add=True)
	
	# created_byForeignKey()
	# modified_by = ForeignKey()
	def __str__(self):
		return self.summary
# in case the XO is also HQ PL designate Someone to hold position.
class ApprovalAuthority (Model):
	class Position(TextChoices):
		SERVICE_MEMBER = 'SM'
		TEAM_LEADER = 'TL'
		SQUAD_LEADER = 'SQD'
		PLT_SGT = 'PSG'
		PLT_LEADER = 'PL'
		PAC_CLERK = 'PAC'
		EXEC_OFFICER = 'XO'
		OPERATIONS = 'OPS'
		FIRST_SERGEANT = '1SG'
		COMMANDER = 'CDR'
		HEADQUARTER = 'HQ'
		__empty__ = ("(Unknown)")
	name = CharField(max_length=50)
	position = CharField(max_length=10, choices=Position.choices, default=Position.SERVICE_MEMBER)

class WorkGroup (Model):
	name = CharField(max_length=128)
	members = models.ManyToManyField(ApprovalAuthority,through='WorkGroupMembership',through_fields=('work_group', 'approval_authority'),)

class WorkGroupMembership(Model):
	work_group  =ForeignKey(WorkGroup, on_delete=CASCADE)
	approval_authority =ForeignKey(ApprovalAuthority, on_delete=CASCADE)
	inviter = ForeignKey(ApprovalAuthority, on_delete=CASCADE, related_name='work_group_memership_invites')
	invite_reason = models.CharField(max_length=64)
