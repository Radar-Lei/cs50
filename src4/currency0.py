import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=731b3535b96c93c67e57d672a843711b&symbols=EUR,USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
