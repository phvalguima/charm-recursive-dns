#!/usr/bin/env python3

import os
import sys

sys.path.append('hooks/')

from charmhelpers.core.hookenv import action_fail
from neutron_utils import (
    pause_unit_helper,
    resume_unit_helper,
    register_configs,
)


def pause(args):
    """Pause the Ceilometer services.
    @raises Exception should the service fail to stop.
    """
    pause_unit_helper(register_configs())


def resume(args):
    """Resume the Ceilometer services.
    @raises Exception should the service fail to start."""
    resume_unit_helper(register_configs())


# A dictionary of all the defined actions to callables (which take
# parsed arguments).
ACTIONS = {"pause": pause, "resume": resume}


def main(args):
    action_name = os.path.basename(args[0])
    try:
        action = ACTIONS[action_name]
    except KeyError:
        s = "Action {} undefined".format(action_name)
        action_fail(s)
        return s
    else:
        try:
            action(args)
        except Exception as e:
            action_fail("Action {} failed: {}".format(action_name, str(e)))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
