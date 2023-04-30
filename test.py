
from plyer import notification

# Create the notification
notification_title = "My Notification Title"
notification_message = "This is the notification message."
notification_icon = r"/home/dananjaya_mudalige/Documents/projects/python_projects/dt_day_planner/images/notify-icon.png" #optional
notification_timeout = 5 # seconds
notification.notify(title=notification_title,
                     message=notification_message,
                     app_icon=notification_icon,
                     timeout=notification_timeout)

