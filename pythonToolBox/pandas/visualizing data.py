import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb

data=pd.read_excel("Orders-With Nulls.xlsx", )



print(data.sample(5))

#data validation:

#check if first names are all capitalized

names=data["Customer Name"].str.split(" ").to_list()
# for name in names:
#     print(name[0].istitle())

#number of correct records
print( len([name[0].isupper () for name in names]))
#compare with the total number of records
print(data.info())

data["Order Quantity"].value_counts().plot(kind='bar')
plt.title("Data from xlsc")
#with seaborn we have more conifg options on the diagrams
#hue: to categorize the data according a third parameter
#pallete: set the coloring form and _r for make the color order reverse
snb.countplot(data=data,x="Product Category", order=["Technology", "Office Supplies", "Furniture"], hue='Ship Mode', palette='coolwarm_r')
plt.show()


#ploting records for customers with name Lena
# selected_data=data[data["Customer Name"].str.contains("Lena")]
# print(selected_data)
# snb.countplot(data=selected_data,x="Product Category", order=["Technology", "Office Supplies", "Furniture"], hue='Ship Mode', palette='coolwarm_r')
# plt.show()

#Barplot number of various customer segment in different ship modes

#data.groupby(['Ship Mode', "Customer Segment"]).size().unstack('Ship Mode').sort_values(['Regular Air' ,'Delivery Truck', 'Express Air'], ascending=False).plot(kind='bar', color=['blue', 'pink'])
#plt.show()
