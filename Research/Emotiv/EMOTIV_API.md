Emotive SDK

**Integrating the Emotive SDK into an application**
- From here on, “Emotive EmoEngine” refers to an abstraction of the Emotive SDK functionality
- The Emotive EmoEngine receives preprocessed EEG and gyroscope data from the Emotive headset, does some post processing and translates this data into opaque data structures called EmoStates
- EmoState data structures are referenced through opaque event handles
  - They contain the current state of the Emotive headset’s readings.
  - Data structures and handles must be allocated and freed by calling *IEE_EmoEngineEventCreate()*  and *IEE_EmoEngineEventFree()* functions respectively
- Prior to calling any Emotive API Functions, application must call *IEE_EngineConnect()* function to establish communication with Emotive EPOC Headset (or *IEE_EngineRemoteConnect()* if connecting to the Xavier Composer, which listens on port 1726)
- Emotive EmoEngine publishes events which can be retrieved by calling *IEE_EngineGetNextEvent()*. Real time applications should poll for new EmoStates 10-15 times per second
- When application terminates, connection to EmoEngine must be closed by calling *IEE_EngineDisconnect()*

Source: http://emotiv.github.io/community-sdk/

Other things to look into:
 - Emotiv Xavier Composer: This functions as an emulator for the Emotiv EPOC headset that lets the user generate user-defined EmoStates that can be sent to an application. (https://emotiv.zendesk.com/hc/en-us/articles/201458205-Emotiv-Xavier-Tools-XavierComposer-usage)
