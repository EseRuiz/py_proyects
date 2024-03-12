class SpaceAge:

    seconds = 0.0

    def __init__(self, seconds):
        self.seconds = seconds

    def get_seconds(self):
        return round(self.seconds,2)
    
    def on_earth(self):
        return round(self.seconds/ 31557600.0,2)
    
    def on_mercury(self):
        mercuryOrbitalPeriod = 0.2408467 * 31557600.0
        return round(self.seconds / mercuryOrbitalPeriod,2)
    
    def on_venus(self):
        venusOrbitalPeriod = 0.61519726 * 31557600.0
        return round(self.seconds / venusOrbitalPeriod,2)
    
    def on_mars(self):
        marsOrbitalPeriod = 1.8808158 * 31557600.0
        return round(self.seconds / marsOrbitalPeriod,2)
    
    def on_jupiter(self):
        jupOrbitalPeriod = 11.862615 * 31557600.0
        return round(self.seconds / jupOrbitalPeriod,2)
    
    def on_saturn(self):
        saturOrbitalPeriod = 29.447498 * 31557600.0
        return round(self.seconds / saturOrbitalPeriod,2)
    
    def on_uranus(self):
        urOrbitalPeriod = 84.016846 * 31557600.0
        return round(self.seconds / urOrbitalPeriod,2)
    
    def on_neptune(self):
        nepOrbitalPeriod = 164.79132 * 31557600.0
        return round(self.seconds / nepOrbitalPeriod,2)