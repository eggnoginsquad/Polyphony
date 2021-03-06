# Polyphony
A more robust implementation of PluralKit that hooks into the PluralKit API

# How to Run
Create a `.env` file in the project root to set your environment variables. Polyphony takes all of it's configuration in the form of environment variables.

- `DEBUG` - Python Boolean, Activates Debug Mode
- `TOKEN` - Discord Bot Token
- `GUILD_ID` - Guild ID of server Polyphony is being used in
- `DATABASE_URI` - Location of the SQLite database ([See more info here](https://docs.python.org/3/library/sqlite3.html)) (default: (project root)/polyphony/polyphony.db)
- `MODERATOR_ROLES` - List of role names (default: [Moderator, Moderators])
- `INSTANCE_ADD_ROLE` - Comma-separated list (no spaces) of role names to automatically add to instance when started (default: [])
- `INSTANCE_REMOVE_ROLE` - Comma-separated list (no spaces) of role names to automatically remove from instance when started (default: [])
- `ALWAYS_SYNC_ROLES` - Comma-separated list (no spaces) of role names assigned to the main user that should always be synced to the member instance (default: [])
- `NEVER_SYNC_ROLES` - Comma-separated list (no spaces) of role names assigned to member instances that should never be synced to the main user
- `DISABLE_ROLESYNC_ROLES` - Comma-separated list (no spaces) of role names that disable rolesync (default: [])
- `DEFAULT_INSTANCE_PERMS` - The permissions to suggest from the invite link generated by the invite command. (default: none, does not create a role)
- `SUSPEND_ON_LEAVE` - **Not Implemented Yet** Suspends instances belonging to a user when that user leaves the server (default: True)
- `SUSPEND_INACTIVE_DAYS` - **Not Implemented Yet** Number of days required for an instance to be considered inactive and auto-suspend (default: 14)
- `LOGGING_CHANNEL_ID` - **Not Implemented Yet** Channel to log Polyphony events (message edits, deletes, user updates, and errors) to
- `COMMAND_PREFIX` - The prefix to be used in Discord to activate Polyphony commands (default: ;;)
- `ADMIN_LOGS_CHANNEL_ID` - Where to put warnings and other logging messages. Make sure it is somewhere you can see. (default: none)
- `DELETE_LOGS_CHANNEL_ID` - The channel ID where your server puts delete logs, the message ID needs to appear somewhere in the embed (default: 0)
- `DELETE_LOGS_USER_ID` - The user ID that posts the delete logs (default: 0)

This project was built on Python 3.8.2.

Dependency, testing, and build management is done using [Poetry](https://python-poetry.org/). Install Poetry on your system and then run `poetry install` in the project root.

> Pipenv will be deprecated

To run polyphony, use `poetry run polyphony`.

# Contributing
Help us build Polyphony!

## How to Contribute Code
1. Fork your own branch
2. Push your branch to GitHub
3. Create a *draft* pull request or create an issue from a project card (yes, do this before writing any code)
  > Make sure to thoroughly describe your goals/changes/additions
  >
  > Check projects to see if someone is already working on that feature
  >
  > Check issues to make sure someone isn't already fixing that problem
4. Write your code
5. Commit and Push updates
6. Mark your pull request as ready for review

## Style Guide
- Code is formatted using Black.
- All modules, functions, and classes contain a docstring conforming to Sphinx conventions
- Readability > Efficiency
- Use camel case for class names and underscores for everything else

## Questions
Ping a mod or open a ticket on The Valley discord server

## Reporting Issues
- Describe what you expected to happen
- If possible, include reproducible examples
- Describe what actually happened (including logging messages and traceback)
- Double check your packages are the same as what is defined in the Pipfile

## Submitting Patches
- Use Black to format your code
- Clearly list/explain what your patch adds/updates (include issue number if relevant)
