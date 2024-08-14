from flask import Flask, render_template
import html

import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

from selenium import webdriver
from selenium.webdriver.common.by import By

category=[]
def scraped_data(category):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.audible.in/?ref=Adbl_ip_rdr_from_US&source_code=AUDTM002080318002F&ipRedirectFrom=US&ipRedirectOriginalURL=search%3Fkeywords%3Dbook%26node%3D18573211011")

    # Find the list of anchor tags within the specified HTML structure
    anchor_tags = driver.find_elements(By.CSS_SELECTOR, ".bc-list-nostyle a")

    # Flag to indicate when to start extracting
    start_extraction = False

    # Extract the non-empty text from each anchor tag, starting from 'Best Sellers'
    categories = []
    for tag in anchor_tags:
        text = tag.text.strip()
        if text == 'Best Sellers':
            start_extraction = True
        if start_extraction and text:
            categories.append(text)

    if category=='bestsellers':
        url = "https://www.audible.in/adblbestsellers?ref_pageloadid=not_applicable&ref=a_hp_t1_navTop_pl1cg0c1r0&pf_rd_p=4e150d5e-ca98-47fb-823b-f6fcb252aced&pf_rd_r=H1DRKA28FEECNWMZR4Y1&pageLoadId=aSRyfgfDKe3PiNPb&creativeId=2e6787a2-0cd0-4a6e-afe0-05766cd505e5"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        #BEST SELLERS
        driver.get("https://www.audible.in/adblbestsellers?ref_pageloadid=not_applicable&ref=a_hp_t1_navTop_pl1cg0c1r0&pf_rd_p=4e150d5e-ca98-47fb-823b-f6fcb252aced&pf_rd_r=H1DRKA28FEECNWMZR4Y1&pageLoadId=aSRyfgfDKe3PiNPb&creativeId=2e6787a2-0cd0-4a6e-afe0-05766cd505e5")
        # Wait for the list items to be present
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]
        driver.quit()
        return book_titles, texts, author_name,duration, language, rating, number

    if category=='newreleases':
        #NEW RELEASES
        url = "https://www.audible.in/newreleases?ref_pageloadid=not_applicable&ref=a_hp_t1_navTop_pl1cg0c1r1&pf_rd_p=4e150d5e-ca98-47fb-823b-f6fcb252aced&pf_rd_r=PTHC2C2F2SQ9207SV47F&pageLoadId=LjmaQJKzuys633rb&feature_six_browse-bin=22212175031&creativeId=2e6787a2-0cd0-4a6e-afe0-05766cd505e5"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        driver.get("https://www.audible.in/newreleases?ref_pageloadid=not_applicable&ref=a_hp_t1_navTop_pl1cg0c1r1&pf_rd_p=4e150d5e-ca98-47fb-823b-f6fcb252aced&pf_rd_r=PTHC2C2F2SQ9207SV47F&pageLoadId=LjmaQJKzuys633rb&feature_six_browse-bin=22212175031&creativeId=2e6787a2-0cd0-4a6e-afe0-05766cd505e5")
        # Wait for the list items to be present
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles_new = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]

        driver.quit()
        return book_titles_new, texts, author_name, duration, language, rating, number
