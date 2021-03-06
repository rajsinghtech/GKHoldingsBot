from sqlite3 import DatabaseError
import sys
from threading import local
sys.path.insert(0, 'Backend')
from Backend import DownloaderFunctions
from Backend import DatabaseFunctions
url = 'https://advisorshares.com/wp-content/uploads/csv/holdings/AdvisorShares_GK_Holdings_File.csv'
local_file = 'Backend/AdvisorShares_GK_Holdings_File.csv'
databaseFile = "Backend/HoldingsOverTime.db"

dStatus = DownloaderFunctions.downloadCSV(url)
if dStatus == 0:
    print("No Change to Database")
elif dStatus == 1:
    file = DownloaderFunctions.cleanupCSV(local_file)
    DatabaseFunctions.addToTableFromFile(databaseFile, file)
    DatabaseFunctions.removeDuplicates(databaseFile)
    print("Database Updated")






