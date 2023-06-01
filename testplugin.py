from backend_core import Backend_core_module
import time
from plyer import notification

activity_list=Backend_core_module().today_activities_show()[0]
activity_list_select=activity_list[2:26]
local_hour=time.strftime("%-H:%M")
activity_notify_dict={}
for items in range(24):
    activity_notify_dict[f"{items}:00"]=activity_list_select[items]


if time.strftime("%Y-%m-%d",time.localtime())==activity_list[1]:
    if local_hour in activity_notify_dict:
        notification.notify(title=f"{local_hour} DT DAT PLANNER ACTIVITY NOTIFICATION ",message=f'{activity_notify_dict[local_hour]}')
else:
    notification.notify(title="NO ACTIVITY (dt day planner)",message="IIt seems like you haven't got any plans today!")        
