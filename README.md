# Mouse_keyboard_recorder
Aplication writen in Python. Using pynput library to monitoring and control input devices (mouse, keyboard).

Main concept:
Application detect events and moves which user made with mouse and keyboard and save all subsequent steps to a .json file.
Then user can run another a program to execute all saved events in selected .json file. Execution can be enabled in a loop mode or in a single mode.

Click package allowed to create command line interface to make easier use.

--------------------
RECORDING
To see a helper type to command line "python detect.py --help"
To turn on recording program type to a command line:
1. "python detect.py" - recorded steps will be saved in default.json file
2. "python detect.py --file_path 'here path of json file'" - example of valid path: my_folder\open_browser.json

Now the following menu will be displayed in the console:
"Press 'F9' to start recording or see helper if you enter '--help'.
Press 'F10' to stop recording.
Press 'F8' if you want restart during recording.
To work application properly display scaling have to be set to 100% in windows settings!"

After properly recording and saving successful completion message will appear.

-----------------
EXECUTING
To see a helper type to command line "python execute.py --help"
To turn on executing program type to a command line:
1. "python executet.py --file_path 'here path of json file'" - You must entry a path of existing json file to load. For example: my_folder\open_browser.json. Program will be executed once.
2. "python detect.py --file_path 'here path of json file' --work_in_loop" - If you enter '--work_in_loop' recording from the selected file will be reapeted until you cancel it manualy.

Now the following menu will be displayed in the console:
Press 'F9' to start executing or if you type '--help' to see helper.
Press 'F10' if you want exit or stop executing in '--work_in_loop' mode.
