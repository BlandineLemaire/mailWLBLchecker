# mailWLBLchecker

This script is used to make sure the mail isn't from a non allowed email address and the destination is
a valid email address

Return values :
0 : The destination address is whitelisted and the sending address is not blacklisted
1 : The destination address isn't whitelisted (sender won't be checked in this case)
2 : The destination address is whitelisted but the sending address is blacklisted
