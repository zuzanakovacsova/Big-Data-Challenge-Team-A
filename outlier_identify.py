import numpy as np

def outlier_find(data):
    # calculate interquartile range
    q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
    iqr = q75 - q25
    median = np.percentile(data, 50)
    # outlier cuttoff: 1.5IQR
    cut_off = iqr * 1.5
    lower, upper = q25 - cut_off, q75 + cut_off
    # identify outliers
    outliers = [x for x in data if x < lower or x > upper]
    outliers_removed = [x for x in data if x >= lower and x <= upper]
    print('Percentiles: 25th=%.3f, 50th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, median, q75, iqr))
    print('Identified outliers: %d' % len(outliers))
    print('Non-outlier observations: %d' % len(outliers_removed))
    return outliers