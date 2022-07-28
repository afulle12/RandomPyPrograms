from datetime import datetime
current_date = datetime.now()
current_date = current_date.strftime('%m/%d/%Y')

email = input("Enter their email: ")
email = (email + "@uwyo.edu")
td    = input("Enter the TD ticket number: ")
professionalAlias = input("Enter their Professional Alias: ")

print("Aliases.edit\n\n# " + current_date + " ALF TD " + td + " Professional Alias\n" + professionalAlias +":               " + email + "\n")
print("Canonical.edit\n\n# " + current_date + " ALF TD " + td + " Professional Alias\n" + email + "                        " + professionalAlias + "\n")