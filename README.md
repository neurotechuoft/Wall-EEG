# Wall-EEG
Mind-controlled bot! :D
## OpenBCI Signal Acquisition
The original OpenBCI code uses a system of Yapsy plugins you can make to do what you want with the data it obtains. It used to have a command-line interface through which you could add plugins you wanted to use and run. We will keep the system of plugins to keep things modular (and not to break any of their code), but plugins can only be added and started/stopped by the main function itself.
However, we had some problems with using certain packages in the plugins, so we made a plugin currently called 'packets-to-csv' that accepts an array of Biosignals objects and utilizes the Observable-Observer design pattern to update objects with data values from the OpenBCI in real time. (This is a very 'hacky' solution and needs to be fixed).
### Plugins
The plugins are stored in the 'plugins' folder. Each plugin has two components: a Python script (.py), and a Yapsy definition file(.yapsy-plugin). The definition file allows the Yapsy system to identify which programs are plugins and which aren't. This is what the Yapsy file looks like:

```
[Core]
Name = (name)
Module = (file name)

[Documentation]
Author = (authors go here)
Version = #.#
Description = (description)
```

### Data Sets
http://www.bbci.de/competition/iv/desc_1.html
This dataset contains motor imagery comparisons btn moving left hand, right hand, and foot.

## Code Structure
Code: Contains our code for the mind-controlled bot.

--OpenBCIPy: Code base for the bot

----main.py: Main script; syncs with OpenBCI and runs plugins that can do whatever you want them to do.

----machine-learning: Contains supervised machine learning classifier and a bunch of other code for a workshop done by BCIMontreal

----plugins: Contains plugins the main function can use. We want to use 'packets-to-csv' for data collection

## How Current Code Works
Let $ = ./Code/OpenBCIPy
### $/src/main.py
* contains main function for the code
* lines 212-288: setting up the OpenBCI
    * loads plugin list, hardware setup, etc
* lines 293-302: sets up view
    * sets up Kivy app to create a GUI
* lines 311-319: starts data collection from OpenBCI
    * done in a separate thread to allow for parallel use of the GUI while the program receives data packets from the OpenBCI
    * list of objects to pass along are added as an argument
        * the objects will receive a list of data every time data is received by the computer (at 256 Hz)
            * functions in the object will parse, process, etc the data

### $/src/biosignals/ECG.py
* contains an ECG object and functions to signal process data

### $/src/kivy_app.py
* controls GUI of app
