from django.shortcuts import render
from applybank.forms import ApplyForms


# Create your views here.
def ApplyForm(request):
    if request.method == 'POST':
        form = ApplyForms(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    else:
        form = ApplyForms()
    context = {
        "applyForm": form
    }
    return render(request, "apply/main.html", context)
