import click
import threading
from pynput.keyboard import Controller, Key, Listener
import main_executor

@click.command()
@click.option('--file_path', 
    type=click.Path(exists=True),
    required=True,
    help="Entry a path of existing file to load.\nFor example: my_folder\open_browser.json.\nRemember that name file have to end with .json extension")
@click.option('--work_in_loop',
    is_flag=True, 
    default=False, 
    help="If you enter '--work_in_loop' recording from the selected file will be reapeted until you cancel it pressing F10.")
def main(file_path, work_in_loop):
    """
    Handles executor of mouse and keyboard work, saved in json file. Supports loop mode or in single mode.
    """
    while work_in_loop:
        if not stopped:
            main_executor.main(file_path)
        else: 
            break
    else:
        keyboard = Controller()
        main_executor.main(file_path)
        keyboard.press(Key.f10)
def on_press(key):
    """Detect keys to start and finish program. Creating a new thread to allow execute function main

    Args:
        key (keyboard.Key): pressed key on keyboard

    Returns:
        bool: Pressed F10 button force to return False and finish program work.
    """    
    global stopped
    global thread
    if key == Key.f9:
        stopped = False
        if thread is None:
            thread = threading.Thread(target=main)
            thread.start()
    if key == Key.f10:
        stopped = True
        return False
        
if __name__ == '__main__':
    paused = True
    thread = None
    with Listener(
        on_press=on_press) as listener:
        print("Press 'F9' to start executing or if you type '--help' to see helper.\nPress 'F10' if you want exit or stop executing in '--work_in_loop' mode.")
        listener.join()