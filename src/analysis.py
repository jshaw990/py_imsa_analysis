import pandas as pd

file_path = '../data/11_road_atlanta/IWSC_MRRA_Race.csv'
# file_path = '../data/11_road_atlanta/IWSC_MRRA_Race_Grid.csv'

try:
	df = pd.read_csv(file_path)

	# print(df.head())

	data_gtp = df[df['Class'] == 'GTP']

	# print(df.info())

	# print(df.describe())

	print(data_gtp.head())
	print(data_gtp.tail())

except Exception as e:
	print(f'An error has occurred: {str(e)}')