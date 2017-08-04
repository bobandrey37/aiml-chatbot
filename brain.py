import aiml
import os

kernel = aiml.Kernel()
kernel.verbose(False)
kernel.setBotPredicate("name", "Rebecca")
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "startup.xml", commands = "'LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response
        print bot_response