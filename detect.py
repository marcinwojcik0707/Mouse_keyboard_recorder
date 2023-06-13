import click
from pynput import keyboard
import main_detector
def json_extension(ctx, param, value):
    """Validator for json extension.

    Args:
        value (str): entered file name

    Raises:
        click.BadParameter: Error whenincorrect extension

    Returns:
        _type_: Return file name if valid
    """    
    if not value.endswith('.json'):
        raise click.BadParameter('File have to end with .json extension.')
    return value

@click.command()
@click.option('--file_path', 
    type=click.Path(),
    callback = json_extension,
    default = 'default.json',
    help='Entry a path and name of file to save your recording.\nFor example: my_folder\open_browser.json.\nRemember that name file have to end with .json extension')
def main(file_path):
    """
    Launches mouse and keyboard detector. Saving detected events in selected json format file.
    """
    main_detector.main(file_path)
    click.echo('Recording saved successfully in file: '+ file_path)
    
def on_release(key):
    """Detect of turning on or turning off key pressed

    Args:
        key (keyboard.Key): released key on keyboard

    Returns:
        bool: Pressed F10 button force to return False and finish program work.
    """    
    if key == keyboard.Key.f9:
        main()
        return False
    elif key == keyboard.Key.f10:
        print('Start button didnt pressed.')
        return False
if __name__ == '__main__':
    with keyboard.Listener(
        on_press=on_release) as listener:
        print("""
        Press 'F9' to start recording or see helper if you enter '--help'.
        Press 'F10' to stop recording.
        Press 'F8' if you want restart during recording.
        To work application properly display scaling have to be set to 100% in windows settings!
        """)
        listener.join()