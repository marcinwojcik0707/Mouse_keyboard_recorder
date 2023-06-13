from pynput import mouse, keyboard
from time import sleep
import json

class Controller:
    """Controll mouse and keyboard
    """
    def __init__(self):
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
    def mouse_click(self, button):
        """Click a mouse button

        Args:
            button (mouse.Button): Button to click
        """
        self.mouse.click(button, 1)
        sleep(1)
    def mouse_position(self, x,y):
        """Positioning mouse

        Args:
            x (int): x coordinate of mouse
            y (int): y coordinate of mouse
        """
        self.mouse.position = (x, y)
        sleep(1)
    def mouse_scroll(self, dx, dy):
        """Scrolling mouse

        Args:
            dx (int): x direct of scrolling
            dy (int): y direct of scrolling
        """
        self.mouse.scroll(dx, dy)
    def mouse_press(self, button):
        """Press a mouse button

        Args:
            button (mouse.Button): button to press
        """
        self.mouse.press(button)
        sleep(1)
    def mouse_release(self, button):
        """Release a mouse button

        Args:
            button (mouse.Button): button to release
        """
        self.mouse.release(button)
        sleep(1)
    def keyboard_press_char(self, char):
        """Press a keyboard character

        Args:
            char (str): character to press
        """
        self.keyboard.press(char)
        sleep(0.1)
    def keyboard_press_special(self, special_key):
        """Press a keyboard special_key

        Args:
            special_key (keyboard.Key): special key to press
        """
        self.keyboard.press(special_key)
        sleep(0.1)
    def keyboard_release_char(self, char):
        """Release a keyboard character

        Args:
            char (str): character to release
        """
        self.keyboard.release(char)
        sleep(0.1)
    def keyboard_release_special(self, special_key):
        """Release a keyboard special key

        Args:
            special_key (keyboard.Key): special key to release
        """
        self.keyboard.release(special_key)
        sleep(0.1)

class Process:
    """Managing the process of performing the relevant tasks loaded from the selected json file
    """    
    def __init__(self, file_name, controller):
        """Constructs the necessary attributes for the process object.

        Args:
            file_name (str): Name of the json file which contains events to perform
            controller (Controller): Object of class Controller 
        """        
        self.file_name = file_name
        self.controller = controller
        self.steps = []
    def load_steps(self):
        """Open the json file and fill a list of steps to perform
        """        
        with open(self.file_name) as file:
            self.steps = json.load(file)
    def start(self):
        """Iterating over the list named 'steps' from which reads the name of the events
        and the arguments needed to call the functions.
        Using dictionary 'action mapper',
        calls the appropriate functions to perform mouse and keyboard actions.
        """        
        action_mapper = {
        'set_mouse_position': self.controller.mouse_position,
        'mouse_click': lambda button: self.controller.mouse_click((getattr(mouse.Button, button))),
        'mouse_scroll': self.controller.mouse_scroll,
        'mouse_press': lambda button: self.controller.mouse_press((getattr(mouse.Button, button))),
        'mouse_release': lambda button: self.controller.mouse_release((getattr(mouse.Button, button))),
        'keyboard_press_char': self.controller.keyboard_press_char,
        'keyboard_press_special': lambda key: self.controller.keyboard_press_special((getattr(keyboard.Key, key))),
        'keyboard_release_char': self.controller.keyboard_release_char,
        'keyboard_release_special': lambda key: self.controller.keyboard_release_special((getattr(keyboard.Key, key))),
        }
        for step in self.steps:
            function = action_mapper[step["eventType"]]
            function(*(step["payload"].values()))
   
def main(file_path):
    """Create objects form classes Controller and Process,
    load all steps from selected json file and execute all tasks.
    """
    controller = Controller()
    process = Process(file_path, controller)
    process.load_steps()
    process.start()
if __name__ == "__main__":
    main()
    
