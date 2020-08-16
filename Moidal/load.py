import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


df = pd.read_csv('C:/Users/Lis/Downloads/DeliveryMuch/AB_NYC_2019.csv')

newdf=df[['id','host_id','price','number_of_reviews','last_review']]

newdf.to_csv("AB_NYC_2019_NEW.csv", index=False)
