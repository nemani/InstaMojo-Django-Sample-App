from django.http import HttpResponse, HttpResponseRedirect
from apitest import API_KEY, AUTH_TOKEN
from django.urls import reverse
from django.shortcuts import render
from .forms import PayForm
from instamojo_wrapper import Instamojo

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("\n\nPOST\n\n" + str(request.POST))
        # create a form instance and populate it with data from the request:
        form = PayForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            # Create a new Payment Request
            response = api.payment_request_create(
                amount=str(data['Amount']),
                purpose=data['Purpose'],
                send_email=False,
                email=data['Email'],
                buyer_name=data['Name'],
                phone=data['Phone'],
                redirect_url=request.build_absolute_uri(reverse("list"))
            )
            print(response)
            return HttpResponseRedirect(response['payment_request']['longurl'])

    # if a GET (or any other method) we'll create a blank form
    else:
        print("\n\nGET\n\n")
        form = PayForm()
        # form.fields['Amount'].clean(10)
        # form.fields['Amount']=10
        print("\n\n"+str(form) + "\n\n")

    return render(request, 'apitest/pay.html', {'form': form})
    # return HttpResponse("Hello, world. You're at the API TEST index.")


def list_payments(request):
    # Create a new Payment Request
    response = api.payment_requests_list()

    # Loop over all of the payment requests
    h = "<div><table><tr><th>ID</th><th>amount</th><th>Purpose</th><th>status</th></tr>"
    for payment_request in response['payment_requests']:
        h += "<tr>"
        h += "<td>" + payment_request['id'] + "</td>"
        h += "<td>" + payment_request['amount'] + "</td>"
        h += "<td>" + payment_request['purpose'] + "</td>"
        h += "<td>" + payment_request['status'] + "</td>"
        h += "</tr>"

    h += "</table></div>"

    return HttpResponse(h)
