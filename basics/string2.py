#

address = "mumbai@uct.ac.in sat 2019"
print("Orginal string is " , address)

atpos=address.find("@")
print("Position of blank space after @" , atpos)
sppos = address.find(' ',atpos)
print("position of blank space after @" , sppos)

host =  address[atpos+1:sppos]
print("host name is " , host)