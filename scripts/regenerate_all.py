import requests
import os
import urllib.parse
import time

OUTPUT_DIR = r"E:\videoclip-project\storyboard\imagenes"

# Perfiles corregidos
ANDRE = "a 40 year old latin man with mature face, slight stubble beard, warm brown skin, dark hair with touches of gray at temples, confident mature expression, fit build, wearing elegant casual button-up shirt sleeves rolled up, dark jeans, leather shoes"
ESPOSA = "a 35 year old latin woman with elegant mature beauty, warm brown skin, long dark wavy hair, confident graceful posture, wearing a beautiful flowing dress, high heels, natural makeup, radiant smile"
MUJER = "a young attractive latin woman in her 20s, flirtatious, trendy clothes"

STYLE = "photorealistic digital painting, warm cinematic lighting, golden hour tones, Venezuelan llanero aesthetic, professional cinematography, sharp facial details, beautiful bokeh, warm orange gold color grading, 8k quality, music video still, realistic human faces"

# Imágenes a regenerar con prompts corregidos
SCENES = {
    "01_zapateria": {
        "prompt": f"Wide establishing shot of an elegant modern shoe store interior at dusk, warm golden light through large windows, beautiful leather shoes on illuminated display shelves, a very large luxurious upholstered bench in the center that can seat 6 to 7 people, polished marble floor, empty quiet atmosphere, {STYLE}",
        "seed": 4001
    },
    "02_andre_entra": {
        "prompt": f"Full body shot of {ANDRE} walking through the glass door of an elegant shoe store, confident mature stride, looking around at beautiful shoes, warm golden evening light, his shadow behind him, cinematic entrance, {STYLE}",
        "seed": 4002
    },
    "03_andre_sienta": {
        "prompt": f"Medium shot of {ANDRE} sitting in the exact center of a very large luxurious upholstered bench in an elegant shoe store, the bench is wide enough for 6-7 people, he sits in the middle with space on both sides, relaxed confident pose arms spread along backrest, surrounded by shoes on shelves, warm golden light, he waits patiently, {STYLE}",
        "seed": 4003
    },
    "04_mujer1_llega": {
        "prompt": f"Medium shot of {MUJER} sitting down next to {ANDRE} on the large bench in the shoe store, she deliberately struggles to remove her high heel, leaning her body toward him flirtatiously, he smiles politely but is not interested, warm lighting, {STYLE}",
        "seed": 4004
    },
    "05_mujer2_cabello": {
        "prompt": f"Close-up of {MUJER} running her fingers through {ANDRE} hair in the shoe store, she is very close to his face, flirtatious expression, her other hand on his shoulder, he smiles politely but looks away, warm golden light, {STYLE}",
        "seed": 4005
    },
    "06_mujer3_pasa": {
        "prompt": f"Full body shot of {MUJER} walking slowly and provocatively past {ANDRE} seated on the large bench in the shoe store, she looks back over her shoulder seductively, he watches her pass with slight smile, warm lighting, {STYLE}",
        "seed": 4006
    },
    "07_andre_canta": {
        "prompt": f"Medium shot of {ANDRE} standing in the shoe store singing passionately, mouth open mid-song, hand gesturing, surrounded by shoes and boxes, warm golden spotlight, musical performance energy, emotional face, {STYLE}",
        "seed": 4007
    },
    "10_mujeres_rodean": {
        "prompt": f"Wide shot of {ANDRE} sitting in the center of the large bench in the shoe store, surrounded by 6 beautiful women all sitting around him on the bench, each in different flirtatious poses, touching his shoulders, leaning on him, he looks toward the door waiting, crowded composition, warm lighting, {STYLE}",
        "seed": 4010
    },
    "13_andre_espera": {
        "prompt": f"Medium shot of {ANDRE} sitting on the large bench in the shoe store, looking toward the glass door with anticipation in his eyes, women visible in background but he ignores them, his face shows he waits for someone specific, warm lighting, emotional, {STYLE}",
        "seed": 4013
    },
    "14_puerta_dorada": {
        "prompt": f"Dramatic silhouette of {ESPOSA} standing in the doorway of the shoe store, golden sunset light streaming from behind creating beautiful halo around her hair, figure backlit, she has arrived, cinematic dramatic entrance, warm golden rays, {STYLE}",
        "seed": 4014
    },
    "15_esposa_entra": {
        "prompt": f"Cinematic slow motion shot of {ESPOSA} walking gracefully into the shoe store, golden warm light surrounding her, hair and dress flowing in slow motion, confident smile, she walks toward {ANDRE} who stands to greet her, dreamy romantic atmosphere, {STYLE}",
        "seed": 4015
    },
    "16_juntos_sillon": {
        "prompt": f"Medium romantic shot of {ANDRE} and {ESPOSA} sitting together on the large luxurious bench in the shoe store, his arm around her waist, she leans into him, they look into each other eyes smiling lovingly, warm golden light, romantic tender moment, {STYLE}",
        "seed": 4016
    },
    "17_pone_zapato": {
        "prompt": f"Cinematic close-up of {ANDRE} kneeling on one knee in front of {ESPOSA} in the shoe store, gently putting a beautiful high heel shoe on her foot, she looks down at him with love, warm golden light, romantic gesture, his hands carefully adjusting the shoe, {STYLE}",
        "seed": 4017
    },
    "18_beso": {
        "prompt": f"Romantic close-up of {ANDRE} and {ESPOSA} sharing a tender kiss in the shoe store, his hand gently holding her face, her hand on his chest, warm golden light creating beautiful glow, shoes in soft focus background, intimate loving moment, {STYLE}",
        "seed": 4018
    },
    "19_mujeres_reaccion": {
        "prompt": f"Medium shot of group of women in the shoe store looking at {ANDRE} and {ESPOSA} together, expressions of disappointment, one rolling eyes, another checking phone, whispering to friend, they realize he is married, warm lighting, {STYLE}",
        "seed": 4019
    },
    "20_mujeres_salen": {
        "prompt": f"Wide shot of women walking out of the shoe store one by one through glass door, looking back with disappointment, couple visible in background sitting together, women leaving one after another, warm evening light, {STYLE}",
        "seed": 4020
    },
    "21_final_juntos": {
        "prompt": f"Wide romantic final shot of {ANDRE} and {ESPOSA} sitting together on the large bench in empty shoe store, his arm around her, her head on his shoulder, peaceful and happy, warm golden light fading to soft dusk, beautiful ending, {STYLE}",
        "seed": 4021
    }
}

total = len(SCENES)
for i, (key, data) in enumerate(SCENES.items(), 1):
    filename = f"{key}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    print(f"[{i:02d}/{total}] {filename} - Generating...")
    
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
files = sorted(os.listdir(OUTPUT_DIR))
print(f"Total: {len(files)} images")
