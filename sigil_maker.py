import matplotlib.pyplot as plt
import numpy as np
import sys
import random

def generate_sigil(statement):
    vowels = 'aeiouAEIOU'
    letters = ''.join([c.upper() for c in statement if c.isalpha() and c not in vowels])
    unique_letters = ''.join(dict.fromkeys(letters))
    
    n = len(unique_letters)
    if n == 0:
        print("No valid letters found.")
        return
    
    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
    radius = 1
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')
    
    circle = plt.Circle((0, 0), radius, fill=False, color='gray', alpha=0.3, linewidth=1)
    ax.add_artist(circle)
    
    for i, let in enumerate(unique_letters):
        offset = random.uniform(-0.05, 0.05)
        ax.text(x[i] + offset, y[i] + offset, let, fontsize=24, ha='center', va='center', fontweight='bold', color='black')
    
    for i in range(n):
        next_i = (i + 1) % n
        control_x = (x[i] + x[next_i]) / 2 + random.uniform(-0.2, 0.2)
        control_y = (y[i] + y[next_i]) / 2 + random.uniform(-0.2, 0.2)
        t = np.linspace(0, 1, 100)
        bez_x = (1 - t)**2 * x[i] + 2 * (1 - t) * t * control_x + t**2 * x[next_i]
        bez_y = (1 - t)**2 * y[i] + 2 * (1 - t) * t * control_y + t**2 * y[next_i]
        color = plt.cm.viridis(i / n)
        ax.plot(bez_x, bez_y, color=color, linewidth=2, alpha=0.8)
    
    for i in range(n):
        ax.plot([0, x[i]], [0, y[i]], color='gray', alpha=0.1, linewidth=0.5)
    
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.savefig('sigil.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    statement = sys.argv[1] if len(sys.argv) > 1 else "May all beings be at peace"
    generate_sigil(statement)
