
#*Defang IP Address*

#Removes period and replaces it
ip = input("Enter an ip: ")
defangedip = ip.replace(".","[.]")

#Declare variable
ip2 = ("192.168.1.1")

#Splits ip address into an array and joins it back with [.]
def defang(ip2: str) -> str:
      array = ip2.split(".")
      newip = "[.]".join(array)
      return newip

# print(defang(ip2))
print(defangedip)
