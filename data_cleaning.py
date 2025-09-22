import pandas as pd

df = pd.read_csv("netflix_titles.csv")

#Handling missing values

#prints a count of missing values in each row
print(df.isnull().sum())

#Inserts "unknown" into all missing values in text and name columns
df['director'].fillna("unknown", inplace=True)
df['cast'].fillna("unknown", inplace=True)
df['country'].fillna("unknown", inplace=True)
df['title'].fillna("Unknown", inplace=True)

#Fill unknown date values to a standard date
df['date_added'].fillna("01-01-2000", inplace=True)

#Filling in mode values for missing values in rating column
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

#Dropping columns with missing values since duration units are uneven and only few missing values
df.dropna(subset=['duration'], inplace=True)

#Handling Duplicate rows
df.drop_duplicates(inplace=True)

#Standardising text values

#strip white spaces and make everything lowecase
df['type'] = df['type'].str.strip().str.lower()

#Give title case to country, cast, director and title columns
df['country'] = df['country'].str.strip().str.title()
df['cast'] = df['cast'].str.strip().str.title()
df['director'] = df['director'].str.strip().str.title()
df['title'] = df['title'].str.strip().str.title()

#Standardise ratings to uppercase
df['rating'] = df['rating'].str.strip().str.upper()


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce',dayfirst=True)


#rename column headers to change everything to lowercase and replace spaces and hiphens with underscores 
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "-").str.replace("-", "_")
df['date_added'].fillna("01-01-2000", inplace=True)

#Final Preview

#number of missing values
print("Missing values per column:")
print(df.isnull().sum())
print("-"*50)

#number of duplicate rows
print("Number of duplicate rows:", df.duplicated().sum())
print("-"*50)

#Check data types
print("Data types of each column:")
print(df.dtypes)
print("-"*50)

#Preview first 10 rows
print("First 10 rows of the dataset:")
print(df.head(10))