from flask import Flask , render_template, Markup

app=Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def home():
    #return 'Hello There Stranger'
    bar_labels=labels
    bar_values=values
    return render_template('home.html', title='Sample BarChart', max=17000, labels=bar_labels, values=bar_values)

#@app.route('/about/')
#def about():
  #  return render_template('about.html')

@app.route('/about/')
def about():
    line_labels=labels
    line_values=values
    return render_template('about.html', title='Sample LineChart', max=17000, labels=line_labels, values=line_values)

#@app.route('/contact/')
#def contact():
#    return render_template('contact.html')

#@app.route("/chart")
#def chart():
#    labels = ["January","February","March","April","May","June","July","August"]
 #   values = [10,9,8,7,6,4,7,8]
 #   colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
 #   return render_template('chart.html', set=zip(values, labels, colors))

@app.route('/contact/')
def contact():
    pie_labels = labels
    pie_values = values
    return render_template('contact.html', title='Sample PieChart', max=17000, set=zip(values, labels, colors))

if __name__ == '__main__':
    app.run(debug=True)
