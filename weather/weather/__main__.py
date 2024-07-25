import requests


def main():
    response = requests.get("http://wttr.in/kiel")
    if response.status_code == 200:
        print(response.content.decode())


if __name__ == "__main__":
    main()
