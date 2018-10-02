
USER = "KateLin"
PASS = "verysecurepassword123!"

def checkInfo(user,pswd):
    if(user == USER and pswd == PASS):
        return "Login Successful"
    elif(user != USER):
        return "ERROR: Invalid Username"
    else:
        return "ERROR: Invalid Password"
