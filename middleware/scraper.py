import requests
from bs4 import BeautifulSoup

def scrape_input_fields(url):
    """
    Scrapes the given website URL and extracts input fields from forms.
    Args:
        url (str): Target website URL.
    Returns:
        list: A list of dictionaries containing input field names and types.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful

        soup = BeautifulSoup(response.content, 'lxml')

        # Extract all input fields in forms
        input_fields = []
        for form in soup.find_all('form'):
            for input_tag in form.find_all(['input', 'textarea', 'select']):
                field_name = input_tag.get('name', None)
                field_type = input_tag.get('type', 'text')
                if field_name:
                    input_fields.append({'name': field_name, 'type': field_type})

        return input_fields

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []
