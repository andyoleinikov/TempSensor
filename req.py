import requests

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }


def get_html(url):
    try:
        result = requests.get(url, headers = headers)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException as e: 
        print(e)
        return False


