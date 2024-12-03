#This code parses data from txt, csv, xml and json files.


def parse_txt_file():
    
    file_path="Documents/groceries.txt"

    with open(file_path, "r") as input_file:
        data=input_file.read()


    print("data: ", data)

    parsed_data=data.split(", ")
    print("parsed data:" , parsed_data)
    print("item at index 2:" , parsed_data[2])


def parse_csv_file():

    import csv
    file_path="Documents/groceries.csv"
    
    with open(file_path, "r") as input_file:
        csv_reader=csv.reader(input_file)
        #to separate headers from data:
        headers=next(csv_reader)
        for row in csv_reader:
            row[1]=int(row[1])
            print(row)

def parse_json_file():

    import json
    file_path="Documents/groceries.json"

    with open(file_path, "r") as input_file:
        data=input_file.read()
    
    parsed_data=json.loads(data)

    print("Bananas Quantity:", parsed_data['bananas'])


def parse_xml_file():

    import xml.etree.ElementTree as ET

    file_path="Documents/groceries.xml"

    tree=ET.parse(file_path)
    root=tree.getroot()

    #collect items with price higher than 6
    items_over_6=[]
    for item in root.findall("grocery_item"):
            name=item.find("name").text
            price=item.find("price").text
            if float(price)>6:
                items_over_6.append(name)
            print(name, price)
    print("items with price higher than 6: ", items_over_6)

parse_xml_file()