import logging as logger
import sys
import warnings
import pandas as pd
import numpy as np
logger.basicConfig(format='%(asctime)s | %(module)s | %(lineno)s | %(threadName)s | %(levelname)s | %(message)s',
                   datefmt='%Y/%m/%d %H:%M:%S',
                   level=logger.INFO,
                   handlers=[logger.StreamHandler(sys.stdout),
                             logger.FileHandler('../data/logs/automatic_model_test.log')
                             ])


def main():
    # logger.captureWarnings(True)

    with warnings.catch_warnings(record=True) as w:
        # Pandas Warnings 'SettingWithCopyWarning'
        df = pd.DataFrame(np.random.choice(10, (3, 5)), columns=list('ABCDE'))
        df[df.A > 5]['B'] = 4
        logger.warning(str(w[0]))

        if issubclass(w[-1].category, pd.core.common.SettingWithCopyWarning):
            logger.warning(str(w[0]))
    print("Done!")


if __name__ == '__main__':
    main()