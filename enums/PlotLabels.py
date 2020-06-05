from enum import Enum


class PlotLabels(Enum):
    x_label = "Date"
    y_label = "{} price ($)"

    title = "{0} prices for the last {1}"

    week_scatter_point = "x"
    month_scatter_point = "."
    year_scatter_point = "*"



