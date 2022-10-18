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

    workbook = load_workbook(filename, data_only=True)
 
    ws = workbook["Sheet1"]
    source_data = ws['B6' : 'BK200']
    market_price_data = ws['B3' : 'BK3'][0]
    analyst_col = 0
    monthly_data = []
    market_prices = []
    analysts = set()
    while analyst_col < len(source_data[0]) - 1:
        current_month_data = dict()
        for row in range(len(source_data)):
            cell_value = source_data[row][analyst_col].value
            if cell_value != 0 and cell_value is not None:
                current_month_data[cell_value] = source_data[row][analyst_col + 1].value
                analysts.add(cell_value)
        monthly_data.append(current_month_data)
        market_prices.append(market_price_data[analyst_col + 1].value)
        #Goes to the next analysts
        analyst_col += 2
    print("Monthly data")
    print(monthly_data)
    print("Market prices")
    print(market_prices)
    print("analysts")
    print(analysts)
    return monthly_data,market_prices,analysts

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

