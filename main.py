from src import analysis
from src import utilities

data_grid = "./data/11_road_atlanta/IWSC_MRRA_Race_Grid.csv"
data_race = "./data/11_road_atlanta/IWSC_MRRA_Race.csv"


def get_plot():
    """Get a plot for the provided csv file"""
    df = analysis.getDataFrameFromFile(
        data_race, filter=("Driver", "Sebastien Bourdais")
    )
    plot = analysis.getPlotFromDataFrame(df)


def main():
    """Application main entry point
    - get_plot()
    """
    print(f"Executing the main script at {utilities.get_formatted_time()}")
    get_plot()


if __name__ == "__main__":
    main()
