#!/usr/bin/env python3
import os, json, base64, pathlib, urllib.request, urllib.error, time, ssl

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise SystemExit("OPENAI_API_KEY is not set")

OUT_DIR = pathlib.Path("/Users/openclaw/.openclaw/workspace/codingdad/english/images/composition")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# PSLE-style: simple black and white line drawings, clear composition, minimal detail
items = [
    ("p4-1-helpful-rainy-day", "Simple black and white line drawing for PSLE exam: school gate with rain clouds, one student with umbrella looking at worried classmate without umbrella, minimal background detail, clear expressions, educational illustration style"),
    ("p4-2-lost-and-found", "Simple black and white line drawing for PSLE exam: playground bench with wallet on it, student examining wallet, student at school office with adult, minimal background, clear composition, educational illustration"),
    ("p4-3-library-manners", "Simple black and white line drawing for PSLE exam: library scene with bookshelves, student reading quietly, two students talking loudly, clear facial expressions, minimal detail, educational illustration style"),
    ("p4-4-sportsmanship", "Simple black and white line drawing for PSLE exam: sports field, player on ground, other players arguing, one student promoting fair play, clear body language, minimal background, educational illustration"),
    ("p4-5-neighbourhood-cleanup", "Simple black and white line drawing for PSLE exam: community clean-up scene with residents, mixed-up recycling bins, student making labels, clear problem-solving sequence, minimal detail, educational illustration"),
    ("p5-1-group-project", "Simple black and white line drawing for PSLE exam: classroom with students around table, project materials scattered, clock showing late time, students arguing then cooperating, clear expressions, educational illustration style"),
    ("p5-2-online-kindness", "Simple black and white line drawing for PSLE exam: student with tablet or phone showing chat screen, another student looking sad, then reconciliation scene, clear emotions, minimal background, educational illustration"),
    ("p5-3-honesty-test", "Simple black and white line drawing for PSLE exam: exam desk with test paper, pencil, visible answer sheet nearby, student's internal struggle shown through expression, choosing honesty, educational illustration style"),
    ("p5-4-emergency-calm", "Simple black and white line drawing for PSLE exam: home interior suddenly dark, younger siblings looking scared, older student with flashlight helping family stay calm, clear sequence, educational illustration"),
    ("p5-5-new-student", "Simple black and white line drawing for PSLE exam: school recess area, new student sitting alone, another student inviting them to join group, later scene showing friendship, clear emotional progression, educational illustration"),
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
            print(f"✓ {name}")
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="ignore")
            print(f"✗ {name} attempt {attempt}: {e.code}")
            if "billing" in detail.lower() or "quota" in detail.lower():
                print(f"  Billing limit hit: {detail[:200]}")
            if attempt == 3:
                raise
            time.sleep(3 * attempt)
        except Exception as e:
            print(f"✗ {name} attempt {attempt}: {e}")
            if attempt == 3:
                raise
            time.sleep(3 * attempt)

print("\n✅ All PSLE-style illustrations generated")
