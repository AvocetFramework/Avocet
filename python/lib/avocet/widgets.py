# type: ignore
import avocet_core
from avocet.core import LayoutManager, EventDispatcher

class Widget:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.margin_x = 0
        self.margin_y = 0
        self.fill_x = False
        self.fill_y = False
        self.align = "left"
        self.absolute_x = 0
        self.absolute_y = 0
        self.visible = True
        self.events = EventDispatcher()

    def update(self, parent_x=0, parent_y=0, parent_w=80, parent_h=25):
        if not self.visible:
            return
        LayoutManager.compute_bounds(self, parent_x, parent_y, parent_w, parent_h)
        self.draw()

    def draw(self):
        pass

class Window(Widget):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height)
        self.title = title
        self.bg_color = bg_color
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def draw(self):
        avocet_core.draw_rect(self.absolute_x, self.absolute_y, self.width, self.height, self.bg_color)
        avocet_core.draw_rect(self.absolute_x, self.absolute_y, self.width, 1, 0x111111)
        
        for child in self.children:
            child.update(self.absolute_x, self.absolute_y + 1, self.width, self.height - 1)

class Label(Widget):
    def __init__(self, text, color=0xFFFFFF):
        super().__init__(len(text), 1)
        self.text = text
        self.color = color

    def draw(self):
        avocet_core.kprint(self.text)

class Button(Widget):
    def __init__(self, width, height, text, bg_color, fg_color):
        super().__init__(width, height)
        self.text = text
        self.bg_color = bg_color
        self.fg_color = fg_color

    def draw(self):
        avocet_core.draw_rect(self.absolute_x, self.absolute_y, self.width, self.height, self.bg_color)

class Toolbar(Widget):
    def __init__(self, width, height, bg_color):
        super().__init__(width, height)
        self.bg_color = bg_color

    def draw(self):
        avocet_core.draw_rect(self.absolute_x, self.absolute_y, self.width, self.height, self.bg_color)
