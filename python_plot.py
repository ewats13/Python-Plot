import re
import sys
import matplotlib.pyplot as plt

# Make sure a text file is provide
if not len(sys.argv[1:]):
	print("Must supply a filename")
	sys.exit(1)

# Open text file
file_name = sys.argv[1]
f = open(file_name)
test_case = str(raw_input('Enter test case (ex. "empty can"): '))
with open (file_name) as f:
	read_data = f.read()			# read entire text file
	mylist = re.split(',|\n|',read_data)	# parse values, using delimeters
	del mylist[-1]				# remove " " from end of array
	float_list = map(float, mylist)		# convert from string to float

# Debugging
#	print ("List from text file:")
#	for index, item in enumerate(float_list):
#		print index, item

# Assign values to their appropriate array [start:stop:step]
	time_val = float_list[0::6]		# elapsed time
	thumb_val = float_list[1::6]		# thumb readings		
	index_val = float_list[2::6]		# index finger readings
	middle_val = float_list[3::6]		# middle finger readings
	ring_val = float_list[4::6]		# ring finger readings
	pinky_val = float_list[5::6]		# pinky readings


plt.title("Sensor Data Plot: %s" % test_case)	# plot title
plt.xlabel('Time (milliseconds)')		# label x axis
plt.ylabel('Sensor Measurements (volts)')	# label y axis 
plt.plot(time_val,thumb_val,'r-',label='Thumb')	# plot thumb in red	
plt.plot(time_val,index_val, 'b-',label='Index')# plot index in blue
plt.plot(time_val,middle_val,'g-',label='Middle')# plot middle in green
plt.plot(time_val,ring_val,'m-',label='Ring')	# plot ring in magenta
plt.plot(time_val,pinky_val,'k-',label='Pinky')	# plot pinky in black

# Create legend with colors labeled
legend = plt.legend(loc='upper left', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')

# Set legend font size
for label in legend.get_texts():
	label.set_fontsize('large')
# Set legend line width
for label in legend.get_lines():
	label.set_linewidth(1.5)

plt.show()
