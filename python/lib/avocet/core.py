# type: ignore
import avocet_core

class LayoutManager:
    @staticmethod
    def compute_bounds(widget, parent_x=0, parent_y=0, parent_w=80, parent_h=25):
        if widget.fill_x:
            widget.width = parent_w - (widget.margin_x * 2)
        if widget.fill_y:
            widget.height = parent_h - (widget.margin_y * 2)
            
        widget.absolute_x = parent_x + widget.margin_x
        widget.absolute_y = parent_y + widget.margin_y
        
        if widget.align == "center":
            widget.absolute_x = parent_x + (parent_w // 2) - (widget.width // 2)
        elif widget.align == "right":
            widget.absolute_x = parent_x + parent_w - widget.width - widget.margin_x

class EventDispatcher:
    def __init__(self):
        self.bindings = {}

    def bind(self, event_name, callback):
        if event_name not in self.bindings:
            self.bindings[event_name] = []
        self.bindings[event_name].append(callback)

    def dispatch(self, event_name, *args, **kwargs):
        if event_name in self.bindings:
            for callback in self.bindings[event_name]:
                callback(*args, **kwargs)
