# Software Engineer assistant - Barcode test

Thank you for applying to Ubisoft New Experiences team. An important early step in our interview process is a
take-home assignment. We feel like completing this assignment will give us a better chance to learn
about you than a traditional whiteboard session, and you’ll be better positioned to show your strengths.

The goal of this assignment is to understand your Python skills, what is your approach to dealing with
constraints and ambiguity of the real world, as well as introduce you to
the technical problems of game streaming. 

## Task
The test's objective is to create a "movie barcode" using a video. Videos are comprised of frames,
essentially images, typically displayed at a rate of 24 frames per second in the case of movies.
A movie barcode is essentially a graph where each stripe represents the average colors of the frames over a specified time interval, denoted as `delta`.

For instance, here's a movie barcode example generated from the video located at `assets/videos/1.mp4` with a `delta` of 1000 milliseconds:

![Barcode image](assets/images/1.png) 

Each stripe on this barcode corresponds to the average color values for one second of video footage. 
This averaging is performed separately for each component of the RGB color space.

![0_1000.png](assets%2Fimages%2F0_1000.png)
![4000_6000.png](assets%2Fimages%2F4000_6000.png)
 
Use `barcode.py` to get started. 

## Submission

Please use git and submit your solution with a link to a private repo on GitHub (also, add 
`louis-segretin-ubisoft` account as a collaborator to your repo).

Before sending an email with your submission, please take a minute and answer the following questions
adding answers to your project README file:
- How long did it take you to complete this assignment?
- What would you do, if you had more time?
- What is your feedback on the assignment?

We hope this task will be a flexible way to show your skills and you’ll enjoy it. There are no strict deadlines for completion, 
and we believe it should not take more than an hour and a half once your development environment is set up.

Good luck ! 
The New Experiences team @ Ubisoft