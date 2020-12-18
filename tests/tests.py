from stock_price_info import stock_info
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json


def test_obtain_stock_description():
    stock_description = stock_info.obtain_stock_description()
    assert type(stock_description) == pd.core.frame.DataFrame

def test_obtain_company_profile(str):
    company_profile = stock_info.obtain_company_profile(str)
    assert type(company_profile) == pd.core.frame.DataFrame

def test_competitors(str):
    competitors = stock_info.competitors(str)
    assert type(company_profile) == list

def test_financial_data(str):
    competitors = stock_info.financial_data(str)
    assert type(competitors) == dict

def test_financial_reported(str):
    financial_reported = stock_info.financial_reported(str)
    assert type(financial_reported) == dict

def test_recommendation(str):
    recommendation = stock_info.recommendation(str)
    assert type(recommendation) == dict
