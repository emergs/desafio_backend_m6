from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import FileUpload, FileParserModel
import ipdb


def open_file(archive):
    file_list = []
    with open(f"storeged_file/{archive.name}", "r", encoding="utf-8") as read_file:
        for file_line in read_file:
            file_list.append(file_line)
        return file_list


def select_type(type):
    match type:
        case "1":
            return "Débito"
        case "2":
            return "Boleto"
        case "3":
            return "Financiamento"
        case "4":
            return "Crédito"
        case "5":
            return "Empréstimo"
        case "6":
            return "Vendas"
        case "7":
            return "TED"
        case "8":
            return "DOC"
        case "9":
            return "Aluguel"


def save_data(tipo, data, valor, cpf, cartao, hora, dono_da_loja, nome_da_loja):
    user_data = FileParserModel.objects.create(
        tipo=select_type(tipo),
        data=data,
        valor=valor,
        cpf=cpf,
        cartao=cartao,
        hora=hora,
        dono_da_loja=dono_da_loja,
        nome_da_loja=nome_da_loja,
    )
    user_data.save()


def getUsers():
    all_users = FileParserModel.objects.values(
        "tipo", "data", "valor", "cartao", "cpf", "hora", "dono_da_loja", "nome_da_loja"
    )

    list_users = []

    def calculate_balance(user, saldo):
        if (
            user["tipo"] == "Boleto"
            or user["tipo"] == "Financiamento"
            or user["tipo"] == "Aluguel"
        ):
            saldo -= user["valor"]
            return saldo
        else:
            saldo += user["valor"]
            return saldo

    for user in all_users:
        saldo = 0

        condition = user not in list_users

        if condition:
            user["new_saldo"] = calculate_balance(user, saldo)
            list_users.append(user)
        else:
            user["new_saldo"] = calculate_balance(user, saldo)

    return list_users


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        archive = request.FILES["file"]

        file_parser = FileUpload.objects.create(file_parser=archive)
        file_parser.save()

        list = open_file(archive)

        for list_line in list:
            tipo = list_line[:1]
            data = f"{list_line[7:9]}/{list_line[5:7]}/{list_line[1:5]}"
            valor = int(list_line[9:19]) / 100
            cpf = list_line[19:30]
            cartao = list_line[30:42]
            hora = f"{list_line[42:44]}:{list_line[44:46]}:{list_line[46:48]}"
            dono_da_loja = list_line[48:62]
            nome_da_loja = list_line[62:81]

            save_data(tipo, data, valor, cpf, cartao, hora, dono_da_loja, nome_da_loja)

        users = getUsers()
        # print(users)

        return render(
            request,
            "results.html",
            context={
                "users": users,
            },
        )

    else:
        form = UploadFileForm()
    return render(request, "fileSend.html", {"form": form})
