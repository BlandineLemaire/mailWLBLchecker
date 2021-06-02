import json
"""
This module is used to make sure the mail isn't from a non allowed email address and the destination is
a valid email address

Return values :
100 : The destination address is whitelisted and the sending address is not blacklisted
0 : The destination address isn't whitelisted (sender won't be checked in this case)
0 : The destination address is whitelisted but the sending address is blacklisted
"""
def CheckMailValidity(jsonFile,to, sender):
    # Opening the json file given in params
    with open(jsonFile) as json_file:
        data = json.load(json_file)

    # Debug
    print(data['to'])
    print(data['sender'])

    # Check if the destination mail is in the whitelist
    if to in data['to']:
        # If it is then we make sure the sender isn't blacklisted
        if sender in data['sender']:
            # If the sender is blacklisted we return 2
            return 2
        else:
            # The sender is allowed to send mail we return 0
            return 0
    else:
        # The destination address isn't allowed we return 1
        return 1


print(CheckMailValidity('/xxx/xxx/xxx/xxx/parameters',"xx@xx.fr","yy@yy.com"))