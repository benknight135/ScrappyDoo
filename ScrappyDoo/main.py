from ScrappyDoo import *

def find_quote_text(quote_div):
    quote_text_span = quote_div.find("span",class_="text")
    quote_text = quote_text_span.get_text()
    return quote_text

sd = ScrappyDoo("https://www.halfyardsewingclub.com/admin/users")
print("Auto logging into webpage...")
sd.login_GUI("https://www.halfyardsewingclub.com/login")


print(sd.soup)

# find all tables on the page
print("Finding tables on page...")
match_headers = ["name", "email", "subscrition plan", "id"]
tables = sd.find_tables(match_headers)