# #INDIAN LISTENS
# #driver.get("https://www.audible.in/ep/truly_indian?ref_pageloadid=not_applicable&ref=a_hp_b1_desktop_footer_column_2_2&pf_rd_p=051c5b3c-c8f2-411c-a2d5-12219b0b6a64&pf_rd_r=PTHC2C2F2SQ9207SV47F&pageLoadId=LjmaQJKzuys633rb&creativeId=574e9da0-9034-4220-8759-9acf82985f30")
#
    if category=='hindiaudiobooks':
        #HINDI AUDIOBOOKS
        url = "https://www.audible.in/search?ref_pageloadid=FofONZJlGjruDnnz&ref=a_ep_hindi-_c1_showmore&pf_rd_p=9fe7c7d3-7f03-47fc-8fe6-8ac81e4933ea&pf_rd_r=WCDCYRW7ZAEVDKAXRQF9&pageLoadId=MKgbXpfSFXB41l7M&feature_twelve_browse-bin=22212147031&sort=popularity-rank&feature_six_browse-bin=22212182031&creativeId=28063e6d-0979-4326-8b3c-7e5fd64a3cb5"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        driver.get("https://www.audible.in/search?ref_pageloadid=FofONZJlGjruDnnz&ref=a_ep_hindi-_c1_showmore&pf_rd_p=9fe7c7d3-7f03-47fc-8fe6-8ac81e4933ea&pf_rd_r=WCDCYRW7ZAEVDKAXRQF9&pageLoadId=MKgbXpfSFXB41l7M&feature_twelve_browse-bin=22212147031&sort=popularity-rank&feature_six_browse-bin=22212182031&creativeId=28063e6d-0979-4326-8b3c-7e5fd64a3cb5")
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles_hindi = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]
        driver.quit()
        return book_titles_hindi, texts, author_name, duration, language, rating, number

    if category=='mysteriesthrillers':
        #MYSTERIES,THRILLERS & SUSPENSE
        url = "https://www.audible.in/search?browseNode=21881787031&ref=left_nav_mys&ref_pageloadid=not_applicable&ref=a_hp_b1_desktop_footer_column_3_0&pf_rd_p=051c5b3c-c8f2-411c-a2d5-12219b0b6a64&pf_rd_r=QYYTXFKHBF2PVQJ3AC4P&pageLoadId=8sHPrlQMNmE46f99&creativeId=574e9da0-9034-4220-8759-9acf82985f30"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        driver.get("https://www.audible.in/search?browseNode=21881787031&ref=left_nav_mys&ref_pageloadid=not_applicable&ref=a_hp_b1_desktop_footer_column_3_0&pf_rd_p=051c5b3c-c8f2-411c-a2d5-12219b0b6a64&pf_rd_r=QYYTXFKHBF2PVQJ3AC4P&pageLoadId=8sHPrlQMNmE46f99&creativeId=574e9da0-9034-4220-8759-9acf82985f30")
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles_mts = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]
        driver.quit()
        return book_titles_mts, texts, author_name, duration, language, rating, number

    if category=='romance':
        #ROMANCE
        url = "https://www.audible.in/search?node=21881804031&sort=popularity-rank&ref_pageloadid=8sHPrlQMNmE46f99&ref=a_cat_Roman_c8_showmore&pf_rd_p=be4f74e4-9068-42fd-9319-73eb8b0c879a&pf_rd_r=3Q97RRPM2784YKC7FSCD&pageLoadId=1xyDKj4va7Boowtv&creativeId=fa240ef5-2ebf-4f43-b1b1-11c01bce5b1b"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        driver.get("https://www.audible.in/search?node=21881804031&sort=popularity-rank&ref_pageloadid=8sHPrlQMNmE46f99&ref=a_cat_Roman_c8_showmore&pf_rd_p=be4f74e4-9068-42fd-9319-73eb8b0c879a&pf_rd_r=3Q97RRPM2784YKC7FSCD&pageLoadId=1xyDKj4va7Boowtv&creativeId=fa240ef5-2ebf-4f43-b1b1-11c01bce5b1b")
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles_rom = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]
        driver.quit()
        return book_titles_rom, texts, author_name, duration, language, rating, number

    if category=='fiction':
        #FICTION
        url = "https://www.audible.in/search?browseNode=21881795031&feature_six_browse-bin=22212175031&feature_six_browse-bin=22212182031&ref_pageloadid=OxKvc449JimF75cx&ref=a_search_l1_feature_six_browse-bin_4&pf_rd_p=548d5de2-cafa-49cf-99a3-de37f89d955d&pf_rd_r=7CNPQA0VKDSC4TFJ6KSE&pageLoadId=T0gSxqyDVx4Vndbc&creativeId=89c16a62-4cd5-487a-bc38-68e0434b056b"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        driver.get("https://www.audible.in/search?browseNode=21881795031&feature_six_browse-bin=22212175031&feature_six_browse-bin=22212182031&ref_pageloadid=OxKvc449JimF75cx&ref=a_search_l1_feature_six_browse-bin_4&pf_rd_p=548d5de2-cafa-49cf-99a3-de37f89d955d&pf_rd_r=7CNPQA0VKDSC4TFJ6KSE&pageLoadId=T0gSxqyDVx4Vndbc&creativeId=89c16a62-4cd5-487a-bc38-68e0434b056b")
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles_fic = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]
        driver.quit()
        return book_titles_fic, texts, author_name, duration, language, rating, number

    if category=='sciencefiction':
        #SCI-FI & FANTASY
        url = "https://www.audible.in/search?node=21881796031&sort=popularity-rank&ref_pageloadid=8sHPrlQMNmE46f99&ref=a_cat_Scien_c8_showmore&pf_rd_p=be4f74e4-9068-42fd-9319-73eb8b0c879a&pf_rd_r=YXJ7SW2Y7N5GR8DTTTNB&pageLoadId=HM5S4e3T8lv8sjda&creativeId=fa240ef5-2ebf-4f43-b1b1-11c01bce5b1b"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        driver.get("https://www.audible.in/search?node=21881796031&sort=popularity-rank&ref_pageloadid=8sHPrlQMNmE46f99&ref=a_cat_Scien_c8_showmore&pf_rd_p=be4f74e4-9068-42fd-9319-73eb8b0c879a&pf_rd_r=YXJ7SW2Y7N5GR8DTTTNB&pageLoadId=HM5S4e3T8lv8sjda&creativeId=fa240ef5-2ebf-4f43-b1b1-11c01bce5b1b")
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles_scifi = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]
        driver.quit()
        return book_titles_scifi, texts, author_name, duration, language, rating, number

    if category=='selfdevelopment':
        #SELF-DEVELOPMENT
        url = "https://www.audible.in/search?feature_six_browse-bin=22212175031&node=21881993031&sort=popularity-rank&ref_pageloadid=HQy1YzDxGk9cGOOo&ref=a_search_l1_feature_six_browse-bin_2&pf_rd_p=548d5de2-cafa-49cf-99a3-de37f89d955d&pf_rd_r=EJGKT0TN4ZDKVJ3GFG66&pageLoadId=bPyNo2oelG3YPgkX&creativeId=89c16a62-4cd5-487a-bc38-68e0434b056b"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        driver.get("https://www.audible.in/search?feature_six_browse-bin=22212175031&node=21881993031&sort=popularity-rank&ref_pageloadid=HQy1YzDxGk9cGOOo&ref=a_search_l1_feature_six_browse-bin_2&pf_rd_p=548d5de2-cafa-49cf-99a3-de37f89d955d&pf_rd_r=EJGKT0TN4ZDKVJ3GFG66&pageLoadId=bPyNo2oelG3YPgkX&creativeId=89c16a62-4cd5-487a-bc38-68e0434b056b")
        list_items = driver.find_elements(By.CSS_SELECTOR, '.bc-list .bc-list-item[aria-label]')

        # Extract book titles and print
        book_titles_sd = html.unescape([item.get_attribute('aria-label') for item in list_items if item.get_attribute('aria-label')])
        # description
        text_elements = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.subtitle .bc-text')
        texts = [element.text.strip() for element in text_elements]
        # author
        span_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.authorLabel .bc-text .bc-link')
        author_name = [element.text.strip() for element in span_element]
        # length
        length_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.runtimeLabel .bc-text')
        duration = [element.text.strip() for element in length_element]
        # language
        lang_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.languageLabel .bc-text')
        language = [element.text.strip() for element in lang_element]
        # ratings
        rating_element = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-pub-offscreen')
        rating = [element.text.strip() for element in rating_element]
        # number of ratings given
        num_rate = driver.find_elements(By.CSS_SELECTOR, '.bc-list-item.ratingsLabel .bc-text.bc-color-secondary')
        number = [element.text.strip() for element in num_rate]
        driver.quit()
        return book_titles_sd, texts, author_name, duration, language, rating, number

    return categories
