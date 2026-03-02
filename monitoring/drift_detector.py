# monitoring/drift_detector.py

import numpy as np

def detect_mean_shift(train_mean, current_mean, threshold=0.3):
    diff = abs(train_mean - current_mean)
    return diff > threshold