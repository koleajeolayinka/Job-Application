from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader 

job_title = ["first_job", "second_job", "third_job"]
job_description = [
    "first job description",
    "second job descrption",
    "third job descrption",
]


def hello(request):
    template = loader.get_template('hello.html')
    context={}
    return HttpResponse(template.render(context, request))

def job_list(request):
    # return HttpResponse("Hello world")
    job_id = "http://127.0.0.1:8000/job/0"

    list_of_jobs = "<ul>"
    for i in job_title:
        job_id = job_title.index(i)
        # print(reverse("jobs_detail", args=(job_id,)))
        detail_url = reverse("jobs_detail", args=(job_id,))
        list_of_jobs = list_of_jobs + f"<a href='{detail_url}'><li>{i}</li></a>"
    list_of_jobs = list_of_jobs + "</ul>"
    return HttpResponse(list_of_jobs)


def job_detail(request, id):
    back = "http://127.0.0.1:8000/"

    try:
        if id == 0:
            return redirect(reverse("jobs_home"))

        return_html = f"<h1>{job_title[int(id)]}</h1> <h3>{job_description[int(id)]}</h3> <a href={back}><h1>back</h1></a>"

        return HttpResponse(return_html)
    except:
        # return HttpResponse("<h1>Not found</h1>")
        return HttpResponseNotFound("<h1>Not Found</h1>")

    # return HttpResponse(f"Job detail page {id} <h1>header</h1>")
