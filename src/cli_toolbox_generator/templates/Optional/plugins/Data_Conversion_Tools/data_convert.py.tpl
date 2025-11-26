# Data Conversion & IO Helpers

import json
import csv
from decimal import Decimal, ROUND_HALF_UP


# JSON Helpers
def json_to_dict(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON '{path}': {e}")
        return None


def dict_to_json(data, path, indent=4):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent)
        return True
    except Exception as e:
        print(f"Error writing JSON '{path}': {e}")
        return False

# CSV Helpers
def csv_to_rows(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            return list(reader)
    except Exception as e:
        print(f"Error reading CSV '{path}': {e}")
        return []


def rows_to_csv(rows, path):
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        return True
    except Exception as e:
        print(f"Error writing CSV '{path}': {e}")
        return False


# Type Conversions
def to_int(value):
    try:
        return int(value)
    except:
        return None

def to_float(value):
    try:
        return float(value)
    except:
        return None

def is_numeric(value):
    try:
        float(value)
        return True
    except:
        return False

# Decimal Helpers
def round_decimal(value, precision=2):
    try:
        d = Decimal(str(value))
        q = Decimal("1." + ("0" * precision))
        return float(d.quantize(q, rounding=ROUND_HALF_UP))
    except:
        return None
