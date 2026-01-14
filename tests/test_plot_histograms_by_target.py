import pandas as pd
import matplotlib
import autoeda.plot as plot


def test_plot_histograms_by_target_basic():
    """Test histogram plotting with numeric features and a categorical target."""

    df = pd.DataFrame({
        "age": [22, 25, 30, 35, 40, 45],
        "income": [40000, 50000, 60000, 70000, 80000, 90000],
        "class": ["A", "A", "B", "B", "A", "B"]
    })

    fig = plot.plot_histograms_by_target(df, target="class")

    assert isinstance(fig, matplotlib.figure.Figure)
