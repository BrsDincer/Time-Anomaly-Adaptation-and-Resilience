from util_main import CLASSINIT,PROCESS,NULL,ERROR,DOCUMENTATION,ErrorModule
import time

class DataCollector(object):
    def __init__(self)->CLASSINIT:
        self.data = []
    def __str__(self)->str:
        return "Data Collector Class - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default
    def __repr__(self)->DOCUMENTATION:
        return DataCollector.__doc__
    def CollectData(self,timeRate:int or float)->PROCESS:
        entry = {"time_rate":timeRate,"time":time.time()}
        self.data.append(entry)
    def AnalyzeData(self)->PROCESS:
        stateChanges = 0
        previousTimeRate = None
        for entry in self.data:
            if "time_rate" in entry:
                currentTimeRate = entry["time_rate"]
                if (previousTimeRate is not None) and (currentTimeRate != previousTimeRate):
                    stateChanges += 1
                else:
                    pass
                previousTimeRate = currentTimeRate
        totalTimePeriod = self.data[-1]["time"] - self.data[0]["time"] if self.data else 0
        changeFrequency = stateChanges/totalTimePeriod if totalTimePeriod > 0 else 0
        totalEntries = len(self.data)
        probabilityChange = stateChanges/totalEntries if totalEntries > 0 else 0
        return stateChanges,changeFrequency,probabilityChange
                