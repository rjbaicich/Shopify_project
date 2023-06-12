import pandas as pd

# Read the CSV file
df = pd.read_csv(r'C:\Users\RedneckRandy\Downloads\archive (14)\atlantic.csv')

column_names = ['ID', 'Name', 'Date', 'Time', 'Event', 'Status', 'Latitude', 'Longitude', 'Maximum Wind',
                'Minimum Pressure', 'Low Wind NE', 'Low Wind SE', 'Low Wind SW', 'Low Wind NW',
                'Moderate Wind NE', 'Moderate Wind SE', 'Moderate Wind SW', 'Moderate Wind NW',
                'High Wind NE', 'High Wind SE', 'High Wind SW', 'High Wind NW']

df.columns = column_names

#Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove rows with "UNNAMED" or empty name fields
df = df[(df['Name'].str.strip() != 'UNNAMED') & (df['Name'].notna())]

# Fill NaN values with 0
df.fillna(0, inplace=True)

df = df.round(2)

#Clean the 'Date' and 'Time' column
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d', errors='coerce')

# Remove rows with invalid 'Date' values
df = df[df['Date'].notna()]
df['Time'] = pd.to_datetime(df['Time'], format='%H%M', errors='coerce').dt.time
#The errors='coerce' argument is used to handle any errors that may occur during the conversion.


#Output the info
df.info()
df.to_csv('hurricane_cleaned.csv', index=False)
