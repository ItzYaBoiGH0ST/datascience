import folium
import pandas as pd
import os
import csv
import collections


dataframe = pd.read_csv("saferparks_dataset.csv")

d = {}
q = {}
z = {}
#print(    (dataframe[""]   )    )

#state_geo = os.path.join('us-states.json')


#m = folium.Map(location=[48, -102], zoom_start=3)

#m.choropleth(
 #  geo_data=state_geo,
  # name='choropleth',

   #key_on='feature.id',
   #fill_color='YlGn',
   #fill_opacity=0.7,
   # line_opacity=0.2,
#)


#folium.LayerControl().add_to(m)

##take column 0 in the statslatlong file and initialize the dictionary to 0

with open('Statslatlong.csv') as f:
   writer = csv.writer(f)
   rows = csv.reader(f)
   for row in rows:
       d[row[0]]=0
with open('saferparks_dataset.csv') as f:
   writer = csv.writer(f)
   rows = csv.reader(f)
   for row in rows:
       if row[2] in d:
            d[row[2]] += 1
       else:
           d[row[2]] = 1
print (d)
the_map = None



total = 0
for key in d:
    total += d[key]



csv_file = "StaetCount.csv"
columns = ["State", "Percentages"]
with open(csv_file, 'w') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(columns)
    for key, value in d.items():
        if key == "state":
            continue
        lst = [key,value/total*100]
        writer.writerow(lst)

state_geo = os.path.join('us-states.json')

state_accidents = os.path.join(csv_file)
state_data = pd.read_csv(state_accidents)

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=columns,
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Amount of accidents (%)'
)
folium.LayerControl().add_to(m)
import folium
import pandas as pd
import os
import csv
import collections


dataframe = pd.read_csv("saferparks_dataset.csv")

d = {}
q = {}
z = {}
#print(    (dataframe[""]   )    )

#state_geo = os.path.join('us-states.json')


#m = folium.Map(location=[48, -102], zoom_start=3)

#m.choropleth(
 #  geo_data=state_geo,
  # name='choropleth',

   #key_on='feature.id',
   #fill_color='YlGn',
   #fill_opacity=0.7,
   # line_opacity=0.2,
#)


#folium.LayerControl().add_to(m)

##take column 0 in the statslatlong file and initialize the dictionary to 0

with open('Statslatlong.csv') as f:
   writer = csv.writer(f)
   rows = csv.reader(f)
   for row in rows:
       d[row[0]]=0
with open('saferparks_dataset.csv') as f:
   writer = csv.writer(f)
   rows = csv.reader(f)
   for row in rows:
       if row[2] in d:
            d[row[2]] += 1
       else:
           d[row[2]] = 1
print (d)
the_map = None



total = 0
for key in d:
    total += d[key]



csv_file = "StaetCount.csv"
columns = ["State", "Percentages"]
with open(csv_file, 'w') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(columns)
    for key, value in d.items():
        if key == "state":
            continue
        lst = [key,value/total*100]
        writer.writerow(lst)

state_geo = os.path.join('us-states.json')

state_accidents = os.path.join(csv_file)
state_data = pd.read_csv(state_accidents)

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=columns,
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Amount of accidents (%)'
)
folium.LayerControl().add_to(m)
tooltip = 'Florida'
tooltipa = 'Alabama'
tooltipb = 'Alaska'
tooltipc = 'New York'
tooltipd = 'Arkansas'
tooltipe = 'New Mexico'
tooltipf = 'Arizona'
tooltipg = 'New Jersey'
tooltiph = 'California'
tooltipi = 'Nevada'
tooltipj = 'Ohio'
tooltipk = 'Washington'
tooltipl = 'Idaho'
tooltipm = 'Missouri'
tooltipn = 'Mississippi'
tooltipo = 'Georgia'
tooltipp = 'West Virginia'
tooltipq = 'Virginia'
tooltipr = 'South Carolina'
tooltips = 'North Carolina'
tooltipt = 'North Dakota'
tooltipu = 'South Dakota'
tooltipv = 'Wyoming'
tooltipw = 'Texas'
tooltipx = 'Wisconsin'
tooltipy = 'Michigan'
tooltipz = 'Massachusetts'
tooltip1 = 'Pennsylvania'
tooltip2 = 'Connecticut'
tooltip3 = 'Maryland'
tooltip4 = 'Maine'
tooltip5 = 'Vermont'
tooltip6 = 'Rhode Island'
tooltip7 = 'Nebraska'
tooltip8 = 'Colorado'
tooltip9 = 'Delaware'
tooltip10 = 'Hawaii'
tooltip11 = 'Iowa'
tooltip12 = 'Illinois'
tooltip13 = 'Indiana'
tooltip14 = 'Kansas'
tooltip15 = 'Kentucky'
tooltip16 = 'Louisiana'
tooltip17 = 'Minnesota'
tooltip18 = 'Montana'
tooltip19 = 'New Hampshire'
tooltip20 = 'Oklahoma'
tooltip21 = 'Oregon'
tooltip22 = 'Tennessee'
tooltip23 = 'Utah'


