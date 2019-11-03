from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from .models import Products
from bokeh.palettes import Category20c, Spectral6
from bokeh.models import ColumnDataSource

# Create your views here.
def products(request):
    # output_file("bar_colormapped.html")
    AccessToVisit = 10
    Policies = 20
    EndUsers = 50
    counts = []
    items = ["AccessToVisit", "Policies", "EndUsers"]
    prod = Products.objects.values()

    for i in prod:
        if "AccessToVisit" in i.values():
            AccessToVisit += 1
        elif ("Policies" in i.values()):
            Policies += 1
        elif ("EndUsers" in i.values()):
            EndUsers += 1
    counts.extend([AccessToVisit, Policies, EndUsers])

    plot = figure(x_range=items, plot_height=400, plot_width=400, title="Objects",
                  toolbar_location="right")
    plot.title.text_font_size = '10pt'

    plot.xaxis.major_label_text_font_size = "10pt"
    plot.vbar(items, top=counts, width=.4, color="green", legend="Objects and Accounts")
    plot.legend.label_text_font_size = '10pt'

    script, div = components(plot)

    return render(request, 'products.html', {'script': script, 'div': div})


def policies(request):
    # output_file("bar_colormapped.html")
    AccessToVisit = 100
    Policies = 200
    EndUsers = 500
    counts = []
    items = ["AccessToVisit", "Policies", "EndUsers"]
    prod = Products.objects.values()

    for i in prod:
        if "AccessToVisit" in i.values():
            AccessToVisit += 1
        elif ("Policies" in i.values()):
            Policies += 1
        elif ("EndUsers" in i.values()):
            EndUsers += 1
    counts.extend([AccessToVisit, Policies, EndUsers])

    plot = figure(x_range=items, plot_height=400, plot_width=400, title="Objects",
                  toolbar_location="right")
    plot.title.text_font_size = '10pt'

    plot.xaxis.major_label_text_font_size = "10pt"
    plot.vbar(items, top=counts, width=.4, color="black", legend="Objects and Accounts")
    plot.legend.label_text_font_size = '10pt'

    script, div = components(plot)

    return render(request, 'programming.html', {'script': script, 'div': div})
