print ("Please insert your full name with no spaces:")
full_name = input()
first_part = full_name[0:3]
last_part = full_name[-3:]
print ("Your intial password is: " + first_part + last_part + "@567")

print ("Do you want to change your password? (yes/no)")
change_password = input().strip().lower()
if change_password == "yes":
    print ("Please insert your new username:")
    new_username = input()
    first_part = new_username[0:3]
    last_part = new_username[-3:]
    print ("Your new password is: " + first_part + last_part + "@567")
else:
    print ("Your password remains unchanged.")
