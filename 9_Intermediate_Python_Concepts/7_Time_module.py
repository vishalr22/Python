'''
Time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions.

time.time()
time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch.

time.sleep()
time.sleep() function suspends the execution of the current thread for a specified number of seconds.

time.strftime()
time.strftime() function formats a time value as a string, based on a specified format.

time.localtime()
time.localtime() gives the the current time.
'''
import time

print("Start:", time.time())
time.sleep(2)
print("Stop:", time.time())

print(time.localtime())
t = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
