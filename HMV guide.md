You only need two libraries to run this code, Numpy and Pandas. These are the steps to perform Handling Missing Values and the considerations to fill it:
1. We need to take a brief look into the dataset. Here I try to get any informations about the data with .head(), .describe(), and .size().
![image](https://user-images.githubusercontent.com/47058384/108614809-d5452080-7438-11eb-828e-042647b2df16.png)

2. Than we calculate the missing values existed in the data. From here we know that the missing data has 23.7% of all the cells. Then we figure out where all these missing datas are distributed.

![image](https://user-images.githubusercontent.com/47058384/108614979-839d9580-743a-11eb-9822-960a103f0d66.png)

Image above shows us the number of missing values for all columns

3. After knowing all columns that contained missing data, then we need to figure out the possibility of that data missing. Is it because of the data not recorded or it doesn't exist.
If the value is missing because of not recorded, we need to fill the possibilty for that cells instead of drop the missing values.
For example The ISO columns has missing values. In fact, every country has ISO Code, it means there are some values that not recorded in this column. So we should't drop the missing
values in this column, we need to figure out what country that has missing values and try to fill it with the ISO Code for that country. So to fill all the missing values, we need to handle this per column
# Total Vaccinations and People Vaccinated
The first thing that I do is dropping the "Total Vaccinations" and "People Vaccinated". Actually these columns are having missing values because of not recorded, but I don't know
approximation should I use to fill this data, so I just need to drop them.

![image](https://user-images.githubusercontent.com/47058384/108615270-7b932500-743d-11eb-9c86-f6219808bff2.png)

So two columns handled by drop the missing values each.
# People Fully Vaccinated
If we take look at column "people full vaccinated", it has relation to "Total Vaccinations" and "People Vaccinated" columns.

![image](https://user-images.githubusercontent.com/47058384/108615346-ffe5a800-743d-11eb-9a83-69165b9fa8fe.png)

There is some pattern that shows us the values on "People Fully Vaccinated" collected by substract the value between "Total Vaccinations" and "People Vaccinated".
So that we should fill the "nan" values with this pattern
![image](https://user-images.githubusercontent.com/47058384/108615383-7f737700-743e-11eb-9de9-ca9e3cbbd33d.png)

# Daily Vaccinations Raw
I Also found a pattern in this column where:

daily_vaccinations_raw[i] = total_vaccinations[i] - total_vaccinations[i-1]

so should fill the "nan" values with pattern that we found with looping. But we need to reset all the index first, because we already drop some rows in this dataframe that 
could affect index order.

# People Fully Vaccinated per Hundred
I can't find the pattern and the best technique to fill missing values in this column, so I just drop the column from the dataframe. It also has a moderately missing values (500+)

# Daily Vaccinations and Daily Vaccinations per Million
I also drop the rows that has missing values in these column. It only has 4 missing values, so I would preferably drop the rows instead of drop this column.

# ISO Code
First we need to know what country that has missing values on "iso_code" columns, then we search what ISO Code should be filled each country using loop function. 

