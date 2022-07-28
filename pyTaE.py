from datetime import datetime
current_date = datetime.now()
current_date = current_date.strftime('%m/%d/%Y')
cutoff_date = current_date[2:]
current_m = current_date[:2]
current_m = int(current_m) + 1
current_m = str(current_m)
current_m = ("0" + current_m)
current_dateLater = (current_m + cutoff_date)

emailFrom = input("Direct email from: ")
emailTo = input("Direct email to: ")
emailTo = (emailTo + "@uwyo.edu")
td    = input("Enter the TD ticket number: ")

print("Aliases.edit\n\n# " + current_date + " ALF TD " + td + " TEMP Forward Until " + current_dateLater + "\n" + emailFrom + ":                " + emailTo + "\n")