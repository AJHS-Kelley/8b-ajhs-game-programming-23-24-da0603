# Python Performance monittoring Module by Damian Arnold, v0.0
import time

def execSpeed():
    startTime = time.time()
    return startTime
    
def execStop():
    stopTime = time.time()
    return stopTime

def execTime(startTime, stopTime):
    return f"Execution Time: {startTime - stopTime} seconds.\n"