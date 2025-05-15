from django.shortcuts import render
from django.http import HttpResponse
from .models import Groupo, Printer, PrinterOuts, User, Organization
from django.test import Client
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import json
import datetime


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


@csrf_exempt
def printouts(request, po, usr):
    msg = "Es un meme"
    if request.method == "POST":
        body_data = json.loads(request.body)
        usr = User.objects.filter(local_id=usr)
        org = Organization.objects.filter(id=1)

        prnt_outs = PrinterOuts()
        prnt_outs.document_name = body_data['DocumentName']
        prnt_outs.job_status = body_data["JobStatus"]
        prnt_outs.local_user_name = body_data['UserName']
        prnt_outs.total_pages = body_data['TotalPages']
        prnt_outs.size = body_data['Size']
        prnt_outs.upload_by = usr[0x0]
        prnt_outs.printer_name = body_data['PrinterName']
        prnt_outs.registered_in = datetime.datetime.now()
        prnt_outs.save()
        msg = "OK"

    return HttpResponse(msg)


@csrf_exempt
def register_user(request, usr_id):
    msg = "Que pasa wuachin"
    usr = User()
    grp = Groupo.objects.filter(id=14)
    org = Organization.objects.filter(id=1)
    usr.local_id = usr_id
    usr.groups = grp[0x0]
    usr.organization = org[0x0]
    usr.save()
    return HttpResponse(msg)


@csrf_exempt
def register_printer(request, prnt_id, usr_id):
    msg = "Hola guachin =("
    if request.method == "POST":
        prnt = Printer()
        org = Organization.objects.filter(id=usr_id)
        body_data = json.loads(request.body)
        prnt.name = body_data["Name"]
        prnt.driver_name = body_data["DriverName"]
        prnt.port_name = body_data["PortName"]
        prnt.owner = usr_id
        prnt.organization = org[0x0].id
        prnt.registered_in = datetime.datetime.now()
        prnt.last_seen = datetime.datetime.now()
        prnt.save()
        msg = "zarpado chuachin =D"

    return HttpResponse(msg)
