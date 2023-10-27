from src import analysis
from src import utilities

# data_grid = "./data/11_road_atlanta/IWSC_MRRA_Race_Grid.csv"
# data_race = "./data/11_road_atlanta/IWSC_MRRA_Race.csv"

data_race = "./data/10_indy/IWSC_Indianapolis_Race.csv"


def get_plot():
    """Get a plot for the provided csv file"""
    data_filter = None
    # data_filter = ("Driver", "Sebastien Bourdais")
    # data_filter = ("Class", "GTP")
    df = analysis.getDataFrameFromFile(data_race, filter=data_filter)
    print(df.to_string())
    plot = analysis.getPlotFromDataFrame(df)


def main():
    """Application main entry point
    - get_plot()
    """
    print(f"[RUN] --- Executing the main script at {utilities.get_formatted_time()}")
    get_plot()
    print(f"[END] --- Completed the main script at {utilities.get_formatted_time()}")


if __name__ == "__main__":
    main()
