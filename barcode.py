from typing import List

import cv2
import skia


def compute_barcode_colors(video_path: str,
                           delta: int = 1000) -> List:
    """
    You need to complete this function to return the color bars for the video under scrutiny
    :param video_path: path to the video
    :param delta: time delta for a video in milliseconds
    :return: list of colors
    """
    colors = []
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
        # TODO: modify to display bars like in the example
        rect = skia.Rect(100, 0, 200, 100)
        paint = skia.Paint(
            Color=skia.ColorBLUE,
            Style=skia.Paint.kFill_Style)
        canvas.drawRect(rect, paint)

    image = surface.makeImageSnapshot()
    image.save(output_path, skia.kPNG)


def main():
    video_path = 'assets/videos/1.mp4'

    colors = compute_barcode_colors(video_path)
    write_barcode_image(colors)


if __name__ == '__main__':
    main()

