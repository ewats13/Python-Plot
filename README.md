# Python-Plot
Python script to analyze data acquired from an array of pressure sensors on a robotic hand.

This program was written to accompany a robotics project that collects data from five Flexiforce pressure sensors - one sensor on each digit of a robotic hand.
The robot's control system was written in Arduino IDE and outputs the time elapsed (in milliseconds) and the voltage readings from each pressure sensors into a text file.

The data in the output text file is formatted line by line as follows: <br /> '''time, thumb sensor, index sensor, middle finger sensor, ring finger sensor, pinky sensor ''' <br />
This python program opens a specified text file, parses the values in an organized manner, and plots them with Matplotlib's Pyplot.
