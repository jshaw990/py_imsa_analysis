import matplotlib.pyplot as plt
import pandas as pd
from src import utilities


def getPlotFromDataFrame(df):
    x_column = "Lap"
    y_column = "Seconds"
    data_to_display = [
        "Lap Time",
        "S01",
        "S02",
        "S03",
    ]

    highlight_condition = df["Flag"] == "Yellow"

    plt.figure(figsize=(10, 6))

    for y in data_to_display:
        df[y_column] = df[y].apply(utilities.lap_time_to_seconds)
        plt.plot(df[x_column], df[y_column], marker="o", linestyle="-", label=y)

    for i, is_highlighted in enumerate(highlight_condition):
        if is_highlighted:
            lap = df.loc[i, "Lap"]
            plt.axvspan(lap - 0.25, lap + 0.25, color="yellow", alpha=0.5)

    # Create a line plot
    plt.title(f"Seconds vs Lap")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.legend()
    plt.grid(True)
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
        if filter == None:
            return df

        filtered_data = df[df[filter[0]] == filter[1]]
        return filtered_data

    except FileNotFoundError:
        print(f"File not found at: {file_path}")

    except pd.errors.EmptyDataError:
        print(f"The .csv file at {file_path} is empty.")

    except pd.errors.ParserError:
        print(f"An error occurred while parsing the .csv file at {file_path}.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
