from datetime import datetime
department       = input("Input the Department Name: ")
userFirstLast    = input("Input the name of the user (First and Last Name): ")
userEmail        = input("Input the email of the user: ")
tdNum            = input("Input the TD Ticket Number: ")
listName         = input("Input the List Name: ")
currentTime      = datetime.now()
currentTime      = str(currentTime)
currentTime      = currentTime[:19]

print("\n\nAdd this to smtp2:/usr/local/upd/new/aliases.edit:\n")
print("# Requesting Department: " + department + "\n# Requesting User:       " + userFirstLast + " <" + userEmail + ">\n# TD:                    " + tdNum)
print("#mailman list: " + listName + "  " + currentTime + " MDT ALF")
print(listName + ":                " + listName + "@lists.uwyo.edu")
print(listName + "-admin:          " + listName + "-admin@lists.uwyo.edu")
print(listName + "-bounces:        " + listName + "-bounces@lists.uwyo.edu")
print(listName + "-confirm:        " + listName + "-confirm@lists.uwyo.edu")
print(listName + "-join:           " + listName + "-join@lists.uwyo.edu")
print(listName + "-leave:          " + listName + "-leave@lists.uwyo.edu")
print(listName + "-owner:          " + listName + "-owner@lists.uwyo.edu")
print(listName + "-request:        " + listName + "-request@lists.uwyo.edu")
print(listName + "-subscribe:      " + listName + "-subscribe@lists.uwyo.edu")
print(listName + "-unsubscribe:    " + listName + "-unsubscribe@lists.uwyo.edu")

print("\n\nAdd this to smtp2:/usr/local/upd/new/notifications.edit:\n")
print(listName + "@uwyo.edu: " + listName + "-owner@uwyo.edu\n\n")