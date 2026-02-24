# Task - Hard: You are given a raw list of IPs with duplicates: ["1.1.1.1", "8.8.8.8", "1.1.1.1", "10.0.0.5"]. Convert this to a set to deduplicate it, then create a dictionary that counts how many times each unique IP appeared in the original list.
 
ip_list = ["1.1.1.1", "8.8.8.8", "1.1.1.1", "10.0.0.5"]
ip_list_set = set(ip_list)
print(ip_list_set)
ip_dict = {x:0 for x in ip_list}
for x in ip_list:
    ip_dict[x] +=1
print(ip_dict)