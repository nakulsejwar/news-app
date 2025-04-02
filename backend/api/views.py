import requests
from django.http import JsonResponse
from django.views import View
from datetime import datetime
import logging


logging.basicConfig(level=logging.INFO)

class HackerNewsAPI(View):
    def get(self, request):
        try:
            
            response = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json", timeout=5)
            response.raise_for_status()
            story_ids = response.json()[:10]
            
            stories = []
            for story_id in story_ids:
                story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=5)
                story_response.raise_for_status()
                story_data = story_response.json()
                
                story_time = datetime.fromtimestamp(story_data.get("time", 0)).strftime('%Y-%m-%d %H:%M:%S')
                
                stories.append({
                    "title": story_data.get("title", "No Title"),
                    "author": story_data.get("by", "Unknown"),
                    "url": story_data.get("url", "#"),
                    "score": story_data.get("score", 0),
                    "time": story_time,
                })
            
            return JsonResponse(stories, safe=False)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data: {e}")
            return JsonResponse({"error": "Failed to fetch data from HackerNews"}, status=500)
