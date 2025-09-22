# Day1_DataAnalystIntership
Task 1: Data Cleaning and Preprocessing

Hi, I am Nischal Binil. This is as part of my Data Analyst internship.

For my day 1 task I had to obtain a dataset and perform some data preprocessing on it.
I started off by checking the Netlix movies and shows dataset that i chose for any null values. there were about 4-5 columns with varying amounts of null values. I replaced all missing string values with "unknown".

Then i replaced all unknown dates with a standardised "01-01-2000" date and mode values for all missing rating columns. I also removed a few columns where the "duration" value was missing. I decided to remove those rows.

I then proceeded to remove all duplicate rows. I found that my dataset had no duplicate rows but Ive included the the code to get rid of duplicate rows anyway.

The next step was to standardize text values. First, I stripped the white spaces and converted all text into lowercase for the "type" attribute.
Then I applied title case and removed spaces for all country names, cast names, director names and titles. The "rating" attribute values where also stripped of white spaces and applied uppercase.

I also made a change to the "date_added attribute by updating its datatype to "datetime" and formatted all dates to dd-mm-yyyy format.

Finally, I added a few extra lines of code where I previewed the final cleaned dataset by returning the number of missing values, number of duplicate rows, a list of data types of each attribute and the first 10 rows of the dataset.

Thank You.


