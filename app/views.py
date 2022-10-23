from cmath import log
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

job_title = ["Google Department", "Linkedin", "dd"]
job_description = ["first job description", "second job descrption"]


def hello(request):
    # return HttpResponse("Hello world")
    job_id = "http://127.0.0.1:8000/job/0"

    return HttpResponse(
        f"<ul> <li>{job_title[0]} <li>{job_description[0]}</li></li> <li>{job_title[1]}</li> <li>{job_description[1]}</li> </ul> <a href={job_id}><h1>Job id </h1></a>"
    )


def job_detail(request, id):
    print(type(id))
    back = "http://127.0.0.1:8000/"

    if id >= 2:
        return redirect("/")

    return_html = f"<h1>{job_title[int(id)]}</h1> <h3>{job_description[int(id)]}</h3> <a href={back}><h1>back</h1></a>"

    return HttpResponse(return_html)

    # return HttpResponse(f"Job detail page {id} <h1>header</h1>")
