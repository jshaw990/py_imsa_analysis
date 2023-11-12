car_class_colors = {
    "GTP": "rgb(33,39,33)",
    "LMP2": "rgb(58,83,164)",
    "LMP3": "rgb(242,104,41)",
    "GTDPRO": "rgb(227,27,35)",
    "GTD": "rgb(0,174,66)",
}

team_colors = {
    "01": "#c02127",
    "6": "#c52104",
    "7": "#c52104",
    "10": "#06c06c",
    "24": "#c02127",
    "25": "#c02127",
    "31": "#ce0e2d",
    "59": "#ff0000",
    "60": "#ff0241",
}


def get_color_for_class(car_class):
    # print(car_class)
    if car_class in car_class_colors:
        return car_class_colors[car_class]
    else:
        # Return a default color if the class_name is not found
        return "rgb(128,128,128)"


def get_color_for_team(car_number):
    print(type(str(car_number)), car_number)
    if str(car_number) in team_colors:
        team = team_colors[str(car_number)]
        print(team)
        return team
    else:
        return "rgb(128,128,128)"