folium.Marker([39.32098,-111.093731], popup='<i>0 accidents,0% of all accidents,2 amusement parks</i>', tooltip=tooltip23).add_to(m)
folium.Marker([32.318231,-86.902298], popup='<i>0 accidents,0% of all accidents,5 amusement parks</i>', tooltip=tooltipa).add_to(m)
folium.Marker([63.588753,-154.493062], popup='<i>0 accidents,0% of all accidents,0 amusement parks</i>', tooltip=tooltipb).add_to(m)
folium.Marker([43.299428,-74.217933], popup='<i>69 accidents,0.46% of all accidents,19 amusement parks</i>', tooltip=tooltipc).add_to(m)
folium.Marker([35.20105,-91.831833], popup='<i>4 accidents,0.03% of all accidents,2 amusement parks</i>', tooltip=tooltipd).add_to(m)
folium.Marker([34.97273,-105.032363], popup='<i>0 accidents,0% of all accidents,3 amusement parks</i>', tooltip=tooltipe).add_to(m)
folium.Marker([34.048928,-111.093731], popup='<i>1 accident,0.007% of all accidents,4 amusement parks</i>', tooltip=tooltipf).add_to(m)
folium.Marker([40.058324,-74.405661], popup='<i>5648 accidents,37.9% of all accidents,17 amusement parks</i>', tooltip=tooltipg).add_to(m)
folium.Marker([36.778261,-119.417932], popup='<i>3426 accidents,23% of all accidents,32 amusement parks</i>', tooltip=tooltiph).add_to(m)
folium.Marker([38.80261,-116.419389], popup='<i>31 accidents,0.2% of all accidents,6 amusement parks</i>', tooltip=tooltipi).add_to(m)
folium.Marker([40.417287,-82.907123], popup='<i>82 accidents,0.55% of all accidents,8 amusement parks</i>', tooltip=tooltipj).add_to(m)
folium.Marker([47.751074,-120.740139], popup='<i>8 accidents,0.05% of all accidents,5 amusement parks</i>', tooltip=tooltipk).add_to(m)
folium.Marker([44.068202,-114.742041], popup='<i>0 accidents,0% of all accidents,2 amusement parks</i>', tooltip=tooltipl).add_to(m)
folium.Marker([37.964253,-91.831833], popup='<i>9 accidents,0.06% of all accidents,5 amusement parks</i>', tooltip=tooltipm).add_to(m)
folium.Marker([32.354668,-89.398528], popup='<i>0 accidents,0% of all accidents,1 amusement park</i>', tooltip=tooltipn).add_to(m)
folium.Marker([32.157435,-82.907123], popup='<i>1 accident,0.007% of all accidents,5 amusement parks</i>', tooltip=tooltipo).add_to(m)
folium.Marker([38.597626,-80.454903], popup='<i>12 accidents,0.08% of all accidents,1 amusement park</i>', tooltip=tooltipp).add_to(m)
folium.Marker([37.431573,-78.656894], popup='<i>2 accidents,0.01% of all accidents,5 amusement parks</i>', tooltip=tooltipq).add_to(m)
folium.Marker([33.836081,-81.163725], popup='<i>0 accidents,0% of all accidents,2 amusement parks</i>', tooltip=tooltipr).add_to(m)
folium.Marker([35.759573,-79.0193], popup='<i>14 accidents,0.09% of all accidents,4 amusement parks</i>', tooltip=tooltips).add_to(m)
folium.Marker([47.551493,-101.002012], popup='<i>0 accidents,0% of all accidents,0 amusement parks</i>', tooltip=tooltipt).add_to(m)
folium.Marker([43.969515,-99.901813], popup='<i>0 accidents,0% of all accidents,2 amusement parks</i>', tooltip=tooltipu).add_to(m)
folium.Marker([43.075968,-107.290284], popup='<i>0 accidents,0% of all accidents,0 amusement parks</i>', tooltip=tooltipv).add_to(m)
folium.Marker([31.968599,-99.901813], popup='<i>3322 accidents,22.3% of all accidents,15 amusement parks</i>', tooltip=tooltipw).add_to(m)
folium.Marker([43.78444,-88.787868], popup='<i>108 accidents,0.72% of all accidents,6 amusement parks</i>', tooltip=tooltipx).add_to(m)
folium.Marker([44.314844,-85.602364], popup='<i>268 accidents,1.8% of all accidents,4 amusement parks</i>', tooltip=tooltipy).add_to(m)
folium.Marker([42.407211,-71.382437], popup='<i>13 accidents,0.09% of all accidents,3 amusement parks</i>', tooltip=tooltipz).add_to(m)
folium.Marker([41.203322,-77.194525], popup='<i>270 accidents,1.8% of all accidents,13 amusement parks</i>', tooltip=tooltip1).add_to(m)
folium.Marker([41.603221,-73.087749], popup='<i>11 accidents,0.07% of all accidents,3 amusement parks</i>', tooltip=tooltip2).add_to(m)
folium.Marker([39.045755,-76.641271], popup='<i>66 accidents,0.44% of all accidents,6 amusement parks</i>', tooltip=tooltip3).add_to(m)
folium.Marker([45.253783,-69.445469], popup='<i>0 accidents,0% of all accidents,3 amusement parks</i>', tooltip=tooltip4).add_to(m)
folium.Marker([44.558803,-72.577841], popup='<i>0 accidents,0% of all accidents,0 amusement parks</i>', tooltip=tooltip5).add_to(m)
folium.Marker([41.580095,-71.477429], popup='<i>5 accidents,0.03% of all accidents,0 amusement parks</i>', tooltip=tooltip6).add_to(m)
folium.Marker([41.4925,-99.9018], popup='<i>0 accidents,0% of all accidents</i>,3 amusement parks', tooltip=tooltip7).add_to(m)
folium.Marker([39.550051,-105.782067], popup='<i>106 accidents,0.71% of all accidents,7 amusement parks</i>', tooltip=tooltip8).add_to(m)
folium.Marker([38.910832,-75.52767], popup='<i>0 accidents,0% of all accidents</i>,0 amusement parks', tooltip=tooltip9).add_to(m)
folium.Marker([19.898682,-155.665857], popup='<i>0 accidents,0% of all accidents</i>,0 amusement parks', tooltip=tooltip10).add_to(m)
folium.Marker([41.878003,-93.097702], popup='<i>15 accidents,0.01% of all accidents</i>,2 amusement parks', tooltip=tooltip11).add_to(m)
folium.Marker([40.633125,-89.398528], popup='<i>155 accidents,1.03% of all accidents</i>,9 amusement parks', tooltip=tooltip12).add_to(m)
folium.Marker([40.551217,-85.602364], popup='<i>8 accidents,0.05% of all accidents</i>,5 amusement parks', tooltip=tooltip13).add_to(m)
folium.Marker([39.011902,-98.484246], popup='<i>0 accidents,0% of all accidents</i>,3 amusement parks', tooltip=tooltip14).add_to(m)
folium.Marker([37.839333,-84.270018], popup='<i>38 accidents,0.25% of all accidents</i>,2 amusement parks', tooltip=tooltip15).add_to(m)
folium.Marker([31.244823,-92.145024], popup='<i>1 accident,0.007% of all accidents</i>,3 amusement parks', tooltip=tooltip16).add_to(m)
folium.Marker([46.729553,-94.6859], popup='<i>0 accidents,0% of all accidents</i>,4 amusement parks', tooltip=tooltip17).add_to(m)
folium.Marker([46.879682,-110.362566], popup='<i>0 accidents,0% of all accidents</i>,1 amusement park', tooltip=tooltip18).add_to(m)
folium.Marker([43.193852,-71.572395], popup='<i>0 accidents,0% of all accidents</i>,5 amusement parks', tooltip=tooltip19).add_to(m)
folium.Marker([35.007752,-97.092877], popup='<i>153,1.03% of all accidents</i>,2 amusement parks', tooltip=tooltip20).add_to(m)
folium.Marker([43.804133,-120.554201], popup='<i>0 accidents,0% of all accidents,2 amusement parks</i>', tooltip=tooltip21).add_to(m)
folium.Marker([35.517491,-86.580447], popup='<i>1 accident,0.007% of all accidents,3 amusement parks</i>', tooltip=tooltip22).add_to(m)
folium.Marker([27.664827,-81.515754], popup='<i>1074 accidents,7.2% of all accidents,25 amusement parks</i>', tooltip=tooltip).add_to(m)


m.save('marker.html')