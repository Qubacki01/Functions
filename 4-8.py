###
# Define a function time_string(hours, minutes, time_format) that, 
# given the number of hours (0..23) and the number of minutes (0..59), 
# returns a string specifying the time in the given format 
# ('24' for 24-hour time and '12' for 12-hour time).
#

def time_string(hours, minutes, time_format):
    minute_str = f"{minutes:02}"
    
    if time_format == '24':
        return f"{hours:02}:{minute_str}"
    
    elif time_format == '12':
        if hours == 0:
            hour_str = 12
            period = 'am'
        elif 1 <= hours < 12:
            hour_str = hours
            period = 'am'
        elif hours == 12:
            hour_str = 12
            period = 'pm'
        else:
            hour_str = hours - 12
            period = 'pm'
        
        return f"{hour_str}:{minute_str}{period}"

# Test cases
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))
