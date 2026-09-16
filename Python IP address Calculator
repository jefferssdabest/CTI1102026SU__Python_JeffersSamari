# Recreational Programming: IP address classing
# ROE:
# W3schools learn python page only
# No copying from other source code pages
# No AI usage
#############################################################################
test = ['10.0.0.2', '/12']
#ip_addr = input("Enter an IP address: ")
#prefix = input("Enter a prefix: (Ex. /24) ")



ip_addr,prefix=test
# yes, I could save myself time and effort by doing my calculations in base 2
# however at this point, it is now faster to finish the code
#ex: 1001 -> 1000|0111 -> 0000|1101 -> 1100
def truncateBinary(num):
    append_zero = 1
    lead_bits_trunc = []
    for digit in num:
        if digit == "0":
            append_zero = 0
        lead_bits_trunc.append(str(append_zero))
    return "".join(lead_bits_trunc)

def simpleNum2binary(num):
    precalc_binaries = [0, 128, 192, 224, 240, 248, 252, 254]
    return str(precalc_binaries[num])

        
# IPV4 ADDRESSES
# have a native prefix
# native subnet mask
# 
class ipv4_address:
    def __init__(self, ip_address, subnet_prefix):
        self.addr = ip_address
        self.prfx = subnet_prefix
        self.octets = ip_address.split('.')

 
    def getSubnetMask(self, slash_prefix=0):
        subnet_mask = []
        prefix = int((self.prfx[1:]))
        # if prefix is not specified, we use the class constructor's prefix
        if slash_prefix != 0: prefix = int(slash_prefix[1:])
        
        for each_octet in range(0,4):
            if (prefix > 7):
                prefix -= 8
                subnet_mask.append("255")
            else:
                subnet_mask.append(simpleNum2binary(prefix))
                prefix = 0
            
        return".".join(subnet_mask)

             
    def getBinary(self):
        new_binary = []
        for octet in self.octets:
            # ex. 192 -> 11000000, 33 -> 000100001
            new_binary.append(bin(int(octet))[2:])
        return new_binary
      

    def getClass(self, return_list_index=1):
        
        first_octet = self.getBinary()[0]
        lead_bits_of_first_octet = first_octet[:4]
        tlbfo = truncateBinary(lead_bits_of_first_octet)

        classful_info = [
            ("0000", "A", "/8"),
            ("1000", "B", "/16"),
            ("1100", "C", "/24"),
            ("1110", "D", "/32"),
            ("1111", "E", "/32")
            ]
        # compare Truncated Lead Bit of First Octet
        #     to the left column of the list above ^
        for i in range(0,3):
            comparison_str = classful_info[i]
            if comparison_str[0] == tlbfo:
                output = comparison_str[return_list_index]
                return output # will usually be "A" .. "E"
        return 1

    
    def getNativeSubnetMask(self):
        native_prefix = self.getClass(2)
        return self.getSubnetMask(native_prefix)

    def AddressSummary(self):
        print(self.getClass())
       
                
                
            
            

i = ipv4_address(ip_addr, prefix)
print(i.getClass(), i.getSubnetMask(), i.getNativeSubnetMask())

