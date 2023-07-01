#! /usr/bin/python

import os
#print(os.getenv("OPENAI_API_KEY"))
import subprocess
import itertools
from colorama import Fore, Style
import sys

# import os
import openai
openai.organization = "org-JPRW7fWaBQsDo5ODvF0orcCs"
openai.api_key = os.getenv("OPENAI_API_KEY")

USER_ARGS = ' '.join(sys.argv[1:])
MODEL = "gpt-3.5-turbo"
FOR_REAL = True
if FOR_REAL:
    response = openai.ChatCompletion.create(
        model=MODEL,
            messages=[
                {"role": "system",
                 "content": "You are an ubuntu shell assistant. "
                 "You will be asked to generate shell commands and "
                 "short shell scripts. "
                 "You can only respond with a single-line shell command in "
                 "a single code block. " 
                 "Do not write anything outside of the code block.",
                 },
                {"role": "user",
                 "content": USER_ARGS},
            ],
            temperature=0.2,
            n=3
    )
    results = [choice['message']['content'] for choice in response.choices]
    results = list(set(results))
else:
    results = ['hej', 'ls -lt']

# No log-prob of results to rank them?

def call_and_print(cmd):
    print(Fore.RED + "AI>" + Fore.GREEN + f" {cmd}" + Style.RESET_ALL)
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr != '':
        print()
        print(Fore.RED + 'STDERR')
        print(Fore.YELLOW + res.stderr)
    if res.returncode != 0:
        print()
        print(Fore.RED + f'RETURN CODE: {res.returncode}' + Style.RESET_ALL)

USER_PROMPT_ONE = lambda res: \
f"""AI says:
{Fore.GREEN + res + Style.RESET_ALL}
Execute? [Y/n] """

def USER_PROMPT_MANY(res):
    lines = '\n'.join([f"({n}): {Fore.GREEN + r + Style.RESET_ALL}" for n, r in enumerate(res)])
    return \
f"""{Fore.WHITE}AI says:{Style.RESET_ALL}
{lines}
Execute (default {res[0]}) [{'/'.join(map(str,range(len(res))))}]
"""

match results:
    case [res]:
        x = input(USER_PROMPT_ONE(res))
        if x.lower().startswith('y') or x == '':
            call_and_print(res)
        else: print("Abort")
    case _:
        x = input(USER_PROMPT_MANY(results))
        if x == '': x = '0'
        if x.isnumeric() and (xi := int(x)) in range(len(results)):
            call_and_print(results[xi])
        else: print('Abort')
