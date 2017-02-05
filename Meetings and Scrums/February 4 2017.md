Meeting Notes

Software Team:

Completed:
   - Converted majority of emostate_logger.py file from Python 2.7 to Python 3.0 syntax
     - This file will be added to Wall-EEG/Code/EmotiveSDK/
   - Successfully compiled and ran emostate_logger.py example on Windows using Python 3.5
   
Issues:
   - Discovered that examples found in \community-sdk-master\examples\Python use a mixture of Python 2.7 and Python 3.0 syntax, making them unrunnable on either Python versions without making changes first
   - emostate_logger.py was unable to connect to an instance of the Emotiv Xavier Composer running on computer
   
Next Steps:
   - Connect emostate_logger.py or any other example to the Emotiv EPOCH headset and see if we can get a stream of data
   - Connect an example to the Emotiv Xavier Composer and receive a stream data. (Try running one of the Emoscripts found in        community-sdk-master\tools\XavierComposer\SampleScripts from the Composer)
