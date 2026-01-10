def plot_correlation_heatmap(df, target=None, method="pearson", figsize=(10, 8)):
    """
    Generate a correlation heatmap for numeric features in a dataset.

    This function computes pairwise correlations between numeric columns
    and visualizes them as a heatmap. Optionally, a target column can be
    highlighted to show correlations specifically with the target.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing numeric and non-numeric features.

    target : str, optional
        Name of the target column. If provided, correlations with the target
        may be emphasized or displayed separately.

    method : str, default="pearson"
        Correlation method to use. Supported values include:
        - "pearson"
        - "spearman"
        - "kendall"

    figsize : tuple, default=(10, 8)
        Size of the heatmap figure.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object containing the heatmap visualization.

    Raises
    ------
    ValueError
        If the target column does not exist in the dataframe.
    """
    pass


def plot_histograms_by_target(df, target, features=None, bins=30, figsize=(12, 8)):
    """
    Plot histograms of features grouped by a target variable.

    This function visualizes the distribution of selected features
    conditioned on the target variable. Useful for understanding
    class separation and feature behavior.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing features and target.

    target : str
        Name of the target column.

    features : list of str, optional
        List of feature column names to plot. If None, all numeric
        columns except the target will be used.

    bins : int, default=30
        Number of bins for the histograms.

    figsize : tuple, default=(12, 8)
        Size of the figure.

    Returns
    -------
    matplotlib.figure.Figure
        Figure object containing the histograms.

    Raises
    ------
    ValueError
        If the target column does not exist in the dataframe.
    """
    pass
