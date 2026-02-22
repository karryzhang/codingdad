#!/usr/bin/env python3
import os, json, base64, pathlib, urllib.request, urllib.error, time, ssl

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise SystemExit("OPENAI_API_KEY is not set")

OUT_DIR = pathlib.Path("/Users/openclaw/.openclaw/workspace/codingdad/english/images/composition")
OUT_DIR.mkdir(parents=True, exist_ok=True)

items = [
    ("p4-1-helpful-rainy-day", "Primary school students at dismissal in heavy rain, one child shares umbrella with worried classmate, warm realistic illustration, Singapore neighborhood, natural colors, no text, no watermark"),
    ("p4-2-lost-and-found", "Primary school playground bench with a found wallet, child brings it to school general office and owner thanks them, realistic illustration, moral theme, no text, no watermark"),
    ("p4-3-library-manners", "Quiet school library scene, two pupils talking loudly, another pupil politely reminds them, then everyone reads calmly, realistic illustration, no text, no watermark"),
    ("p4-4-sportsmanship", "School field sports game, teammate falls and players argue, one child promotes fair play and game resumes, realistic illustration, dynamic but friendly, no text, no watermark"),
    ("p4-5-neighbourhood-cleanup", "Neighborhood clean-up event, kids and residents sorting litter, simple bin labels improve teamwork, realistic illustration, community spirit, no text, no watermark"),
    ("p5-1-group-project", "Primary 5 classroom group project near deadline, students blaming each other then reorganizing tasks and finishing in time, realistic illustration, no text, no watermark"),
    ("p5-2-online-kindness", "Student using tablet in class chat context, realizes hurtful comment and apologizes sincerely to classmate, realistic illustration, empathetic mood, no text, no watermark"),
    ("p5-3-honesty-test", "During a classroom test, student tempted to look at nearby answers but chooses integrity and works independently, realistic illustration, no text, no watermark"),
    ("p5-4-emergency-calm", "Home blackout at night, younger siblings panic, older child calmly uses flashlight and helps family cooperate, realistic illustration, no text, no watermark"),
    ("p5-5-new-student", "School recess scene, new student alone then invited into group, later smiling and confident with friends, realistic illustration, no text, no watermark"),
]

url = "https://api.openai.com/v1/images/generations"

for name, prompt in items:
    payload = {
        "model": "gpt-image-1",
        "prompt": prompt,
        "size": "1024x1024",
        "quality": "high",
        "output_format": "png"
    }

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Authorization", f"Bearer {API_KEY}")
    req.add_header("Content-Type", "application/json")

    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=180, context=ssl._create_unverified_context()) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            b64 = data["data"][0]["b64_json"]
            out_file = OUT_DIR / f"{name}.png"
            out_file.write_bytes(base64.b64decode(b64))
            print(f"OK {name} -> {out_file}")
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="ignore")
            print(f"HTTPError {name} attempt {attempt}: {e.code} {detail[:300]}")
            if attempt == 3:
                raise
            time.sleep(3 * attempt)
        except Exception as e:
            print(f"Error {name} attempt {attempt}: {e}")
            if attempt == 3:
                raise
            time.sleep(3 * attempt)

print("DONE")
