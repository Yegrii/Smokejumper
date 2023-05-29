import fastf1
from matplotlib import pyplot as plt
import fastf1.plotting
cache_to_dir = '/Users/anastasiakuzmenko/Desktop/cachesF1/'
fastf1.Cache.enable_cache(cache_to_dir)
session = fastf1.get_session(2023, 3, 'R')
print(session.date)
print(session.name)
print(session.event)

schedule = fastf1.get_event_schedule(2023)
print(schedule)

session.load()
print(session.results)
print(session)
