import numpy as np
import cv2
from threading import Thread
from queue import Queue
import imutils
from imutils.video import FileVideoStream
import pprint
import time


filename = "Backend\pokemon.mp4"


def Y_to_lux(Y):
    return 413.435 * (0.002745*Y + 0.0189623)**2.2

def get_avg_diff(hist, N):
    quants = hist[0]
    vals = hist[1]

    # positive
    count = 0
    index = len(quants) - 1
    tot = 0

    while count < N and index >= 0:
        if count + quants[index] <= N:
            count += quants[index]
            tot += vals[index] * quants[index]
        else:
            diff = N - count
            count = N
            tot += vals[index] * diff
        index -= 1

    avgP = tot / count
    
    # negative 
    count = 0
    index = 0
    tot = 0

    while count < N and index < len(quants):
        if count + quants[index] <= N:
            count += quants[index]
            tot += vals[index] * quants[index]
        else:
            diff = N - count
            count = N
            tot += vals[index] * diff
        index += 1

    avgL = tot / count

    return avgP if abs(avgP) > abs(avgL) else avgL



def get_events(filename, fps=30, rad=2, senstivity=12):
    fvs = FileVideoStream(filename).start()
    first = True
    prev_lux = None
    prev_diff = 0
    accum = None
    frame_num = 0
    prev_event = -1
    events = []

    diffs = []

    while fvs.more():
        frame = fvs.read()
        frame_num += 1
        if frame is not None:
            frame = imutils.resize(frame, width=450)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if accum is None:
                accum = np.zeros(shape=frame.shape)

            lux = Y_to_lux(frame)
            if prev_lux is not None:
                diff = np.subtract(lux, prev_lux)
                if first:
                    first = False

                N = (frame.shape[0] * frame.shape[1]) // 3
                
                avg_diff = get_avg_diff(np.histogram(diff, bins=200), N)
                diffs.append(avg_diff)

                print(avg_diff)
                '''if avg_diff * prev_diff < 0:
                    avg_accum_diff = get_avg_diff(np.histogram(accum, bins=200), N)
                    if prev_event == -1:
                        prev_event = frame_num
                    else:
                        diff_frames = frame_num - prev_event
                        events.append((frame_num, diff_frames, avg_accum_diff))
                        accum = np.zeros(shape=frame.shape)

                else:
                    accum = np.add(accum, lux)
                
                prev_diff = avg_diff'''
                cv2.putText(frame, "Diff {}".format(avg_diff),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.imshow("Frame", frame)
                cv2.waitKey(1)
                time.sleep(0.3)


            prev_lux = lux

            

    return events
            

pprint.pprint(get_events(filename))