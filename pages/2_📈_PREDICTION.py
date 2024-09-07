import numpy as np
import pandas as pd
from datetime import  date
import yfinance as yf
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import datetime as dt
import streamlit as st
import base64

st.set_page_config(page_title="CRYPTO WEB-APP",page_icon="🪙")

#bg img func
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover


    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/hetgabdu.jpg')


start = dt.datetime(2016,1,1)
end = dt.datetime.now()
st.title("Cryptocurrency Price Prediction")

#<------------SELECTING CURRENCY--------------->

crypto_name = ("ETH-USD", "MATIC-USD", "DOGE-USD")
selection = st.selectbox("Select", crypto_name)


df = yf.download(selection, start, end)

st.subheader('\n\nDataSet')
st.write("\n\n", df.tail())
df.reset_index(inplace=True)
p_days = 15

df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=True)

#<------------TIME PERIOD & PREDICTION--------------->

p_days = st.slider("Time Duiration:", 1, 30)
period = p_days * 15
df['prediction'] = df['Adj Close'].shift(-p_days)

#<------------INDEPENDENT DATA--------------->
X = np.array(df.drop(['prediction', 'Date'], axis=1))
X = X[:len(df)-p_days]
print(X)

#<------------DEPENDENT DATA--------------->
y = np.array(df['prediction'])
y = y[:-p_days]
print(y)

#<------------SPLITING--------------->
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

print(x_train.shape)
print(x_test.shape)
p_days_array = np.array(df.drop(['prediction', 'Date'], axis=1))[-p_days:]
print(p_days_array)

#<------------CREATING MODEL--------------->

svr = SVR(kernel = 'rbf', C=1e3, gamma=0.1)
svr.fit (x_train, y_train)

svr_accuracy = svr.score(x_test, y_test)
print("Accuracy: ", svr_accuracy)

#<------------PREDICTION--------------->
svm_prediction = svr.predict(x_test)
print(svm_prediction)

print(y_test)

svm_prediction = svr.predict(p_days_array)
print(svm_prediction)

#<------------GRAPHS--------------->
st.subheader("ALL TIME PRICE")
fig = plt.figure(figsize = (12, 6))
plt.plot(df['Adj Close'], label = "ALL TIME PRICE")
plt.xlabel("TIME")
plt.ylabel("Price")
plt.legend()
st.pyplot(fig)

st.subheader("LAST 15 days")
last_15_days = df['Adj Close'].tail(15)
fig1 = plt.figure(figsize = (12, 6))
plt.plot(last_15_days, 'b', label="Recent 15")
plt.legend()
plt.show()
st.pyplot(fig1)

df.drop(['Date'], axis=1)
last_1_year = df['Adj Close'].tail(365)

st.subheader('PREDICTION')

fig = plt.figure(figsize=(12, 6))
gs = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[3, 1])
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :])

ax1.plot(df['Adj Close'], label="All Time Price")
ax1.plot(svm_prediction, label="Prediction", color='red')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price')
ax1.legend()

ax2.plot(last_1_year, color='blue')
ax2.set_xlabel('Time')
ax2.set_ylabel('Price')
ax2.set_title('Last 1 Year')

plt.tight_layout()
st.pyplot(fig)
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(50, 50))

# Plot ALL TIME PRICE in the first subplot

axs[0].plot(df['Adj Close'], label="ALL TIME PRICE")
axs[0].set_xlabel("TIME")
axs[0].set_ylabel("Price")
axs[0].legend()

# Plot LAST 15 days in the second subplot
last_15_days = df['Adj Close'].tail(15)
axs[1].plot(last_15_days, 'b', label="Recent 15")
axs[1].legend()

# Plot the prediction in the first subplot
axs[0].plot(svm_prediction, 'r', label="prediction")
axs[0].legend()

# Set the title for the second subplot
axs[1].set_title("LAST 15 days")

plt.show()

st.write(svr_accuracy)
#st.subheader("Prediction")
#fig2 = plt.figure(figsize= (12,6))
#plt.plot(last_1_year, 'b', label = "ALL TIME PRICE")
#plt.plot(svm_prediction, 'red', label = "prediction")
#plt.xlabel('TIME')
#plt.ylabel('PRICE')
#plt.legend()
#st.pyplot(fig2)

st.subheader("Predicted Prices")
st.write(p_days_array)



