import os
from dotenv import load_dotenv
import readline
import sys

# Load the environment variables from the .env file
load_dotenv()

import openai
import subprocess

# Get the API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_unix_commands(prompt):
    """
    Uses OpenAI GPT-3.5 to generate a list of Unix commands from a natural language prompt
    """
    prompt = f"Generate a command or series of commands that can be used in the Linux CLI to complete the following (DO NOT INCLUDE ANY DESCRIPTIVE TEXT OR EXPLANATIONS, ONLY PROVIDE THE LINUC CLI COMMANDS.  DO NOT INCLUDE 'in the current directory'.  THE COMMAND YOU PROVIDE MUST BE FUNCTIONAL EVEN IF THE CONTENT IS UNEXPECTED. PROVIDE NO CONTEXT): {prompt}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    command = response.choices[0].text.strip()
    commands = command.split("\n")
    return commands

def execute_command(command):
    """
    Executes a Unix command and returns the success state and output or error message
    """
    try:
        result = subprocess.run(
            command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output = result.stdout.decode("utf-8")
        return True, output
    except subprocess.CalledProcessError as e:
        error = e.stderr.decode("utf-8")
        return False, error
    except Exception as e:
        print(f"Command failed with error: {e}")
        return False, ""

# Check if the script was run with arguments
if len(sys.argv) > 1:
    # Combine the arguments into a single string
    user_input = " ".join(sys.argv[1:])
    # Use readline to allow arrow up functionality to access previous commands
    readline.add_history(user_input)
    # Check if the user input contains any text
    if user_input:
        prompt = user_input.strip()
        unix_commands = get_unix_commands(prompt)
        for command in unix_commands:
            # Print and execute the Unix command
            print(f"Attempting the following command: {command}")
            success, output = execute_command(command)
            if success:
                print(output)
            else:
                print(output)
else:
    # Prompt the user for input
    while True:
        user_input = input("Welcome to UnixGPT, what would you like me to do? ")
        # Use readline to allow arrow up functionality to access previous commands
        readline.add_history(user_input)
        # Check if the user input contains any text
        if user_input:
            prompt = user_input.strip()
            unix_commands = get_unix_commands(prompt)
            for command in unix_commands:
                # Print and execute the Unix command
                print(f"Attempting the following command: {command}")
                success, output = execute_command(command)
                if success:
                    print(output)
                else:
                    print(output)
        else:
            print("Invalid input, please provide a natural language statement")
