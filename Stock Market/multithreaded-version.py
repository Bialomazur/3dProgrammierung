import threading
from yahoo_fin import stock_info as si
import time



stock_prices = {}
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
MOT:Motorola Inc.
DB:Deutsche Bank AG
EBAY:eBay Inc.
BA:Boeing Company
FNM:Federal National Mortgage Association
GS:Goldman Sachs
LNVGY: Lenovo Group
WDI.DE:Wirecard AG
BMW.DE:BMW AG
F:Ford Motor Company
NEL.OL:Nel ASA
NOK:Nokia Corporation
VOW.DE:Volkswagen AG
SNAP:Snap Inc.
IBM:International Business Machines Corporation
""".split("\n")]




def get_stock_price(ticker):

    price = si.get_live_price(ticker)
    print(price)


def main():
    t1 = time.perf_counter()
    for ticker in tickers:
        threading.Thread(target=get_stock_price, args=(ticker,)).start()
    t2 = time.perf_counter()
    print(f"\n\nDURATION: {t2-t1} seconds")


if __name__ == "__main__":

    main()

