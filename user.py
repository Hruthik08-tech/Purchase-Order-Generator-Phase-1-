from datetime import datetime 
class AskDetails:

    def askName(self):
        while True:
            input_name = input("Enter your name: ")
            if input_name.isdigit() == True:
                print("Enter valid name")
                continue
            if len(input_name) < 3:
                print("Enter valid input name")
                continue

            break
        
        return input_name

    def askDateOfBirth(self):
        while True:
            try:
                date_of_birth = input("Enter your date of birth: ")
                input_date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

            except ValueError:
                print("Enter valid format {YYYY-MM-DD}")
                continue
                
            break 

        return input_date_of_birth
    
    def askMailId(self):
        while True:
           
            input_mail_id = str(input("Enter your mail id: "))
            if input_mail_id.endswith("@gmail.com") == False:
                print("Enter valid email adress")
                continue

            break 

        return input_mail_id
    
    def askContactNo(self):
        while True:
            try:
                input_contact_no = int(input("Enter your contact no: "))
                if len(str(input_contact_no)) != 10:
                    print("No.of digits is not equal to 10")
                    continue
            except ValueError:
                print("Enter valid contact no.")
                continue
            break

        return input_contact_no
        
# ask_details = AskDetails()
# get_name = ask_details.askName()
# get_date_of_birth = ask_details.askDateOfBirth()
# get_mail_id = ask_details.askMailId()


class Person:

    def __init__(self, get_name, get_date_of_birth, get_mail_id, get_contact_no):
        self.name = get_name
        self.date_of_birth = get_date_of_birth
        self._mail_id = get_mail_id
        self.contact_no = get_contact_no

        
            
            
class Customer(Person):

    def __init__(self):
        self.name = get_name
        self.date_of_birth = get_date_of_birth
        self._mail_id = get_mail_id
        self.contact_no = get_contact_no 

        

if __name__ == "__main__":
    ask_details = AskDetails()
    get_name = ask_details.askName()
    get_date_of_birth = ask_details.askDateOfBirth()
    get_mail_id = ask_details.askMailId()
    get_contact_no = ask_details.askContactNo()
            
