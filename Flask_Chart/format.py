# Example tuples
tuple1 = (datetime.datetime(2023, 10, 14, 0, 0), 36, 56, 44)
tuple2 = (datetime.datetime(2023, 10, 15, 0, 0), 42, 60, 48)
tuple3 = (datetime.datetime(2023, 10, 16, 0, 0), 38, 58, 46)

# Combine the tuples into a list
combined_list = []

# Add the tuples to the list
combined_list.extend([tuple1, tuple2, tuple3])

# Print the combined list
print(combined_list)
