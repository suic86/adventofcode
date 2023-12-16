from dataclasses import dataclass, field
from itertools import chain


@dataclass(unsafe_hash=True)
class Ray:
    position: tuple[int, int]
    direction: tuple[int, int]

    def advance(self) -> None:
        self.position = (
            self.position[0] + self.direction[0],
            self.position[1] + self.direction[1],
        )


@dataclass
class Layout:
    height: int = 0
    width: int = 0
    objects: dict[tuple[int, int], str] = field(default_factory=dict)


def ray_in_layout(ray: Ray, layout: Layout) -> bool:
    return 0 <= ray.position[0] < layout.height and 0 <= ray.position[1] < layout.width


def show_layout(layout: Layout) -> str:
    data = [["." for _ in range(layout.width)] for _ in range(layout.height)]
    for (y, x), o in layout.objects.items():
        data[y][x] = o
    return "\n".join(map("".join, data))


def parse_data(path: str = "input.data") -> Layout:
    layout = Layout()
    with open(path) as fobj:
        x = y = 0
        for y, r in enumerate(map(str.strip, fobj)):
            for x, c in enumerate(r):
                if c in "\\/-|":
                    layout.objects[(y, x)] = c
        layout.height = y + 1
        layout.width = x + 1
    return layout


def trace_ray(layout: Layout, ray: Ray) -> int:
    rays = [ray]
    traced = set()
    visited = set()
    while rays:
        ray = rays.pop()
        traced.add((ray.position, ray.direction))
        while ray_in_layout(ray, layout):
            visited.add(ray.position)

            if ray.position not in layout.objects:
                ray.advance()
                continue

            obj = layout.objects[ray.position]
            dy, dx = ray.direction

            if obj == "/":
                ray.direction = (-dx, -dy)
            elif obj == "\\":
                ray.direction = (dx, dy)
            elif obj == "|" and dx:
                ray.direction = (dx, dy)
                split_ray = Ray(ray.position, (-dx, dy))
                split_ray.advance()
                if (split_ray.position, split_ray.direction) not in traced:
                    rays.append(split_ray)
            elif obj == "-" and dy:
                ray.direction = (dx, dy)
                split_ray = Ray(ray.position, (dx, -dy))
                split_ray.advance()
                if (split_ray.position, split_ray.direction) not in traced:
                    rays.append(split_ray)
            ray.advance()
    return len(visited)


def solution_01(path: str = "input.data") -> int:
    return trace_ray(parse_data(path), Ray((0, 0), (0, 1)))


def solution_02(path: str = "input.data") -> int:
    layout = parse_data(path)
    h = layout.height
    w = layout.width

    return max(
        trace_ray(layout, ray)
        for ray in chain(
            # top row (heading downward)
            (Ray((0, i), (1, 0)) for i in range(w)),
            # bottom row (heading upward)
            (Ray((h - 1, i), (-1, 0)) for i in range(w)),
            # leftmost column (heading right)
            (Ray((i, 0), (0, 1)) for i in range(h)),
            # any tile in the rightmost column (heading left)
            (Ray((i, w - 1), (0, -1)) for i in range(h)),
        )
    )


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
