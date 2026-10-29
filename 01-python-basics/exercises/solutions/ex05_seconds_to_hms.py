"""Convert a number of seconds into hours, minutes and seconds."""

total_seconds = int(input("Seconds: "))

hours = total_seconds // 3600          # whole hours
remaining = total_seconds % 3600       # what is left after the hours
minutes = remaining // 60
seconds = remaining % 60

print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")