@app.route('/')
def index():
    return render_template('index.html')

# Route for dynamically loading content based on category
@app.route('/bestsellers')
def bestsellers():
    # Scrape data for Best Sellers
    book_titles, texts, author_name, duration, language, rating, number = scraped_data('bestsellers')
    return render_template('bestsellers.html', book_titles=book_titles, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

@app.route('/newreleases')
def newreleases():
    # Scrape data for New Releases
    book_titles_new, texts, author_name, duration, language, rating, number = scraped_data('newreleases')
    return render_template('newreleases.html', book_titles_new=book_titles_new, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

@app.route('/hindiaudiobooks')
def hindiaudiobooks():
    # Scrape data for New Releases
    book_titles_hindi, texts, author_name, duration, language, rating, number  = scraped_data('hindiaudiobooks')
    return render_template('hindiaudiobooks.html', book_titles_hindi=book_titles_hindi, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

@app.route('/mysteriesthrillers')
def mysteriesthrillers():
    # Scrape data for New Releases
    book_titles_mts, texts, author_name, duration, language, rating, number  = scraped_data('mysteriesthrillers')
    return render_template('mysteriesthrillers.html', book_titles_mts=book_titles_mts, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

@app.route('/romance')
def romance():
    # Scrape data for New Releases
    book_titles_rom, texts, author_name, duration, language, rating, number  = scraped_data('romance')
    return render_template('romance.html', book_titles_rom=book_titles_rom, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

@app.route('/fiction')
def fiction():
    # Scrape data for New Releases
    book_titles_fic, texts, author_name, duration, language, rating, number  = scraped_data('fiction')
    return render_template('fiction.html', book_titles_fic=book_titles_fic, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

@app.route('/sciencefiction')
def sciencefiction():
    # Scrape data for New Releases
    book_titles_scifi, texts, author_name, duration, language, rating, number  = scraped_data('sciencefiction')
    return render_template('sciencefiction.html', book_titles_scifi=book_titles_scifi, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

@app.route('/selfdevelopment')
def selfdevelopment():
    # Scrape data for New Releases
    book_titles_sd, texts, author_name, duration, language, rating, number  = scraped_data('selfdevelopment')
    return render_template('selfdevelopment.html', book_titles_sd=book_titles_sd, texts=texts, author_name=author_name, duration=duration, language=language, rating=rating, number=number)

if __name__ == '__main__':
    app.run(debug=True)
