import json


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    data = load_data('jsonbars.json')
    print('The biggest bar {0}'.format(get_biggest_bar(data)))
    print('The smallest bar {0}'.format(get_smallest_bar(data)))
    print('The closest bar {0}'.format(get_closest_bar(data)))
