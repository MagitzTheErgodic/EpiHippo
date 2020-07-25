# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import *
from botbuilder.schema import *

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    def __init__(self):
        self.isChat = False
    
    async def on_message_activity(self, turn_context: TurnContext):
        if turn_context.activity.text.lower() == "end chat":
            self.isChat = False
            await turn_context.send_activity("Chat ended.")
        elif self.isChat:
            await turn_context.send_activity("You typed: " + turn_context.activity.text)
        elif turn_context.activity.text.lower() == "wait":
            return await turn_context.send_activities([
                Activity(
                    type=ActivityTypes.typing
                ),
                Activity(
                    type="delay",
                    value=3000
                ),
                Activity(
                    type=ActivityTypes.message,
                    text="Finished Typing"
                )
            ])
        elif turn_context.activity.text.lower() == "show logo":
            await self._handle_outgoing_attachment(turn_context)

        elif turn_context.activity.text.lower() == "chat":
            self.isChat = True
            await turn_context.send_activity("Let's chat!")
        else:
            await self._display_options(turn_context)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def _handle_outgoing_attachment(self, turn_context: TurnContext):
        reply = Activity(type=ActivityTypes.message)
        reply.attachments = [self._get_internet_attachment()]

        await turn_context.send_activity(reply)
        
    def _get_internet_attachment(self) -> Attachment:
        """
        Creates an Attachment to be sent from the bot to the user from a HTTP URL.
        :return: Attachment
        """
        return Attachment(
            name="962121595530161121.png",
            content_type="image/png",
            content_url="https://hackboxstorage.blob.core.windows.net/projectimages/962121595530161121.jpg",
        )
        
    async def _display_options(self, turn_context: TurnContext):
        """
        Create a HeroCard with options for the user to interact with the bot.
        :param turn_context:
        :return:
        """

        # Note that some channels require different values to be used in order to get buttons to display text.
        # In this code the emulator is accounted for with the 'title' parameter, but in other channels you may
        # need to provide a value for other parameters like 'text' or 'displayText'.
        card = HeroCard(
            text="Hello dear user! What would you like to do?",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="Show logo", value="show logo"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="Wait", value="wait"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="Chat", value="chat"
                ),
            ],
        )

        reply = MessageFactory.attachment(CardFactory.hero_card(card))
        await turn_context.send_activity(reply)