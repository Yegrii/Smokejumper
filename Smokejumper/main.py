import fastf1
from matplotlib import pyplot as plt
import fastf1.plotting
cache_to_dir = '/Users/anastasiakuzmenko/Desktop/cachesF1/'
fastf1.Cache.enable_cache(cache_to_dir)
session = fastf1.get_session(2023, 1, 'R')
session.load()
schedule = fastf1.get_event_schedule(2023)
laps = session.laps
drivers = session.drivers


# print(session.date)
# # print(session.name)
# # print(session.event)
# print(schedule)
# print(session.results)
# print(session)
# print(laps)
# print(drivers)


best_bottas = session.laps.pick_driver('BOT').pick_fastest()
print(best_bottas['LapTime'])
lap_time = best_bottas['LapTime']


# Функция для форматирования времени
def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    d["milliseconds"] = tdelta.microseconds // 1000
    return fmt.format(**d)


formatted_time = strfdelta(lap_time, "{minutes:02d}:{seconds:02d}.{milliseconds:03d}")
print(formatted_time)
