from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpRequest
from .db_queries import *


# Create your views here.


def firstPage(request : HttpRequest):

    # initialize connection
    # ask()

    # # to show the content of each table
    # clients_rows = show_clients()
    # bills_rows = show_bills()
    # medicines_rows = show_medicine()
    # stores_rows = show_store()
    # medicine_bills_rows = show_medicine_bill()


    # # check for post request
    # if (request.method == 'POST'):
    #     print(request.POST)

    #     # checks for inputs in client table
    #     if request.POST.get('client_id') :
    #         id = request.POST.get('client_id')
    #         client_name = request.POST.get('client_name')
    #         phone = request.POST.get('client_phone')
    #         address = request.POST.get('client_address')
    #         insert_client(id , client_name , phone , address)
    #         # clients_rows = show_clients()
        

    #     # checks for inputs in bill table
    #     if  request.POST.get('bill_id'):
    #         id = request.POST.get('bill_id')
    #         bill_date = request.POST.get('bill_date')
    #         bill_state = request.POST.get('bill_state')
    #         client_id  = request.POST.get('bill_client_id')
    #         # total_price = request.POST.get('total_price')
    #         insert_bill(id ,bill_date ,bill_state ,client_id)
    #         # bills_rows = show_bills()


    #     # checks for inputs in medicine table
    #     if request.POST.get('medicine_id') : 
    #         id = request.POST.get('medicine_id')
    #         name = request.POST.get('medicine_name')
    #         type = request.POST.get('medicine_type')
    #         amount = request.POST.get('medicine_amount')
    #         expdate = request.POST.get('medicine_expdate')
    #         sell_price =  request.POST.get('medicine_sell_price')
    #         buy_price = request.POST.get('medicine_buy_price')
    #         store_id = request.POST.get('medicine_store_id')
    #         insert_medicine(id,name,type, amount ,expdate,sell_price ,buy_price ,store_id )
    #         # medicines_rows = show_medicine()
    

    #     # checks for inputs in store table
    #     if request.POST.get('store_id') : 
    #         id = request.POST.get('store_id')
    #         name = request.POST.get('store_name')
    #         phone_number = request.POST.get('store_number')
    #         insert_store(id , name , phone_number)
    #         # stores_rows = show_store()



    #     # checks for inputw in medicine_bill table
    #     if request.POST.get('medicine_bill_medicine_id') : 
    #         medicine_id = request.POST.get('medicine_bill_medicine_id')
    #         bill_id = request.POST.get('medicine_bill_bill_id')
    #         amount = request.POST.get('medicine_bill_amount')
    #         insert_medicine_bill(medicine_id , bill_id , amount)
    #         # medicine_bills_rows = show_medicine_bill()


    #     if request.POST.get('medicine_bill_medicine_id') : 
    #         medicine_id = request.POST.get('medicine_bill_medicine_id')
    #         bill_id = request.POST.get('medicine_bill_bill_id')
    #         medicine_amount = request.POST.get('medicine_bill_medicine_amount')
    #         insert_medicine_bill(medicine_id,bill_id,medicine_amount)



    # context = {
    #     'clients_rows' : clients_rows,
    #     'bills_rows' : bills_rows,
    #     'medicines_rows' : medicines_rows,
    #     'stores_rows' : stores_rows,
    #     'medicine_bills_rows' : medicine_bills_rows,
    # }

    return render(request , 'main/index.html' )

def clients(request : HttpRequest):
    context = {
        'rows' : show_clients()   
    }
    return render(request , 'main/clients.html' , context )

def companies(request : HttpRequest):
    context = {
        'rows' : show_store()   
    }
    return render(request , 'main/clients.html' , context )

def bills(request : HttpRequest):
    context = {
        'rows' : show_bills()   
    }
    return render(request , 'main/clients.html' , context )

def medicines(request : HttpRequest):
    context = {
        'rows' : show_medicine()   
    }
    return render(request , 'main/clients.html' , context )

def medical_bills(request : HttpRequest):
    context = {
        'rows' : show_medicine_bills()   
    }
    return render(request , 'main/clients.html' , context )
