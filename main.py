# Have to add these 3 lines due to Module Not Found Error
import os
import sys
sys.path.append('src')


from textSummarizer.logging import logger

logger.info("Welcome to basic log")
