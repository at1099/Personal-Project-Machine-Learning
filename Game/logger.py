import pandas as pd
import os

FILE_NAME = "level_scores.csv"

COLUMNS = [
    "num_obs",
    "avg_gap",
    "obs_height",
    "speed",
    "variance",
    "score",
    "completed"
]

def log_result(level, score, completed):
    row = {
        "num_obs": level.num_obs,
        "avg_gap": level.avg_gap,
        "obs_height": level.obs_height,
        "speed": level.speed,
        "variance": level.variance,
        "score": score,
        "completed": int(completed)
    }

    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row], columns=COLUMNS)

    df.to_csv(FILE_NAME, index=False)
