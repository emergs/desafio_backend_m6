# Desafio Back-End

## Instruções para utilização

1. Faça o clone do repositório
   
2. Crie um ambiente virtual 
   
    ```python -m venv venv```

3. Ative o ambiente virtual

    Windows: ```.\venv\Scripts\activate```


    Linux: ```source venv/bin/activate```

4. Instale as dependências necessárias

    ```pip install -r requirements.txt```

5. Execute as migrações
   
    ```python manage.py migrate```

6. Inicie o servidor
   
    ```python manage.py runserver```

7. Acesse o seguint link 
   
    ```http://127.0.0.1:8000/api/file_parser/```

8. Com a aplicação rodando selecione o arquivo cnab.txt que está no diretório raiz da aplicação, e clique no botão enviar arquivo