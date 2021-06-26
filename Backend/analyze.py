import numpy as np
import cv2
import imutils
from imutils.video import FileVideoStream
import pprint
import time
import matplotlib.pyplot as plt


filename = "Backend/videos/pokemon.mp4"


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
    
    plt.plot([i+1 for i in range(len(diffs))], diffs, 'ro')
    plt.plot([i+1 for i in range(len(diffs))], get_triggers(diffs), 'bo')
    plt.axis([0, 320, -200, 200])
    plt.ylabel('avg diffs')
    plt.show()

    
    

    """
    plt.plot([i+1 for i in range(len(diffs))], accums, 'ro')
    plt.axis([0, 500, -200, 200])
    plt.ylabel('avg accums')
    plt.show()
    """
    """
    rolling_avg = []
    for i in range(len(diffs) - 5):
        avg = sum([abs(j) for j in diffs[i:i+5]]) / 5
        std = np.std(diffs[i:i+5])
        
        rolling_avg.append(avg)

    plt.plot([i+1 for i in range(len(diffs)-5)], rolling_avg, 'ro')
    plt.axis([0, 320, -100, 100])
    plt.ylabel('avg diffs')
    plt.show()
    """
    
    return events

def get_triggers(diffs, fps=30, rad=10, senstivity=12, density=0.4):
    queue = [diffs[i] for i in range(rad)]
    out = [0 for i in range(len(diffs))]

    for i in range(rad, len(diffs)):
        queue.pop(0)
        queue.append(diffs[i])

        avg = sum(queue) / 10
        count = 0
        for val in queue:
            if abs(val) > senstivity:
                count += 1
        if count / rad > density:
            out[i] = 200

    i, j = 0, 0

    while i < len(out) - 1:
        if out[i]:
            count = 0
            j = i
            while j < len(out) and out[j]:
                count += 1
                j += 1
                
            if count < 15:
                for k in range(i, j):
                    out[k] = 0
            
            i = j + 1
        
        else:
            i += 1

    return out
        

            
get_events(filename)
#pprint.pprint(get_events(filename))