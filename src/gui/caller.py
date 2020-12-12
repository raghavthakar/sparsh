import yaml
import time

current_mode="bruh"
current_rate=23
with open('data/sparsh_state.yaml', 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    current_rate=(yaml_data[1]['rate'])
    current_mode=(yaml_data[0]['current_mode'])
    print(current_rate, current_mode)

while True:
    previous_mode=current_mode
    previous_rate=current_rate
    with open('data/sparsh_state.yaml', 'r') as yaml_file:
        time.sleep(0.1)
        yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        current_rate=(yaml_data[1]['rate'])
        current_mode=(yaml_data[0]['current_mode'])

    if current_rate != previous_rate:
        print(current_rate)

    if current_mode != previous_mode:
        print(current_mode)
