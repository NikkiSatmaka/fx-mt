import pandas as pd
import shutil
import sys

import MetaTrader5 as mt5

from datetime import datetime
from pathlib import Path


# mt5 directory
mt5dir = 'C:/Program Files/MetaTrader 5 IC Markets (SC) - 1'
# mt5dir = 'C:/Program Files/Pepperstone MetaTrader 5'
mt5loc = Path(mt5dir) / 'terminal64.exe'

    
# connect to MetaTrader 5
if not mt5.initialize(str(mt5loc)):
    print("initialize() failed")
    mt5.shutdown()

# Print connection status
print(
    f'Connected to {mt5.terminal_info().name}',
    f'at {mt5.terminal_info().path}',
    f'with server {mt5.account_info().server}'
)

