from facial_req import facial_req
from send_email import send_email

import datetime

complete_names = ['Alice', 'Bob', 'Charlotte', 'David', 'Elliot', 'Fiona']

start_time = ['09:00', '10:15', '11:30', '12:45', '13:30', '14:40']

currentDT = datetime.datetime.now()
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)

while True:
	currentDT = datetime.datetime.now()
	time = str(currentDT.hour) + ':' + str(currentDt.minute)

	if time in start_time:
		present_names = facial_req()
		type = 'present'
		send_email(present_names, type)

		tardy_names = run_model(tardy_names) 
		type = 'tardy' 
		send_email(tardy_names,type)
		absent_names = [] 

		for name in complete_names:
			if name in present_names: 
				pass 
			elif name in tardy_names: 
				pass 
			else:
				absent_names.append(name) 

		type = 'absent' 
		send_email(tardy_names)