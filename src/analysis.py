import plotly.express as px
import plotly.graph_objects as go

import traceback
import matplotlib.pyplot as plt
import pandas as pd
from config import lap_plot, imsa

from src import utilities

__TEAM_COLORS__ = {
    1: "#ffd50b",
    2: "#1f3e98",
    5: "#ffe200",
    6: "#ed1c24",  # '#ffffff'
    7: "#0b0a0a",
    10: "#007dc5",
    24: "#1569b3",
    25: "#e12c26",
    31: "#e8242a",
    59: "#ff0000",
    60: "#e61f8e",
}


def getPlotFromPlotly(df):
    try:
        x_column = "Lap number"
        y_column = "Lap time in seconds"
        fcy_condition = df["Flag"] == "Yellow"
        pit_condition = df["Location"] == "Pit"

        df[y_column] = df["Lap Time"].apply(utilities.lap_time_to_seconds)
        # class_color = df["Class"].apply(imsa.get_color_for_class)
        # team_color = df["Car"].apply(imsa.get_color_for_team)
        data_tooltip = ["Car", "Driver", "Lap", "Lap Time", "Flag", "Location"]

        # print(f'car => {df["Car"]}')

        fig = px.line(
            df,
            x="Lap",
            y=df[y_column],
            line_group=df["Car"],
            markers=True,
            color=df["Car"],
            color_discrete_map=__TEAM_COLORS__,
            range_y=[75, 83],
            hover_data=data_tooltip,
            title="",
        )

        # fig.update_traces(line_color=class_color)
        # fig.update_traces(marker=dict(color=team_color))

        for i, is_fcy in enumerate(fcy_condition):
            if is_fcy:
                lap = df.iloc[i]
                x_start = lap["Lap"] - 0.25
                x_end = lap["Lap"] + 0.25

                fig.add_vrect(
                    x0=x_start,
                    x1=x_end,
                    layer="below",
                    line_width=0,
                    fillcolor="yellow",
                    opacity=0.5,
                )

        fig.show()
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: [{type(e)}] {e}")


def getPlotFromDataFrame(df, plot_list=lap_plot.data_to_display):
    try:
        x_column = "Lap"
        y_column = "Lap time in seconds"
        highlight_condition = df["Flag"] == "Yellow"

        plt.figure(figsize=(10, 6))

        for y in plot_list:
            df[y_column] = df[y].apply(utilities.lap_time_to_seconds)
            plt.plot(df[x_column], df[y_column], marker="o", linestyle="-", label=y)

        for i, is_highlighted in enumerate(highlight_condition):
            if is_highlighted:
                lap = df.iloc[i]
                plt.axvspan(
                    lap["Lap"] - 0.25, lap["Lap"] + 0.25, color="yellow", alpha=0.5
                )

        # Create a line plot
        plt.title(f"Seconds vs Lap")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        # print(f"An error occurred: {str(e)}")
        traceback.print_exc()
        print(f"An error occurred: [{type(e)}] {e}")


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
