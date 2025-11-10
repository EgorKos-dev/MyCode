class Alert:
   def generic_display_info(self): 
         print("This is a generic alert.")

class EmailAlert(Alert):
    def display_info(self):
        print("This is an email alert.")

class SMSAlert(Alert):
    def display_info(self):
        print("This is an SMS alert.")

object = [EmailAlert(), SMSAlert()]
for alert in object:
    alert.generic_display_info()
    alert.display_info()