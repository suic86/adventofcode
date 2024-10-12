#!/usr/bin/env python3


import logging
import pathlib
from datetime import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

ROOT = pathlib.Path(__file__).parent


def scaffold() -> None:
    date = datetime.now()
    day_dir = ROOT / str(date.year) / f"day_{date.day:02}"
    if day_dir.exists():
        logger.info(f"{day_dir} already exists.")
    else:
        logger.info(f"{day_dir} created.")
        day_dir.mkdir(parents=True)

    solution = day_dir / "solution.py"
    test = day_dir / "test_solution.py"

    if solution.exists():
        logger.info(f"{solution} already exists.")
    else:
        solution.touch()
        logger.info(f"{solution} created.")

    if test.exists():
        logger.info(f"{test} already exists.")
    else:
        test.touch()
        logger.info(f"{test} created.")


if __name__ == "__main__":
    scaffold()
