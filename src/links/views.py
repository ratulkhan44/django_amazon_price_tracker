from django.shortcuts import render
from .forms import AddLinkForm
from .models import Link

# Create your views here.


def home_view(request):
    no_discounted = 0
    error = None
    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Upss! Couldn't Get the Name Or Price"
        except:
            error = "Upss! something Went the wrong"

    form = AddLinkForm()
    items = Link.objects.all()
    items_no = items.count()

    if items_no > 0:
        discount_list = []
        for item in items:
            if item.old_price > item.current_price:
                discount_list.append(item)
                no_discounted = len(discount_list)

    context = {
        "form": form,
        "items": items,
        "no_discounted": no_discounted,
        "items_no": items_no,
        "error": error
    }

    return render(request, 'index.html', context)
