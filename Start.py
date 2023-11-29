import subprocess

def execute_script(script_name):
    try:
        subprocess.run(['python', script_name])
    except FileNotFoundError:
        print(f"Error: {script_name} not found.")

if __name__ == "__main__":
    message = """How would your represent your self as a 'RECIECVER' or 'SENDER'
     PRESS 1 FOR ---->  As a Sender
     else write anything for as a Reciever :-  """
    print(message)

    user_input = input(message)

    if user_input == '1':
        execute_script('Sender.py')

    else:
        execute_script('Reciever.py')