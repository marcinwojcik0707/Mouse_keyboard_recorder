from pynput import mouse, keyboard
import json
class Detector:
    """Detect and save mouse and keyboard actions made by user"""
    def __init__(self):       
        self.json_tab = [] # list of actions made by user
    def on_click(self, x, y, button, pressed):
        """Append mouse click action

        Args:
            x (int): x coordinate of mouse
            y (int): y coordinate of mouse
            button (mouse.Button): which button of mouse is clicked
            pressed (bool): if button is pressed or released
        """        
        step = {
            "eventType": "set_mouse_position",
            "payload": { "x": x, "y": y }
            }
        self.json_tab.append(step)
        if pressed:
            step = {
            "eventType": "mouse_press",
            "payload": { "button": str(button).split('.')[1] } 
            }
            self.json_tab.append(step)
        if not pressed:
            step = {
            "eventType": "mouse_release",
            "payload": { "button": str(button).split('.')[1] } 
            }
            self.json_tab.append(step)
    def on_scroll(self, x, y, dx, dy):
        """Append mouse scroll action

        Args:
            x (int): x coordinate of mouse
            y (int): y coordinate of mouse
            dx (int): x direct of scrolling
            dy (int): y direct of scrolling
        """
        step = {
            "eventType": "mouse_scroll",
            "payload": { "horizontal": dx, "vertical": dy }
            } 
        self.json_tab.append(step)
    def on_press(self, key):
        """Append keyboard press key action

        Args:
            key (keyboard.Key): pressed key on keyboard

        Returns:
            bool: If user press F10 key then detector will stop recording mouse and keyboard events
        """
        if key == keyboard.Key.f10:
            # Stop listener
            return False
        try:
            step = {
            "eventType": "keyboard_press_char",
            "payload": { "key": key.char } 
            }
            self.json_tab.append(step)
        except AttributeError:
            step = {
            "eventType": "keyboard_press_special",
            "payload": { "key": str(key).split('.')[1] } 
            }
            self.json_tab.append(step)
        
    def on_release(self, key):
        """Append keyboard release key action

        Args:
            key (keyboard.Key): released key on keyboard
        """     
        try:
            step = {
            "eventType": "keyboard_release_char",
            "payload": { "key": key.char } 
            }
            self.json_tab.append(step)
        except AttributeError:
            step = {
            "eventType": "keyboard_release_special",
            "payload": { "key": str(key).split('.')[1] } 
            }
            self.json_tab.append(step)
        if key == keyboard.Key.f8:
            self.json_tab.clear()
def main(file_path):
    detector = Detector()
    with mouse.Listener(
        on_click=detector.on_click,
        on_scroll=detector.on_scroll) as listener:
        with keyboard.Listener(
            on_press=detector.on_press,
            on_release=detector.on_release) as listener:
                listener.join()
    with open(file_path, 'w') as file: 
        json.dump(detector.json_tab[1:], file) # save the events stored in the list to a json file
