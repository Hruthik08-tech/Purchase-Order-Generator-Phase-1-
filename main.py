from product import OpenData, InputData, Search, Display
from user import AskDetails

def main():
    print("="*60)
    print("Menu")
    print("="*60)

    open_data = OpenData("product.csv")
    data = open_data.openData()

    print("\n")
    print(data)
    print("\n")

    print("="*60)
    print("Place your order")
    print("="*60)

    input_data = InputData()
    print("\n")
    get_product_name = input_data.inputProductName()
    print("\n")

    print("="*60)
    print("Search Results")
    print("="*60)
    search_user_data = Search(data, get_product_name)
    product_name, product_id = search_user_data.searchProductNameId()

    print("\n")
    display_search_results = Display(product_name, product_id, get_product_name)
    print(display_search_results.displayValidSearch())
    display_search_results.displayProductDetails()
    print("\n")

    print("="*60)
    print("Enter your details")
    print("="*60)

    ask_details = AskDetails()
    print("\n")
    get_name = ask_details.askName()
    get_contact_no = ask_details.askContactNo()
    print("\n")

    print("="*40)
    print("Purchase Order")
    print("="*40)
    print("\n")
    print(f"Customer Name: \t\t {get_name}")
    print(f"Contact NO: \t\t {get_contact_no}")
    print("\n")
    display_search_results = Display(product_name, product_id, get_product_name)
    display_search_results.displayProductDetails()
    print("\n")
    print("="*40)






if __name__ == "__main__":
    main()

