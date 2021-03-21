#pip install wapi-python first
import wapi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


session = wapi.Session(client_id='0Le.lY6.VzLuNCdwNNrX64aB6R8AI6I7', client_secret='BS35Qwr8NWLTZTG6obeAJpUtNVDuKwo.Y05joYoDs8nsLjYG5idmm7nXnBk9Y_vwXJrmHkjoEigJh4yZ4kMNqxV79XYT9rPbUZRG')


print('Enter the Dataset Name')
dataset = 'pro de wnd ec00 mwh/h cet min15 f'
#dataset = input()

#input: pro de wnd ec00 mwh/h cet min15 f (this is the forecasted production of wind power, DE)



def getdata(name1):
    curve = session.get_curve(name=name1)
    ts = curve.get_instance(issue_date='2021-03-20T00:00')
    pd_s = ts.to_pandas()
    return pd_s


data = getdata
x = data(dataset)

supply = x.to_frame()

supply.columns = ['supply']

demand = supply['supply']*0.3 +10000
demand = demand.to_frame()
demand.columns = ['demand']

combined = pd.concat([supply, demand], axis = 1)



# Data


# Shade the area between y1 and y2
plt.xlabel("Time")
plt.ylabel("mvh/h")

ax = plt.axes()
ax.set_facecolor("black")


time =  combined.index
demand = combined.demand
supply = combined.supply
plt.title("Produced wind energy vs. demand")

for i in range(956):
    plt.plot(time[:i], demand[:i], color = 'red')
    plt.plot(time[:i], supply[:i], color = 'green')
    
    plt.fill_between(time[:i], demand[:i], supply[:i],
                     facecolor="orange", # The fill color
                     color='red',       # The outline color
                     alpha=0.2,     # Transparency of the fill
                     where = (demand[:i]>supply[:i]),
                     interpolate=True, label='Not enough supply')          
    
    plt.fill_between(time[:i], demand[:i], supply[:i],
                     facecolor="orange", # The fill color
                     color='green',       # The outline color
                     alpha=0.2,     # Transparency of the fill
                     where = (demand[:i]<supply[:i]),
                     interpolate=True, label='Too much supply')
    plt.pause(0.0001)
      

    # Show the plot
plt.legend()




#IGNORE BELOW

#pri de intraday €/mwh cet min15 a = intraday price of power
#def getdata2(name2):
#    curve = session.get_curve(name=name2)
#    ts = curve.get_data(data_from='2021-03-20',data_to='2021-03-21')
#    pd_s = ts.to_pandas()
#    return pd_s


