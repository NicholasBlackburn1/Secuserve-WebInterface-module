'''
this class is going to be the data class for holding and or coverting all the data from the data base for the seen users into a list 

'''

from app.base import const 

class DateData:
    
    _monday: int
    _tuesday: int
    _wensday: int
    _thurday: int 
    _friday: int
    _saterday: int 
    _sunday: int 

    #! this is were all data from database info intaked and orginized based on day
    def __init__(self, monday: int, tuseday: int, wensday: int, thursday: int, 
    friday:int, saterday: int, sunday: int) -> int:

       self.setMonday(monday)
       self.setTuesday(tuseday)
       self.setWensday(wensday)
       self.setThrusday(thursday)
       self.setFriday(friday)
       self.setSaterday(saterday)
       self.setSunday(sunday)

    # sets mondays data
    def setMonday(self,monday) -> int:
        mon = monday

        if mon == "" or None:
            self._monday = 0
        
        if mon < 0:
            self._monday = 0
        else:
            self._monday = mon

    #sets tusedays data
    def setTuesday(self,tuesday)-> int:
        tues = tuesday

        if tues == "" or None:
            self._tuesday = 0
        
        if tues < 0:
            self._tuesday = 0

        else:
            self._tuesday = tues

    # sets wensday data
    def setWensday(self, wensday)-> int:
        wens = wensday

        if wens == "" or None:
            self._wensday = 0
        
        if wens < 0:
            self._wensday = 0

        else:
            self._wensday = wens



    # ssets thrusdays sdata s
    def setThrusday(self, thrusday)-> int:
        thrus = thrusday

        if thrus == "" or None:
            self._thurday = 0
        
        if thrus < 0:
            self._thurday = 0

        else:
            self._thurday = thrus



    def setFriday(self, friday)-> int:
        thrus = friday

        if thrus == "" or None:
            self._friday = 0
        
        if thrus < 0:
            self._friday = 0

        else:
            self._friday = thrus
        

    
    def setSaterday(self, saterday)-> int:
        thrus = saterday

        if thrus == "" or None:
            self._saterday = 0
        
        if thrus < 0:
            self._saterday = 0

        else:
            self._saterday = thrus


    def setSunday(self, sunday)-> int:
        thrus = sunday

        if thrus == "" or None:
            self._sunday = 0
        
        if thrus < 0:
            self._sunday = 0

        else:
            self._sunday = thrus
            
    def getModay(self)-> int:
        return self._monday

    def getTuesay(self)-> int:
        return self._tuesday

    def getWensday(self)-> int:
        return self._wensday

    def getThursday(self)-> int:
        return self._thurday

    def getFriday(self)-> int:
        return self._friday

    def getSaterday(self)-> int:
        return self._saterday

    def getSunday(self)-> int:
        return self._sunday


    def __repr__(self):
        return {'monday':self.getModay(), 'tuesday':self.getTuesay(), 'wensday':self.getWensday(),
        'thursday':self.getThursday(),'friday':self.getFriday(),'saterday':self.getSaterday(), 'sunday':self.getSunday()}


        


