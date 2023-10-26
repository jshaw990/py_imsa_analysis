import matplotlib.pyplot as plt
import pandas as pd


def getPlotFromDataFrame(dataframe):
    # print(type(dataframe))
    # print(dataframe)
    plt.figure()
    print(dataframe)
    dataframe.plot(x="Lap", y="Lap Time")
    plt.show()


def getDataFrameFromFile(file_path, filter=None):
    """Converts the provided file_path to a dataframe
    Args:
                file_path (str): csv file to convert to a dataframe,
                filter (tuple | None): Key, Value pair to return specific data
    Returns:
                Pandas dataframe
    Raises:
                FileNotFoundError: File not found,
        EmptyDataError: File was found, but empty,
        ParserError: Error occurred while parsing the file,
        Exception: Undefined error
    """
    try:
        print(f"Getting dataframe from file: {file_path}")
        df = pd.read_csv(file_path)
        df.plot()
        # print(df.head())
        if filter == None:
            return df

        filtered_data = df[df[filter[0]] == filter[1]]
        # print(type(filtered_data))
        return filtered_data

    except FileNotFoundError:
        print(f"File not found at: {file_path}")

    except pd.errors.EmptyDataError:
        print(f"The CSV file at {file_path} is empty.")

    except pd.errors.ParserError:
        print(f"An error occurred while parsing the CSV file at {file_path}.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
