# aimbot
Camera tracking program with 2 axis servo

Goals for this mini project:

	properly setting up of opencv (how hard can it be? xqcL)
	gitting used to git
	access the camera
	object detection (maybe with numpy, look into)
	manual control
	be able to recognize and track moving objects (don't know what i'm getting into here, but its the aim part of aimbot)
	recognize an object, store its location based on servo positions, and be able to move the camera to the recalled location
	gimbal-like stabilization (might be a stretch, only have two axis of movement)


Logs:

commit 1 12-7-2020:
ayy first commit
ok some notes:
Currently very vague pseudo-nonsense.
NEED to learn library functions for maestro servo controller and opencv
Probably gonna long term implement progressive tracking based on distance from blob to center of image feed.
Probably want to lean torwards slower tracking and keeping the object in frame, sort of like a gimbal, rather than trying 
to position the camera as quickly as possible to center that object on screen. 
