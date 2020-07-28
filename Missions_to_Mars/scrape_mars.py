from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    time.sleep(2)
    try:
        news_title = soup.find("div", class_="content_title").get_text()
    except:
        news_title= ""
    try:
        news_p = soup.find("div", class_="article_teaser_body").get_text()
    except:
        news_p=""
   

    mars_dict = {
        "news_title": news_title, 
        "news_paragraph": news_p,
        "space_imgage": scrape_mars_space_img(browser),
        "weather": scrape_mars_weather(browser),
        "facts": scrape_facts(browser),
        "hemispheres": scrape_hemispheres(browser)
    }


    return mars_dict


def scrape_mars_space_img(browser):
    

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17845_ip.jpg'

    mars_dict = featured_image_url


    return mars_dict


def scrape_mars_weather(browser):
   

    twitter_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_weather_url)

    html_weather = browser.html
    soup = BeautifulSoup(html_weather, "html.parser")
    try:
    
        mars_weather = soup.find("span", class_="css-901oao").get_text()
    except:
        mars_weather=""
        
    mars_dict = mars_weather

    return mars_dict


def scrape_facts(browser):
    

    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    tables = pd.read_html(facts_url)
    tables

    df = tables[0]
    df.columns = ['Type', 'Results']
    df.set_index('Type', inplace=True)
    html_table = df.to_html()
    

    mars_dict = html_table

    return mars_dict

def scrape_hemispheres(browser):
    

    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, "html.parser")

    hemispheres_dict = []

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    ]


    mars_dict = hemisphere_image_urls

    return mars_dict






     