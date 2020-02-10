from ScrappyDoo import ScrappyDoo, AutoBrowser

sd = ScrappyDoo("http://quotes.toscrape.com/")
sd.login_page("http://quotes.toscrape.com/login","admin","12345")