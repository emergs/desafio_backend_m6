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


def normalize(list):
    ...


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        archive = request.FILES["file"]

        file_parser = FileUpload.objects.create(file_parser=archive)
        file_parser.save()

        list = open_file(archive)

        for list_line in list:
            tipo = list_line[:1]
            data = list_line[1:9]
            valor = list_line[9:19]
            cpf = list_line[19:30]
            cartao = list_line[30:42]
            hora = list_line[42:44]
            minuto = list_line[44:46]
            segundo = list_line[46:48]
            dono_da_loja = list_line[48:62]
            nome_da_loja = list_line[62:81]

            # data = f"{dia}/{mes}/{ano}"
            valor = int(valor) / 100
            horario = f"{hora}:{minuto}:{segundo}"

            # ipdb.set_trace()

            if tipo == "1":
                tipo = "Débito"

            elif tipo == "2":
                tipo = "Boleto"

            elif tipo == "3":
                tipo = "Financiamento"

            elif tipo == "4":
                tipo = "Crédito"

            elif tipo == "5":
                tipo = "Empréstimo"

            elif tipo == "6":
                tipo = "Vendas"

            elif tipo == "7":
                tipo = "TED"

            elif tipo == "8":
                tipo = "DOC"

            elif tipo == "9":
                tipo = "Aluguel"

            reader = FileParserModel.objects.create(
                tipo=tipo,
                data=data,
                valor=valor,
                cpf=cpf,
                cartao=cartao,
                hora=horario,
                dono_da_loja=dono_da_loja,
                nome_da_loja=nome_da_loja,
            )

            reader.save()

        operacoes = FileParserModel.objects.values(
            "tipo", "valor", "data", "cpf", "hora", "dono_da_loja", "nome_da_loja"
        )

        saldo_total = 0

        for operacao in operacoes:
            if (
                operacao["tipo"] == "Boleto"
                or operacao["tipo"] == "Financiamento"
                or operacao["tipo"] == "Aluguel"
            ):
                saldo_total -= operacao["valor"]
            else:
                saldo_total += operacao["valor"]

        return render(
            request,
            "results.html",
            context={"operacoes": operacoes, "saldo_total": saldo_total},
        )

    else:
        form = UploadFileForm()
    return render(request, "fileSend.html", {"form": form})
