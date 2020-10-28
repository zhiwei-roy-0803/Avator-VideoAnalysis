import os
import sys
import time
from multiprocessing import Pool

this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_dir, ''))
sys.path.insert(0, os.path.join(this_dir, '../hysia'))
sys.path.insert(0, os.path.join(this_dir, '../third'))

from model_servers.detection_model_server import main as detection_server

# Time constant
_ONE_DAY_IN_SECONDS = 24 * 60 * 60

model_runners = [
    detection_server
]

if __name__ == "__main__":

    with Pool(processes=len(model_runners)) as pool:
        for runner in model_runners:
            pool.apply_async(runner)
        while True:
            try:
                time.sleep(_ONE_DAY_IN_SECONDS)
            except KeyboardInterrupt:
                logger.info("Shutting down model servers")
                pool.terminate()
                exit(0)