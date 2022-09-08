import pandas as pd

def set_index_dates(df:pd.DataFrame,date_column_name='Date'):
    df[date_column_name] = pd.to_datetime(df[date_column_name], dayfirst = True)
    df.sort_values(by=date_column_name,inplace=True)
    df.set_index(date_column_name,inplace=True)
    return df

def filter_columns(data:pd.DataFrame,column_names=['Type','Name','Category','Amount','Description']):
    data = data[column_names]
    return data

def filter_tax_year(data:pd.DataFrame,start_year,country='uk'):
    start_year_str = str(start_year)
    end_year_str = str(start_year + 1)
    if country == 'uk':
        start_date_str = '-04-06'
        end_date_str = '-04-05'
    elif country == 'usa':
        start_date_str = '-01-01'
        end_date_str = '-12-31'
    else:
        return 'ERROR Enter Valid Country: "uk" or "usa"'
    start_date = start_year_str + start_date_str
    end_date = end_year_str + end_date_str
    tax_year_dates = (data.index > start_date) & (data.index <= end_date)
    return data[tax_year_dates]

def expenses(data:pd.DataFrame,income_categories=['Incoming','Incoming Investment','Payment']):
    total = data[~data['Category'].isin(income_categories)]['Amount'].sum()
    return abs(total)

def turnover(data:pd.DataFrame,turnover_categories=['Incoming']):
    total = data[data['Category'].isin(turnover_categories)]['Amount'].sum()
    return total
