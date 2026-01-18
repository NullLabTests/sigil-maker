# sigil_maker.py
# Compatible with Gradio for web interface, but CLI runnable

from PIL import Image, ImageDraw
import random
import math
import sys

def generate_sigil(phrase):
    if not phrase or not phrase.strip():
        img = Image.new('RGB', (512, 512), color=(20, 20, 30))
        draw = ImageDraw.Draw(img)
        draw.text((100, 240), 'Enter a phrase!', fill=(180, 180, 255))
        return img

    cleaned = set(c.upper() for c in phrase if c.isalpha() and c.upper() not in 'AEIOU')
    consonants = ''.join(sorted(cleaned))
    
    if not consonants:
        img = Image.new('RGB', (512, 512), color=(20, 20, 30))
        draw = ImageDraw.Draw(img)
        draw.text((80, 240), 'No consonants found!', fill=(180, 180, 255))
        return img

    size = 512
    img = Image.new('RGB', (size, size), color=(10, 10, 25))
    draw = ImageDraw.Draw(img)
    
    center = size // 2
    radius = 200
    n = len(consonants)
    
    points = []
    for i, char in enumerate(consonants):
        angle = i * (360 / n) + random.uniform(-10, 10)
        r = radius + random.uniform(-30, 30)
        x = center + r * math.cos(math.radians(angle))
        y = center + r * math.sin(math.radians(angle))
        points.append((x, y))
        draw.text((x - 20, y - 25), char, fill=(200, 220, 255))
    
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        col = (
            random.randint(140, 255),
            random.randint(100, 220),
            random.randint(180, 255)
        )
        width = random.randint(4, 12)
        draw.line([p1, p2], fill=col, width=width)
        if random.random() > 0.5:
            mid_x = (p1[0] + p2[0]) / 2 + random.uniform(-70, 70)
            mid_y = (p1[1] + p2[1]) / 2 + random.uniform(-70, 70)
            bbox = (
                min(p1[0], p2[0], mid_x) - 40,
                min(p1[1], p2[1], mid_y) - 40,
                max(p1[0], p2[0], mid_x) + 40,
                max(p1[1], p2[1], mid_y) + 40
            )
            draw.arc(bbox, random.randint(0, 360), random.randint(0, 360), fill=col, width=3)
    
    draw.ellipse(
        (center - 240, center - 240, center + 240, center + 240),
        outline=(100, 100, 160),
        width=6
    )
    
    return img

if __name__ == '__main__':
    statement = sys.argv[1] if len(sys.argv) > 1 else "May all beings be at peace"
    img = generate_sigil(statement)
    img.save('sigil.png')
    print('Sigil saved to sigil.png')
