<p align="center">
  <img src="screenshots/icon.png" alt="icon" width="250px" /><br/>
</p>

# Flash Player

## Inspiration
Epilepsy is a chronic non-communicable disease of the brain that affects people of all ages. In 2019, the World Health Organization (WHO) reported that approximately 50 million people worldwide have epilepsy. This makes it the most common neurological disease globally, and unfortunately, there is no cure.
Triggers of epilepsy can occur from sleep deprivation, stress, flashing lights, and many other provocations. With thousands of tweets, posts and videos at our fingertips, for those with epilepsy, it is easier to land upon a video that contains a segment of flashing colours. 

## What it does
Flash Player is a chrome extension that prevents epileptic seizures by skipping parts of videos with flashing lights. 
Upon opening Flash Player on YouTube, users can scan videos for triggers of seizures. When reaching a segment with a trigger, Flash Player will skip to a non-trigger segment.

## How we built it
The chrome extension was built using Javascript, HTML, and CSS. The backend used a Flask server with a MongoDB database to interact with the Chrome extension. OpenCV and Numpy were used for the video analysis to determine what parts of the video have triggers.

## Challenges we ran into
- Setting up the chrome extension and understanding its ecosystem
- Implementing detection algorithm to prevent false positives without missing triggers
- Setting up the popup window

## Accomplishments that we're proud of
- Creating aesthetically pleasing and easy to use extension
- Using OpenCV and Numpy to perform calculations

## What we learned
- How to create a chrome extension and use chrome extensions API to interact with website content (play, pause videos)
- How to use OpenCV to modify images to optimize performance when performing video analysis
- How flashing lights can cause seizures in epileptic persons

## What's next for Flash Player
- Implement red saturation analysis in addition to luminosity 
- Increasing performance times to reduce time required 
- Improving accuracy of the algorithm by applying machine learning techniques
