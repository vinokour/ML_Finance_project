from fileinput import filename
from openpyxl import load_workbook
import sys

# """
# """
# Input:
#      - filename: str of an excel file
# Output data:
#     - market_prices: [100, 200, ..,] len(marker_prices) = num_months
#     - monthly_data: [{analyst_code: target_price, ...},{...}, ...] len(monthly_data) = num_months,
#     - analysts: set {analyst_code, analyst_code, ...}
# """
def GetData(filename):
    print(filename)
    workbook = load_workbook(filename, data_only=True)
    ws = workbook["Sheet1"]
    source_data = ws['B6' : 'B200']
    market_price_data = ws['B3' : 'BK3'][0]
    
    analyst_col = 0

    pass

# """
# Input:
#     - monthly_data: [{analyst_code: target_price, ...},{...}, ...] len(monthly_data) = num_months,
#     - analysts: set {analyst_code, analyst_code, ...}
# Output data:
#     - analyst_data: [[100,200,300],[150,150,400],[...],] len(analyst_data) = num_analysts, len(analyst_data[0]) = num_months
# """
def Clean():
    pass

# Input:
#     - monthly_data: [{analyst_code: target_price, ...},{...}, ...] len(monthly_data) = num_months,
#     - analysts: set {analyst_code, analyst_code, ...}
# Output data:
#     - analyst_data: [[100,200,300],[150,150,400],[...],] len(analyst_data) = num_analysts, len(analyst_data[0]) = num_months
# """

def LearnWeights():
    # Input:
#     - leanrned_weights: [float, ..] len = num_analysts
#     - target_prices: [float, ...] len = num_analysts
# Output:
#     - predicted price floats
# """
    pass

def Predict():
    pass

filename = sys.argv[1]
analyst_data = GetData(filename)

