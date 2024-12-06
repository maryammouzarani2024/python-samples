import pandas as pd

#creating a pandas dataframe from two lists
cities=["London", "Tokyo", "Hamburg", "Rome"]
cities2=["Rio", "Tokyo", "Hamburg", "Rome"]
start_date=["27th Jul, 2010", "5th Aug, 2023", "23rd Jun, 2017"]
end_date=["21-09-2012", "8th Aug, 2024","07-27-2019"]

data=pd.DataFrame(zip(pd.Series(cities), pd.Series(start_date), pd.Series(end_date)), columns=["City", "Start Date", "End Date"])
#by zip function we correspond the items in the lists to each other
print("Dataframe created from the lists: ")
print(data)

#unifroming the dates
data["Start Date"]=pd.to_datetime(data["Start Date"], format='mixed')
data["End Date"]=pd.to_datetime(data["End Date"], format='mixed')

print("Dataframe after revising the dates: ")
print(data)

#calculate the difference between two fields and add the result as a new field
print("calculate the difference between two fields and add the result as a new field")

data=data.assign(duration=data["End Date"]-data["Start Date"])
print(data)


start_data=pd.DataFrame(zip(pd.Series(cities), pd.Series(start_date)), columns=["city", "Start Date"])
end_data=pd.DataFrame(zip(pd.Series(cities2), pd.Series(end_date)), columns=["city", "End Date"])

print("concating two data frames: ")
concated_data=pd.concat([start_data, end_data], axis=0)
print(concated_data)

print("Inner Merging of  two data frames: ")
merged_data=pd.merge(left=start_data, right=end_data, on="city", how='inner')
print(merged_data)


print("Outer Merging of  two data frames: ")
outer_merged_data=pd.merge(left=start_data, right=end_data, on="city", how='outer')
print(outer_merged_data)

print("Left Merging of  two data frames: ")
left_merged_data=pd.merge(left=start_data, right=end_data, on="city", how='left')
print(left_merged_data)


print("Right Merging of  two data frames: ")
right_merged_data=pd.merge(left=start_data, right=end_data, on="city", how='right')
print(right_merged_data)



#droping records with nan at Start or End date
print("droping records with nan at Start or End date")
processed_data=merged_data.dropna(subset=["Start Date", "End Date"], how="any")
print(processed_data)


#setting default values for nans 
print("setting default values for nans ")
concated_data["Start Date"]=concated_data["Start Date"].fillna(value="01-01-1999")
print(concated_data)



#working with duplicates
print("working with duplicates")
duplicated_data=pd.concat([left_merged_data, right_merged_data], axis=0)
print(duplicated_data)

print("duplicated records: ")
print(duplicated_data.duplicated())

print("number of duplicated records: ")
print(duplicated_data.duplicated().sum())

#drop duplicates
print("removing duplicated records: ")
duplicated_data=duplicated_data.drop_duplicates()
print(duplicated_data)
