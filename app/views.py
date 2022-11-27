from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost


class test_clas:
    x = 3


job_title = ["first_job", "second_job", "third_job"]
job_description = [
    "first job description",
    "second job descrption",
    "third job descrption",
]

job = JobPost.objects.all()


def hello(request):
    # template = loader.get_template('app/hello.html')
    temp = test_clas()
    list_item = ["orange", "mango", "pineapple"]
    name1 = "tobs"
    if_authenticated = False
    age = {
        name1: 17,
        "tons": 18,
    }
    context = {
        "name": "django_",
        "item": list_item,
        "num": temp,
        "user": age,
        # "name": name1,
        "mark": if_authenticated,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)


def job_list(request):
    # return HttpResponse("Hello world")

    # detail_url = reverse("jobs_detail", args=(job_id,))

    context = {
        "job_title": job,
    }

    #     list_of_jobs = list_of_jobs + f"<a href='{detail_url}'><li>{i}</li></a>"
    # list_of_jobs = list_of_jobs + "</ul>"
    # return HttpResponse(list_of_jobs)

    return render(request, "app/index.html", context)


def job_detail(request, id):
    # job

    try:
        # if id == 0:
        #     return redirect(reverse("jobs_home"))
        context = {
            "job": job[id],

        }
        # return_html = f"<h1>{job_title[int(id)]}</h1> <h3>{job_description[int(id)]}</h3> <a href={
        # back}><h1>back</h1></a>"

        return render(request, "app/jobdetail.html", context)
    except:
        # return HttpResponse("<h1>Not found</h1>")
        return HttpResponseNotFound("<h1>Not Found</h1>")

    # return HttpResponse(f"Job detail page {id} <h1>header</h1>")
