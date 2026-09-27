from collections import deque
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    (Path(r"C:/Users/jayme/AppData/Local/Temp/codex-clipboard-e1dc2c5d-205b-4a20-97ac-2300098ade8b.png"), "cheetos-cutout.png"),
    (Path(r"C:/Users/jayme/AppData/Local/Temp/codex-clipboard-c1528713-ba53-4dd7-ac8c-ca41b81a0711.png"), "chewy-granola-cutout.png"),
    (Path(r"C:/Users/jayme/AppData/Local/Temp/codex-clipboard-7c0f7fad-05eb-4a77-8e49-f49aeaeb0b82.png"), "kirkland-water-cutout.png"),
    (Path(r"C:/Users/jayme/AppData/Local/Temp/codex-clipboard-1ef33e36-714c-42ca-8d17-7df06388dbf0.png"), "haribo-cutout.png"),
    (Path(r"C:/Users/jayme/AppData/Local/Temp/codex-clipboard-be503f1a-979d-42ee-a7c3-8224ac094f6e.png"), "martinellis-cutout.png"),
]


def is_background(pixel):
    r, g, b, _ = pixel
    return min(r, g, b) > 236 and max(r, g, b) - min(r, g, b) < 14


def remove_white_background(source, destination):
    image = Image.open(source).convert("RGBA")
    pixels = image.load()
    width, height = image.size
    queue = deque()
    seen = set()

    for x in range(width):
        queue.extend(((x, 0), (x, height - 1)))
    for y in range(height):
        queue.extend(((0, y), (width - 1, y)))

    while queue:
        x, y = queue.popleft()
        if (x, y) in seen or not is_background(pixels[x, y]):
            continue
        seen.add((x, y))
        pixels[x, y] = (*pixels[x, y][:3], 0)
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height:
                queue.append((nx, ny))

    image.save(destination, "PNG")


output_dir = ROOT / "assets"
output_dir.mkdir(exist_ok=True)
for source, filename in SOURCES:
    remove_white_background(source, output_dir / filename)
