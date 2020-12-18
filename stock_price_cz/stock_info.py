import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import finnhub
import requests
import json

"""
This package is designed to obtain historical data and implement analysis with Finnhub API.
API documentation: https://finnhub.io/docs/api#introduction
"""

API_URL = "https://finnhub.io/api/v1"
API_USER = os.environ.get('SP_USER')
token = os.environ.get('SP_KEY')

def obtain_stock_description():
    """
    This is a function to fetch general basic stock description using Finnhub API.

    Parameters (Inputs)
    ----------
    
    Returns (Output)
    -------
    DataFrame
        A dataframe containing data of stock description, symbol, type, and currency

    Examples
    --------
    >>>

     currency                   description displaySymbol    symbol type
0         USD      AGILENT TECHNOLOGIES INC             A         A  EQS
1         USD                    ALCOA CORP            AA        AA  EQS
2               AAF FIRST PRIORITY CLO BOND           AAA       AAA     
3         USD  PERTH MINT PHYSICAL GOLD ETF          AAAU      AAAU  ETF
4         USD   ATA CREATIVITY GLOBAL - ADR          AACG      AACG   DR
...       ...                           ...           ...       ...  ...
9464                               ICON USD       ICXUSDT   ICXUSDT     
9465                                NEO USD       NEOUSDT   NEOUSDT     
9466                            VeChain USD       VENUSDT   VENUSDT     
9467                     Stellar Lumens USD       XLMUSDT   XLMUSDT     
9468                               Qtum USD      QTUMUSDT  QTUMUSDT     

    """
    r = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=')
    stock_description = r.json()
    print(pd.DataFrame(stock_description))

def obtain_company_profile(str):
    """
    This is a function to obtain company profile information with Finnhub API.

    Parameters (Inputs)
    ----------
    str
        A string of the compnay's symbol (capitalized characters). For instance, 'AAPL' for Apple.
    
    Returns (Output)
    -------
    DataFrame
        A dataframe containing data of country, currency, exchange, ipo date, market capitalization, name, phone, outstanding shares, etc.

    Examples
    --------
    >>> 
    {
      "country": "US",
      "currency": "USD",
      "exchange": "NASDAQ/NMS (GLOBAL MARKET)",
      "ipo": "1980-12-12",
      "marketCapitalization": 1415993,
      "name": "Apple Inc",
      "phone": "14089961010",
      "shareOutstanding": 4375.47998046875,
      "ticker": "AAPL",
      "weburl": "https://www.apple.com/",
      "logo": "https://static.finnhub.io/logo/87cb30d8-80df-11ea-8951-00000000092a.png",
      "finnhubIndustry":"Technology"
    }
    """
    inquiry = 'https://finnhub.io/api/v1/stock/profile2?symbol=' + str + '&token='
    company_profile = requests.get(inquiry)
    company_profile_json = json.loads(company_profile.content)
    cpj_df = pd.json_normalize(data = company_profile_json)
    return cpj_df

def competitors(str):
    """
    This is a function to obtain the company's competitors in the stock market.

    Parameters (Inputs)
    ----------
    str
        A string of the compnay's symbol (capitalized characters). For instance, 'AAPL' for Apple.
    
    Returns (Output)
    -------
    list of str
        A list of competitors with json format containing the stock symbols of the competitors

    Examples
    --------
    >>> 
    [
      "AAPL",
      "EMC",
      "HPQ",
      "DELL",
      "WDC",
      "HPE",
      "NTAP",
      "CPQ",
      "SNDK",
      "SEG"
    ]
    """
    inquiry = 'https://finnhub.io/api/v1/stock/peers?symbol=' + str + '&token='
    competitors = requests.get(inquiry)
    print(competitors.json())

