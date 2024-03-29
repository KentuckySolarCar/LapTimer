import math
import numpy as np
import scipy.stats
from SCTimeUtility.system.TimeReferences import LapTime
from SCTimeUtility.log.Log import getLog


def predictNextLapTime(lapTimes):
    # Returns the predicted time for the next lap.
    if len(lapTimes) > 1:
        percentile = 0.05
        elapsedArr = np.array([t.elapsedTime for t in lapTimes])
        sampleMean = np.mean(elapsedArr)
        sampleStd = np.std(elapsedArr, ddof=1)
        t = scipy.stats.t.ppf(percentile, len(lapTimes) - 1)
        lower = sampleMean + (t * sampleStd * math.sqrt(1 + (1 / float(len(lapTimes)))))
    elif len(lapTimes) == 1:
        lower = lapTimes[0].elapsedTime
    else:
        raise LapPredictionError("Need at least one lap time to predict.")
    newestTime = max(lapTimes, key=lambda t: t.recordedTime)
    return LapTime(newestTime.recordedTime + lower, lower)


class LapPredictionError(Exception):
    pass
