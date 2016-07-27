# Wall-EEG
Mind-controlled bot! :D
## OpenBCI Signal Acquisition
The original OpenBCI code uses a system of Yapsy plugins you can make to do what you want with the data it obtains. It used to have a command-line interface through which you could add plugins you wanted to use and run. We will keep the system of plugins to keep things modular (and not to break any of their code), but plugins can only be added and started/stopped by the main function itself.
### Plugins
The plugins are stored in the 'plugins' folder. Each plugin has two components: a Python script, and a Yapsy definition file. The definition file allows the Yapsy system to identify which programs are plugins and which aren't.
## Files
Code: Contains our code for the mind-controlled bot.
--OpenBCIPy: Code base for the bot
----user.py: Main script; syncs with OpenBCI and runs plugins that can do whatever you want them to do.
