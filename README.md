# Wall-EEG
Mind-controlled bot! :D

## Progress:
- Studied LORETA source localization algorithm; found Python implementation we can use
   - R.D. Pascual-Marqui. Review of Methods for Solving the EEG Inverse Problem. International Journal of Bioelectromagnetism 1999, Volume 1, Number 1, pp:75-86.
      - http://www.uzh.ch/keyinst/NewLORETA/TechnicalDetails/TechnicalDetails.htm

- Studying research paper showing example of controlling robot with motor imagery
   - Will help us understand ML/statistical analysis techniques to capture motor imagery
   - Lafleur, K., Cassady, K., Doud, A., Shades, K., Rogin, E., & He, B. (2013). Quadcopter control in three-dimensional space using a noninvasive motor imagery-based brain–computer interface. Journal of Neural Engineering,10(4), 046003. doi:10.1088/1741-2560/10/4/046003
   - Yuan, H., Perdoni, C., & He, B. (2010). Relationship between speed and EEG activity during imagined and executed hand movements. Journal of Neural Engineering,7(2), 026001. doi:10.1088/1741-2560/7/2/026001
- Experimented with Emotiv, OpenBCI, and their softwares.
- Designing C testing tool to ‘feed’ test OpenBCI data to ttyUSB serial port
   - Goal: virtual OpenBCI for testing purposes
   - Idea: open USB serial port in a file descriptor; use dup2 to redirect another source of data to file descriptor
      - http://tldp.org/HOWTO/Serial-Programming-HOWTO/x115.html

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
