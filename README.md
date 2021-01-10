# web-scraping-challenge
Web Scraping - Mission to Mars

Step 1 - Scraping
* Complete scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

* Use Pandas to convert the data to a HTML table string.

Step 2 - MongoDB and Flask Application
* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

* Store the return value in Mongo as a Python dictionary.

* Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

