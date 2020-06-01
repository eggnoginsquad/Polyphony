"""
Instances are individual bots accounts that act as system members.
"""

import discord
import logging

log = logging.getLogger(__name__)

class PolyphonyInstance(discord.Client):
    """Polyphony Member Instance."""

    def __init__(self, store: dict, **options):
        """
        :param store: (dict) Instance information from Database
        :param options: Discord Client Options
        """
        super().__init__(**options)
        self.store: dict = store

    async def on_ready(self):
        """Execute on bot initialization with the Discord API."""
        log.info(f"Instance started as {self.user}")
