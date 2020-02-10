from ScrappyDoo import *

def find_quote_text(quote_div):
    quote_text_span = quote_div.find("span",class_="text")
    quote_text = quote_text_span.get_text()
    return quote_text

sd = ScrappyDoo("http://quotes.toscrape.com/")
print("Auto logging into webpage...")
sd.login_page("http://quotes.toscrape.com/login","admin","12345")
# find the first quote on the page
print("Finding quote on page...")
quote_div = sd.soup.find("div",class_="quote")
quote_text = find_quote_text(quote_div)
print(quote_text)

# find all quotes on the page
print("Finding quotes on page...")
quote_divs = sd.soup.find_all("div",class_="quote")
for quote_div in quote_divs:
    quote_text = find_quote_text(quote_div)
    print(quote_text)