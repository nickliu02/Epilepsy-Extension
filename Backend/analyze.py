import numpy as np
import cv2
import imutils
from imutils.video import FileVideoStream
import pprint
import time
import matplotlib.pyplot as plt


filename = "Backend/pokemon.mp4"


def Y_to_lux(Y):
    return 413.435 * (0.002745*Y + 0.0189623)**2.2

def get_avg_diff(hist, N, p=False):
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



def get_events(filename):
    fvs = FileVideoStream(filename).start()
    first = True
    prev_lux = None
    prev_diff = 0
    accum = None
    frame_num = 0
    prev_event = -1
    events = []

    luxes = []
    accums = []
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
            luxes.append(lux)

            if prev_lux is not None:
                diff = np.subtract(lux, prev_lux)
                if first:
                    first = False

                N = (frame.shape[0] * frame.shape[1]) // 4
                
                avg_diff = get_avg_diff(np.histogram(diff, bins=200), N)
                diffs.append(avg_diff)

                accum = np.add(accum, diff)
                avg_accum_diff = get_avg_diff(np.histogram(accum, bins=200), N, True)
                accums.append(avg_accum_diff)

                if avg_diff * prev_diff < 0:
                    avg_accum_diff = get_avg_diff(np.histogram(accum, bins=200), N, True)

                    

                    if prev_event == -1:
                        prev_event = frame_num
                    else:
                        diff_frames = frame_num - prev_event
                        events.append((frame_num, diff_frames, avg_accum_diff))
                        accum = np.zeros(shape=frame.shape)
                        prev_event = frame_num

                        #print(avg_accum_diff)
                
                prev_diff = avg_diff

                
                """
                cv2.imshow("Frame", frame)
                cv2.waitKey(1)
                time.sleep(0.3)
                """
                
                


            prev_lux = lux
    """
    plt.plot([i+1 for i in range(len(diffs))], diffs, 'ro')
    plt.axis([0, 500, -200, 200])
    plt.ylabel('avg diffs')
    plt.show()
    """

    """
    plt.plot([i+1 for i in range(len(diffs))], accums, 'ro')
    plt.axis([0, 500, -200, 200])
    plt.ylabel('avg accums')
    plt.show()
    """

    rolling_avg = []
    for i in range(len(diffs) - 5):
        rolling_avg.append(sum([abs(j) for j in diffs[i:i+5]])/5)

    plt.plot([i+1 for i in range(len(diffs)-5)], rolling_avg, 'ro')
    plt.axis([0, 320, 0, 100])
    plt.ylabel('avg diffs')
    plt.show()

    return events

def get_avg_and_sd(events, rad):
    pass

def get_triggers(events, fps=30, rad=5, senstivity=20):
    queue = []

    for i in range(rad):
        pass
        

            

pprint.pprint(get_events(filename))