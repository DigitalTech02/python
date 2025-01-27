from datetime import datetime, timedelta

def time_difference(start: str, end: str) -> str:
    """
    Calculate the difference between two datetime strings.
    
    Parameters:
    - start: A string representing the start datetime in 'YYYY-MM-DD HH:MM:SS' format.
    - end: A string representing the end datetime in 'YYYY-MM-DD HH:MM:SS' format.
    
    Returns:
    - A string representing the time difference in days, hours, minutes, and seconds.
    """
    start_dt = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end_dt = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    delta = end_dt - start_dt
    
    days = delta.days
    seconds = delta.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# Example usage
start_time = "2023-10-01 12:00:00"
end_time = "2023-10-05 15:30:45"
result = time_difference(start_time, end_time)
print(result)  # Output: "4 days, 3 hours, 30 minutes, 45 seconds"
