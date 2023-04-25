import cv2
import os

def convert_video_to_frames(video_path, storage_path, end_time, fps, start_time="00:00:00"):
    # Convert start and end times to milliseconds
    try:
        start_ms = sum(x * int(t) for x, t in zip([3600000, 60000, 1000], start_time.split(":")))
        end_ms = sum(x * int(t) for x, t in zip([3600000, 60000, 1000], end_time.split(":")))
    except ValueError:
        print("Invalid time format. Time format should be 'hh:mm:ss'.")
        return
    
    # Create directory to store frames
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Check if video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file.")
        return

    # Get total video length in milliseconds
    total_ms = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps * 1000)

    # Convert total video length to hours, minutes, and seconds
    total_seconds = total_ms // 1000
    total_minutes, total_seconds = divmod(total_seconds, 60)
    total_hours, total_minutes = divmod(total_minutes, 60)

    # Print total video length in hours, minutes, and seconds
    print("Total video length: {:02d}:{:02d}:{:02d}".format(total_hours, total_minutes, total_seconds))

    # Set video position to start time
    cap.set(cv2.CAP_PROP_POS_MSEC, start_ms)

    # Read frames and save PNG files
    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Check if current frame time exceeds end time
        current_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
        if current_ms > end_ms:
            break

        # Save frame as PNG file
        filename = "frame_{}.png".format(frame_num)
        cv2.imwrite(os.path.join(storage_path, filename), frame)

        # Print progress
        print("Saved frame {} at {} ms".format(frame_num, current_ms))

        frame_num += 1

    # Release video file and close all windows
    cap.release()
    cv2.destroyAllWindows()
convert_video_to_frames("test.mp4","frames","00:00:05",1)
