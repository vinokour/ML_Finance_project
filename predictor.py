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
    # print("Monthly data")
    # print(monthly_data)
    # print("Market prices")
    # print(market_prices)
    # print("analysts")
    # print(analysts)
    return monthly_data,market_prices,analysts

# """
# Input:
#     - monthly_data: [{analyst_code: target_price, ...},{...}, ...] len(monthly_data) = num_months,
#     - analysts: set {analyst_code, analyst_code, ...}
# Output data:
#     - analyst_data: [[100,200,300],[150,150,400],[...],] len(analyst_data) = num_analysts, len(analyst_data[0]) = num_months
# """
def Clean(monthly_data, analysts):
    def Cleaned_single_analyst(single_analyst_monthly_prediction):
        for index in range(len(single_analyst_monthly_prediction)):
            price_target = single_analyst_monthly_prediction[index]
            if not price_target is None:
                continue
            def GetNextVal(index):
                next_index = index + 1
                while next_index < len(single_analyst_monthly_prediction):
                    val = single_analyst_monthly_prediction[next_index]
                    if not val is None:
                        return val, next_index - index +1
                    next_index += 1
                return None, None
            #3 scenarios
            #no precvious, yes next 
            next_val, next_distance = GetNextVal(index)
            if index == 0 and not next_val is None:
                single_analyst_monthly_prediction[index] = next_val
            elif  index !=0 and not next_val is None:
                prev_value = single_analyst_monthly_prediction[index - 1]
                single_analyst_monthly_prediction[index] = prev_value + ((next_val - prev_value) / next_distance)
            elif index != 0 and next_val is None:
                prev_value = single_analyst_monthly_prediction[index - 1]
                single_analyst_monthly_prediction[index] = prev_value
        return single_analyst_monthly_prediction
            #yes previous, no next
            #yes previous, yes next
    sorted_analysts = sorted(list(analysts))
    cleaned_data = []
    
    for analyst in sorted_analysts:
        single_analyst_monthly_prediction = []
        nones_count = 0
        previous_none = False
        for curr_month in monthly_data:
            if not analyst in curr_month or curr_month[analyst] is None or curr_month[analyst] == "@NA":
                single_analyst_monthly_prediction.append(None) 
                if previous_none:
                    nones_count += 1
                    if nones_count > 5:
                        break
                else:
                    nones_count = 1
                previous_none = True

                # nones_count += 1
            else:
                single_analyst_monthly_prediction.append(curr_month[analyst])
                previous_none = False
        if nones_count <= 5: 
            single_analyst_monthly_prediction = Cleaned_single_analyst(single_analyst_monthly_prediction) if nones_count > 0 else single_analyst_monthly_prediction
            cleaned_data.append(single_analyst_monthly_prediction)
    return cleaned_data


        
    pass

# Input:
#     - monthly_data: [{analyst_code: target_price, ...},{...}, ...] len(monthly_data) = num_months,
#     - analysts: set {analyst_code, analyst_code, ...}
# Output data:
#     - analyst_data: [[100,200,300],[150,150,400],[...],] len(analyst_data) = num_analysts, len(analyst_data[0]) = num_months
# """
#Learn the weights on which analysts to include 
def LearnWeights(analyst_data, market_prices):

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
analyst_data, mkt_prices, analysts = GetData(filename)
clean_data = Clean(analyst_data, analysts)
print(clean_data)
training_data = []
for row in clean_data:
    #ignores last 6 months
    training_data.append(row[:-6])
learned_weights, avg_months, stdev = LearnWeights(training_data, market_prices)



