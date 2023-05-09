import pandas as pd
import numpy as np

# Read the online file by the URL provides above, and assign it to variable "df"

other_path = "/Users/Ali/Downloads/imports-85.data"
df = pd.read_csv(other_path, header=None)

# show the first 5 rows using dataframe.head() method

# print("The first 5 rows of the dataframe")
# print(df.head(5))
#
# print("The last 10 rows of the dataframe\n")
# print(df.tail(10))


headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df.columns = headers
# print(df.head(10))
#
# # We need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
#
df1 = df.replace('?', np.NaN)
# print(df1)


# We can drop missing values along the column "price" as follows:

df = df1.dropna(subset=["price"], axis=0)
df.head(20)
print(df)

# <b>Find the name of the columns of the dataframe.</b>
print(df.columns)

# For example, if you would save the dataframe df as automobile.csv to your local machine, you may use the syntax below,
# where index = False means the row names will not be written.

# df.to_csv("automobile.csv", index=False)
# print(df.to_csv("automobile.csv", index=False))
# print(df.to_csv("norowautomobile.csv"))
print(df.describe())

# You can select the columns of a dataframe by indicating the name of each column. For example, you can select the three columns as follows:

dataframe[[' column 1 ',column 2', 'column 3']]

# Apply the method to ".describe()" to the columns 'length' and 'compression-ratio

print(df[['length', 'compression-ratio']].describe())