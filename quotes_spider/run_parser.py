import os
import subprocess
import sys

# Установим необходимые зависимости
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Запускаем парсер
os.system("scrapy crawl quotes -o quotes.json")
