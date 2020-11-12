import pandas as pd


def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
    lighting_loans = [{
        'day': D1,
        'rate': R1
    }, {
        'day': D2,
        'rate': R2
    }, {
        'day': D3,
        'rate': R3
    }]

    sorted_loans = sorted(lighting_loans, key=lambda k: k['day'])
    unique_arr = pd.DataFrame(sorted_loans).groupby('day', as_index=False).rate.sum().to_dict('r')

    basic_rate = 0
    for idx, item in enumerate(unique_arr):
        unique_arr[idx]['rate'] = item['rate'] + basic_rate
        basic_rate = unique_arr[idx]['rate']

    rest_k = K
    days = 0
    for idx, item in enumerate(unique_arr):
        if idx + 1 >= len(unique_arr):
            days = days + rest_k // item['rate']
        else:
            for it in range(item['day'], unique_arr[idx + 1]['day']):
                rest_k = rest_k - item['rate']
                if rest_k >= 0:
                    days = days + 1
                else:
                    break
        if rest_k < 0:
            break

    return days


# get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
# get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
# get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)
# get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)
