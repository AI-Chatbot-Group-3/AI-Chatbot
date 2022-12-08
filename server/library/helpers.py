import copy

STATE_DEFAULT = {"state": "start", "order": []}


def new_state():
    state = copy.deepcopy(STATE_DEFAULT)
    return state
