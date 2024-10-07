import json
import requests
import bs4 as BeautifulSoup
import time

with open("./data1.json", 'r') as f:
    data = json.load(f)

#ef find_company_website_bing(company_name):
    # Replace spaces with '+' for the search query
    #search_query = company_name.replace(' ', '+')
    #url = f"https://www.bing.com/search?q={search_query}"
    #headers = {
    #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    #}

    #try:
        #response = requests.get(url, headers=headers)
        #response.raise_for_status()
        #soup = BeautifulSoup(response.content, 'html.parser')
        #link = soup.find_all("cite")
        #link_new = list()
        #for l in link:
        #    link_new.append(l.string)
        ##print(url, link_new)
        #return link_new

    #except requests.exceptions.HTTPError as e:
    #    return f"HTTP error occurred: {e}"
    #except Exception as e:
    #    return f"An error occurred: {e}"
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
list_all = list()
for d in data:
    #time.sleep(1)
    d_new = d.replace(" ","")
    search_link = f"https://www.google.com/search?q={d_new}"
    company_website = {d:search_link}
    list_all.append(company_website)


data2_new = json.dumps(list_all, indent=4)
with open(f"./data.json", 'w') as r:
        #json.dump(data2, r, indent=4)
        r.write(data2_new)
        r.write("\n")