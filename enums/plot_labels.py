from enum import Enum


class PlotLabels(Enum):
    x_label = "Date"
    y_label = "{} price ($)"

    title = "{0} prices for the last {1}"

    week_scatter_point = "x"
    month_scatter_point = "."
    year_scatter_point = "*"
    scatter_color_max = "black"
    scatter_color_min = "red"
    scatter_label_max = "Max {} price\nfor each {}"
    scatter_label_min = "Max {} price\nfor each {}"

    crypto_color = "orange"
    crypto_linewidth = 4
    crypto_alpha = 0.3
    crypto_label = "{} price"

    sma_color = "red"
    sma_linewidth = 1
    sma_alpha = 0.5
    sma_label = "Simple moving\naverage"

    ema_color = "blue"
    ema_linewidth = 1
    ema_alpha = 0.5
    ema_label = "Exponential moving\naverage"
