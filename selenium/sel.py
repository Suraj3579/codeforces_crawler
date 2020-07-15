from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
browser = Firefox(options = opts)
browser.get('https://www.imdb.com/list/ls057823854/')



