from datetime import datetime
import os
import pandas as pd
from ast import Bytes
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
from pathlib import Path
import numpy as np


class Data:
    def __init__(self, dataset, start, end):
        self.dataset = dataset
        self.start = start
        self.end = end