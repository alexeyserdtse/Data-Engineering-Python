import yfinance as yf
import pandas as pd
from datetime import date
import sys


def currency_rate(currency):
    # Replace 'USD' with the base currency and 'EUR' with the target currency
    base = currency
    target = "ILS"  # we always compare to new israel's shekel

    # Create a Ticker object for the currency pair
    currency_pair = f"{base}{target}=X"

    historical_data = yf.download(
        currency_pair, period="1d", interval="1m", progress=False)

    # Print the most recent exchange rate
    latest_rate = historical_data['Close'].iloc[-1]
    return latest_rate


def append_To_currency_rate_df(dest_df, currency):
    # Create new df with current currecy change rate.
    data = {'Currency': [currency.upper()],
            'Rate': [currency_rate(currency)]}

    data_df = pd.DataFrame(data)

    df = pd.concat(
        [dest_df, data_df], ignore_index=True)

    return df


if __name__ == '__main__':
    column_names = ["Currency", "Rate"]
    today_currency_rate_df = pd.DataFrame(columns=column_names)

    currency_list = ['USD', 'GBP', 'JPY', 'EUR',
                     'AUD', 'CAD', 'SEK', 'CHF', 'AUD']

    # extend df with currencies from the list.
    for currency in currency_list:
        try:
            today_currency_rate_df = append_To_currency_rate_df(
                today_currency_rate_df, currency)
        except (IndexError, NameError) as e:
            err = e
            print(err)
            sys.exit()

    # Add last updated date for all the currencies.
    today_currency_rate_df['Last_Update_Date'] = date.today()

    print(today_currency_rate_df)
