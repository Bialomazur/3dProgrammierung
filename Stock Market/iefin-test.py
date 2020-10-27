from iexfinance.stocks import Stock
import sys 



tickers =  [ ticker.split(":")[0] for ticker in """
AMZN:Amazon
GOOG:Google
AAPL:Apple Inc
FB:Facebook
BABA:Alibaba
V:Visa
JNJ:Johnson & Johnson
WMT:Walmart
MA:Mastercard
PG:Procter & Gamble
UNH:UnitedHealth
JPM:JPMorgan Chase
TSM:Taiwan Semiconductor
HD:Home Depot
INTC:Intel
VZ:Verizon
NVDA:NVIDIA
PFE:Pfizer
DIS:Disney
T:AT&T
MRK:Merck
NFLX:Netflix
BAC:Bank of America
NVS:Novartis AG
KO:Coca-Cola
XOM:ExxonMobil
CSCO:Cisco Systems
PEP:Pepsi
ADBE:Adobe
CVX:Chevron
CMCSA:Comcast
PYPL:PayPal
ORCL:Oracle
TM:Toyota
ABBV:AbbVie
ABT:Abbott Laboratories
CRM:Salesforce
CHL:China Mobile
LLY:Eli Lilly
TSLA:Tesla
BMY:Bristol-Myers Squibb
NKE:Nike
AZN:AstraZeneca
SAP:SAP SE
AMGN:Amgen
TMO:Thermo Fisher Scientific
MCD:McDonald's
COST:Costco Wholesale
ADDYY:Adidas
SAP:Sap
DCX.TI:Daimler
OGZPY:Gazprom
LHA.DE:Lufthansa
HSBC:HSBC
TMUS:T-Mobile
NKE:Nike
GE:General Electric Company
BP:BP p.l.c.
DT:Deutsche Telekom AG
DELL:DELL Inc.
MS:Morgan Stanley
AXP:American Express Company
CAJ:Canon Inc.
YHOO:Yahoo!
MSI:Motorola Inc.
DB:Deutsche Bank AG
EBAY:eBay Inc.
BA:Boeing Company
FNMFO:Federal National Mortgage Association
GS:Goldman Sachs
LNVGY: Lenovo Group
BMWYY:BMW AG
F:Ford Motor Company
NLLSF:Nel ASA
NOK:Nokia Corporation
VLKAF:Volkswagen AG
SNAP:Snap Inc.
IBM:International Business Machines Corporation
""".split("\n")]





while True:

    ticker = input("Enter ticker\n>  ")
    batch = Stock(ticker, token="pk_e2e1c058fb4649f8ab69035f86d2e84a")
    data = batch.get_quote()
    print(data)






sys.exit()


with open("tickers.txt", "w") as file:
    for ticker in tickers:
        file.write(ticker+"\n")





for ticker in tickers:

    try:
        batch = Stock(ticker, token="pk_e2e1c058fb4649f8ab69035f86d2e84a")
        stock_market_data = batch.get_quote()["open"]
        print(f"WORKING {ticker}")
    except:
        print(f"ERROR:   {ticker}")





print(stock_market_data)
