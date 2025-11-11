import pandas as pd 

class OpenData:

    def __init__(self, filename):
        self.filename = filename 

    def openData(self):
        df = pd.read_csv(self.filename)
        return df 
    
# open_data = OpenData("product.csv")
# data = open_data.openData()



class InputData:

    def inputProductName(self):
        while True:
            try:
                input_product_name = str(input("Enter product name: "))
                if len(input_product_name) < 3:
                    print("Enter appropriate product name")
                    continue

            except ValueError:
                print("Enter valid product name")
                continue
                
            break 
        return input_product_name
    

    def inputBudget(self):
        pass 

# input_data = InputData()
# get_product_name = input_data.inputProductName()


class Search:
    

    def __init__(self, data, get_product_name):
        self.loaded_data = data 
        self.get_product_name = get_product_name

    def searchProductNameId(self):
            
        for id, name in enumerate(self.loaded_data["product_name"]):
            if self.get_product_name == name:
                return name, id + 1 
            

# search_user_data = Search()
# product_name, product_id = search_user_data.searchProductNameId()


class Display:
    valid_search = None

    def __init__(self, product_name, product_id, get_product_name):
        self.product_name = product_name
        self.product_id = product_id
        self.get_product_name = get_product_name

    def displayValidSearch(self):
        if self.product_name != None and self.product_name != None:
            Display.valid_search = True 
            return f" Matching results for '{self.get_product_name}'"
        
        else:
            return f"No matching results found for '{self.get_product_name}'"

    def displayProductDetails(self):
        if Display.valid_search == True:

            print("-"*30)
            print(f"Product Name: \t\t {self.product_name}")
            print(f"Product Id: \t\t {self.product_id}")
            print("-"*30)


# display_search_results = Display()
# print(display_search_results.displayValidSearch())
# display_search_results.displayProductDetails()


if __name__ == "__main__":
    open_data = OpenData("product.csv")
    data = open_data.openData()

    input_data = InputData()
    get_product_name = input_data.inputProductName()

    search_user_data = Search(data, get_product_name)
    product_name, product_id = search_user_data.searchProductNameId()

    display_search_results = Display(product_name, product_id, get_product_name)
    print(display_search_results.displayValidSearch())
    display_search_results.displayProductDetails()


