import pandas as pd
import matplotlib
import pytest

import autoeda.plot as plot



def test_plot_correlation_heatmap_basic():
    # Create a simple numeric dataframe
    df = pd.DataFrame({
        "age": [22, 25, 30, 35],
        "income": [40000, 50000, 60000, 70000],
        "score": [60, 65, 70, 75]
    })

    ax = plot.plot_correlation_heatmap(df)

    # Check that the function returns a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)
