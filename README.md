## Examples
```bash
alex@laptop:~/english2bash$ ai make a commit with current working directory in a new branch, then move to where HEAD was before making the new commit
AI says:
(0): git checkout -b new_branch && git commit -m "Committing current working directory" && git checkout -
(1): git checkout -b new_branch && git commit -m "New commit with current working directory" && git checkout -
Execute (default git checkout -b new_branch && git commit -m "Committing current working directory" && git checkout -) [0/1]

AI> git checkout -b new_branch && git commit -m "Committing current working directory" && git checkout -
[new_branch 4f2fe1b] Committing current working directory
 1 file changed, 79 insertions(+)
 create mode 100755 openai_prompt.py


STDERR
Switched to a new branch 'new_branch'
Switched to branch 'master'

```


```bash
alex@laptop:~/english2bash$ ai show tree of all git branches and commits
AI says:
git log --all --graph --decorate --oneline
Execute? [Y/n]
AI> git log --all --graph --decorate --oneline
* 4f2fe1b (new_branch) Committing current working directory
* 8d9c3b1 (HEAD -> master) .
```


## Installation:
Get an OpenAI API key and put it in env variable `$OPENAI_API_KEY`. I have 
`export OPENAI_API_KEY="sk-<the key>"` in my `.bashrc`. Then run the `ai.py` script. 

## Prompt
Inspired by https://github.com/atinylittleshell/aicmd/blob/main/packages/web/utils/openai.ts

```
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
    {"role": "user", "content": USER_ARGS},
  ],
  temperature=0.2,
```
