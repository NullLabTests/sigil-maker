# sigil_generator_fixed.py
# Tested compatible with Gradio 3.50.2 + FastAPI 0.111.0 + Pydantic 2.7.4

import gradio as gr
from PIL import Image, ImageDraw
import random
import math

def generate_sigil(phrase):
    if not phrase or not phrase.strip():
        # Empty input fallback
        img = Image.new('RGB', (512, 512), color=(20, 20, 30))
        draw = ImageDraw.Draw(img)
        draw.text((100, 240), "Enter a phrase!", fill=(180, 180, 255))
        return img

    # Step 1: uppercase, letters only, remove vowels, remove duplicates, sort
    cleaned = set(c.upper() for c in phrase if c.isalpha() and c.upper() not in 'AEIOU')
    consonants = ''.join(sorted(cleaned))
    
    if not consonants:
        img = Image.new('RGB', (512, 512), color=(20, 20, 30))
        draw = ImageDraw.Draw(img)
        draw.text((80, 240), "No consonants found!", fill=(180, 180, 255))
        return img

    # Canvas
    size = 512
    img = Image.new('RGB', (size, size), color=(10, 10, 25))
    draw = ImageDraw.Draw(img)
    
    center = size // 2
    radius = 200
    n = len(consonants)
    
    points = []
    for i, char in enumerate(consonants):
        # Circle placement + small random offset
        angle = i * (360 / n) + random.uniform(-10, 10)
        r = radius + random.uniform(-30, 30)
        x = center + r * math.cos(math.radians(angle))
        y = center + r * math.sin(math.radians(angle))
        points.append((x, y))
        
        # Draw letter (using default font, no external files needed)
        draw.text((x - 20, y - 25), char, fill=(200, 220, 255), font_size=48)
    
    # Connect letters with lines + random color/thickness
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
        
        # Random chance for a curve flourish
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
    
    # Outer circle seal
    draw.ellipse(
        (center - 240, center - 240, center + 240, center + 240),
        outline=(100, 100, 160),
        width=6
    )
    
    return img

# Gradio interface (no deprecated gr.inputs / gr.outputs)
demo = gr.Interface(
    fn=generate_sigil,
    inputs=gr.Textbox(
        lines=2,
        placeholder="I AM POWERFUL AND ABUNDANT",
        label="Your Statement of Intent"
    ),
    outputs=gr.Image(
        label="Your Sigil",
        type="pil"          # ← This fixes the error! Return PIL → display as PIL
    ),
    title="Simple Chaos Sigil Maker",
    description="Type desire → vowels removed → letters connected into glyph",
    theme="dark",
    live=False
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        # share=True   # Uncomment for temporary public link if needed
    )
