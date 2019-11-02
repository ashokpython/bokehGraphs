from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from .models import Products
from bokeh.palettes import Category20c, Spectral6
from bokeh.models import ColumnDataSource

# Create your views here.
def products(request):
    # output_file("bar_colormapped.html")
    shoes = 10
    belts = 20
    shirts = 50
    counts = []
    items = ["Shoes", "Belts", "Shirts"]
    prod = Products.objects.values()

    for i in prod:
        if "Shoes" in i.values():
            shoes += 1
        elif ("Belts" in i.values()):
            belts += 1
        elif ("Shirts" in i.values()):
            shirts += 1
    counts.extend([shoes, belts, shirts])

    plot = figure(x_range=items, plot_height=400, plot_width=400, title="Objects",
                  toolbar_location="right")
    plot.title.text_font_size = '10pt'

    plot.xaxis.major_label_text_font_size = "10pt"
    plot.vbar(items, top=counts, width=.4, color="blue", legend="Objects")
    plot.legend.label_text_font_size = '10pt'

    script, div = components(plot)

    return render(request, 'products.html', {'script': script, 'div': div})
