# Note: allow_list.txt is a list of private ip addresses provided
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
#Open file to read
with open(import_file, "r") as file:
    
    ip_addresses = file.read()


#Convert the string of the file into a list using .split()
ip_addresses = ip_addresses.split()


#Iterate through the remove list
for ips in remove_list:
    if ips in ip_addresses:
        
        #Remove the matches from the removed_list
        ip_addresses.remove(ips)

#Convert list back into a string to update the new file
ip_addresses = " ".join(ip_addresses)

#Rewrite the file with the updated list
with open(import_file, "w") as file:
    file.write(ip_addresses)


with open(import_file, "r") as file:
    text = file.read()
print(text)
