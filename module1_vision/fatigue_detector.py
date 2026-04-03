import time

class FatigueDetector:
    def __init__(self):
        self.EAR_THRESHOLD = 0.2
        self.BLINK_COUNT = 0
        self.EYE_CLOSED_FRAMES = 0
        self.start_time = time.time()

    def update(self, ear):
        
        if ear < self.EAR_THRESHOLD:
            self.EYE_CLOSED_FRAMES += 1
        else:
            if self.EYE_CLOSED_FRAMES > 2:
                self.BLINK_COUNT += 1

            self.EYE_CLOSED_FRAMES = 0

        eye_closure_duration = self.EYE_CLOSED_FRAMES / 10

        elapsed_time = time.time() - self.start_time

        if elapsed_time == 0:
            blink_rate = 0
        else:
            blink_rate = self.BLINK_COUNT / (elapsed_time / 60)

        return {
            "blink_rate": round(blink_rate, 2),
            "eye_closure_duration": round(eye_closure_duration, 2)
        }