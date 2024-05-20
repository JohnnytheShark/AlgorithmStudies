voted = {}
def check_voter(name):
    if voted.get(name):
        print("Kicked Out")
    else:
        voted[name] = True
        print("Allowed to vote")

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data 