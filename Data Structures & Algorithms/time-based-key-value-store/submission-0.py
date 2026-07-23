class TimeMap:

    def __init__(self):
        self.timeMap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append( (value,timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap[key]
        l, r=0,len(arr)-1
        while l<=r:
            m=r+(l-r)//2
            if int(arr[m][1])==timestamp:
                return arr[m][0]
            elif int(arr[m][1])>timestamp:
                r=m-1
            else:
                l=m+1
        if key in self.timeMap:return arr[r][0]
        return ""
    
