def doiticket(speed, bday):
    if (bday==True):
        speed=speed-5
    if(speed<60):
        return "0"
    if (speed<80):
        return "1"
    return "2"
