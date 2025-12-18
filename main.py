from playwright.sync_api import sync_playwright
import time

def run_rpa_challenge():
    # Datos estáticos para el formulario (10 registros)
    data = [
        {
            "firstName": "John",
            "lastName": "Smith",
            "companyName": "IT Solutions",
            "role": "Analyst",
            "address": "98 North Road",
            "email": "jsmith@itsolutions.co.uk",
            "phone": "40716543298"
        },
        {
            "firstName": "Jane",
            "lastName": "Dorsey",
            "companyName": "MediCare",
            "role": "Medical Engineer",
            "address": "11 Crown Street",
            "email": "jdorsey@mc.com",
            "phone": "40791345621"
        },
        {
            "firstName": "Albert",
            "lastName": "Kipling",
            "companyName": "Waterfront",
            "role": "Accountant",
            "address": "22 Guild Street",
            "email": "kipling@waterfront.com",
            "phone": "40735416854"
        },
        {
            "firstName": "Michael",
            "lastName": "Robertson",
            "companyName": "MediCare",
            "role": "IT Specialist",
            "address": "17 Farburn Terrace",
            "email": "mrobertson@mc.com",
            "phone": "40733652145"
        },
        {
            "firstName": "Doug",
            "lastName": "Derrick",
            "companyName": "Timepath Inc.",
            "role": "Analyst",
            "address": "99 Shire Oak Road",
            "email": "dderrick@timepath.co.uk",
            "phone": "40799885412"
        },
        {
            "firstName": "Jessie",
            "lastName": "Marlowe",
            "companyName": "Aperture Inc.",
            "role": "Scientist",
            "address": "27 Cheshire Street",
            "email": "jmarlowe@aperture.us",
            "phone": "40733154268"
        },
        {
            "firstName": "Stan",
            "lastName": "Hamm",
            "companyName": "Sugarwell",
            "role": "Advisor",
            "address": "10 Dam Road",
            "email": "shamm@sugarwell.org",
            "phone": "40712462257"
        },
        {
            "firstName": "Michelle",
            "lastName": "Norton",
            "companyName": "Aperture Inc.",
            "role": "Scientist",
            "address": "13 White Rabbit Street",
            "email": "mnorton@aperture.us",
            "phone": "40731254562"
        },
        {
            "firstName": "Stacy",
            "lastName": "Shelby",
            "companyName": "TechDev",
            "role": "HR Manager",
            "address": "19 Pineapple Boulevard",
            "email": "sshelby@techdev.com",
            "phone": "40741785214"
        },
        {
            "firstName": "Lara",
            "lastName": "Palmer",
            "companyName": "Timepath Inc.",
            "role": "Programmer",
            "address": "87 Orange Street",
            "email": "lpalmer@timepath.co.uk",
            "phone": "40731653845"
        }
    ]

    with sync_playwright() as p:
        # Iniciar navegador
        browser = p.chromium.launch(headless=False)  # headless=False para ver la ejecución
        context = browser.new_context()
        page = context.new_page()

        # Navegar a la página del desafío
        page.goto("https://rpachallenge.com/")
        
        # Hacer clic en el botón Start
        page.click("button:has-text('Start')")
        
        # Iterar a través de los datos y completar el formulario para cada conjunto de datos
        for user_data in data:
            # Rellenar los campos identificando por los atributos ng-reflect-name
            page.fill("input[ng-reflect-name='labelFirstName']", user_data["firstName"])
            page.fill("input[ng-reflect-name='labelLastName']", user_data["lastName"])
            page.fill("input[ng-reflect-name='labelCompanyName']", user_data["companyName"])
            page.fill("input[ng-reflect-name='labelRole']", user_data["role"])
            page.fill("input[ng-reflect-name='labelAddress']", user_data["address"])
            page.fill("input[ng-reflect-name='labelEmail']", user_data["email"])
            page.fill("input[ng-reflect-name='labelPhone']", user_data["phone"])
            
            # Enviar el formulario haciendo clic en el botón Submit
            page.click("input[value='Submit']")
            
            # Pequeña pausa para visualizar mejor (opcional)
            time.sleep(0.5)
        
        # Esperar unos segundos para ver el resultado final
        time.sleep(5)
        
        # Capturar una instantánea del resultado
        page.screenshot(path="rpa_challenge_result.png")
        
        # Cerrar el navegador
        browser.close()
        
        print("Desafío completado correctamente!")

if __name__ == "__main__":
    run_rpa_challenge()
