import json
import random

data = json.load(open('medsim.json','r'))

population = int(data['population'])
cost_per_treatment = int(data['costpertreatment'])
physician_ratio = float(data['phyratio'])
chance_to_need_treatment = float(data['chancetogetsick'])

physicians = int(population*physician_ratio)
year = 365
days = 0
total_cost=0


class physician(object):
	"""
	This will define what a physcian can do

	Patient capacity, = hours worked per day / how long it takes for him to see a patient
	"""
	def __init__(self):
		self.hours_per_day = 8 # Default value for hours worked per day
		self.time_per_patient = 1 # This metric is in hours
		self.current_patients = 0
	

	def add_patient(self):
		"""
		returns true Adds a patient to current patient
		returns false if unable to add patient
		"""
		if  self.current_patients >= (self.hours_per_day/self.time_per_patient):
			return False
		else:
			self.current_patients += 1
			return True

	def new_day(self):
		"""
		resets patients to zero
		"""
		self.current_patients = 0

class person(object):
	"""
	Currently this defines someone who is not a physician
	"""

	def __init__(self,chance_to_need_treatment):
		"""
		Currently a person is sick or isnt
		"""
		self.is_sick = False
		self.chance_to_need_treatment = chance_to_need_treatment
		self.chance = int(self.chance_to_need_treatment*100)

	def new_day(self):
		"""
		"""
		ran = random.randrange(0,100)
		if self.chance >= ran:
			self.is_sick = True
		else:
			self.is_sick = False


people = []
doctor = []
for x in range(population):
	people.append(person(chance_to_need_treatment))

for x in range(physicians):
	doctor.append(physician())



day = 1

def day_cycle(physicians,cost_per_treatment,people):
	"""
	"""
	sick_people = 0


	for each in people:
		each.new_day()
		if each.is_sick:
			sick_people += 1
	print sick_people,"people got sick today."
	print "Each doctor saw",sick_people/physicians,"patients."
	print "At",cost_per_treatment,"dollars per treatment, that would cost $",sick_people*cost_per_treatment

day_cycle(physicians,cost_per_treatment,people)

print 'Compiled Successfully'