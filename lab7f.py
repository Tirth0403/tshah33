#!/usr/bin/env python3
# Student ID: Tirth Amitkumar Shah {175983212}

class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation for the object self."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object self."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Overload the '+' operator to add two Time objects."""
        return self.sum_times(t2)

    def sum_times(self, t2):
        """Add two time objects and return their sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def time_to_sec(self):
        """Convert a time object to a single integer representing the number of seconds from midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
           return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
           return False
        return True

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def format_time(time):
    """Format a time object as a string."""
    return f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'

# Example usage if needed
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    t2 = Time(1, 1, 1)
    print(t1.sum_times(t2))  # Using sum_times() directly
    print(t2.sum_times(t1))  # Using sum_times() directly
    print(t1 + t2)  # Using operator overloading with __add__()
    x = t1 + t2
    print(type(x))
    print(x)

