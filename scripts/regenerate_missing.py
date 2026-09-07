import requests
import os
import urllib.parse
import time

OUTPUT_DIR = r"E:\videoclip-project\storyboard\imagenes"

ANDRE = "a 40 year old latin man with mature face, slight stubble beard, warm brown skin, dark hair with touches of gray at temples, confident mature expression, fit build, wearing elegant casual button-up shirt sleeves rolled up, dark jeans, leather shoes"
ESPOSA = "a 35 year old latin woman with elegant mature beauty, warm brown skin, long dark wavy hair, confident graceful posture, wearing a beautiful flowing dress, high heels, natural makeup, radiant smile"

STYLE = "photorealistic digital painting, warm cinematic lighting, golden hour tones, Venezuelan llanero aesthetic, professional cinematography, sharp facial details, beautiful bokeh, warm orange gold color grading, 8k quality, music video still, realistic human faces"

MISSING = {
    "08_flashback_estrellas": {
        "prompt": f"Wide cinematic shot of a beautiful woman silhouette walking alone under spectacular starry night sky, Milky Way visible, her hair blowing in wind, dreamy romantic atmosphere, soft blue moonlight and golden starlight, magical fantasy flashback, {STYLE}",
        "seed": 5008
    },
    "09_huellas_arena": {
        "prompt": f"Extreme close-up of bare feet walking on soft golden sand leaving beautiful footprints, warm sunset light casting long shadows, each footprint visible, poetic romantic detail shot, shallow depth of field, golden hour, {STYLE}",
        "seed": 5009
    },
    "11_ojos_reflejo": {
        "prompt": f"Extreme close-up of beautiful brown eyes reflecting a sunset landscape of Venezuelan llanos like a mirror, eyelashes visible, warm golden light, poetic dreamy, shallow depth of field, only eyes in frame, {STYLE}",
        "seed": 5011
    },
    "12_cielo_arrebol": {
        "prompt": f"Breathtaking wide landscape of Venezuelan llanos at sunset, deep orange red pink sky known as arrebol, tall golden grass waving, single palm tree silhouette on horizon, warm golden hour, cinematic drone shot, {STYLE}",
        "seed": 5012
    },
    "19_mujeres_reaccion": {
        "prompt": f"Medium shot of group of women in shoe store looking at couple together, expressions of disappointment, one rolling eyes, another checking phone, whispering, they realize he is married, warm lighting, {STYLE}",
        "seed": 5019
    },
    "20_mujeres_salen": {
        "prompt": f"Wide shot of women walking out of shoe store one by one through glass door, looking back with disappointment, couple visible in background sitting together, warm evening light, {STYLE}",
        "seed": 5020
    },
    "21_final_juntos": {
        "prompt": f"Wide romantic final shot of {ANDRE} and {ESPOSA} sitting together on large bench in empty shoe store, his arm around her, her head on his shoulder, peaceful happy, warm golden light fading, beautiful ending, {STYLE}",
        "seed": 5021
    },
    "22_fundido": {
        "prompt": f"Fade to black romantic ending, silhouette of couple sitting together in shoe store, light fading to darkness, minimalist poetic, final frame of love story, {STYLE}",
        "seed": 5022
    }
}

for key, data in MISSING.items():
    filename = f"{key}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    print(f"{filename} - Generating...")
    
    encoded = urllib.parse.quote(data["prompt"])
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&seed={data['seed']}&model=flux"
    
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
