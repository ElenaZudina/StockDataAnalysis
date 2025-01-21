import streamlit as st
import matplotlib.pyplot as plt
import nbimporter
from stock_analysis import get_company_name, get_current_price, get_stock_info, get_history_data, get_average_trading_volume, plot_price_trend, plot_volume_trend

st.title("Веб-приложение для анализа акций")

ticker = st.text_input("Введите тикер акции")

volume_period = "1mo"

if ticker:
    st.subheader(f"Информация о компании {ticker}")

    company_name = get_company_name(ticker)
    st.write(f"Название компании: **{company_name}**")

    price = get_current_price(ticker)
    st.write(f"Цена: **{price} USD**")

    st.subheader(f"Изменение цены {ticker}")
    
    period = st.selectbox("Выберите период данных", ["1mo", "3mo", "1y", "5y"], key="period_price") #Период 1d не выводится на график
    #interval = "1m" if period == "1d" else "1d"

    data = get_history_data(ticker, period)

    plot_price_trend(data, ticker)

    st.pyplot(plt)

    company_info = get_stock_info(ticker)
    for key, value in company_info.items():
        st.write(f"{key}: **{value}**")

    average_volume = get_average_trading_volume(ticker)
    st.write(f"Средний объем торгов за 10 дней: **{average_volume}**")

    st.subheader(f"Объем торгов {ticker}")

    period = st.selectbox("Выберите период данных", ["1mo", "3mo", "1y", "5y"], key="period_volume") #Период 1d не выводится на график

    data = get_history_data(ticker, period)

    plot_volume_trend(data, ticker)

    st.pyplot(plt)

   