def financial_data(str):
    """
    This is a function to obtain basic financial data, including margin, P/E ratio, trading volume, etc.

    Parameters (Inputs)
    ----------
    str
        A string of the compnay's symbol (capitalized characters). For instance, 'AAPL' for Apple.
    
    Returns (Output)
    -------
    list of dictionary
        A list of dictionaries of financial data with json format

    Examples
    --------
    >>> 
       {
   "series": {
    "annual": {
      "currentRatio": [
        {
          "period": "2019-09-28",
          "v": 1.5401
        },
        {
          "period": "2018-09-29",
          "v": 1.1329
        }
      ],
      "salesPerShare": [
        {
          "period": "2019-09-28",
          "v": 55.9645
        },
        {
          "period": "2018-09-29",
          "v": 53.1178
        }
      ],
      "netMargin": [
        {
          "period": "2019-09-28",
          "v": 0.2124
        },
        {
          "period": "2018-09-29",
          "v": 0.2241
        }
      ]
  },
  "metric": {
    "10DayAverageTradingVolume": 32.50147,
    "52WeekHigh": 310.43,
    "52WeekLow": 149.22,
    "52WeekLowDate": "2019-01-14",
    "52WeekPriceReturnDaily": 101.96334,
    "beta": 1.2989,
  },
  "metricType": "all",
  "symbol": "AAPL"
}
    """
    inquiry = 'https://finnhub.io/api/v1/stock/metric?symbol=' + str + '&metric=all&token='
    summary = requests.get(inquiry)
    print(summary.json())

def financial_reported(str):
    """
    This is a function to obtain the financial filings reported by the firm.

    Parameters (Inputs)
    ----------
    str
        A string of the compnay's symbol (capitalized characters). For instance, 'AAPL' for Apple.
    
    Returns (Output)
    -------
    Dictionary
        A dictionary of the financial filings reported by the firm in json format

    Examples
    --------
    >>>
    {
  "cik": "320193",
  "data": [
    {
      "accessNumber": "0000320193-19-000119",
      "symbol": "AAPL",
      "cik": "320193",
      "year": 2019,
      "quarter": 0,
      "form": "10-K",
      "startDate": "2018-09-30 00:00:00",
      "endDate": "2019-09-28 00:00:00",
      "filedDate": "2019-10-31 00:00:00",
      "acceptedDate": "2019-10-30 18:12:36",
      "report": {
        "bs": {
          "Assets": 338516000000,
          "Liabilities": 248028000000,
          "InventoryNet": 4106000000,
          ...
        },
        "cf": {
          "NetIncomeLoss": 55256000000,
          "InterestPaidNet": 3423000000,
          ...
        },
        "ic": {
          "GrossProfit": 98392000000,
          "NetIncomeLoss": 55256000000,
          "OperatingExpenses": 34462000000,
           ...
        }
      }
    }
  ],
  "symbol": "AAPL"
}
    """
    inquiry = 'https://finnhub.io/api/v1/stock/financials-reported?symbol=' + str + '&token='
    r = requests.get(inquiry)
    print(r.json())

def ipo_info(str1,str2):
    """
    This is a function to obtain company information that offered their first public offereings during a certain date.

    Parameters (Inputs)
    ----------
    str
        Two arguments of the inquired date range. For instance, "2020-04-01" and "2020-04-03".
    
    Returns (Output)
    -------
    List of Dictionaries
        A list of dictionaries of companies that had IPO during the date range.

    Examples
    --------
    >>>
    {
  "ipoCalendar": [
    {
      "date": "2020-04-03",
      "exchange": "NASDAQ Global",
      "name": "ZENTALIS PHARMACEUTICALS, LLC",
      "numberOfShares": 7650000,
      "price": "16.00-18.00",
      "status": "expected",
      "symbol": "ZNTL",
      "totalSharesValue": 158355000
    },
    {
      "date": "2020-04-01",
      "exchange": "NASDAQ Global",
      "name": "WIMI HOLOGRAM CLOUD INC.",
      "numberOfShares": 5000000,
      "price": "5.50-7.50",
      "status": "expected",
      "symbol": "WIMI",
      "totalSharesValue": 43125000
    },
  ]
}
    """
    inquiry = 'https://finnhub.io/api/v1/calendar/ipo?from=' + str1 + '&to=' + str2 + '&token='
    r = requests.get(inquiry)
    print(r.json())

def recommendation(str):
    """
    This is a function to analyze whether to buy, sell, or hold a company's stock.

    Parameters (Inputs)
    ----------
    str
        A string of the compnay's symbol (capitalized characters). For instance, 'AAPL' for Apple.
    
    Returns (Output)
    -------
    list of str
        A list of competitors with json format containing the stock symbols of the competitors

    Examples
    --------
    >>>
    [
  {
    "buy": 24,
    "hold": 7,
    "period": "2020-03-01",
    "sell": 0,
    "strongBuy": 13,
    "strongSell": 0,
    "symbol": "AAPL"
  }]
    """
    inquiry = 'https://finnhub.io/api/v1/stock/recommendation?symbol=' + str + '&token='
    r = requests.get(inquiry)
    print(r.json())
    
