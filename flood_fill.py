from collections import deque


def flood_fill(image, sr, sc, color):
    visited = set()
    q = deque()
    q.append((sr, sc))
    og_color = image[sr][sc]
    rows, cols = len(image), len(image[0])
    while q:
        r, c = q.pop()
        if (r, c) in visited or r >= rows or c >= cols or r < 0 or c < 0 or image[r][c] != og_color:
            continue
        else:
            visited.add((r, c))
            image[r][c] = color
            q.append((r + 1, c))
            q.append((r - 1, c))
            q.append((r, c + 1))
            q.append((r, c - 1))
    return image
