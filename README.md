# Wall-EEG
Mind-controlled bot! :D
## OpenBCI Signal Acquisition
The original OpenBCI code uses a system of Yapsy plugins you can make to do what you want with the data it obtains. It used to have a command-line interface through which you could add plugins you wanted to use and run. We will keep the system of plugins to keep things modular (and not to break any of their code), but plugins can only be added and started/stopped by the main function itself.
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

## Code Structure
Code: Contains our code for the mind-controlled bot.
--OpenBCIPy: Code base for the bot
----user.py: Main script; syncs with OpenBCI and runs plugins that can do whatever you want them to do.
----machine-learning: Contains supervised machine learning classifier and a bunch of other code for a workshop done by BCIMontreal
----plugins: Contains plugins the main function can use. We want to use 'packets-to-csv' for data collection

