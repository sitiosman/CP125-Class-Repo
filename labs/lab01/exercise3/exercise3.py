# Lab 01 Exercise 3: Secure Vault System
def  validate_entry(name, pin):
    if name == "Director" and pin == 1122:
        return True
    if name == "Security" and pin == 9900 :
        return True
    return False
    
    