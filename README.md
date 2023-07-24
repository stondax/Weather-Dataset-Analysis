# Weather-Dataset-Analysis

Weather Data Analysis
This Python script analyzes weather data stored in the "1. Weather Data.csv" file. The data contains information on temperature, humidity, wind speed, visibility, pressure, and weather conditions for each hour of the year 2012.

### Data Overview
The script uses the pandas library to read the data file and display its contents. It shows the first few rows of the dataset using the data.head() function. The dataset has 8784 rows and 8 columns.

### Data Exploration
To explore the data, the script provides various statistics like data types, unique values, and count of non-null entries for each column using data.dtypes, data.nunique(), and data.count().

The script also shows the unique values of the "Weather" column and their respective counts using data['Weather'].unique() and data['Weather'].value_counts().

### Data Filtering
You can filter the data based on specific conditions. For example, the script shows instances when the "Wind Speed" was exactly 4 km/h using data[data['Wind Speed_km/h'] == 4].

It also filters and displays data when the weather condition contains the word "Snow" using data[data['Weather Condition'].str.contains('Snow')].

### Data Statistics
The script calculates and displays statistics for selected columns. It finds the mean visibility using data.Visibility_km.mean(), the standard deviation of pressure using data.Press_kPa.std(), and the variance of relative humidity using data['Rel Hum_%'].var().

### Renaming Columns
You can rename the "Weather" column to "Weather Condition" using data.rename(columns={'Weather': 'Weather Condition'}, inplace=True).

### Data Cleaning
The script checks for null values using data.isnull().sum() and finds none in this dataset.
