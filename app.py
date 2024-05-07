from flask import Flask, request, render_template
from urllib.parse import urlencode 
from bs4 import BeautifulSoup
import urllib.parse
import requests
import base64
import re

app = Flask(__name__)

def vegamovies(movie_link,quality):
    slash_index = movie_link.find('/', 8)

    domain = movie_link[:slash_index] if slash_index != -1 else movie_link
    h1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "X-Forwarded-For": "192.168.29.7",
    }
    r0 = requests.get(url = movie_link, headers = h1)
    soup = BeautifulSoup(r0.text, 'html.parser')
    links = soup.find_all('a', attrs={'rel': 'nofollow noopener noreferrer'})
    download_links = {}
    for index, link in enumerate(links):  
        href = link['href']
        download_links[str(index)] = urlencode({'': href})[1:]

    if quality in download_links:
        value = download_links[quality]

    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    r1 = requests.post(url = f'{domain}/red.php', headers = h, data = f"link={value}")
    url_match = re.search(r'window\.location\.href\s*=\s*"([^"]+)"', r1.text)
    if url_match:
        link1 = url_match.group(1)



    r2 = requests.get(url = link1, headers = h1)
    link_match = re.search(r'https://vcloud\.lol/\S+', r2.text)
    if link_match:
        link2 = link_match.group(0)
        link2 = link2[:-1]


    r3 = requests.get(url = link2, headers = h)
    url_match1 = re.search(r"var url = '([^']+)';", r3.text)
    if url_match1:
        link3 = url_match1.group(1)
        url_match2 = re.search(r"id=([^']+)", link3)
        if url_match2:
            url = url_match2.group(1)
    final = f"{link2}?token={url}"
    return final


def bollyflix(movie_link):
    q_m_i = movie_link.find('?')
    new_url = movie_link[q_m_i:]

    # urls = {
    #     "dizztips.com": "https://ww2.dizztips.com/",
    #     "tech-news.app": "https://box.tech-news.app/",
    #     "sidexfee.com": "https://web.sidexfee.com/"
    # }

    # for key in urls:
    #     r0 = requests.get(url = f"https://check.{key}/wp.json")
    #     if r0.status_code == 200:
    #         link = urls[key]
    #         break
    #     else:
    #         print(f"Failed to retrieve data from {urls[key]} for {key}.")


    # r = requests.get(url = f"{link}{new_url}")
    r = requests.get(url = f"https://web.sidexfee.com/{new_url}")

    pattern = r'var item = ({.*?});'
    match = re.search(pattern, r.text)
    if match:
        json_str = match.group(1)
        link_pattern = r'"link":"(.*?)"'
        link_match = re.search(link_pattern, json_str)

        if link_match:
            base64_link = link_match.group(1)
            decoded_bytes = base64.b64decode(base64_link)
            quarter_final = decoded_bytes.decode('utf-8')
            dec_part = quarter_final.split('?id=')[1].split('&type=')[0]
            decoded_part = urllib.parse.quote(dec_part)
            semi_final = quarter_final.replace(dec_part, decoded_part)

    r1 = requests.get(url = semi_final, allow_redirects=False)
    final = r1.headers['Location']
            
    return final

# Helper function for movie logic
def moviesmod_m(movie_link):
    h1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "X-Forwarded-For": "192.168.29.7",
    }
    r = requests.get(url = movie_link, headers = h1)
    #print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')
    anchor_tag = soup.find('a', class_='maxbutton-fast-server-gdrive')
    if anchor_tag:
        href_link = anchor_tag['href']
        link1 = href_link

    r1 = requests.post(url = link1)

    soup = BeautifulSoup(r1.text, 'html.parser')
    input_tag = soup.find('input', {'name': '_wp_http'})
    if input_tag:
        value = input_tag.get('value')
    link2 = urllib.parse.quote(value,safe='')

    headers = {
        "Host": "tech.unblockedgames.world",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
    }
    data = f"_wp_http={link2}"
    r2 = requests.post(url = "https://tech.unblockedgames.world/", headers = headers, data = data)

    soup = BeautifulSoup(r2.text, 'html.parser')
    link3 = soup.form.get('action')
    http2 = urllib.parse.quote(soup.find('input', {'name': '_wp_http2'}).get('value'),safe='')
    token = soup.find('input', {'name': 'token'}).get('value')

    headers1 = {
        "Host": "tech.unblockedgames.world",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://tech.unblockedgames.world",
        "Content-Type": "application/x-www-form-urlencoded",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://tech.unblockedgames.world/",
    }
    data1 = f"_wp_http2={http2}&token={token}"
    r3 = requests.post(url = link3, headers = headers1, data = data1)

    match1 = re.findall(r'pepe-[a-zA-Z\d]+', r3.text)
    match2 = re.findall(r"\'eJ(.*?)\', 60\)", r3.text)
    if match1:
        pepe_number = match1[0]
    link4 = f"https://tech.unblockedgames.world/?go={pepe_number}"
    intro = re.sub(r'^.*?pepe-', 'pepe-', link4)
    if match2:
        val = match2[0]
    pepe = f"eJ{val}"

    headers2 = {
        "Host": "tech.unblockedgames.world",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": link3,
    }
    cookies = {
        intro: pepe
    }
    r4 = requests.get(url = link4, headers = headers2, cookies = cookies)
    soup = BeautifulSoup(r4.text, 'html.parser')
    quarter_final = soup.find('meta', {'http-equiv': 'refresh'}).get('content').split('url=')[1]
    index = quarter_final.find('/r?')
    if index != -1:
        modi5_url = quarter_final[:index]

    r5 = requests.get(url = quarter_final)
    match3 = re.search(r'window\.location\.replace\("([^"]+)"\)', r5.text)
    if match3:
        url = match3.group(1)
        semi_final = url
    final = f"{modi5_url}{semi_final}"

    return final

