# [Stacy Frady] - Assignment 1

def verify_access(username, password, clearance_level):

    if username != "soc_admin" or password != "S3cur3_P@ss": 
        return "INTRUSION_DETECTED"

# Otherwise (meaning the username and password are correct), check clearance_level:

    if clearance_level >= 5: 
        return "ROOT_ACCESS_GRANTED"

    if clearance_level >= 3 and clearance_level <= 4: 
        return "ANALYST_ACCESS_GRANTED"

    else: 
        return "INSUFFICIENT_CLEARANCE"
