class Canvas:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._field = self._create_canvas()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def _create_canvas(self):
        field = [[" "] * (self._width + 2) for _ in range(self._height + 2)]

        for i in range(self._height + 2):
            for j in range(self._width + 2):
                if (i == 0) or (i == self._height + 1):
                    field[i][j] = "-"
                elif (j == 0) or (j == self._width + 1):
                    field[i][j] = "|"

        return field

    def get_item(self, x, y):
        return self._field[y][x]

    def create_line(self, x1, y1, x2, y2):
        if y1 == y2:
            for i in range(x1, x2 + 1):
                self._field[y1][i] = "x"
        elif x1 == x2:
            for i in range(y1, y2 + 1):
                self._field[i][x1] = "x"

    def create_rectangle(self, x1, y1, x2, y2):
        self.create_line(x1, y1, x2, y1)
        self.create_line(x1, y2, x2, y2)
        self.create_line(x1, y1, x1, y2)
        self.create_line(x2, y1, x2, y2)

    def create_flood_fill(self, x, y, current_char, fill_char):
        if self._field[y][x] != current_char:
            return

        self._field[y][x] = fill_char
        self.create_flood_fill(x - 1, y, current_char, fill_char)
        self.create_flood_fill(x + 1, y, current_char, fill_char)
        self.create_flood_fill(x, y - 1, current_char, fill_char)
        self.create_flood_fill(x - 1, y + 1, current_char, fill_char)

        return

    def write_to_file(self, path_to):
        f = open(path_to, 'a')

        for i in range(self._height + 2):
            for j in range(self._width + 2):
                f.write(self._field[i][j])
            f.write('\n')

        f.close()


class DrawingTool:
    def choose_actions(self, path_from, path_to):
        with open(path_from, 'r') as f:
            while True:
                line = f.readline()
                if len(line) == 0:
                    break

                if line.startswith("C"):
                    self.draw_canvas(line, path_to)
                elif line.startswith("L"):
                    self.draw_line(line, path_to)
                elif line.startswith("R"):
                    self.draw_rectangle(line, path_to)
                elif line.startswith("B"):
                    self.draw_flood_fill(line, path_to)

    def draw_canvas(self, line, path_to):
        width, height = [int(s) for s in line.split() if s.isdigit()]

        self._canvas = Canvas(width, height)
        self._canvas.write_to_file(path_to)

    def draw_line(self, line, path_to):
        x1, y1, x2, y2 = [int(s) for s in line.split() if s.isdigit()]

        if not getattr(self, "_canvas", None):
            print(f"L {x1} {y1} {x2} {y2} : Can't draw a line without canvas.")
            return

        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
        else:
            print(f"L {x1} {y1} {x2} {y2} : Line must be horizontal or vertical.")
            return

        self._canvas.create_line(x1, y1, x2, y2)
        self._canvas.write_to_file(path_to)

    def draw_rectangle(self, line, path_to):
        x1, y1, x2, y2 = [int(s) for s in line.split() if s.isdigit()]

        if not getattr(self, "_canvas", None):
            print(f"R {x1} {y1} {x2} {y2} : Can't draw a rectangle without canvas.")
            return

        if x1 <= x2 and y1 <= y2:
            self._canvas.create_rectangle(x1, y1, x2, y2)
            self._canvas.write_to_file(path_to)
        else:
            print(f"R {x1} {y1} {x2} {y2} : Incorrect coordinates.")
            return

    def draw_flood_fill(self, line, path_to):
        line = line[2:]
        x, y, fill_char = [s for s in line.split()]
        x = int(x)
        y = int(y)

        if not getattr(self, "_canvas", None):
            print(f"B {x} {y} {fill_char} : Can't flood fill without canvas.")
            return

        current_char = self._canvas.get_item(x, y)

        if current_char == 'x':
            print(f"B {x} {y} {fill_char} : Can't flood fill on the border of the area.")
            return

        self._canvas.create_flood_fill(x, y, current_char, fill_char)
        self._canvas.write_to_file(path_to)