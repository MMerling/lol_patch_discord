import requests
from bs4 import BeautifulSoup, element
import interactions

def lol_latest_patch_notes():
    """
    Returns url latest League of Legends patch notes
    """

    base_url = "https://www.leagueoflegends.com"
    url = f"{base_url}/en-us/news/tags/patch-notes/"
    main_req = requests.get(url)

    soup = BeautifulSoup(main_req.content,"html.parser")

    latest_patch = soup.find('a', href=True)

    return f"{base_url}{latest_patch['href']}"

def main():
    bot_token = "your token"

    bot = interactions.Client(token=bot_token)

    @bot.command(name="lol_patch", description="url for latest LoL patch notes")
    async def lol_patch(ctx):
        response = lol_latest_patch_notes()
        await ctx.send(response)

    bot.start()

if __name__ == "__main__":
    main()