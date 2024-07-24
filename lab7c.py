#!/usr/bin/env python4
class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Change the time object by adding or subtracting seconds."""
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

def time_to_sec(time):
    """Convert a time object to seconds since midnight."""
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    """Convert seconds since midnight to a time object."""
    time = Time()
    time.hour = seconds // 3600
    seconds %= 3600
    time.minute = seconds // 60
    time.second = seconds % 60
    return time

