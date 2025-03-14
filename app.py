## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
""" print(data)   # Output the list """
#task number 1
""" def calcRow(data):
    row_totals = {}
    row_averages = {}
    rounded_averages ={}
    x = -1
    for i in data[1]:
        x += 1
        print(x)

    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals = sum(sales)  # Sum up sales for the store
        row_averages = row_totals / x
        rounded_averages[store_name] = round(row_averages,2)



    return rounded_averages

totals = calcRow(data)
print(totals) """
#task number 2
def calcRow(data):
    row_totals = {}
    row_averages = {}
    rounded_averages ={}
    profit = []
    x = -1
    for i in data[1]:
        x += 1

    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals = sum(sales)  # Sum up sales for the store
        row_averages = row_totals / x
        rounded_averages[store_name] = round(row_averages,2)
    for store in rounded_averages:
        profit.append(store)
    for store in profit:
        g = max(profit)
        print(g)
        profit.remove(g)


    
        
    
       



    

totals = calcRow(data)
print(totals)





    

