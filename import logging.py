import logging

logger = logging.getLogger(__name__)


default_formatter = logging.Formatter(
    '%(asctime)s:[%(levelname)s]:%(name)s:%(message)s')

control = logging.getLogger('control')
control.setLevel(logging.INFO)
to_control_log_file_handler = logging.FileHandler('control.log')
to_control_log_file_handler.setFormatter(default_formatter)
control.addHandler(to_control_log_file_handler)

# now defense is a child of control
defense = logging.getLogger('control.defense')
defense.setLevel(logging.WARNING)
to_defense_log_file_handler = logging.FileHandler('defense.log')
to_defense_log_file_handler.setFormatter(default_formatter)
defense.addHandler(to_defense_log_file_handler)

control.info('No news, good news')
control.warning('Enemy, incoming')

defense.info('Cleaning out the enemy')
defense.warning('Running out of ammo')