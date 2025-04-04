from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Evita bloqueios anti-bot
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Inicializa o WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Habilita a captura de rede via CDP
driver.execute_cdp_cmd("Network.enable", {})

# URL do vídeo no Google Drive
url = "https://drive.google.com/file/d/1FDUw6f9m-O2XFIquNoB5lW9RTYnfol80/view"
driver.get(url)

# Aguarda o vídeo carregar
time.sleep(10)

# Captura as requisições de rede e busca pela URL do vídeo
logs = driver.execute_cdp_cmd("Network.getResponseBody", {})

# Obtém todas as requisições
logs = driver.execute_cdp_cmd("Network.getResponseBody", {})

for entry in logs:
    if "videoplayback" in entry.get("url", ""):
        print("URL do vídeo encontrada:", entry["url"])

# Fecha o navegador
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Evita bloqueios anti-bot
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Inicializa o WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Habilita a captura de rede via CDP
driver.execute_cdp_cmd("Network.enable", {})

# Lista para armazenar URLs do videoplayback
video_urls = []

# Função para capturar eventos de requisição
def log_request(event):
    request = event.get("params", {}).get("request", {})
    url = request.get("url", "")

    # Filtra apenas as URLs que contêm "videoplayback"
    if "videoplayback" in url:
        video_urls.append(url)
        print("URL do vídeo encontrada:", url)

# Registra evento para capturar requisições
driver.execute_script("""
window.performance.getEntries().forEach(entry => {
    if (entry.name.includes("videoplayback")) {
        console.log("URL do vídeo encontrada:", entry.name);
    }
});
""")

# URL do vídeo no Google Drive
url = "https://drive.google.com/file/d/1FDUw6f9m-O2XFIquNoB5lW9RTYnfol80/view"
driver.get(url)

# Aguarda o vídeo carregar
time.sleep(10)

# Fecha o navegador
driver.quit()

# Mostra todas as URLs capturadas
if video_urls:
    print("URLs capturadas:")
    for video in video_urls:
        print(video)
else:
    print("Nenhuma URL de vídeo encontrada.")
