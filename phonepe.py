import os
import json
import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

#path for json file of aggregated transition
path_1 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/aggregated/transaction/country/india/state/"
agreTransactionStateList = os.listdir(path_1)
columns_1 = {"States":[], "Years":[], "Quarters":[], "typeOfPayment":[], "totalNumOfTransactions":[], "totalValue":[]}

for state in agreTransactionStateList:
    cur_states= path_1+state+"/"
    aggYearList = os.listdir(cur_states)

    for year in aggYearList:
        curYears = cur_states+year+"/" 
        aggFileList = os.listdir(curYears)

        for file in aggFileList:
            curFile = curYears+ file
            data = open(curFile,"r")
            A = json.load(data)
            
            for i in A["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                columns_1["typeOfPayment"].append(name)
                columns_1["totalNumOfTransactions"]. append(count)
                columns_1["totalValue"].append(amount)
                columns_1["States"].append(state.replace("&","and"))
                columns_1["Years"].append(year)
                columns_1["Quarters"].append(int(file.strip(".json")))

aggreTransaction = pd.DataFrame(columns_1)

#path for json file of aggregated user 
path_2 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/aggregated/user/country/india/state/"
columns_2 = {"States":[], "Years":[], "Quarters":[], "Brands":[], "registeredUsers":[], "Percentage":[]}
aggUserStateList = os.listdir(path_2)

for state in aggUserStateList:
    currStates= path_2+state+"/"
    aggYearList = os.listdir(currStates)

    for year in aggYearList:
        currYears = currStates+year+"/" 
        aggFileList = os.listdir(currYears)


        for file in aggFileList:
            currFile = currYears+ file
            data = open(currFile,"r")
            B = json.load(data)
    #             print(B)
            try:

                for i in B["data"]["usersByDevice"]:
                    name = i["brand"]
                    count = i["count"]
                    percentage = i["percentage"]
                    columns_2["States"].append(state.replace("&","and"))
                    columns_2["Years"].append(year)
                    columns_2["Quarters"].append(int(file.strip(".json")))
                    columns_2["Brands"].append(name)
                    columns_2["registeredUsers"].append(count)
                    columns_2["Percentage"].append(percentage)
            except:
                pass

aggrUserList = pd.DataFrame(columns_2)

#path for json file of aggregated insurance
path_3 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/aggregated/insurance/country/india/state/"
aggreInsuranceStateList = os.listdir(path_3)
columns_3 = {"States":[], "Years":[], "Quarters":[], "typeOfPaymentCategory":[], "insuranceCount":[], "totalValue":[]}

for state in aggreInsuranceStateList:
    currStates =path_3+state+"/"
    aggYearList = os.listdir(currStates)
    
    for year in aggYearList:
        currYears = currStates+year+"/"
        aggFileList = os.listdir(currYears)

        for file in aggFileList:
            curFiles = currYears+file
            data = open(curFiles,"r")
            C = json.load(data)

            for i in C["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                columns_3["typeOfPaymentCategory"].append(name)
                columns_3["insuranceCount"].append(count)
                columns_3["totalValue"].append(amount)
                columns_3["States"].append(state.replace("&","and"))
                columns_3["Years"].append(year)
                columns_3["Quarters"].append(int(file.strip(".json")))
aggreInsurance = pd.DataFrame(columns_3)

#path for json file of map insurance
path_4 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/map/insurance/hover/country/india/state/"
mapInsuranceStateList = os.listdir(path_4)
columns_4 = {"States":[], "Years":[], "Quarters":[], "Districts":[], "insuranceCount":[], "totalInsuranceValue":[]}
for state in mapInsuranceStateList:
    currStates = path_4+state+"/"
    mapYearList = os.listdir(currStates)
    
    for year in mapYearList:
        currYear = currStates+year+"/"
        mapFileList = os.listdir(currYear)
        
        for file in mapFileList:
            currFiles = currYear+file
            data = open(currFiles,"r")
            D = json.load(data)
            
            for i in D["data"]["hoverDataList"]:
                name = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns_4["States"].append(state.replace("&","and"))
                columns_4["Years"].append(year)
                columns_4["Quarters"].append(int(file.strip(".json")))
                columns_4["Districts"].append(name)
                columns_4["insuranceCount"].append(count)
                columns_4["totalInsuranceValue"].append(amount)
mapInsuranceList = pd.DataFrame(columns_4)     

#path for json file of map transaction
path_5 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/map/transaction/hover/country/india/state/"
mapTransactionStateList = os.listdir(path_5)   
columns_5 = {"States":[], "Years":[], "Quarters":[], "Districts":[], "transactionCount":[], "totalTransactionValue":[]}
for state in mapTransactionStateList:
    currStates = path_5+state+"/"
    mapYearList = os.listdir(currStates)
    
    for year in mapYearList:
        currYears = currStates+year+"/"
        currFileList = os.listdir(currYears)
        
        for file in currFileList:
            currFile = currYears+file
            data = open(currFile,"r")
            E = json.load(data)
            
            for i in E["data"]["hoverDataList"]:
                name = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns_5["States"].append(state.replace("&","and"))
                columns_5["Years"].append(year)
                columns_5["Quarters"].append(int(file.strip(".json")))
                columns_5["Districts"].append(name.replace("&","and"))
                columns_5["transactionCount"].append(count)
                columns_5["totalTransactionValue"].append(amount)

mapTransactionList = pd.DataFrame(columns_5)      

#path for json file of map user
path_6 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/map/user/hover/country/india/state/"               
mapUserStateList = os.listdir(path_6)            
columns_6 = {"States":[], "Years":[], "Quarters":[], "Districts":[], "registeredUser":[], "appOpens":[]}       

for state in mapUserStateList:
    currStates = path_6+state+"/"
    mapYearList = os.listdir(currStates)
    
    for year in mapYearList:
        currYears = currStates+year+"/"
        mapFileList = os.listdir(currYears)
        
        for file in mapFileList:
            currFiles = currYears+file
            data = open(currFiles,"r")
            F = json.load(data)

            for i in F["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appopens = i[1]["appOpens"]
                columns_6["Districts"].append(district.replace("&","and"))
                columns_6["registeredUser"].append(registereduser)
                columns_6["appOpens"].append(appopens)
                columns_6["States"].append(state.replace("&","and"))
                columns_6["Years"].append(year)
                columns_6["Quarters"].append(int(file.strip(".json")))

mapUserList = pd.DataFrame(columns_6)

#path for json file of top insurance
path_7 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/top/insurance/country/india/state/"
topInsuranceStateList = os.listdir(path_7)
columns_7 =  {"States":[], "Years":[], "Quarters":[], "Districts":[],  "insuranceCount":[], "totalValueOfInsurance":[]}
columns_8 = {"States":[], "Years":[], "Quarters":[],"Pincodes":[],"insuranceCount":[], "totalValueOfInsurance":[]}

for state in topInsuranceStateList:
    currStates = path_7 + state + "/"
    topYearList = os.listdir(currStates)
    
    for year in topYearList:
        currYears = currStates + year + "/"
        topFileList = os.listdir(currYears)
        
        for file in topFileList:
            currFiles = currYears + file
            data = open(currFiles, "r")
            
            G = json.load(data)
            
            for i in G["data"]["districts"]:
                name = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                columns_7["States"].append(state.replace("&","and"))
                columns_7["Years"].append(year)
                columns_7["Quarters"].append(int(file.strip(".json")))
                columns_7["Districts"].append(name.replace("&","and"))
                columns_7["insuranceCount"].append(count)
                columns_7["totalValueOfInsurance"].append(amount)
                
        #by PINCODES
            for j in G["data"]["pincodes"]:
                pincode = j["entityName"]
                count = j["metric"]["count"]
                amount = j["metric"]["amount"]
                columns_8["States"].append(state.replace("&","and"))
                columns_8["Years"].append(year)
                columns_8["Quarters"].append(int(file.strip(".json")))
                columns_8["Pincodes"].append(pincode)
                columns_8["insuranceCount"].append(count)
                columns_8["totalValueOfInsurance"].append(amount)

topInsuranceDistrictList = pd.DataFrame(columns_7)
topInsurancePincodeList = pd.DataFrame(columns_8)

#path for json file of top transaction
path_8 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/top/transaction/country/india/state/"
topTransactionStateList = os.listdir(path_8)
columns_9 = {"States":[], "Years":[], "Quarters":[],"Districts":[],"transactionCount":[], "totalValueOfTransactions":[]}
columns_10 = {"States":[], "Years":[], "Quarters":[],"Pincodes":[],"transactionCount":[], "totalValueOfTransactions":[]}

for state in topTransactionStateList:
    currStates = path_8 + state + "/"
    topYearList = os.listdir(currStates)
    
    for year in topYearList:
        currYears = currStates + year + "/"
        topFileList = os.listdir(currYears)
        
        for file in topFileList:
            currFiles = currYears + file
            data = open(currFiles, "r")
            
            H = json.load(data)
            
            for i in H["data"]["districts"]:
                name = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                columns_9["States"].append(state.replace("&","and"))
                columns_9["Years"].append(year)
                columns_9["Quarters"].append(int(file.strip(".json")))
                columns_9["Districts"].append(name.replace("&","and"))
                columns_9["transactionCount"].append(count)
                columns_9["totalValueOfTransactions"].append(amount)

        #by pincodes   
            for j in H["data"]["pincodes"]:
                pincode = j["entityName"]
                count = j["metric"]["count"]
                amount = j["metric"]["amount"]
                columns_10["States"].append(state.replace("&","and"))
                columns_10["Years"].append(year)
                columns_10["Quarters"].append(int(file.strip(".json")))
                columns_10["Pincodes"].append(pincode)
                columns_10["transactionCount"].append(count)
                columns_10["totalValueOfTransactions"].append(amount)

topTranDistrictList = pd.DataFrame(columns_9)
topTranPincodeList = pd.DataFrame(columns_10)
# print(topTranPincodeList)

#path for json file of top user
path_9 = "D:/GUVI/Projects/Project.2/PhonePe/pulse/data/top/user/country/india/state/"
topUserStateList = os.listdir(path_9)
columns_11 = {"States":[], "Years":[], "Quarters":[], "Pincodes":[], "registeredUsers":[]}
columns_12 = {"States":[], "Years":[], "Quarters":[], "registeredUsers":[],"Districts":[]}
for state in topUserStateList:
    currStates = path_9+state+"/"
    topYearList = os.listdir(currStates)
    
    for year in topYearList:
        currYears = currStates + year+"/"
        topFileList = os.listdir(currYears)
        
        for file in topFileList:
            currFiles = currYears + file
            data = open(currFiles,"r")
            
            I = json.load(data)
            
            for i in I["data"]["pincodes"]:
                name = i["name"]
                registeredUser = i["registeredUsers"]
                columns_11["States"].append(state.replace("&","and"))
                columns_11["Years"].append(year)
                columns_11["Quarters"].append(int(file.strip(".json")))
                columns_11["Pincodes"].append(name)
                columns_11["registeredUsers"].append(registeredUser)
                
            for j in I["data"]["districts"]:
                name = j["name"]
                regUser = j["registeredUsers"]
                columns_12["States"].append(state.replace("&","and"))
                columns_12["Years"].append(year)
                columns_12["Quarters"].append(int(file.strip(".json")))
                columns_12["Districts"].append(name)
                columns_12["registeredUsers"].append(regUser)

topUserPincodeList = pd.DataFrame(columns_11)
topUserDistrictList = pd.DataFrame(columns_12)
                
# SQL connection
username = 'root'
password = '255244'
host = 'localhost'
database_name = 'PhonePePulse'

# Create the engine
mydb = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database_name
)

if mydb.is_connected():
    print(f"Connected to {database_name} database on {host}")
else:
    print("Connection failed")
    
cursor = mydb.cursor()   

def table_AT(mydb, cursor):
    
    create_query = """CREATE TABLE IF NOT EXISTS AGGREGATED_TRANSACTION(STATES VARCHAR(50),
                                                                        YEARS INT,
                                                                        QUARTERS INT,
                                                                        TYPE_OF_PAYMENT VARCHAR(50),
                                                                        TOTAL_TRANSACTIONS BIGINT,
                                                                        TOTAL_VALUE BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()
    print("Table created")
    for index, row in aggreTransaction.iterrows():
        insert_query = """INSERT INTO AGGREGATED_TRANSACTION(STATES,
                                                            YEARS,
                                                            QUARTERS,
                                                            TYPE_OF_PAYMENT,
                                                            TOTAL_TRANSACTIONS,
                                                            TOTAL_VALUE)
                                                            values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["typeOfPayment"],
                  row["totalNumOfTransactions"],
                  row["totalValue"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
            print("Data loaded")
        except Exception as e:
            print(f"Error inserting data: {e}")
# print("calling table AT")
# # table_AT(mydb, cursor)
# print("exit table AT")
def table_AI(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS AGGREGATED_INSURANCE(STATES VARCHAR(50),
                                                                        YEARS INT,
                                                                        QUARTERS INT,
                                                                        TYPE_OF_PAYMENT_CATEGORY VARCHAR(50),
                                                                        INSURANCE_COUNT BIGINT,
                                                                        TOTAL_VALUE BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()
    
    for index, row in aggreInsurance.iterrows():
        insert_query = """INSERT INTO AGGREGATED_INSURANCE(STATES,
                                                            YEARS,
                                                            QUARTERS,
                                                            TYPE_OF_PAYMENT_CATEGORY,
                                                            INSURANCE_COUNT,
                                                            TOTAL_VALUE)
                                                            values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["typeOfPaymentCategory"],
                  row["insuranceCount"],
                  row["totalValue"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_AI(mydb, cursor)
def table_AU(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS AGGREGATED_USER(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                BRANDS VARCHAR(20),
                                                                REGISTERED_USERS BIGINT,
                                                                PERCENTAGE FLOAT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in aggrUserList.iterrows():
        insert_query = """INSERT INTO AGGREGATED_USER(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    BRANDS,
                                                    REGISTERED_USERS,
                                                    PERCENTAGE)
                                                    values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["Brands"],
                  row["registeredUsers"],
                  row["Percentage"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_AU(mydb, cursor)
def table_MI(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS MAP_INSURANCE(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                DISTRICTS VARCHAR(50),
                                                                INSURANCE_COUNT BIGINT,
                                                                TOTAL_INSURANCE_VALUE FLOAT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in mapInsuranceList.iterrows():
        insert_query = """INSERT INTO MAP_INSURANCE(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    DISTRICTS,
                                                    INSURANCE_COUNT,
                                                    TOTAL_INSURANCE_VALUE)values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["Districts"],
                  row["insuranceCount"],
                  row["totalInsuranceValue"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_MI(mydb, cursor)
def table_MT(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS MAP_TRANSACTION(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                DISTRICTS VARCHAR(50),
                                                                TRANSACTION_COUNT BIGINT,
                                                                TOTAL_TRANSACTION_VALUE FLOAT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in mapTransactionList.iterrows():
        insert_query = """INSERT INTO MAP_TRANSACTION(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    DISTRICTS,
                                                    TRANSACTION_COUNT,
                                                    TOTAL_TRANSACTION_VALUE)values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["Districts"],
                  row["transactionCount"],
                  row["totalTransactionValue"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_MT(mydb, cursor)
def table_MU(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS MAP_USER(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                DISTRICTS VARCHAR(50),
                                                                REGISTERED_USER BIGINT,
                                                                APP_OPEN BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in mapUserList.iterrows():
        insert_query = """INSERT INTO MAP_USER(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    DISTRICTS,
                                                    REGISTERED_USER,
                                                    APP_OPEN)values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["Districts"],
                  row["registeredUser"],
                  row["appOpens"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_MU(mydb, cursor)
def table_TID(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS TOP_INSURANCE_DISTRICT_WISE(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                DISTRICTS VARCHAR(50),
                                                                INSURANCE_COUNT BIGINT,
                                                                TOTAL_VALUE_OF_INSURANCE BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in topInsuranceDistrictList.iterrows():
        insert_query = """INSERT INTO TOP_INSURANCE_DISTRICT_WISE(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    DISTRICTS,
                                                    INSURANCE_COUNT,
                                                    TOTAL_VALUE_OF_INSURANCE)values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["Districts"],
                  row["insuranceCount"],
                  row["totalValueOfInsurance"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_TID(mydb, cursor)
def table_TIP(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS TOP_INSURANCE_PINCODE_WISE(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                PINCODES INT,
                                                                INSURANCE_COUNT BIGINT,
                                                                TOTAL_VALUE_OF_INSURANCE BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in topInsurancePincodeList.iterrows():
        insert_query = """INSERT INTO TOP_INSURANCE_PINCODE_WISE(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    PINCODES,
                                                    INSURANCE_COUNT,
                                                    TOTAL_VALUE_OF_INSURANCE)values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["Pincodes"],
                  row["insuranceCount"],
                  row["totalValueOfInsurance"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_TIP(mydb, cursor)
def table_TTD(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS TOP_TRANSACTION_DISTRICT_WISE(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                DISTRICTS VARCHAR(50),
                                                                TRANSACTION_COUNT BIGINT,
                                                                TOTAL_VALUE_OF_TRANSACTION BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in topTranDistrictList.iterrows():
        insert_query = """INSERT INTO TOP_TRANSACTION_DISTRICT_WISE(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    DISTRICTS,
                                                    TRANSACTION_COUNT,
                                                    TOTAL_VALUE_OF_TRANSACTION)values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["Districts"],
                  row["transactionCount"],
                  row["totalValueOfTransactions"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_TTD(mydb, cursor)
def table_TTP(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS TOP_TRANSACTION_PINCODE_WISE(STATES VARCHAR(50), YEARS INT,
                                                                            QUARTERS INT, PINCODES INT, TRANSACTION_COUNT BIGINT,
                                                                            TOTAL_VALUE_OF_TRANSACTION BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index,row in topTranPincodeList.iterrows():
        insert_query = """INSERT INTO TOP_TRANSACTION_PINCODE_WISE(STATES, YEARS, QUARTERS, PINCODES, TRANSACTION_COUNT,
                                                                    TOTAL_VALUE_OF_TRANSACTION) values(%s,%s,%s,%s,%s,%s)"""
        values = (row["States"], row["Years"], row["Quarters"],row["Pincodes"],row["transactionCount"], 
                  row["totalValueOfTransactions"])
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data:{e}")
# table_TTP(mydb, cursor)
def table_TUD(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS TOP_USER_DISTRICT_WISE(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                DISTRICTS VARCHAR(50),
                                                                REGISTERED_USERS BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()

    for index, row in topUserDistrictList.iterrows():
        insert_query = """INSERT INTO TOP_USER_DISTRICT_WISE(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    REGISTERED_USERS,
                                                   DISTRICTS)values(%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["registeredUsers"],
                  row["Districts"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
# table_TUD(mydb, cursor)
def table_TUP(mydb, cursor):
    create_query = """CREATE TABLE IF NOT EXISTS TOP_USER_PINCODE_WISE(STATES VARCHAR(50),
                                                                YEARS INT,
                                                                QUARTERS INT,
                                                                PINCODES INT,
                                                                REGISTERED_USERS BIGINT)"""
    cursor.execute(create_query)
    mydb.commit()
    print("table created")
    for index, row in topUserPincodeList.iterrows():
        insert_query = """INSERT INTO TOP_USER_PINCODE_WISE(STATES,
                                                    YEARS,
                                                    QUARTERS,
                                                    REGISTERED_USERS,
                                                   PINCODES)values(%s,%s,%s,%s,%s)"""
        values = (row["States"],
                  row["Years"],
                  row["Quarters"],
                  row["registeredUsers"],
                  row["Pincodes"]
                  )
        try:
            cursor.execute(insert_query, values)
            mydb.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
    
#-----------------Streamlit Part--------------
st.set_page_config(page_title='PhonePe Pulse',
                    page_icon=':phone:', layout="wide")

# page header transparent color
page_background_color = """
<style>

[data-testid="stHeader"] 
{
background: rgba(0,1,0,0);
}

</style>
"""
st.markdown(page_background_color, unsafe_allow_html=True)

# title and position
st.markdown(f'<h1 style="text-align: center;">PhonePe Pulse</h1>',
            unsafe_allow_html=True)

#Display Map  for Transactions
def map_display_T(year, quarter):
    st.write(":rainbow[**Map Representation for " +year_quarter+"**]")
    states = json.load(open("states_india.geojson","r"))
    
    q = "select states, total_value from aggregated_transaction where years = "+year+" and quarters = "+quarter+" and type_of_payment = 'Financial Services'"
    cursor.execute(q)
    a = cursor.fetchall()
    df = pd.DataFrame(a, columns = ["State", "Transaction Amount"])
    new_states=[]
    new_amount=[]
    for i in range(0,35):
        new_states.append(a[i][0])
        new_amount.append(a[i][1])
    
    dict = { 'States': new_states,'Amount': new_amount} 
        
    df1 = pd.DataFrame(dict)    

    india_states = json.load(open("states_india.geojson", "r"))
    list_states=[]
    for i in range(0,36):
        list_states.append((india_states["features"][i]["properties"]["ST_NM"]))
        
    json1=f"states_india.geojson"
    fig = px.choropleth(df1, geojson=india_states, locations='States', color='Amount',
                            featureidkey="properties.ST_NM",
                            color_continuous_scale="Viridis",
                            range_color=(0, 12),
                            scope="asia",
                            #labels={'States':'Amount'}
                            )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)
    #Display Map End           

#Map display for Insurance
def map_display_I(year, quarter):
    st.write(":rainbow[**Map Representation for " +year_quarter+"**]")
    states = json.load(open("states_india.geojson","r"))
    
    q = "select states, total_value from aggregated_insurance where years = "+year+" and quarters = "+quarter
    cursor.execute(q)
    a = cursor.fetchall()
    df = pd.DataFrame(a, columns = ["State", "Transaction Amount"])
    new_states=[]
    new_amount=[]
    for i in range(0,35):
        new_states.append(a[i][0])
        new_amount.append(a[i][1])
    
    dict = { 'States': new_states,'Amount': new_amount} 
        
    df1 = pd.DataFrame(dict)    

    india_states = json.load(open("states_india.geojson", "r"))
    list_states=[]
    for i in range(0,36):
        list_states.append((india_states["features"][i]["properties"]["ST_NM"]))
        
    json1=f"states_india.geojson"
    fig = px.choropleth(df1, geojson=india_states, locations='States', color='Amount',
                            featureidkey="properties.ST_NM",
                            color_continuous_scale="Viridis",
                            range_color=(0, 12),
                            scope="asia",
                            #labels={'States':'Amount'}
                            )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)
            
# map display of User
def map_display_U(year, quarter):
    st.write(":rainbow[**Map Representation for " +year_quarter+"**]")
    states = json.load(open("states_india.geojson","r"))
    
    q = "select states, registered_users from aggregated_user where years = "+year+" and quarters = "+quarter+" order by brands"
    cursor.execute(q)
    a = cursor.fetchall()
    df = pd.DataFrame(a, columns = ["State", "Registered Users"])
    new_states=[]
    new_amount=[]
    for i in range(0,35):
        new_states.append(a[i][0])
        new_amount.append(a[i][1])
    
    dict = { 'States': new_states,'Registered Users': new_amount} 
        
    df1 = pd.DataFrame(dict)    

    india_states = json.load(open("states_india.geojson", "r"))
    list_states=[]
    for i in range(0,36):
        list_states.append((india_states["features"][i]["properties"]["ST_NM"]))
        
    json1=f"states_india.geojson"
    fig = px.choropleth(df1, geojson=india_states, locations='States', color='Registered Users',
                            featureidkey="properties.ST_NM",
                            color_continuous_scale="Viridis",
                            range_color=(0, 12),
                            scope="asia",
                            #labels={'States':'Amount'}
                            )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)

#sidebar selectbox for Home, Insrance, Payment    
ex = st.sidebar.selectbox("**Explore Data**",("Home","Insurance", "Payment", "Top 10 Interesting Facts"))
if ex == "Home":
    st.header("**:rainbow[PhonePe]**")
    st.subheader("**India's Best Transaction App**")
    st.markdown("PhonePe  is an Indian digital payments and financial technology company")
    st.write("**Features**")
    st.write("Credit & Debit card linking")
    st.write("Bank Balance check")
    st.write("Money Storage")
    st.write("PIN Authorization")
    st.link_button(":blue[DOWNLOAD THE APP NOW]", "https://www.phonepe.com/app-download/")

if ex == "Insurance":
    year_quarter = st.sidebar.selectbox(
        "Select the Year and Quarter",
        ("2020 Q1", "2020 Q2", "2020 Q3","2020 Q4","2021 Q1", "2021 Q2", "2021 Q3","2021 Q4",
        "2022 Q1", "2022 Q2", "2022 Q3","2022 Q4", "2023 Q1", "2023 Q2", "2023 Q3","2023 Q4" ))
    
    if year_quarter =="2020 Q1":
        year = "2020"
        quarter = "1"
        st.write("**:red[Data is not available for] :rainbow[ "+year_quarter+"]**")

    elif year_quarter =="2020 Q2":
        year = "2020"
        quarter = "2"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2020 Q3":
        year = "2020"
        quarter = "3"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2020 Q4":
        year = "2020"
        quarter = "4"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2021 Q1":
        year = "2021"
        quarter = "1"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2021 Q2":
        year = "2021"
        quarter = "2"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2021 Q3":
        year = "2021"
        quarter = "3"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2021 Q4":
        year = "2021"
        quarter = "4"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2022 Q1":
        year = "2022"
        quarter = "1"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2022 Q2":
        year = "2022"
        quarter = "2"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2022 Q3":
        year = "2022"
        quarter = "3"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2022 Q4":
        year = "2022"
        quarter = "4"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2023 Q1":
        year = "2023"
        quarter = "1"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2023 Q2":
        year = "2023"
        quarter = "2"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))

    elif year_quarter =="2023 Q3":
        year = "2023"
        quarter = "3"
        col1,col2 = st.columns(2)
        with col1:
            query = "select sum(insurance_count) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Count :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Count"]))
        with col2:
            query4 = "select sum(total_value) from aggregated_insurance where quarters ="+quarter+" and years ="+year
            # st.write(query)
            cursor.execute(query4)
            q1 = cursor.fetchall()
            st.write("**Total Insurance Amount :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Total Insurance Amount"]))
    else:
        year = "2023"
        quarter = "4"
        st.write(":red[**Data is not available for] :rainbow[ "+year_quarter+"]**")

    top10 = st.sidebar.radio("**Display Insurance Details by:-**", ["States", "Districts", "Postal Codes"])
    states = ["andaman-and-nicobar-islands","andhra-pradesh","arunachal-pradesh","dadra-and-nagar-haveli-and-daman-and-diu",
            "assam","bihar","chandigarh",
            "chhattisgarh","delhi","goa","gujarat","haryana","himachal-pradesh","jammu-and-kashmir",
            "jharkhand","karnataka","kerala","ladakh","lakshadweep","madhya-pradesh","maharashtra",
            "manipur","meghalaya","mizoram","nagaland","odisha","puducherry","punjab","rajasthan","sikkim","tamil-nadu",
            "telangana","tripura","uttar-pradesh","uttarakhand","west-bengal"]

    if top10 == "States":
        col1,col2= st.columns(2)
        with col1:
            q = "select states, total_value, insurance_count from aggregated_insurance where years = "+year+" and quarters ="+quarter+" order by total_value desc limit 50"
            cursor.execute(q)
            q1 = cursor.fetchall()
            st.write("**Insurance Details State-Wise :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["States","Insurance Amount","Insurance Count"]))
            
        with col2:  
            df = pd.DataFrame(q1, columns = ["States","Insurance Amount","Insurance Count"])
            fig = px.histogram(df, x='States', y='Insurance Amount')
            st.plotly_chart(fig)
        map_display_I(year, quarter)

    if top10 == "Districts":
        col1,col2= st.columns(2)
        with col1:
            q = "select districts, insurance_count, total_value_of_insurance from top_insurance_district_wise where years = '"+year+"' and quarters ='"+quarter+"' order by total_value_of_insurance desc limit 30"
            cursor.execute(q)
            q1 = cursor.fetchall()
            st.write("**Insurance Details District-Wise :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Districts","Insurance Count", "Insurance Amount"]))
            df = pd.DataFrame(q1, columns = ["Districts","Insurance Count", "Insurance Amount"])
        with col2:   
            fig = px.histogram(df, x='Districts', y='Insurance Amount')
            st.plotly_chart(fig)

    if top10 == "Postal Codes":
        q = "select pincodes, insurance_count, total_value_of_insurance from top_insurance_pincode_wise where years = '"+year+"' and quarters ='"+quarter+"' order by total_value_of_insurance desc limit 30"
        cursor.execute(q)
        q1 = cursor.fetchall()
        st.write("**Insurance Details Postal Code-Wise :rainbow[ "+year_quarter+"]**")
        st.write(pd.DataFrame(q1, columns = ["Postal Codes","Insurance Count", "Insurance Amount"]))
        
if ex == "Payment":
    option = st.sidebar.selectbox("",("Transaction", "User"))

    if option == "Transaction":
        year_quarter = st.sidebar.selectbox(
        "Select the Year and Quarter",
        ("2018 Q1", "2018 Q2", "2018 Q3","2018 Q4","2019 Q1", "2019 Q2", "2019 Q3","2019 Q4","2020 Q1", "2020 Q2", "2020 Q3","2020 Q4","2021 Q1", "2021 Q2", "2021 Q3","2021 Q4",
        "2022 Q1", "2022 Q2", "2022 Q3","2022 Q4", "2023 Q1", "2023 Q2", "2023 Q3","2023 Q4" ))

        if year_quarter =="2018 Q1":
            col1,col2= st.columns(2)
            with col1:
                year = "2018"
                quarter = "1"
                query1 = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query1)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                year = "2018"
                quarter = "1"
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2018 Q2":
            col1,col2= st.columns(2)
            with col1:
                year = "2018"
                quarter = "2"
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                year = "2018"
                quarter = "2"
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2018 Q3":
            col1,col2= st.columns(2)
            with col1:
                year = "2018"
                quarter = "3"
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                year = "2018"
                quarter = "3"   
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2018 Q4":

            year = "2018"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2019 Q1":
            year = "2019"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2019 Q2":
            year = "2019"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2019 Q3":
            year = "2019"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2019 Q4":
            year = "2019"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"])) 
            with col2:   
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2020 Q1":
            year = "2020"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2020 Q2":
            year = "2020"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2020 Q3":
            year = "2020"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2020 Q4":
            year = "2020"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2021 Q1":
            year = "2021"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2021 Q2":
            year = "2021"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2021 Q3":
            year = "2021"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2021 Q4":
            year = "2021"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2022 Q1":
            year = "2022"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2022 Q2":
            year = "2022"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2022 Q3":
            year = "2022"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2022 Q4":
            year = "2022"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2023 Q1":
            year = "2023"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2023 Q2":
            year = "2023"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        elif year_quarter =="2023 Q3":
            year = "2023"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select sum(total_transactions) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Count for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Count"]))
            with col2:
                query2 = "select sum(total_value) from aggregated_transaction where quarters ="+quarter+" and years ="+year
                cursor.execute(query2)
                q1 = cursor.fetchall()
                st.write("**Total Transaction Amount for :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Total Transaction Amount"]))

        else:
            year = "2023"
            quarter = "4"
            st.write("**:red[Data not available for] :rainbow[ "+year_quarter+"]**")

        top10 = st.sidebar.radio("**Display transactions based on below options:**", ["States", "Districts", "Postal Codes","Payment Category"])
        states = ["andaman-and-nicobar-islands","andhra-pradesh","arunachal-pradesh","dadra-and-nagar-haveli-and-daman-and-diu",
                "assam","bihar","chandigarh",
                "chhattisgarh","delhi","goa","gujarat","haryana","himachal-pradesh","jammu-and-kashmir",
                "jharkhand","karnataka","kerala","ladakh","lakshadweep","madhya-pradesh","maharashtra",
                "manipur","meghalaya","mizoram","nagaland","odisha","puducherry","punjab","rajasthan","sikkim","tamil-nadu",
                "telangana","tripura","uttar-pradesh","uttarakhand","west-bengal"]

        if top10 == "States":
            col1,col2= st.columns(2)
            # s = st.selectbox("Choose State", (states))
            with col1:
                q = "select states,total_value, total_transactions from aggregated_transaction where years = '"+year+"' and quarters ='"+quarter+"' and type_of_payment = 'Financial Services' order by total_value desc limit 50"
                # # st.write(q)
                cursor.execute(q)
                q1 = cursor.fetchall()
                st.write("**Transaction Details State-Wise :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Transaction Amount","Total Transaction Count"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Transaction Amount","Total Transaction Count"])
            
                fig = px.histogram(df, x='States', y='Transaction Amount')
                st.plotly_chart(fig)
            map_display_T(year, quarter)
            
        if top10 == "Districts":
            col1,col2= st.columns(2)
            with col1:

                q = "select districts, transaction_count, total_value_of_transaction from top_transaction_district_wise where years = '"+year+"' and quarters ='"+quarter+"' order by total_value_of_transaction desc limit 30"

                cursor.execute(q)
                q1 = cursor.fetchall()
                st.write("**Transaction Details District-Wise :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Districts","Total Transaction Count","Transaction Amount"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["Districts","Total Transaction Count","Transaction Amount"])
            
                fig = px.histogram(df, x='Districts', y='Transaction Amount')
                st.plotly_chart(fig)

        if top10 == "Postal Codes":
            q = "select pincodes, transaction_count, total_value_of_transaction from top_transaction_pincode_wise where years = '"+year+"' and quarters ='"+quarter+"' order by total_value_of_transaction desc limit 50"
            # st.write(q)
            cursor.execute(q)
            q1 = cursor.fetchall()
            st.write("**Transaction Details Postal Code-Wise :rainbow[ "+year_quarter+"]**")
            st.write(pd.DataFrame(q1, columns = ["Postal Codes","Total Transaction Count","Transaction Amount"]))
            

        if top10 == "Payment Category":
            t = []
            t = ["Recharge & bill payments","Peer-to-peer payments","Merchant payments","Financial Services","Others"]

            for i in t:
                q = "select sum(total_value), sum(total_transactions) from aggregated_transaction where type_of_payment = '"+i+"' and years = "+year+" and quarters ="+quarter
            # q = "select states, type_of_payment, sum(total_value) from aggregated_transaction where years = '"+year+"' and quarters ='"+quarter+"' and type_of_payment = Recharge & bill payments"
            # st.write(q)
                cursor.execute(q)
                q1=cursor.fetchall()
                st.write("**Payment Category for :rainbow["+i+"] :rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Transaction Amount", "Transaction Count"]))

    if option == "User":
        year_quarter = st.sidebar.selectbox(
        "Select the Year and Quarter",
        ("2018 Q1", "2018 Q2", "2018 Q3","2018 Q4","2019 Q1", "2019 Q2", "2019 Q3","2019 Q4","2020 Q1", "2020 Q2", "2020 Q3","2020 Q4","2021 Q1", "2021 Q2", "2021 Q3","2021 Q4",
        "2022 Q1", "2022 Q2", "2022 Q3","2022 Q4", "2023 Q1", "2023 Q2", "2023 Q3","2023 Q4" ))

        if year_quarter =="2018 Q1":
            year = "2018"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)
        elif year_quarter =="2018 Q2":
            year = "2018"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2018 Q3":
            year = "2018"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2018 Q4":
            year = "2018"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2019 Q1":
            year = "2019"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)
        elif year_quarter =="2019 Q2":
            year = "2019"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2019 Q3":
            year = "2019"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2019 Q4":
            year = "2019"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])) 
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)     
        elif year_quarter =="2020 Q1":
            year = "2020"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)


        elif year_quarter =="2020 Q2":
            year = "2020"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2020 Q3":
            year = "2020"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2020 Q4":
            year = "2020"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2021 Q1":
            year = "2021"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2021 Q2":
            year = "2021"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2021 Q3":
            year = "2021"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)
            

        elif year_quarter =="2021 Q4":
            year = "2021"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2022 Q1":
            year = "2022"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 50"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

        elif year_quarter =="2022 Q2":
            year = "2022"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='Registered Users', y='AppOpen')
                st.plotly_chart(fig)


        elif year_quarter =="2022 Q3":
            year = "2022"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='Registered Users', y='AppOpen')
                st.plotly_chart(fig)

        elif year_quarter =="2022 Q4":
            year = "2022"
            quarter = "4"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # # # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='Registered Users', y='AppOpen')
                st.plotly_chart(fig)

        elif year_quarter =="2023 Q1":
            year = "2023"
            quarter = "1"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # # # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='Registered Users', y='AppOpen')
                st.plotly_chart(fig)

        elif year_quarter =="2023 Q2":
            year = "2023"
            quarter = "2"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # # # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='Registered Users', y='AppOpen')
                st.plotly_chart(fig)

        elif year_quarter =="2023 Q3":
            year = "2023"
            quarter = "3"
            col1,col2= st.columns(2)
            with col1:
                query = "select states, districts, registered_user, app_open from map_user where quarters ="+quarter+" and years ="+year+" order by registered_user desc limit 30"
                # # # st.write(query)
                cursor.execute(query)
                q1 = cursor.fetchall()
                st.write("**Registered Users and App_Open Count:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Districts","Registered Users","AppOpen"])
            
                fig = px.histogram(df, x='Registered Users', y='AppOpen')
                st.plotly_chart(fig)

        else:
            year = "2023"
            quarter = "4"
            st.write(":red[**Data is not available for] :rainbow[ "+year_quarter+"]**")

    

        top10 = st.sidebar.radio("**Display transactions based on below options:**", ["States", "Districts", "Postal Codes"])
        states = ["andaman-and-nicobar-islands","andhra-pradesh","arunachal-pradesh","dadra-and-nagar-haveli-and-daman-and-diu",
                "assam","bihar","chandigarh",
                "chhattisgarh","delhi","goa","gujarat","haryana","himachal-pradesh","jammu-and-kashmir",
                "jharkhand","karnataka","kerala","ladakh","lakshadweep","madhya-pradesh","maharashtra",
                "manipur","meghalaya","mizoram","nagaland","odisha","puducherry","punjab","rajasthan","sikkim","tamil-nadu",
                "telangana","tripura","uttar-pradesh","uttarakhand","west-bengal"]

        if top10 == "States":
            col1,col2= st.columns(2)
            with col1:
                q = "select states, registered_users, brands from aggregated_user where years = '"+year+"' and quarters ='"+quarter+"' order by registered_users desc "
                # # st.write(q)
                cursor.execute(q)
                q1 = cursor.fetchall()
                st.write("**Registered Users and Brands State-Wise:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Registered Users","Brands"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Registered Users","Brands"])
            
                fig = px.histogram(df, x='Brands', y='Registered Users')
                st.plotly_chart(fig)
            map_display_U(year, quarter)
            
        if top10 == "Districts":
            col1,col2= st.columns(2)
            with col1:
                q = "select districts, registered_users from top_user_district_wise where years = '"+year+"' and quarters ='"+quarter+"' order by registered_users desc limit 30"
                # # st.write(q)
                cursor.execute(q)
                q1 = cursor.fetchall()
                st.write("**Registered Users District-Wise:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["Districts","Registered Users"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["Districts","Registered Users"])
            
                fig = px.bar(df, x='Districts', y='Registered Users')
                st.plotly_chart(fig)

        if top10 == "Postal Codes":
            col1,col2= st.columns(2)
            with col1:
                q = "select states, pincodes, registered_users from top_user_pincode_wise where years = '"+year+"' and quarters ='"+quarter+"' order by registered_users desc limit 30"
                # # st.write(q)
                cursor.execute(q)
                q1 = cursor.fetchall()
                st.write("**Registered Users Postal Code-Wise:rainbow[ "+year_quarter+"]**")
                st.write(pd.DataFrame(q1, columns = ["States","Postal Codes","Registered Users"]))
            with col2:
                df = pd.DataFrame(q1, columns = ["States","Postal Codes","Registered Users"])
            
                fig = px.histogram(df, x='States', y='Registered Users')
                st.plotly_chart(fig)

if ex == "Top 10 Interesting Facts":
    facts = st.sidebar.selectbox(
        "Select the Fact", 
        ("Select","1. Top Mobile Brands", "2. States with most number of transaction count", "3. States with highest Transaction Amount",
         "4. Districts with highest number of registered users", "5. Trends of Payment Categories for Transaction Amount",
         "6. States with most number of Insurance count", "7.States with most number of Insurance Amount",
         "8. States with most active users", "9. Pincodes with highest number of Transaction Amount",
         "10. Districts with highest number of Transaction Amount"))
    if facts == "Select":
        pass

    elif facts == "1. Top Mobile Brands":
        brand= aggrUserList[["Brands","registeredUsers"]]
        brand1= brand.groupby("Brands")["registeredUsers"].sum().sort_values(ascending=False)
        brand2= pd.DataFrame(brand1).reset_index()

        fig_brands= px.pie(brand2, values= "registeredUsers", names= "Brands", color_discrete_sequence=px.colors.sequential.dense_r,
                        title= "Top Mobile Brands of registeredUsers")
        st.plotly_chart(fig_brands)

    elif facts == "2. States with most number of transaction count":
        transaction= aggreTransaction[["States", "totalNumOfTransactions"]]
        transaction1= transaction.groupby("States")["totalNumOfTransactions"].sum().sort_values(ascending= False)
        transaction2= pd.DataFrame(transaction1).reset_index().head(20)

        fig_trans= px.bar(transaction2, x= "States", y= "totalNumOfTransactions",title= "States with most number of transaction count",
                        color_discrete_sequence= px.colors.sequential.Oranges_r)
        st.plotly_chart(fig_trans)

    elif facts == "3. States with highest Transaction Amount":
        transaction= aggreTransaction[["States", "totalValue"]]
        transaction1= transaction.groupby("States")["totalValue"].sum().sort_values(ascending= False)
        transaction2= pd.DataFrame(transaction1).reset_index().head(20)

        fig_trans= px.histogram(transaction2, x= "States", y= "totalValue",title= "States with most number of Transaction Amount",
                        color_discrete_sequence= px.colors.sequential.Oranges_r)
        st.plotly_chart(fig_trans)
    
    elif facts == "4. Districts with highest number of registered users":
        user= topUserDistrictList[["Districts", "registeredUsers"]]
        user1= user.groupby("Districts")["registeredUsers"].sum().sort_values(ascending= False)
        user2= pd.DataFrame(user1).reset_index().head(20)

        fig= px.histogram(user2, x= "Districts", y= "registeredUsers",title= "Districts with highest number of registered users",
                        color_discrete_sequence= px.colors.sequential.Oranges_r)
        st.plotly_chart(fig)
    
    elif facts == "5. Trends of Payment Categories for Transaction Amount":
        # aggreTransaction
        user= aggreTransaction[["totalValue", "typeOfPayment"]]
        user1= user.groupby("typeOfPayment")["totalValue"].sum().sort_values(ascending= False)
        user2= pd.DataFrame(user1).reset_index().head(10)

        fig= px.histogram(user2, x= "typeOfPayment", y= "totalValue",color_discrete_sequence= px.colors.sequential.Oranges_r,
                    title= "Trends of Payment Categories for Transaction Amount",)
        st.plotly_chart(fig)

    elif facts == "6. States with most number of Insurance count":
        user= aggreInsurance[["insuranceCount", "States"]]
        user1= user.groupby("States")["insuranceCount"].sum().sort_values(ascending= False)
        user2= pd.DataFrame(user1).reset_index().head(10)

        fig= px.histogram(user2, x= "States", y= "insuranceCount",color_discrete_sequence= px.colors.sequential.Oranges_r,
                    title= "Trends of Payment Categories for Insurance Count",)
        st.plotly_chart(fig)
    
    elif facts == "7.States with most number of Insurance Amount":
        user= aggreInsurance[["totalValue", "States"]]
        user1= user.groupby("States")["totalValue"].sum().sort_values(ascending= False)
        user2= pd.DataFrame(user1).reset_index().head(10)

        fig= px.histogram(user2, x= "States", y= "totalValue",color_discrete_sequence= px.colors.sequential.Oranges_r,
                    title= "Trends of Payment Categories for Insurance Amount",)
        st.plotly_chart(fig)

    elif facts == "8. States with most active users":
        user= aggrUserList [["States", "registeredUsers"]]
        user1= user.groupby("States")["registeredUsers"].sum().sort_values(ascending= False)
        user2= pd.DataFrame(user1).reset_index().head(10)

        fig= px.pie(user2, values= "registeredUsers", names= "States",color_discrete_sequence= px.colors.sequential.Oranges_r,
                    title= "States with most active users",)
        st.plotly_chart(fig)

    elif facts == "9. Pincodes with highest number of Transaction Amount":
        user= topTranPincodeList [["Pincodes", "totalValueOfTransactions"]]
        user1= user.groupby("Pincodes")["totalValueOfTransactions"].sum().sort_values(ascending= False)
        user2= pd.DataFrame(user1).reset_index().head(10)

        fig= px.pie(user2, values= "totalValueOfTransactions", names= "Pincodes",color_discrete_sequence= px.colors.sequential.Oranges_r,
                    title= "Pincodes with highest number of Transaction Amount")
        st.plotly_chart(fig)

    elif facts == "10. Districts with highest number of Transaction Amount":
        user= topTranDistrictList [["Districts", "totalValueOfTransactions"]]
        user1= user.groupby("Districts")["totalValueOfTransactions"].sum().sort_values(ascending= False)
        user2= pd.DataFrame(user1).reset_index().head(10)

        fig= px.pie(user2, values= "totalValueOfTransactions", names= "Districts",color_discrete_sequence= px.colors.sequential.Oranges_r,
                    title= "Pincodes with highest number of Transaction Amount")
        st.plotly_chart(fig)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by<a style='display: block; right-align: right;' href="https://www.linkedin.com/in/sabreena-gulzar-5a0227176" target="_blank" = blank>©Sabreena Gulzar</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


