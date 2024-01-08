import time
import numpy as np
from scipy.stats import skew, kurtosis
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import joblib
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL
import pygame  # Import pygame library
import imageio