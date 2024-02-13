import requests
from bs4 import BeautifulSoup
import openpyxl


# Envia os dados de login
login_url = "https://loja.imdepa.com.br/login"
login_data = {
    "username": username,
    "password": password,
}

login_response = requests.post(login_url, data=login_data)

# Verifica se o login foi bem-sucedido
if login_response.status_code == 200:
    # Acessa a página de rolamentos
    rolamentos_url = "https://loja.imdepa.com.br/categoria/rolamentos"
    rolamentos_response = requests.get(rolamentos_url)

    # Obtém os dados dos rolamentos
    rolamentos_soup = BeautifulSoup(rolamentos_response.content, "html.parser")
    rolamentos = rolamentos_soup.find_all("div", class_="y-item mt-none hidden-btn-reveal")

    # Cria um arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Escreve os dados dos rolamentos no Excel
    for rolamento in rolamentos:
        nome = rolamento.find("h3").text if rolamento.find("h3") else ""
        preco = rolamento.find("span", class_="price").text if rolamento.find("span", class_="price") else ""
        sheet.append([nome, preco])

    # Salva o arquivo Excel
    workbook.save("rolamentos.xlsx")

else:
    print("Falha no login")