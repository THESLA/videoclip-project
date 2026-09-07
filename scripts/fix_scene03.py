import requests
import os
import urllib.parse

OUTPUT_DIR = r"E:\videoclip-project\storyboard\imagenes"

ANDRE = "a 40 year old latin man, mature handsome face, slight stubble, warm brown skin, confident expression, dark hair with some gray, fit build, wearing an elegant casual button-up shirt with sleeves rolled up, dark jeans, leather shoes"

STYLE_LLANERO = "photorealistic digital painting, warm cinematic lighting, golden hour tones, Venezuelan llanero aesthetic, professional cinematography look, sharp details, beautiful bokeh background, color grading warm orange and gold tones, 8k quality, professional music video still"

# Mueble grande tipo banca que sienta 6-7 personas
prompt = f"Medium shot of {ANDRE} sitting in the exact middle of a very large luxurious upholstered bench or long sofa in an elegant shoe store, the bench is big enough to seat 6 to 7 people, he sits in the center leaving space on both sides, relaxed confident pose with arms spread along the backrest, surrounded by beautiful shoes on illuminated shelves, warm golden lighting from above, he is waiting patiently, the large bench dominates the center of the store, {STYLE_LLANERO}"

encoded = urllib.parse.quote(prompt)
url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&seed=3003&model=flux"

print("Generating 03_andre_sienta.png with large bench...")
try:
    resp = requests.get(url, timeout=180)
    if resp.status_code == 200 and len(resp.content) > 1000:
        filepath = os.path.join(OUTPUT_DIR, "03_andre_sienta.png")
        with open(filepath, "wb") as f:
            f.write(resp.content)
        print(f"OK - {len(resp.content)} bytes")
    else:
        print(f"FAIL - HTTP {resp.status_code}")
except Exception as e:
    print(f"FAIL - {e}")
