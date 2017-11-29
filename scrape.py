import requests
from bs4 import BeautifulSoup

base_url = "http://api.genius.com"
headers = { "Authorization": "Bearer T7wAi-o3litnY4WQemF3kjpsXBWbXHXTNgSgzJev8dvXRXOIMsXytIF1OsI679G5" }

song_title = "Runaway"
artist_name = "Kanye West"

def lyrics_from_song_api_path(song_api_path):
	song_url = base_url + song_api_path
	response = requests.get(song_url, headers=headers)
	json = response.json()
	path = json["response"]["song"]["path"]

	page_url = "http://genius.com" + path
	page = requests.get(page_url)
	html = BeautifulSoup(page.text, "html.parser")

	# Remove script tags that they put in the middle of the lyrics
	[h.extract() for h in html('script')]

	lyrics = html.find("div", class_="lyrics").get_text()
	return lyrics

if __name__ == "__main__":
	search_url = base_url + "/search"
	params = {'q': song_title}
	response = requests.get(search_url, params=params, headers=headers)
	json = response.json()
	song_info = None
	for hit in json["response"]["hits"]:
		if hit["result"]["primary_artist"]["name"] == artist_name:
			song_info = hit
		if song_info:
			song_api_path = song_info["result"]["api_path"]
			print lyrics_from_song_api_path(song_api_path)
			break