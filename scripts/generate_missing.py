import requests
import os
import urllib.parse
import time

OUTPUT_DIR = r"E:\videoclip-project\storyboard\imagenes"

ANDRE = "a 40 year old latin man, mature handsome face, slight stubble, warm brown skin, confident expression, dark hair with some gray, fit build, wearing an elegant casual button-up shirt with sleeves rolled up, dark jeans, leather shoes"
ESPOSA = "a 35 year old latin woman, elegant mature beauty, warm brown skin, long dark wavy hair, confident graceful walk, wearing a beautiful flowing dress, high heels, natural makeup, radiant smile"

STYLE_LLANERO = "photorealistic digital painting, warm cinematic lighting, golden hour tones, Venezuelan llanero aesthetic, professional cinematography look, sharp details, beautiful bokeh background, color grading warm orange and gold tones, 8k quality, professional music video still"

MISSING = {
    "03_andre_sienta": {
        "prompt": f"Medium shot of {ANDRE} sitting down confidently in a large luxurious velvet armchair in the center of a shoe store, crossing his legs, leaning back with arms on the armrests, relaxed and patient expression, surrounded by beautiful shoes on illuminated shelves, warm golden lighting from above, he is waiting for someone, {STYLE_LLANERO}",
        "seed": 2003
    },
    "08_flashback_estrellas": {
        "prompt": f"Wide cinematic shot of a beautiful woman silhouette walking alone under a spectacular starry night sky, the Milky Way visible above, her hair blowing in the wind, dreamy romantic atmosphere, soft blue moonlight and golden starlight, magical fantasy flashback moment, {STYLE_LLANERO}",
        "seed": 2008
    },
    "09_huellas_arena": {
        "prompt": f"Extreme close-up of bare feet walking on soft golden sand leaving beautiful footprints, warm sunset light casting long shadows, each footprint clearly visible, poetic and romantic detail shot, shallow depth of field, golden hour tones, {STYLE_LLANERO}",
        "seed": 2009
    },
    "15_esposa_entra": {
        "prompt": f"Cinematic slow motion shot of {ESPOSA} walking gracefully into the shoe store, golden warm light surrounding her like an angel, her hair and dress flowing as if in slow motion, her confident smile, she walks directly toward {ANDRE} who is standing up to greet her, dreamy romantic atmosphere, {STYLE_LLANERO}",
        "seed": 2015
    },
    "16_juntos_sillon": {
        "prompt": f"Medium romantic shot of {ANDRE} and {ESPOSA} sitting together on the luxurious armchair in the shoe store, his arm around her waist, she leans into him, they look into each other eyes and smile lovingly, warm golden light wrapping around them, romantic and tender moment, {STYLE_LLANERO}",
        "seed": 2016
    },
    "17_pone_zapato": {
        "prompt": f"Cinematic close-up of {ANDRE} kneeling on one knee in front of {ESPOSA} in the shoe store, he is gently putting a beautiful high heel shoe on her foot, she looks down at him with love and admiration in her eyes, warm golden light illuminating the moment, romantic gesture, his hands carefully adjusting the shoe on her foot, {STYLE_LLANERO}",
        "seed": 2017
    },
    "18_beso": {
        "prompt": f"Romantic close-up of {ANDRE} and {ESPOSA} sharing a tender kiss in the shoe store, his hand gently holding her face, her hand on his chest, warm golden light creating a beautiful glow around them, surrounded by shoes in soft focus background, intimate and loving moment, {STYLE_LLANERO}",
        "seed": 2018
    }
}

for key, data in MISSING.items():
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
for f in files:
    print(f"  {f}")
