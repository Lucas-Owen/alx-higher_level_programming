#!/usr/bin/python3
"""This is a script that adds saves all its arguments in a list
as a json object to a file add_item.json
"""


if __name__ == '__main__':
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    loaded = []
    try:
        loaded = load_from_json_file('add_item.json')
    except FileNotFoundError:
        pass
    loaded += [sys.argv[i] for i in range(1, len(sys.argv))]
    save_to_json_file(loaded, 'add_item.json')
