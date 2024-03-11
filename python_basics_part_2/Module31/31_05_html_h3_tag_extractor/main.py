import requests
from bs4 import BeautifulSoup


def get_html_from_url(url: str) -> str:
    """ Fetch HTML content from a given URL. """
    response = requests.get(url)
    return response.text


def get_html_from_file(file_path: str) -> str:
    """ Read HTML content from a specified file. """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_h3_tags(html_content: str) -> list:
    """ Extract and return all <h3> tags from the given HTML content. """
    soup = BeautifulSoup(html_content, 'html.parser')
    h3_tags = soup.find_all('h3')
    return [tag.get_text().strip() for tag in h3_tags]


def main():
    choice = input("Enter 'url' to load HTML from a web address or 'file' to read HTML from a file: ").strip().lower()

    if choice == 'url':
        url = input("Enter URL: ")
        html_content = get_html_from_url(url)
    elif choice == 'file':
        file_path = input("Enter file path: ")
        html_content = get_html_from_file(file_path)
    else:
        print("Invalid choice")
        return

    subheadings = get_h3_tags(html_content)
    for subheading in subheadings:
        print(subheading)


if __name__ == "__main__":
    main()
