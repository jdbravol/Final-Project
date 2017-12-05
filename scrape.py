import requests
from bs4 import BeautifulSoup

base_url = "http://api.genius.com"
headers = { "Authorization": "Bearer T7wAi-o3litnY4WQemF3kjpsXBWbXHXTNgSgzJev8dvXRXOIMsXytIF1OsI679G5" }

artist_name = "Kanye West"
artist_id = "72"


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
	file = open('raw/kanye', 'a', encoding='utf-8')

	# Get 50 songs at a time for a given artist ID
	search_url = base_url + "/artists/" + artist_id + "/songs"
	page = 1
	keep_going = True

	print("Scraping lyrics for " + artist_name + ", 50 songs at a time")

	while keep_going:
		print ("Page: " + str(page))
		params = {'per_page': 50, 'page': page, 'sort': 'popularity'}

		response = requests.get(search_url, params=params, headers=headers)
		print(response)
		json = response.json()

		song_info = None
		for song in json["response"]["songs"]:
			if (artist_name in song["primary_artist"]["name"] and "twitter" not in song["url"] and "speech" not in song["url"]
				and "tracklist" not in song["url"] and "interview" not in song["url"] and "credit" not in song["url"]):
				song_info = song
			if song_info:
				song_api_path = song_info["api_path"]
				file.write(lyrics_from_song_api_path(song_api_path))
				song_info = None

		page += 1

		if json["response"]["next_page"] is None:
			keep_going = False