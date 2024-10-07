import requests
from googlesearch import search
from bs4 import BeautifulSoup
import json
import time

#def find_company_url(company_name):
#    query = f"{company_name} official url"
#    for result in search(query, num_results=10, lang="en"):
#        if 'http' in result:
#            if 'linkedin' not in result and 'facebook' not in result:
#                return result
#    return None
def save_to_file(data):
    data_new = json.dumps(data, indent=4)
    with open("./data1.json", 'w') as f:
        #json.dump(data, f, indent=4)
        f.write(data_new)
        f.write("\n")
    

def find_company_website_bing(company_name):
    # Replace spaces with '+' for the search query
    search_query = company_name.replace(' ', '+')
    url = f"https://www.bing.com/search?q={search_query}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the first result's link
        link = soup.find_all("cite")
        link_new = list()
        for l in link:
            link_new.append(l.string)
        #print(url, link_new)
        return link_new

    except requests.exceptions.HTTPError as e:
        return f"HTTP error occurred: {e}"
    except Exception as e:
        return f"An error occurred: {e}"
#def find_company_website(company_name):
#    #query = f"{company_name} official website"
#    try:
#        time.sleep(1)
#        for result in search(company_name, num_results=10, lang="en"):
#            print("result",result)
#            if 'http' in result:
#                if 'linkedin' not in result and 'facebook' not in result:
#                    return result
#    except Exception as e:
#        print(f"An error accured: {e}")
#    #return "No website found"

#def find_company_career_page(company_name):
#    # Refine the query to search for career pages specifically
#    query = f"{company_name} careers site"
#    
#    for result in search(query, num_results=10, lang="en"):
#        # Look for URLs that likely contain the careers page
#        if ('careers' in result or 'jobs' in result) and 'http' in result:
#            return result
#    return "No career site found"

def scrape_url_content(url):
    try:
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            print(soup)
            element_list = list()
            element_list2 = list()
            for i, element in enumerate(soup.find_all("td")):
                element_new = element.string if i%2 == 0 and i != 0 else None
                print(element_new)
                if element_new:
                    element_list2.append(element_new)
                    #website = find_company_website(element_new)
                    #career_page = find_company_career_page(element_new)
                    #element_list.append({element_new:[website, career_page]}
                    #if i<100:
                        #time.sleep(5)
                    #websites = find_company_website_bing(element_new)
                    #if len(websites) > 0:
                    #    websites.insert(0,element_new)
                    #    element_list.append(websites)
            #print(len(element_list))
            #print("ELEMENT LIST", element_list, element_list2)
            save_to_file(element_list)
            #return element_list

           # title = soup.title.string if soup.title else "No Title"
           # return {
           #     "title": title,
           #     #"content": soup.get_text()
           # }
        else:
            return {"error": "Failed to retrieve page"}
    except Exception as e:
        return {"error": str(e)}
    
#url = input("Please specify url you want to exemine.\n")
url = "https://ind.nl/en/public-register-recognised-sponsors/public-register-regular-labour-and-highly-skilled-migrants"

if url:
    print(f"Scraping url...")
    start = time.time()
    scraped_content = scrape_url_content(url)
    end = time.time()
    print(f"Scraped content from {url}:")
    print("Elapsed Time:", end-start)
    #print(*scraped_content, sep="\n")
    #print(len(scraped_content))
else:
    print(f"No url found as: {url}")
