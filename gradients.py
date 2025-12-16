def generate_gradient(c1, c2, steps=10):
    gradient = []
    for i in range(steps):
        rgb = tuple(
            int(c1[j] + (c2[j] - c1[j]) * i / (steps - 1))
            for j in range(3)
        )
        gradient.append(rgb)
    return gradient
