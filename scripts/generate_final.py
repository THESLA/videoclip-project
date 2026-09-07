import requests
import os
import urllib.parse
import time

OUTPUT_DIR = r"E:\videoclip-project\storyboard\imagenes"

ANDRE = "a 40 year old latin man, mature handsome face, slight stubble, warm brown skin, confident expression, dark hair with some gray, fit build, wearing an elegant casual button-up shirt with sleeves rolled up, dark jeans, leather shoes"
ESPOSA = "a 35 year old latin woman, elegant mature beauty, warm brown skin, long dark wavy hair, confident graceful walk, wearing a beautiful flowing dress, high heels, natural makeup, radiant smile"

STYLE_LLANERO = "photorealistic digital painting, warm cinematic lighting, golden hour tones, Venezuelan llanero aesthetic, professional cinematography look, sharp details, beautiful bokeh background, color grading warm orange and gold tones, 8k quality, professional music video still"

REMAINING = {
    "19_mujeres_reaccion": {
        "prompt": f"Medium shot of the group of women in the shoe store looking at {ANDRE} and his wife together, their expressions showing disappointment and annoyance, one woman rolling her eyes, another checking her phone dismissively, another whispering to her friend, they realize he was never available, warm lighting, {STYLE_LLANERO}",
        "seed": 1019
    },
    "20_mujeres_salen": {
        "prompt": f"Wide shot of the women walking out of the shoe store one by one through the glass door, looking back with expressions of defeat and disappointment, the couple is visible in the background sitting together in love, the women leave one after another, warm evening light, {STYLE_LLANERO}",
        "seed": 1020
    },
    "21_final_juntos": {
        "prompt": f"Wide romantic final shot of {ANDRE} and his wife sitting together on the luxurious armchair in the now empty shoe store, his arm around her, her head resting on his shoulder, they look peaceful and happy together, warm golden light fading to soft dusk, beautiful ending moment, {STYLE_LLANERO}",
        "seed": 1021
    },
    "22_fundido": {
        "prompt": f"Fade to black romantic ending, silhouette of couple sitting together in a shoe store, light fading to complete darkness around them, minimalist and poetic, final frame of a love story, {STYLE_LLANERO}",
        "seed": 1022
    }
}

for key, data in REMAINING.items():
    filename = f"{key}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(filepath):
        print(f"{filename} - EXISTS")
        continue
    
    encoded = urllib.parse.quote(data["prompt"])
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&seed={data['seed']}&model=flux"
    
    print(f"{filename} - Generating...")
    try:
        resp = requests.get(url, timeout=180)
        if resp.status_code == 200 and len(resp.content) > 1000:
            with open(filepath, "wb") as f:
                f.write(resp.content)
            print(f"  OK - {len(resp.content)} bytes")
        else:
            print(f"  FAIL - HTTP {resp.status_code}")
    except Exception as e:
        print(f"  FAIL - {e}")
    time.sleep(2)

print("\nDone!")
files = sorted(os.listdir(OUTPUT_DIR))
print(f"Total: {len(files)} images")
