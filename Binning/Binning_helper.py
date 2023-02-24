import pandas as pd

import numpy as np
import re

def get_unique_from_column(column, unique_fields = []):
    for row in column:
        try:
            fields = re.split(r", |; ", row)
        except:
            continue
        unique_fields.extend(fields)
    unique_fields = set(unique_fields)
    return unique_fields
