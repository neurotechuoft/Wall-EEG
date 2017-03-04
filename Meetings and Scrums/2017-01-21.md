#WallEEG: Meeting

##Meeting Agenda

- 1:00--1:10: Welcome
- 1:10--1:20: Timeline Overview
- 1:20--1:30: Teams Overview
- 1:30--1:40: Plan Meeting Times
- 1:40--2:00: Decide first steps for each subdiscipline
- 2:00--2:40: Split into separate Hangouts chats
- 2:40--3:00: Recombine, summary, assign tasks

##Meeting Notes

- 1:00--1:10: Welcome
- 1:10--1:20: Timeline Overview
    - GOALS:
        - control land bot based on Emotiv
        - control land bot with custom software
    - Tick: Emotiv (2 months)
		- get bot to work based on Emotiv API
	- Tock: In-House Code (6 months)
		- Jan 20--Feb 20: control 1 motor based on alpha power
			- will take more time than previously thought
				- random bugs in hardware
		- Feb 20--March 20: control (hypothetical) land-based vehicle based on alpha power
			- just code the software for control
		- (will look at the rest later)
		- (June 10--September 30: control aerial based vehicle based on motor thoughts)
    - August 1--September 1: Final touches
- 1:20--1:30: Teams Overview
    - Software Team
        - create main code based on ROSPy
        - allow for Emotiv to be plugged in
	- people:
		- Paul
	- progress:
		- Paul has 2 motors that can be controlled at will
			-NodeJS, Python
			- commands sent through internet
			- https://github.com/mullinat/NetworkedRobot2
    - Algorithms Team
        - design algs to pick up motor thoughts
	- people:
		- Romeo
		- Sayan
		- Alisa
	- first steps:
		- use SVM classifier to control motor using alpha power
		- then we can use SVM + FFT for motor thoughts
    - Hardware Team
        - build bot
	- people:
		- Albert
		- Oishe
	- Paul also has all the parts required for a drone
    - note: all 3 teams will have to work very closely with each other to ensure there isn't integration hell
- 1:30--1:40: Plan Meeting Times
	- Saturdays 1--3pm in person at the Clubhouse
	- Algs team: Fridays 6--8pm
- 1:40--2:00: Decide first steps for each subdiscipline
	- first month: try to finish the land-based robot
		- emphasis on alg
- 2:00--2:10: Recombine, summary, assign tasks
	- Alisa: research "What area of the brain allows for directionality thoughts?"
	- Romeo, Sayan: research machine learning techniques with emphasis on reducing training time
