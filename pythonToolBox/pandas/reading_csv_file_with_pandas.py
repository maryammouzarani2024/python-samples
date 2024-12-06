import pandas as pd 


data=pd.read_csv("tips.csv")
#you can skip the first 5 rows:
# pd.read_csv("tips.csv", skiprows=5)

#print the dimension of the data
print(" the dimension of the data")
print(data.shape)


#print the types of the data
print(" the types of the data")
print(data.dtypes)




#print the first n rows of data, default=5
print("the first n rows of data, default=5")
print(data.head(12))

#print the last n rows of data, default=5
print("the last n rows of data, default=5")
print(data.tail(12))


#print 5 random rows of data
print(" 5 random rows of data")
print(data.sample(5))

#print data info
print(" data info")
print(data.info())


#print the number of indexes
print(" data index")
print(data.index)


print("tip value at index 220")
print(data.loc[220, "tip"])



# #print statistical data info
# print("statistical data info")
# print(data.describe())

# #to show all the rows:
# pd.set_option("display.max_rows", None)
# print(data)


# #print unique size values
# print(data["size"].unique())

# #how many of each size exists in the data
# print(data["size"].value_counts())

# #change the name of some columns
# print(data.columns)
# #mapper= {data.columns[5]:"smoker_size", data.columns[4]:"smoke_day"}  or:
# mapper= {"size":"smoker_size", "day":"smoke_day"}
# data=data.rename(columns=mapper)

# print("new columns: ", data.columns)


# #drop some columns from data
# data=data.drop('sex', axis=1)
# print("new columns: ", data.columns)


# #filter rows by total_bill value
# print("rows with total_bill<=10 ")
# low_bills=data["total_bill"]<=10.00

# # print(data[low_bills])
# #or :
# print(data[data["total_bill"]<=10.00])


# #filter rows for non-smokers on sunday and Friday
# print("records of non-smokers on sunday and Friday")
# selected_content= ((data["smoke_day"]=="Sun") | (data["smoke_day"]=="Fri" )) & ~(data["smoker"]=="Yes")
# print(data[selected_content] )

# #filter records having in 'inn' in time column
# print("records having in 'inn' in time column ")
# selected_content=data["time"].str.contains("inn")
# print(data[selected_content] )

# #sorting records by total_bill value
# print("sorted data according to total_bill and tip")
# print(data.sort_values(by=["total_bill", "tip"], ascending=[True, False]))