def moviesmod_e(series_link):
    h1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "X-Forwarded-For": "192.168.29.7",
    }
    r = requests.get(url = series_link, headers = h1)
    html_source = r.text
    soup = BeautifulSoup(html_source, 'html.parser')
    episode_links = soup.find_all('h3')
    results = []
    for i, link in enumerate(episode_links, start=1):
        episode_number = link.text.strip()
        episode_url = link.find('a')['href']

        r1 = requests.post(url = episode_url)

        soup = BeautifulSoup(r1.text, 'html.parser')
        input_tag = soup.find('input', {'name': '_wp_http'})
        if input_tag:
            value = input_tag.get('value')
        link2 = urllib.parse.quote(value,safe='')


        headers = {
            "Host": "tech.unblockedgames.world",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
        }
        data = f"_wp_http={link2}"
        r2 = requests.post(url = "https://tech.unblockedgames.world/", headers = headers, data = data)

        soup = BeautifulSoup(r2.text, 'html.parser')
        link3 = soup.form.get('action')
        http2 = urllib.parse.quote(soup.find('input', {'name': '_wp_http2'}).get('value'),safe='')
        token = soup.find('input', {'name': 'token'}).get('value')


        headers1 = {
            "Host": "tech.unblockedgames.world",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://tech.unblockedgames.world",
            "Content-Type": "application/x-www-form-urlencoded",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://tech.unblockedgames.world/",
        }
        data1 = f"_wp_http2={http2}&token={token}"
        r3 = requests.post(url = link3, headers = headers1, data = data1)

        match1 = re.findall(r'pepe-[a-zA-Z\d]+', r3.text)
        match2 = re.findall(r"\'eJ(.*?)\', 60\)", r3.text)
        if match1:
            pepe_number = match1[0]
        link4 = f"https://tech.unblockedgames.world/?go={pepe_number}"
        intro = re.sub(r'^.*?pepe-', 'pepe-', link4)
        if match2:
            val = match2[0]
        pepe = f"eJ{val}"


        headers2 = {
            "Host": "tech.unblockedgames.world",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": link3,
        }
        cookies = {
            intro: pepe
        }
        r4 = requests.get(url = link4, headers = headers2, cookies = cookies)
        soup = BeautifulSoup(r4.text, 'html.parser')
        quarter_final = soup.find('meta', {'http-equiv': 'refresh'}).get('content').split('url=')[1]
        index = quarter_final.find('/r?')
        if index != -1:
            modi5_url = quarter_final[:index]


        r5 = requests.get(url = quarter_final)
        match3 = re.search(r'window\.location\.replace\("([^"]+)"\)', r5.text)
        if match3:
            url = match3.group(1)
            semi_final = url
#        final = f"{modi5_url}{semi_final}"

        final = f"{modi5_url}{semi_final}" 
        results.append(f"Episode {i}: {final}") 
    return "\n".join(results) 

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    input_data = request.get_json() 
    movie_link = input_data['data']  
    choice = input_data['choice']
    quality = input_data['quality']
    if choice == 'vegamovies':
        result = vegamovies(movie_link,quality)
    elif choice == 'bollyflix':
        result = bollyflix(movie_link)
    elif choice == 'movie':
        result = moviesmod_m(movie_link)
    elif choice == 'episodes':
        result = moviesmod_e(movie_link)
    else:
        result = "Invalid choice. Please select 'movie' or 'episodes'."

    return result  

if __name__ == '__main__':
    app.run(debug=True) 
