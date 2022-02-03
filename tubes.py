#Usual imports for data processing
import pandas as pd

#Bokeh libraries and modules
from bokeh.io import curdoc
from bokeh.layouts import widgetbox, row
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter, ColumnDataSource

#loading dataset
data = pd.read_excel('kasus aktif cov 19 jawa bali.xlsx')

#change "tanggal" column tp datetime format from string
data['Tanggal'] =  pd.to_datetime(data['Tanggal'], format='%y-%m-%d')

#declare necessary tools
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,hover"

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
'x' : data[data['Provinsi']=='Banten']['Tanggal'],
'y1' : data[data['Provinsi']=='Banten']['Kasus Aktif'],
'y2' : data[data['Provinsi']=='DKI Jakarta']['Kasus Aktif'],
'y3' : data[data['Provinsi']=='Jawa Barat']['Kasus Aktif'],
'y4' : data[data['Provinsi']=='Jawa Tengah']['Kasus Aktif'],
'y5' : data[data['Provinsi']=='DI Yogyakarta']['Kasus Aktif'],
'y6' : data[data['Provinsi']=='Jawa Timur']['Kasus Aktif'],
'y7' : data[data['Provinsi']=='Bali']['Kasus Aktif'],
})

p = figure(plot_width=1200, plot_height=600, tools=TOOLS)

p.line('x',                                        #horizontal axis
       'y1',
       source=source,
       line_color = 'red',
      legend_label='Banten'                #line legend
      )
p.line('x',                                        #horizontal axis
       'y2',
       source=source,
       line_color = 'green',
      legend_label='DKI Jakarta'                #line legend
      )
p.line('x',                                        #horizontal axis
       'y3',
       source=source,
       line_color = 'blue',
      legend_label='Jawa Barat'                #line legend
      )
p.line('x',                                        #horizontal axis
       'y4',
       source=source,
       line_color = 'yellow',
      legend_label='Jawa Tengah'                #line legend
      )
p.line('x',                                        #horizontal axis
       'y5',
       source=source,
       line_color = 'purple',
      legend_label='DI Yogyakarta'                #line legend
      )
p.line('x',                                        #horizontal axis
       'y6',
       source=source,
       line_color = 'black',
      legend_label='Jawa Timur'                #line legend
      )
p.line('x',                                        #horizontal axis
       'y7',
       source=source,
       line_color = 'pink',
      legend_label='Bali'                #line legend
      )

#Additional visualization parameters
p.title = "Kasus Aktif Covid 19 Jawa Bali"
p.xaxis.axis_label = "Tanggal"                      #horizontal axis' label
p.yaxis.axis_label = "Kasus Aktif"                      #horizontal axis' label
p.legend.location = "top_right"                     #legend's location
p.xgrid.grid_line_color = 'green'                #horizontal axis' color
p.xgrid.grid_line_alpha = .3                     #horizontal axis opacity
p.ygrid.grid_line_color = 'blue'                 #vertical axis' color
p.ygrid.grid_line_alpha = .3                     #vertical axis' opacity
p.xaxis.formatter = DatetimeTickFormatter(hourmin = ['%y-%m-%d']) #making datetime format for x axis

#showing visualization
layout = row(widgetbox(p))
curdoc().add_root(layout)