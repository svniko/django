from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewItemForm(forms.Form):
    item = forms.CharField(label="New Item")
    # quantity = forms.IntegerField(label="New Item")


# shop_list = ["bread","butter","cheese"]

def index(request):
    # Check if there already exists a "tasks" key in our session

    if "shop_list" not in request.session:
    # If not, create a new list
        request.session["shop_list"] = []


    return render(request, "shopping/index.html",{
        "shop_list":request.session["shop_list"],
        "title":"Items"
    })

def add(request):
    # if request.method == "POST":
    #     item = request.POST.get('item')
    #     shop_list.append(item)
    # # request.POST['item']=''

# Add a new item:

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewItemForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the item from the 'cleaned' version of form data
            item = form.cleaned_data["item"]

            # Add the new item to our shopping list
            request.session["shop_list"]+=[item]

            # Redirect user to shopping list 
            return HttpResponseRedirect(reverse("shopping:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "shopping/add.html", {
        "form": NewItemForm()
    })

def error_404_view(request, exception):
    return render(request,'shopping/404.html')