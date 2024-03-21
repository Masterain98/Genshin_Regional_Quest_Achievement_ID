import json
import os
import httpx

FULL_ENDPOINT_URL = os.getenv("ENDPOINT")

CITY_ID = {
    "mondstadt": 1,
    "liyue": 2,
    "inazuma": 3,
    "sumeru": 4,
    "fontaine": 5,
}

if __name__ == "__main__":
    data = json.load(open("DailyQuestAchievement.json", "r"))
    for city_name, city_quest_id_list in data.items():
        city_id = CITY_ID[city_name]
        response = httpx.post(
            FULL_ENDPOINT_URL.format(city_id=city_id),
            json=city_quest_id_list,
        )
        print(f"{city_name} submit result: {response.status_code} - {response.text}")
