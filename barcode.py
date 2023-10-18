from typing import List

import cv2
import skia
import numpy as np


def compute_barcode_colors(video_path: str,
                           delta: int = 1000) -> List:
    """
    You need to complete this function to return the color bars for the video under scrutiny
    :param video_path: path to the video
    :param delta: time delta for a video in milliseconds
    :return: list of colors
    """
    colors = []
    frames = []  # > List to store the frames in delta time
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return []
    else:

        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            # Check if we have reached the end of the video
            if not ret:
                break

            # Convert frame to RGBA
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            presentation_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)

            # Check if delta time has passed
            if presentation_timestamp % delta == 0:
                # Get the average color of each frame period
                if frames:
                    # Get the average color of each frame in delta time
                    frames_sum = np.sum(frames, axis=0)
                    frames_avg = np.multiply(frames_sum, 1 / len(frames))

                    # Get the final average color
                    average_color = np.mean(frames_avg, axis=(0, 1)).astype(int)
                    average_color = average_color.tolist()  # > Converting from numpy array to list

                    # Append the average color to the list of colors
                    colors.append(average_color)

                frames = []

            frames.append(frame)

        cap.release()
        return colors


def write_barcode_image(colors: List, width: int = 500,
                        height: int = 300,
                        output_path: str = "output.png"):
    """
    Writes a barcode png image of the colors
    :param colors: List of colors
    :param width: width of the output image
    :param height: height of the output image
    :param output_path: path to the output image
    """
    surface = skia.Surface(width, height)

    with surface as canvas:

        x = 0                            # > Variable to keep track of the X position
        width_bar = width / len(colors)  # > Width of each bar

        # Iterate over the colors and draw a bar for each color
        for color in colors:
            # Define the bar area
            rect = skia.Rect(x, 0, x + width_bar, height)

            # Draw the bar using the colors of the actual frame
            paint = skia.Paint(
                Color=skia.Color(color[0], color[1], color[2]),
                Style=skia.Paint.kFill_Style)
            canvas.drawRect(rect, paint)

            # Update the X position
            x += width_bar

    image = surface.makeImageSnapshot()
    image.save(output_path, skia.kPNG)


def main():
    video_path = 'assets/videos/1.mp4'

    colors = compute_barcode_colors(video_path)
    write_barcode_image(colors)


if __name__ == '__main__':
    main()
