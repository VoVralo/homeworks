some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]


def check_data(some_data):
    if type(some_data) in [int, float] and item > 500:
        return True
    return False


filtered_names = list(filter(check_data, some_data))
print(filtered_names)
