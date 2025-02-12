def timeConversion(s):
    # Write your code here
    h = s[0:2]
    ms = s[3:8]
    ampm = s[8:10]
    if (ampm == "AM"):
        if int(h) == 12:
            return str(int(h) - 12) + ":" + ms
        else:
            return h + ":" + ms
    elif (ampm == "PM"):
        if int(h) < 12:
            return str(int(h) + 12) + ":" + ms
        else:
            return h + ":" + ms
        
print(timeConversion("12:40:22AM"))