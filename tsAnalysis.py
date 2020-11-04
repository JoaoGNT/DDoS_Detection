import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def holt_winters(ts, slen, extra_periods, alpha=0.4, beta=0.4, phi=0.9, gamma=0.3, plot=False):
    """
    This function calculates a forecast with an exponential smoothing + damped trend method.

    Inputs
      - ts: the historical values (a list, a numpy array or a pandas series)
      - extra_perios: the number of data points that you want to forecast
      - alpha: the level parameter
      - beta: the trend parameter
      - phi: the trend damping parameter
      - gamma: the seasonality parameter
      - plot: if True the function will print the dataset and a plot of the forecast
    """



    #
    # - Clean input
    #

    # Avoid any edition of original list, array or dataframe
    ts = ts.copy()
    # Transform ts into list if needed
    try:
        ts = ts.tolist()
    except:
        pass

    #
    # - Forecast Creation
    #

    # Function to determine first seasonal estimation
    def init_season(ts, slen):
        s = np.array([])
        ts = np.array(ts)
        for i in range(slen):
            # - Calculate columns that correspond to this season
            col = [x for x in range(len(ts)) if x % slen == i]

            # - Calculate season average
            s = np.append(s, np.mean(ts[col]))

        # - Normalize all season parameters (sum of parameters = slen)
        s /= np.mean(s)
        return s.tolist()

    # Initialize seasonal factors
    s = init_season(ts, slen)

    # Define forecast, level(a) &amp;amp;amp; trend(b)
    f = [np.nan]
    a = [ts[0] / s[0]]
    b = [(ts[1] / s[1]) - (ts[0] / s[0])]

    # Create the forecast for the first season
    for t in range(1, slen):
        # Update forecast based on last level (a) and trend (b)
        f.append((a[-1] + b[-1] * phi) * s[t])

        # Update the level based on the new data point
        a.append(alpha * ts[t] / s[t] + (1 - alpha) * (a[-1] + phi * b[-1]))

        # Update the trend based on the new data point
        b.append(beta * (a[-1] - a[-2]) + (1 - beta) * b[-1] * phi)

        # Create the forecast after the first season
    for t in range(slen, len(ts)):
        # Update forecast based on last level (a) and trend (b)
        f.append((a[-1] + b[-1] * phi) * s[-slen])

        # Update the level based on the new data point
        a.append(alpha * ts[t] / s[-slen] + (1 - alpha) * (a[-1] + phi * b[-1]))

        # Update the trend based on the new data point
        b.append(beta * (a[-1] - a[-2]) + (1 - beta) * b[-1] * phi)

        # Update season
        s.append(gamma * ts[t] / a[-1] + (1 - gamma) * s[-slen])

    # Forecast for all extra months
    for t in range(extra_periods):
        # Update the forecast as the most up-to-date level + trend
        f.append((a[-1] + b[-1] * phi) * s[-slen])
        # the level equals the forecast
        a.append(f[-1] / s[-slen])
        # Update the trend as the previous trend
        b.append(b[-1] * phi)
        # Update the seasonality as the same seasonality factor last season
        s.append(s[-slen])
        # fill in ts by np.nan for easy plotting
        ts.append(np.nan)

    #
    # - Analysis &amp;amp;amp; results
    #

    # Populate table with all the results
    dic = {"demand": ts, "forecast": f, "level": a, "trend": b, "season": s}
    results = pd.DataFrame.from_dict(dic)[["demand", "forecast", "level", "trend", "season"]]
    results.index.name = "Period"
    results["error"] = results["demand"] - results["forecast"]
    if (results["demand"].sum() == 0):
        maep = abs(results["error"]).sum() / (results["demand"].sum())
    else:
        maep = 1

    # Show the results if plot==True
    print(results)
    results[["demand", "forecast", "level", "season"]].plot(title="Holt-Winters", secondary_y=["season"],
                                                                figsize=(15, 15))
    plt.plot(results["forecast"])
    plt.show()
    # Return only the next period forecast and an indicator of past MAEP
    return f[-extra_periods:], maep
