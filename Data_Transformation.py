import pandas as pd
import config
import spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder().master("local[1]")
          .appName("Justin_Bieber")
          .getOrCreate()
Justin_Songs_df = spark.read.csv("/GitHub/Walmart/Justin_Songs.csv")
Songs_Analtics_df = spark.read.csv("/GitHub/Walmart/Songs_Analtics.csv")

Distinct_Justin_Songs_df = Justin_Songs_df.distinct()
print("Distinct count: "+str(Distinct_Justin_Songs_df.count())) #Distinct Song records(No duplicates)

Distinct_Songs_Analtics_df = Songs_Analtics_df.distinct()
print("Distinct count for analytics dataset: "+str(Distinct_Songs_Analtics_df.count())) #Distinct analytics records(No duplicates)


print("count of all tweets consumed: "+str(Justin_Songs_df.count())) #count of all tweets consumed including duplicates

Distinct_Justin_Songs_df.write.mode('overwrite').parquet("/GitHub/Walmart/Justin_Songs_Final.parquet") 
Distinct_Songs_Analtics_df.write.mode('overwrite').parquet("/GitHub/Walmart/Songs_Analtics_Final.parquet") 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#or if we need to write to sql

sql.write_frame(Distinct_Justin_Songs_df, con=con, name='Justin_Songs_Final', 
                    if_exists='replace', flavor='mysql')

    sql.write_frame(Distinct_Songs_Analtics_df, con=con, name='Songs_Analtics_Final', 
                    if_exists='replace', flavor='mysql')
