import pandas as pd
from dateutil.relativedelta import relativedelta

def calculate_sip_with_step_up(monthly, years, rate, step_up, lump_sum=0, start_date=None):
    
    if start_date:
        start_date = pd.to_datetime(start_date)
    else:
        start_date = pd.Timestamp.today()

    months = years * 12
    monthly_rate = rate / 12 / 100
    step_up_factor = 1 + (step_up / 100)
    future_value = lump_sum * ((1 + monthly_rate) ** months)
    invested = lump_sum
    sip = monthly
    records = []

    for m in range(1, months + 1):
        
        future_value += sip * ((1 + monthly_rate) ** (months - m))
        invested += sip

        
        date = start_date + relativedelta(months=m)
        records.append([date, invested, future_value,sip])

        
        if m % 12 == 0:
            sip *= step_up_factor
    

    df = pd.DataFrame(records, columns=["Date", "Total Invested", "Future Value","SIP/month"])
    
    
    
    df["Total Invested"] = df["Total Invested"].round()
    df["Future Value"] = df["Future Value"].round()
    
    df["Year"] = df["Date"].dt.year
    yearly_df = df.groupby("Year").agg({
        
        "Total Invested": "last",
        "Future Value": "last",
        "SIP/month":"last"
        
    }).reset_index() 
    
    yearly_df["SIP/month"] = yearly_df["SIP/month"].round()
    return df,yearly_df
