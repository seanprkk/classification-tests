import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/riceClassiciation.csv"))
X = df.drop(columns=['Class'])
y = df['Class'].values

