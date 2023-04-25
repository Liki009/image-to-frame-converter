def convert_ms_to_hms(duration_ms):
    # convert milliseconds to seconds
    duration_sec = duration_ms // 1000

    # calculate hours, minutes, and seconds
    hours = duration_sec // 3600
    minutes = (duration_sec % 3600) // 60
    seconds = duration_sec % 60

    # format the result as hh:mm:ss
    duration_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    return duration_str
def extract(string):
    hr,minute,sec=[int(substring) for substring in string.split(":")]
    return hr,minute,sec
def hms_to_ms(time_str):
    hr,minute,sec=extract(time_str)
    milli=(hr*3600+minute*60+sec)*1000
    return milli

#o=hms_to_ms("10:30:45")
#print(o)
#t=convert_ms_to_hms(o)
#print(t)
#a,b,c=extract("12:3:4")
#print(a)
