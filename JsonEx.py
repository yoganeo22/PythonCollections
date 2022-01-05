import json

#data = "{'Meta Data': {'1. Information': 'Product and Quantity', '2. Time Zone': 'US/Eastern'}, 'Timestamp': {'2022-01-02': {'1. product': 'Computer', '2. quantity': '20'}, '2022-01-01': {'1. product': 'Keyboard', '2. quantity': '22'}}}"
data_dict = {
    'Meta Data': {
        '1. Information': 'Product and Quantity',
        '2. Time Zone': 'US/Eastern'
    },
    'Timestamp': {
        '2022-01-02': {
            '1. product': 'Computer',
            '2. quantity': '20'
        },
        '2022-01-01': {
            '1. product': 'Keyboard',
            '2. quantity': '22'
        }
	}
}

if __name__ == "__main__":
    print("This is Json Example")

    # 1. json.dumps && json.loads
    # ==============================================================================================
    # data_dict = <class 'dict'>

    data_string = json.dumps(data_dict)
    print(data_string)                     # data_string = <class 'str'>
    # {"Meta Data": {"1. Information": "Product and Quantity", "2. Time Zone": "US/Eastern"}, ...
    data_json = json.loads(data_string)
    print(data_json)                       # data_json = <class 'dict'>
    # {'Meta Data': {'1. Information': 'Product and Quantity', '2. Time Zone': 'US/Eastern'}, ...

    # Get product and quantity on '2022-01-01'
    product = data_json["Timestamp"]["2022-01-01"]["1. product"]
    qty = data_json["Timestamp"]["2022-01-01"]["2. quantity"]

    print("Product: {}, Qty: {}".format(product, qty))
    # Product: Keyboard, Qty: 22


    # 2. json.dump && json.load
    # ==============================================================================================
    with open("JsonEx.json", "w") as outputfile:
        json.dump(data_dict, outputfile)

    # Opening JSON file
    f = open('JsonEx.json', )
    fileContent = json.load(f)
    print("File Content: {}".format(fileContent))
    # File Content: {'Meta Data': {'1. Information': 'Product and Quantity', '2. Time Zone': 'US/Eastern'}, ...
