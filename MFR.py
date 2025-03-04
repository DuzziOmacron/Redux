import threading
from kik_unofficial.datatypes.xmpp.login import LoginResponse, ConnectionFailedResponse
from kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse
from kik_unofficial.datatypes.xmpp.errors import LoginError
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.client import KikClient
import kik_unofficial.datatypes.xmpp.chatting as chatting
from startup import use_preset, preset_username, preset_password, preset_num_of_bots
import sys
import os
import time
import subprocess
import socket
import contextlib
# from keepalive import keep_alive
# keep_alive()
from urllib.request import urlopen
check_for_startup = os.path.exists("startup.py")
if check_for_startup == False:
    clear = open("startup.py", "w+")
    clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = False\n\npreset_username = \"\"\n\npreset_password = \"\"\n\npreset_num_of_bots = 0")
    clear.close()

# This allows us to use the bcolors class and ominous_dots function later in the script.
global ominous_dots, bcolors, antipurge
antipurge = False


class bcolors:  # This is for adding colors to text in the terminal.
    OKBLUE = '\033[94m'  # This is blue
    FAIL = '\033[91m'  # This is red
    OKGREEN = '\033[92m'  # This is green
    ENDC = '\033[0m'  # This is to stop using color.


# This function is for making a "..." with a delay? FUCK A DELAY! AINT NOBODY GOT TIME FOR THAT.
def ominous_dots(string):
    # This prints the string that was given to the function
    sys.stdout.write(string)
    # This makes the periods green
    dots = bcolors.OKGREEN + ("...") + bcolors.ENDC
    for dot in dots:  # This loops through the 3 periods
        sys.stdout.write(dot)  # This prints a period
        sys.stdout.flush()  # This makes sure it doesn't make a new line like print() would
        time.sleep(0.003)  # This waits 3/1000s of a sec too long
    # This waits another split second so that the total wait time is exactly 0.001 second
    time.sleep(0.001)

ominous_dots(bcolors.OKGREEN + ("Toking up") + bcolors.ENDC)

# This hides the output from installation to avoid spam
with contextlib.redirect_stdout(None):
    # This checks if the user has already installed the Kik Bot API
    automatic_setup = os.path.isdir("kik-bot-api-unofficial")
    if automatic_setup == False:  # This is triggered if they have not
        # This installs the stuff from stetho's fork of Tomer8007's API. Just has some redundant stuff quoted out, keys added
        os.system(
            'git clone -b new https://github.com/StethoSaysHello/kik-bot-api-unofficial')
    os.system('pip3 install ./kik-bot-api-unofficial')

try:
    # This grabs the page where the current version is
    version_page = "https://pastebin.com/7f4Ak7br"
    page = urlopen(version_page)  # This opens the page
    raw_version = page.read()  # This reads the page
    # This decodes the page and gives us a string
    version = raw_version.decode("utf-8")
    '''
 if version == "killswitch": #This checks if the killswitch has been activated
      print(bcolors.FAIL + ("This version of the botnet has been killswitched!\nThis is only used if a serious, potentially harmful bug or exploit in the botnet's code is discovered.\nPlease visit https://github.com/StethoSaysHello/KikBotnet to check for updates! If you need help, email StethoSpasm@Gmail.com\n\nFor your saftey, I am now deleting this script.\nDon't worry, this will not cause any harm to your local machine!") + bcolors.ENDC) #This explains the killswitch to a user
      path = os.getcwd() #This finds the path the script is running on
      os.remove(path + '\%s' % sys.argv[0]) #This removes the script
      exit() #This stops the script if its still somehow active
  '''
    if version == "Blaze":  # This checks if this script is up to date
        pass
    else:  # This is activated if the user is not up to date
        print(bcolors.FAIL + ("There is a new version of the botnet available! Please install the update, it can be found at https://github.com/StethoSaysHello/KikBotnet") +
              bcolors.ENDC)  # This asks the user to update
        input("Press enter to continue if you still want to use this outdated version! (Weirdo! lol)")
except:
    print(bcolors.FAIL + "Oh no! There was a problem checking for updates... This is probably from hosting issues. If you need to check for updates in the meantime, please visit Github.com/StethoSaysHello/KikBotnet\n(You can still use the botnet!)" + bcolors.ENDC)
    input(bcolors.OKBLUE + "Press enter to continue: " + bcolors.ENDC)


def install(package):
    # This installs the package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try: 
    import emoji
except ModuleNotFoundError:  
    print(bcolors.OKGREEN + ("\nOne moment while I install the emoji module.") +
          bcolors.ENDC)  
    install('emoji')  
    import emoji
try:  # This tries to import
    import colorama
except ModuleNotFoundError:  
    print(bcolors.OKGREEN + ("\nOne moment while I install the colorama module.") +
          bcolors.ENDC)  
    install('colorama')
    import colorama
try:  # This tries to import
    import kik_unofficial
except ModuleNotFoundError: 
    print(bcolors.OKGREEN + ("\nOne moment while I install the kik_unofficial module.") +
          bcolors.ENDC)  
    install('kik_unofficial')  
    import kik_unofficial


clear = open("kik-debug.log", "w+")
clear.close()  
clear = open("jidlist.txt", "w+")
clear.close()

global username_thing, spam, debug_jid, bot_count, attempt_number, MFR_secret, setup_preset, jid_list, name
attempt_number = 0
print(bcolors.OKGREEN + ("╭╮╭━╮╭╮    ╭━━╮   ╭╮      ╭╮\n┃┃┃╭╯┃┃    ┃╭╮┃  ╭╯╰╮    ╭╯╰╮\n┃╰╯╯╭┫┃╭╮  ┃╰╯╰┳━┻╮╭╋━╮╭━┻╮╭╯\n┃╭╮┃┣┫╰╯╯  ┃╭━╮┃╭╮┃┃┃╭╮┫┃━┫┃\n┃┃┃╰┫┃╭╮╮  ┃╰━╯┃╰╯┃╰┫┃┃┃┃━┫╰╮\n╰╯╰━┻┻╯╰╯  ╰━━━┻━━┻━┻╯╰┻━━┻━╯\n##### Created by Stetho #####") +
      bcolors.ENDC) 
spam = "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv"
# This is where activity info is sent to. Has to be a JID, not a GJID.
debug_jid = "JID_420@talk.kik.com" #no your JID goes here RETARD...now KYS 
jid_list = []

print(bcolors.OKBLUE + ("\nHello! This script was modified by blaze to combine stethos 5.3 update with the discontinued premium commands. DUZZI spiced up the responses!!  Skidded? HELL NAH!") + bcolors.ENDC)

name = input(bcolors.OKBLUE + ("\nWhat is your name?: ") + bcolors.ENDC)

print(bcolors.OKGREEN + "\nHello, " + name +
      "! Let's Get-Lit And Break Shit!" + bcolors.ENDC)

setup_preset = False


def get_preset():
    global setup_preset
    ask_preset = input(
        bcolors.OKGREEN + ("Would you like to setup automatic startup?\n[1] Yes, I would like to set it up.\n[2] No, I would like to startup manually.\n> ") + bcolors.ENDC)
    if str(ask_preset) == "1":
        print(bcolors.OKGREEN + ("Great! I'll setup automatic startup for you.\nJust input your details like normal and I'll do the rest!") + bcolors.ENDC)
        setup_preset = True
    elif str(ask_preset) == "2":
        ominous_dots(
            bcolors.OKGREEN + ("Okay, continuing without automatic startup") + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Invalid input! Please only use the number \"1\" or \"2\" (without quotations)\nExiting..." + bcolors.ENDC)
        exit()


if use_preset == False:
    get_preset()

if use_preset == True:
    ask_preset = input(
        bcolors.OKGREEN + ("\nI see you have startup.py configured.\nWould you like to use automatic startup?\n[1] Yes, I want to use automatic startup.\n[2] No, I want to startup manually.\n[3] No, I want to change automatic startup settings.\n> ") + bcolors.ENDC)
    if str(ask_preset) == "1":
        ominous_dots(bcolors.OKGREEN +
                     ("\nOkay! Using automatic startup") + bcolors.ENDC)
        print("\n")
    elif str(ask_preset) == "2":
        ominous_dots(
            bcolors.OKGREEN + ("Okay, continuing without automatic startup") + bcolors.ENDC)
        use_preset = False
    elif str(ask_preset) == "3":
        ask_change = input(
            bcolors.OKGREEN + ("Okay! Let's change automatic startup.\n[1] Change credentials\n[2] Reset to default settings\n") + bcolors.ENDC)
        if str(ask_change) == "1":
            print(bcolors.OKGREEN + ("Great! I'll setup automatic startup for you.\nJust input your details like normal and I'll do the rest!") + bcolors.ENDC)
            setup_preset = True
        elif str(ask_change) == "2":
            clear = open("startup.py", "w+")
            clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = False\n\npreset_username = \"\"\n\npreset_password = \"\"\n\npreset_num_of_bots = 0")
            clear.close()
            input(bcolors.OKGREEN + "Okay, I've reset your settings to the default. Press enter to continue with manual startup." + bcolors.ENDC)
            use_preset = False
        else:
            print(bcolors.FAIL + "Invalid input! Please only use the number \"1\" or \"2\" (without quotations)\nExiting..." + bcolors.ENDC)
            exit()
    else:
        print(bcolors.FAIL + "Invalid input! Please only use the number \"1\", \"2\" or \"3\" (without quotations)\nExiting..." + bcolors.ENDC)
        exit()


def get_prefix():  
    username_thing = input(
        bcolors.OKGREEN + ("\n\nWhat is the prefix of your bots usernames?: ") + bcolors.ENDC)
    return username_thing


if use_preset == True:
    username_thing = preset_username
else:
    # This triggers the function that aske for the bot prefix
    username_thing = get_prefix()
    # This checks for blank prefixes, and retries get_prefix if there are any.
    if len(username_thing) == 0:
        print(bcolors.FAIL + ("Uh-oh, it looks like you didn't provide any input! Let's try that again.") + bcolors.ENDC)
        username_thing = get_prefix()
    # This checks for spaces in the prefix, and retries get_prefix if there are any.
    if " " in username_thing:
        print(bcolors.FAIL + ("Uh-oh! There is a space in the username prefix you provided. Let's try that again.") + bcolors.ENDC)
        username_thing = get_prefix()
    print(bcolors.OKGREEN + ("\nOkay, I will be signing into your botnet as \"" + username_thing + "1\", \"" + username_thing +
          "2\", and so on.\nIf this is incorrect, please restart this session.") + bcolors.ENDC)  # This explains how the bots will sign in.


def get_bot_quantity():  # This function asks the user how many bots they wanna use.
    try:
        bot_count = int(
            input(bcolors.OKGREEN + ("\nHow many bots do you have?: ") + bcolors.ENDC))
    except ValueError:  # This is triggered when the input is not a number.
        print(bcolors.FAIL +
              ("That's not a number, lol. Lets try that again.") + bcolors.ENDC)
        # Just put a random string here to catch ValueError, could have put whatever.
        bot_count = "NULL"
    return bot_count


if use_preset == True:
    bot_count = preset_num_of_bots
else:
    # This triggers the above function to ask the user how many bots they wanna use,
    bot_count = get_bot_quantity()
    if bot_count == "NULL":  # This retries get_bot_quantity when the input is not a number.
        bot_count = get_bot_quantity()
    else:  # Else statement used because im mixing str/int in 'bot_count'
        # This retries get_bot_quantity when the input is equal to or lower than 0.
        if bot_count <= 0:
            print(bcolors.FAIL + ("You must use a number greater than or equal to 1. Let's try that again.") + bcolors.ENDC)
            bot_count = get_bot_quantity()

if use_preset == True:
    MFR_secret = preset_password
    bootup_message = "I am logging in with the preset options: \nUsername prefix - " + \
        str(preset_username) + "\nPassword - " + str(preset_password) + \
        "\nNumber of bots - " + str(preset_num_of_bots)
    print(bcolors.OKGREEN + bootup_message + bcolors.ENDC)
else:
    # This asks for the bot's password, it doesn't need error handling.
    MFR_secret = input(bcolors.OKGREEN + ("\n" + str(bot_count) +
                       " bots, got it! What is the password for your bots?: ") + bcolors.ENDC)

if setup_preset == True:
    clear = open("startup.py", "w+")
    clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = True\n\npreset_username = \"" +
                str(username_thing) + "\"\n\npreset_password = \"" + str(MFR_secret) + "\"\n\npreset_num_of_bots = " + str(bot_count))
    clear.close()
    bootup_message = "I've added the following presets to setup.py: \n\nUsername prefix - " + \
        str(username_thing) + "\nPassword - " + str(MFR_secret) + \
        "\nNumber of bots - " + str(bot_count) + "\n"
    print(bcolors.OKGREEN + bootup_message + bcolors.ENDC)
    time.sleep(1)
    input(bcolors.OKGREEN + "Press enter to begin logging in: " + bcolors.ENDC)

time.sleep(1)
print(bcolors.FAIL + emoji.emojize(":warning: This color means you skid like shit.") +
      bcolors.ENDC)  # This is an example red text, ooooo
time.sleep(3)
print(bcolors.OKBLUE +
      emoji.emojize("Okay, lets get this shit over with..") + bcolors.ENDC)


def handle_login(username, password):
    # code to handle login for a specific user

    def start_login(usernames, passwords):
        threads = []
    for username, password in zip(usernames, passwords):
        t = threading.Thread(target=handle_login, args=(username, password))
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()


def login(give_a_username, give_a_password, bot_count):
    MFR = give_a_username
    MFR_secret = give_a_password
    username = sys.argv[1] if len(sys.argv) > 1 else MFR
    password = sys.argv[2] if len(sys.argv) > 2 else MFR_secret

    def main():
        SpamBotnet(username, password)

    class SpamBotnet(KikClientCallback):
        def __init__(self, username, password):
            self.username = username
            self.password = password
            self.client = KikClient(self, self.username, self.password)

        def on_login_ended(self, response: LoginResponse):
            ominous_dots(bcolors.OKGREEN + ("Logging in as @" +
                         str(self.username)) + bcolors.ENDC)

        def on_authenticated(self):
            print(bcolors.OKGREEN + (" Successfully logged in!"))
            self.client.request_roster()

            def get_my_jid():
                try:
                    my_jid = self.client.get_jid(MFR)
                    return my_jid
                except:
                    return False

            my_jid = get_my_jid()
            while my_jid == False:
                my_jid = get_my_jid()
            jidlist = open("jidlist.txt", "a+")
            jidlist.write(my_jid + "\n")
            jidlist.close()

    threads = []
    for i in range(bot_count):

        # LOLZ:

        # tha/FUKN DUZZ way to miltithread.
        '''
def login(give_a_username, give_a_password, bot_count): #This is a function for logging in, it asks for user/pass and # of bots. Its a function so that it can be called on to retry later if there are any closed connections.
    #These arent really relevant but I didnt feel like changing variable names when I added retry on connection error, sooo....
    MFR = give_a_username
    MFR_secret = give_a_password
    #This is where the username goes
    username = sys.argv[1] if len(sys.argv) > 1 else MFR
    #This is where the password goes
    password = sys.argv[2] if len(sys.argv) > 2 else MFR_secret

    def main(): #This function is used to execute the login process only if the file was run directly, and not imported.
        SpamBotnet()

    class SpamBotnet(KikClientCallback):
        def __init__(self): #Constructor for the SpamBotnet class above
            #This is where the previously stored user/pass goes to login
            self.client = KikClient(self, username, password)

        global result, antipurge, name
        result = None #This makes the login scripts wait until the login succeeds or fails before trying again

        #This is triggered when the bot is done logging in
        def on_login_ended(self, response: LoginResponse):
            #This lets you know your bot logged in in the terminal. It says the first/last name and username.
            ominous_dots(bcolors.OKGREEN + ("Logging in as @" + \
                         str(username)) + bcolors.ENDC)

        #This is triggered when the bot is authenticated (yayyyy no closed connection)
        def on_authenticated(self):
            print(bcolors.OKGREEN + (" Successfully logged in!"))
            global result
            result = True #This lets the login stanzas know that the login was authenticated and it can continue with the next login
            # This requests the roster, which is later used in on_roster_recieved
            self.client.request_roster()
            def get_my_jid():
                try:
                    my_jid = self.client.get_jid(MFR)
                    return my_jid
                except:
                    return False

            my_jid = get_my_jid()
            while my_jid == False:
                my_jid = get_my_jid()
            jidlist = open("jidlist.txt", "a+")
            jidlist.write(my_jid + "\n")
            jidlist.close()
        '''
# Create a whitelist. Create a text file that contains the usernames of the people that you want to allow to send commands.

# Here's what i did.


whitelist = []
custom_response = "HELL NAH."


def check_whitelist(sender):
    if sender in whitelist:
        return True
    else:
        return False


def read_whitelist():
    with open("whitelist.txt", "r") as f:
        for line in f:
            whitelist.append(line.strip())


read_whitelist()

# Example usage
sender = "example_username"
if check_whitelist(sender):
    # Accept commands from the sender
    pass
else:
    # Respond with the custom response
    print(custom_response)

    def on_friend_attribution(self, response: chatting.IncomingFriendAttribution):
        print("[+] Friend attribution request from " + response.referrer_jid)
        self.client.add_friend(response.referrer_jid)

    def on_chat_message_received(self, chat_message: chatting.IncomingChatMessage):
        global antipurge  # This is triggered when a PM is recieved
        # This grabs the sender's JID because I dont feel like typing that a million times
        JID = chat_message.from_jid
        # This grabs the message, encodes emojis, and makes it lowercase.
        mssg = emoji.demojize(chat_message.body.lower())
        if mssg == "ping":  # command to check if bot is online
            self.client.send_chat_message(
                JID, "Ping these nuts, motherfucker!")
            self.client.add_friend(JID)
        elif mssg == "slaves":
            self.client.send_chat_message(JID, "Yes Daddy?")
        elif mssg == ".spin":
            self.client.send_chat_message(JID, ".spin")
        elif mssg == "loop20":
            for x in array(1, 20):
                self.client.send_chat_message(JID, "skrttt")
            return
        elif mssg.startswith("antipurge"):
            if mssg == "antipurge on":
                self.client.send_chat_message(
                    JID, "Turning antipurge on...")
                antipurge = True
                time.sleep(2)
                self.client.send_chat_message(
                    JID, "Vete los chingasos puto MADRE")
            elif mssg == "antipurge off":
                self.client.send_chat_message(
                    JID, "Turning off antipurge...")
                antipurge = False
                time.sleep(2)
                self.client.send_chat_message(JID, "voy por chellas")
            elif mssg == "antipurge check":
                if antipurge == True:
                    self.client.send_chat_message(JID, "listo cabron")
                elif antipurge == False:
                    self.client.send_chat_message(JID, "hecho un gallo")
        elif mssg == "refresh":
            number_of_users = 0
            for user in jid_list:  # This loops through each user in the errors list
                if user:  # This counts the number of users in the error list
                    number_of_users += 1
            self.client.send_chat_message(
                JID, "sale pues voy por los vatos locos...\n(Estimated completion time is " + str(number_of_users) + " second(s).)")
            for user in jid_list:
                if user:
                    self.client.add_friend(user)
                    self.client.send_chat_message(
                        user, "Wake up, Dumbass.")
                time.sleep(1)
            self.client.send_chat_message(JID, "Whole squad ready!")
        elif mssg.startswith("promote"):
            self.client.send_chat_message(
                JID, "The promote command only works in groups.")
        elif mssg.startswith("demote"):
            self.client.send_chat_message(
                JID, "The demote command only works in groups.")
        elif mssg == "addall":
            self.client.send_chat_message(
                JID, "The addall command only works in groups.")
        elif mssg == "friend":  # command to add the bot as a friend
            self.client.add_friend(JID)  # This is a friend attribution request
            self.client.send_chat_message(
                JID, "Add me places, I need groups.")
        elif mssg.startswith("gif"):
            gif_query = mssg.replace("gif ", "", 1)
            self.client.send_chat_message(
                JID, "Searching for a gif with the query \"" + str(gif_query) + "\"...")
            try:  # This attempts the gif query once first to check if its valid
                # This tries to send a gif with the query
                self.client.send_gif_image(JID, gif_query)
            except:
                self.client.send_chat_message(
                    JID, "welp I fukt that all to hell and lost your gif for the query" + gif_query + "\"!")
        elif mssg == "commands":  # command for listing the commands.
            self.client.send_chat_message(
                JID, "To spam a user's PMs, use \"spam [JID or Username] w/ [Message]\", this command works both in groups and PMs.\n\nTo spam a group, say \"friend\" in PMs to add me then add me to the group you wish to spam and say \"groupspam [message]\".\n\n Keep in mind that once you start spam, it will not stop until you restart the bot.")
        elif mssg.startswith("spam"):  # Command for spamming a user.
            if mssg == "spam":  # Elaborates on how to use spam if the message is just "spam"
                self.client.send_chat_message(
                    JID, "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
            else:
                if " w/ " in mssg:  # This checks if "w/" was in the string and continues if so
                    if mssg.startswith("spam gif"):
                        failed = False
                        # This takes the first part of the message off to isolate the jid/username and query
                        remove_spam = mssg.replace("spam gif ", "")
                        # This splits the message into the JID/username and message
                        split_string = remove_spam.split(" w/ ", 1)
                        # This isolates the JID we got in split_string
                        jid_to_spam = split_string[0]
                        '''
                            The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                            '''
                        if "@talk.kik.com" in jid_to_spam:  # Temporary patch
                            jid_to_spam = jid_to_spam[:-17]  # Temporary patch
                        # This isolates the query we got in split_string
                        gif_query = split_string[1]
                        try:  # This attempts the gif query once first to check if its valid
                            # This tries to send a gif with the query
                            self.client.send_gif_image(jid_to_spam, gif_query)
                        except:  # This is triggered if it fails
                            # I could have just used "raise someerror" and except, but I was tired when I wrote this... I'ma just leave it. Don't @ me nobody really reads my code anyways. Except you... Hi nerd.
                            failed = True
                        if failed == True:  # This is triggered when gif grabbing fails
                            # This lets the user know it failed
                            self.client.send_chat_message(
                                JID, "Im wayyy to high for this bro i lost your gif for the query" + gif_query + "\"!")
                        else:  # This is triggered if the gif query does not fail
                            self.client.send_chat_message(JID, "I am shitting gifs on \"" + jid_to_spam + "\" with the query \"" + gif_query +
                                                          "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")  # This lets the user on kik know it is spamming gifs
                            # This displays in the terminal that gif spam was triggered
                            print("I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" +
                                  gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")
                            # This triggers a while loop with the random string we made global earlier
                            while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                                self.client.send_gif_image(
                                    jid_to_spam, gif_query)  # This sends the gif
                                # This is the wait between each message. Never change it to 0, IP bans suck.
                                time.sleep(0.2)
                    else:
                        # This takes the first part of the message off to isolate the jid/username and message
                        remove_spam = mssg.replace("spam ", "")
                        # This splits the message into the JID/username and message
                        split_string = remove_spam.split(" w/ ", 1)
                        jid_to_spam = split_string[0]  # This isolates the JID
                        '''
                            The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                            '''
                        if "@talk.kik.com" in jid_to_spam:  # Temporary patch
                            jid_to_spam = jid_to_spam[:-17]  # Temporary patch
                        # This reminds the user they dont need an @ if they use one, and removes it for them.
                        if jid_to_spam.startswith("@"):
                            # This reminds the user that they dont
                            self.client.send_chat_message(
                                JID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                            # This gets rid of the @ in the username
                            jid_to_spam = jid_to_spam.replace("@", "", 1)
                            time.sleep(0.5)  # Waits half a second
                        # Isolates the message we got in split_string
                        message_to_spam = split_string[1]
                        # Checks if the JID they gave is actually a GJID and warns them if so.
                        if "groups" in jid_to_spam:
                            self.client.send_chat_message(
                                JID, "You can't use a GJID for the spam command.")
                        else:  # Sends a confirmation of who is being spammed with what
                            self.client.send_chat_message(
                                JID, "I am spamming the user \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(message_to_spam) + "\"!")
                            print("I am spamming the usr \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(
                                message_to_spam) + "\"!")
                            while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                                self.client.send_chat_message(jid_to_spam, emoji.emojize(
                                    message_to_spam))  # This is the bot spamming
                                # < This is the delay between each message. You should leave it alone but if you need it to be faster/slower you can change it. NEVER set to 0, IP bans suck.
                                time.sleep(0.2)
                else:  # This lets the user know when they used the command wrong because "w/" isnt in the string
                    self.client.send_chat_message(
                        JID, "You need to put a \"w/\" with one space on both sides between the JID/username and the spam message.")
                    time.sleep(0.5)
                    self.client.send_chat_message(
                        JID, "To use the spam tool, use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\"\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue is a pretty color!\"")
        elif mssg.startswith("poke"):  # Command for sending a single message to a user
            if mssg == "poke":
                self.client.send_chat_message(
                    JID, "To use the poke tool, please use \"poke [JID or Username] w/ [Message]\".\n\nExample: \"poke bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
            else:
                if " w/ " in mssg:
                    # This takes the first part of the message off to isolate the jid/username and message
                    remove_poke = mssg.replace("poke ", "")
                    # This splits the message into the JID/username and message.
                    split_string = remove_poke.split(" w/ ", 1)
                    jid_to_poke = split_string[0]  # This isolates the JID.
                    '''
                        The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                        '''
                    if "@talk.kik.com" in jid_to_poke:  # Temporary patch
                        jid_to_poke = jid_to_poke[:-17]  # Temporary patch
                    # This reminds the user they dont need an @ if they use one, and removes it for them.
                    if jid_to_poke.startswith("@"):
                        self.client.send_chat_message(
                            JID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                        jid_to_poke = jid_to_poke.replace("@", "", 1)
                    # Isolates the message we got in remove_poke
                    message_to_send = split_string[1]
                    # Checks if the JID they gave is actually a GJID and warns them if so.
                    if "groups" in jid_to_poke:
                        self.client.send_chat_message(
                            JID, "You can't use a GJID for the poke command.")
                    else:  # Sends a confirmation of who is being sent what
                        self.client.send_chat_message(
                            JID, "I am poking the user \"" + jid_to_poke + "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                        print("I am poking the user \"" + jid_to_poke +
                              "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                        self.client.send_chat_message(
                            jid_to_poke, emoji.emojize(message_to_send))
                else:  # This lets the user know when they used the command wrong because "w/" isn't in the string
                    self.client.send_chat_message(
                        JID, "You need to put a \"w/\" with one space on both sides between the JID/username and the message.\n\n(Error: w/ not found in message string.)")
                    time.sleep(0.5)
                    self.client.send_chat_message(
                        JID, "To use the poke tool, use \"spam [JID or Username] w/ [Message]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
        # This is a command for sending a friend request to a JID
        elif mssg.startswith("sendfriend"):
            self.client.send_chat_message(
                JID, "Tip: You should only use this in groups so that you can trigger all of your bots at once! That's kinda the point of this command...")
            if mssg == "sendfriend":
                # This reminds the user that this command is best for groups
                self.client.send_chat_message(
                    JID, "To use the sendfriend tool, please use \"sendfriend [JID or Username]\".\n\nExample: \"sendfriend stethosayshello_3pf@talk.kik.com\"")
            else:
                # This removes the beginning of the message to isolate the JID
                remove_sendfriend = mssg.replace("sendfriend ", "", 1)
                '''
                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                    '''
                if "@talk.kik.com" in remove_sendfriend:  # Temporary patch
                    # Temporary patch
                    remove_sendfriend = remove_sendfriend[:-17]
                self.client.send_chat_message(
                    JID, "I am sending a friend attribution request and \"I'm adding you as a friend\" message to \"" + remove_sendfriend + " !")
                # This lets the user know they are being added
                self.client.send_chat_message(
                    remove_sendfriend, "I'm adding you as a friend!")
                # This adds the user as a friend
                self.client.add_friend(remove_sendfriend)
        elif mssg.startswith("leave"):  # This command is for eaving groups with a GJID
            # This removes the first part of the message to isolate the GJID
            remove_leave = mssg.replace("leave ", "", 1)
            if mssg == "leave":  # This checks if the message is just "leave" and gives instructions if so
                self.client.send_chat_message(
                    JID, "To use the leave command, please use \"leave [GJID]\"")
            else:
                if "groups" in remove_leave:  # This checks if the given GJID is in fact a GJID
                    self.client.send_chat_message(
                        JID, "Attempting to leave \"" + remove_leave + "\"!")
                    # This leaves the group
                    self.client.leave_group(remove_leave)
                else:  # This tells the user that they used a JID or otherwise invalid input
                    self.client.send_chat_message(
                        JID, "You must use a valid GJID in the leave command! You used \"" + remove_leave + "\"!")

    def on_group_status_received(self, response: chatting.IncomingGroupStatus):
        GJID = response.group_jid
        if antipurge == True:
            for user in jid_list:
                self.client.unban_member_from_group(GJID, user)
                self.client.add_peer_to_group(GJID, user)
                self.client.promote_to_admin(GJID, user)

    def on_group_message_received(self, chat_message: chatting.IncomingGroupChatMessage):
        global antipurge
        mssg = emoji.demojize(chat_message.body.lower())
        GJID = chat_message.group_jid
        if antipurge == True:
            for user in jid_list:
                self.client.unban_member_from_group(GJID, user)
                self.client.add_peer_to_group(GJID, user)
                self.client.promote_to_admin(GJID, user)
        elif mssg.startswith("promote"):
            if mssg == "promote":
                self.client.send_chat_message(
                    GJID, "To use the promote command, say \"promote [JID or username]\"")
            else:
                jid_to_promote = mssg.replace("promote ", "")
                if jid_to_promote.startswith("@"):
                    self.client.send_chat_message(
                        GJID, "Reminder: You do not need to add an \"@\" to the username in this command.")
                    jid_to_promote = jid_to_promote.replace("@", "", 1)
                self.client.send_chat_message(
                    GJID, "Attempting to promote \"" + jid_to_promote + "\" to admin!")
                self.client.promote_to_admin(GJID, jid_to_promote)
        elif mssg.startswith("demote"):
            if mssg == "demote":
                self.client.send_chat_message(
                    GJID, "To use the demote command, say \"demote [JID or username]\"")
            else:
                jid_to_demote = mssg.replace("demote ", "")
                if jid_to_demote.startswith("@"):
                    self.client.send_chat_message(
                        GJID, "Reminder: You do not need to add an \"@\" to the username in this command.")
                    jid_to_demote = jid_to_demote.replace("@", "", 1)
                self.client.send_chat_message(
                    GJID, "Attempting to demote \"" + jid_to_demote + "\"!")
                self.client.demote_admin(GJID, jid_to_demote)
        elif mssg == "kikmobd":
            self.client.send_chat_message(GJID, "Lets do it!")
            for user in jid_list:
                self.client.add_peer_to_group(GJID, user)
                time.sleep(0.3)
        elif mssg.startswith("antipurge"):
            if mssg == "antipurge on":
                self.client.send_chat_message(
                    GJID, "Turning antipurge on...")
                antipurge = True
                time.sleep(2)
                self.client.send_chat_message(GJID, "Antipurge now on.")
            elif mssg == "antipurge off":
                self.client.send_chat_message(
                    GJID, "Turning off antipurge...")
                antipurge = False
                time.sleep(2)
                self.client.send_chat_message(GJID, "Antipurge now off.")
            elif mssg == "antipurge check":
                if antipurge == True:
                    self.client.send_chat_message(GJID, "Antipurge is on.")
                elif antipurge == False:
                    self.client.send_chat_message(
                        GJID, "Antipurge is off.")
        # This command spams a group with a message.
        if mssg.startswith("groupspam"):
            if mssg == "groupspam":  # This elaborates on how to use groupspam if the user just says "groupspam"
                self.client.send_chat_message(
                    "To use the group spam tool, use \"groupspam [Message]\", or \"groupspam gif [query]\"")
            else:  # This is the spam part
                # This checks if it's the gif command and continues if so
                if mssg.startswith("groupspam gif"):
                    failed = False  # This sets the failed variable we use later
                    # This isolates the gif query
                    gif_query = str(mssg.replace("groupspam gif ", "", 1))
                    try:
                        # This lets the user know it is testing the query
                        self.client.send_chat_message(
                            GJID, "Testing query \"" + str(gif_query) + "\"...")
                        # This attempts to send a gif with the query
                        self.client.send_gif_image(GJID, gif_query)
                    except:  # This is triggered if the attempt fails
                        failed = True
                    if failed == True:
                        # This lets the user know the attemot failed
                        self.client.send_chat_message(
                            GJID, "I couldn't find a gif for the query" + gif_query + "\"!")
                    else:
                        self.client.send_chat_message(GJID, "I will spam gifs with the query \"" + gif_query +
                                                      "\"!\nTHIS IS YOUR 5 SECOND WARNING TO LEAVE THE GROUP.\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")  # This confirms the request
                        time.sleep(5)
                        # This confirms the request in the terminal
                        print("I am spamming gifs with the query \"" + gif_query +
                              "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")
                        # This is a random variable to trigger the while loop
                        while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                            # This sends the gof with the query
                            self.client.send_gif_image(GJID, gif_query)
                            # This is the wait between each message. Never change it to 0, IP bans suck.
                            time.sleep(0.3)
                else:
                    self.client.send_chat_message(
                        GJID, "THIS IS YOUR 5 SECOND WARNING TO LEAVE THE GROUP.")
                    time.sleep(5)
                    # This triggers a while loop with a random variable
                    while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                        # This isolates the message the user wants to send.
                        spam_message = mssg.replace("groupspam ", "", 1)
                        while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                            # This sends the given message in a loop
                            self.client.send_chat_message(
                                GJID, emoji.emojize(spam_message))
                            # This is the wait between each message. Never change it to 0, IP bans suck.
                            time.sleep(0.3)
        elif mssg == "ping":  # command to check if bot is online
            # Replies "pong". Pretty simple
            self.client.send_chat_message(GJID, "pong")
        elif mssg == "friend":  # This command lets the user know the friend command only works in PMs
            self.client.send_chat_message(
                GJID, "This can only be used in PMs")
        elif mssg.startswith("gif"):
            gif_query = mssg.replace("gif ", "", 1)
            self.client.send_chat_message(
                GJID, "Searching for a gif with the query \"" + str(gif_query) + "\"...")
            try:  # This attempts the gif query once first to check if its valid
                # This tries to send a gif with the query
                self.client.send_gif_image(GJID, gif_query)
            except:
                self.client.send_chat_message(
                    GJID, "I couldn't find a gif for the query" + gif_query + "\"!")
        elif mssg == "commands":  # command for listing the commands.
            self.client.send_chat_message(
                GJID, "To spam a user's PMs, use \"spam [JID or Username] w/ [Message]\", this command works both in groups and PMs.\n\nTo spam a group, say \"friend\" in PMs to add me then add me to the group you wish to spam and say \"groupspam [message]\".\n\n Keep in mind that once you start spam, it will not stop until you restart the bot.")
        elif mssg.startswith("spam"):  # Command for spamming a user.
            if mssg == "spam":  # Elaborates on how to use spam if the message is just "spam"
                self.client.send_chat_message(
                    GJID, "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
            else:
                if " w/ " in mssg:  # This checks if "w/" was in the string and continues if so
                    if mssg == "spam":  # Elaborates on how to use spam if the message is just "spam"
                        self.client.send_chat_message(GJID,
                                                      "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                    else:
                        if " w/ " in mssg:  # This checks if "w/" was in the string and continues if so
                            if mssg.startswith("spam gif"):
                                failed = False
                                remove_spam = mssg.replace("spam gif ",
                                                           "")  # This takes the first part of the message off to isolate the jid/username and query
                                split_string = remove_spam.split(" w/ ",
                                                                 1)  # This splits the message into the JID/username and message
                                # This isolates the JID we got in split_string
                                jid_to_spam = split_string[0]
                                '''
                                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                                    '''
                                if "@talk.kik.com" in jid_to_spam:  # Temporary patch
                                    # Temporary patch
                                    jid_to_spam = jid_to_spam[:-17]
                                # This isolates the query we got in split_string
                                gif_query = split_string[1]
                                try:  # This attempts the gif query once first to check if its valid
                                    self.client.send_gif_image(jid_to_spam,
                                                               gif_query)  # This tries to send a gif with the query
                                except:  # This is triggered if it fails
                                    # I could have just used "raise someerror" and except, but I was tired when I wrote this... I'ma just leave it. Don't @ me nobody really reads my code anyways. Except you... Hi nerd.
                                    failed = True
                                if failed == True:  # This is triggered when gif grabbing fails
                                    self.client.send_chat_message(GJID,
                                                                  "I couldn't find a gif for the query" + gif_query + "\"!")  # This lets the user know it failed
                                else:  # This is triggered if the gif query does not fail
                                    self.client.send_chat_message(GJID,
                                                                  "I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")  # This lets the user on kik know it is spamming gifs
                                    print(
                                        "I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")  # This displays in the terminal that gif spam was triggered
                                    # This triggers a while loop with the random string we made global earlier
                                    while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                                        self.client.send_gif_image(
                                            jid_to_spam, gif_query)  # This sends the gif
                                        # This is the wait between each message. Never change it to 0, IP bans suck.
                                        time.sleep(0.3)
                            else:
                                # This takes the first part of the message off to isolate the jid/username and message
                                remove_spam = mssg.replace("spam ", "")
                                # This splits the message into the JID/username and message
                                split_string = remove_spam.split(" w/ ", 1)
                                # This isolates the JID
                                jid_to_spam = split_string[0]
                                '''
                                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                                    '''
                                if "@talk.kik.com" in jid_to_spam:  # Temporary patch
                                    # Temporary patch
                                    jid_to_spam = jid_to_spam[:-17]
                                # This reminds the user they dont need an @ if they use one, and removes it for them.
                                if jid_to_spam.startswith("@"):
                                    self.client.send_chat_message(
                                        GJID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                                    jid_to_spam = jid_to_spam.replace(
                                        "@", "", 1)
                                    time.sleep(0.5)  # Waits half a second
                                # Isolates the message we got in split_string
                                message_to_spam = split_string[1]
                                # Checks if the JID they gave is actually a GJID and warns them if so.
                                if "groups" in jid_to_spam:
                                    self.client.send_chat_message(
                                        GJID, "You can't use a GJID for the spam command.")
                                else:  # Sends a confirmation of who is being spammed with what
                                    self.client.send_chat_message(
                                        GJID, "I am spamming the user \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(message_to_spam) + "\"!")
                                    print("I am spamming the user \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(
                                        message_to_spam) + "\"!")
                                    while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                                        self.client.send_chat_message(jid_to_spam, emoji.emojize(
                                            message_to_spam))  # This is the bot spamming
                                        # < This is the delay between each message. You should leave it alone but if you need it to be faster/slower you can change it. NEVER set to 0, IP bans suck.
                                        time.sleep(0.2)
                else:  # This lets the user know when they used the command wrong because "w/" isnt in the string
                    self.client.send_chat_message(
                        GJID, "You need to put a \"w/\" with one space on both sides between the JID/username and the spam message.")
                    time.sleep(0.5)
                    self.client.send_chat_message(
                        GJID, "To use the spam tool, use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ i like dick.\"")
        elif mssg.startswith("poke"):  # Command for sending a single message to a user
            if mssg == "poke":
                self.client.send_chat_message(
                    GJID, "To use the poke tool, please use \"poke [JID or Username] w/ [Message]\".\n\nExample: \"poke bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
            else:
                if " w/ " in mssg:
                    # This takes the first part of the message off to isolate the jid/username and message
                    remove_poke = mssg.replace("poke ", "")
                    # This splits the message into the JID/username and message.
                    split_string = remove_poke.split(" w/ ", 1)
                    jid_to_poke = split_string[0]  # This isolates the JID.
                    '''
                        The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                        '''
                    if "@talk.kik.com" in jid_to_poke:  # Temporary patch
                        jid_to_poke = jid_to_poke[:-17]  # Temporary patch
                    # This reminds the user they dont need an @ if they use one, and removes it for them.
                    if jid_to_poke.startswith("@"):
                        self.client.send_chat_message(
                            GJID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                        jid_to_poke = jid_to_poke.replace("@", "", 1)
                    # Isolates the message we got in remove_poke
                    message_to_send = split_string[1]
                    # Checks if the JID they gave is actually a GJID and warns them if so.
                    if "groups" in jid_to_poke:
                        self.client.send_chat_message(
                            GJID, "You can't use a GJID for the poke command.")
                    else:  # Sends a confirmation of who is being sent what
                        self.client.send_chat_message(
                            GJID, "I am poking the user \"" + jid_to_poke + "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                        print("I am poking the user \"" + jid_to_poke +
                              "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                        self.client.send_chat_message(
                            jid_to_poke, emoji.emojize(message_to_send))
                else:  # This lets the user know when they used the command wrong because "w/" isn't in the string
                    self.client.send_chat_message(
                        GJID, "You need to put a \"w/\" with one space on both sides between the JID/username and the message.\n\n(Error: w/ not found in message string.)")
                    time.sleep(0.5)
                    self.client.send_chat_message(
                        GJID, "To use the poke tool, use \"spam [JID or Username] w/ [Message]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
        # This is a command for sending a friend request to a JID
        elif mssg.startswith("sendfriend"):
            if mssg == "sendfriend":
                # This reminds the user that this command is best for groups
                self.client.send_chat_message(
                    GJID, "To use the sendfriend tool, please use \"sendfriend [JID or Username]\".\n\nExample: \"sendfriend stethosayshello_3pf@talk.kik.com\"")
            else:
                # This removes the beginning of the message to isolate the JID
                remove_sendfriend = mssg.replace("sendfriend ", "", 1)
                '''
                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                    '''
                if "@talk.kik.com" in remove_sendfriend:  # Temporary patch
                    # Temporary patch
                    remove_sendfriend = remove_sendfriend[:-17]
                self.client.send_chat_message(
                    GJID, "I am sending a friend attribution request and \"I'm adding you as a friend\" message to \"" + remove_sendfriend + " !")
                # This lets the user know they are being added
                self.client.send_chat_message(
                    remove_sendfriend, "I'm adding you as a friend!")
                # This adds the user as a friend
                self.client.add_friend(remove_sendfriend)
        elif mssg.startswith("leave"):  # This command is for eaving groups with a GJID
            # This removes the first part of the message to isolate the GJID
            remove_leave = mssg.replace("leave ", "", 1)
            if mssg == "leave":  # This checks if the message is just "leave" and gives instructions if so
                self.client.send_chat_message(
                    GJID, "To use the leave command, please use \"leave [GJID]\"")
            else:
                if "groups" in remove_leave:  # This checks if the given GJID is in fact a GJID
                    self.client.send_chat_message(
                        GJID, "Attempting to leave \"" + remove_leave + "\"!")
                    # This leaves the group
                    self.client.leave_group(remove_leave)
                else:  # This tells the user that they used a JID or otherwise invalid input
                    self.client.send_chat_message(
                        GJID, "You must use a valid GJID in the leave command! You used \"" + remove_leave + "\"!")

        # This function is triggered when the roster is recieved.
        def on_roster_received(self, response: FetchRosterResponse):
            global name
        response: chatting.IncomingChatMessage
        '''
            Rather than using access keys, the botnet just keeps track of IPs now.
            If Stetho notices the premium version has spread, the next update will include blacklisting. 
           
            #You can add an option to view the rosters here, but it was removed to avoid spam in the terminal. Just unquote it if you want to use it.
            #print("Roster:\n" + '\n'.join([str(member) for member in response.peers]))
            '''
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        self.client.send_chat_message(debug_jid, emoji.emojize(
            ":warning: \"" + name + "\" is online!\nHost: " + str(hostname) + "\nIP: " + str(ip_address)))
        for user in jid_list:
            self.client.add_friend(user)
            time.sleep(0.3)

        # This function is triggered when your kik bot's connection is closed/fails
        def on_connection_failed(self, response: ConnectionFailedResponse):
            global result
        # This lets the login stanzas know that the login failed and it can continue with the next one.
        result = False
        # This lets the user know the connection was closed
        print(bcolors.OKGREEN +
              emoji.emojize(" Kik was on some shit..") + bcolors.ENDC)
        # This opens the loginerror.txt file
        oof = open("loginerror.txt", "a+")
        # This writes the username of the bot into the loginerror.txt file for the login retry later
        oof.write(username_thing + str(bot_count) + "\n")
        oof.close()  # This closes the text file. Always a good practice

        # This function is triggered when there is a login error.
        def on_login_error(self, login_error: LoginError):
            global result
        # This lets the login stanzas know that the login failed and it can continue with the next one.
        result = False
        # This is triggered when the error is a captcha. Would have added the captcha wizard, but thats not very useful in a botnet.
        if login_error.is_captcha():
            print(bcolors.FAIL + emoji.emojize(":warning: Oh no! There is a captcha on @" + username_thing + str(bot_count) +
                  ", I can't login! Please sign into it manually on your own device to clear the captcha.") + bcolors.ENDC)  # This warns the user of the captcha.
        # Any other issues are username/password mismatches, so this is triggered when the error is not a captcha.
        else:
            # This warns the user the username/password is incorrect.
            print(bcolors.FAIL + emoji.emojize(":warning: Oh no! Your username or password for @" +
                  username_thing + str(bot_count) + " is incorrect!") + bcolors.ENDC)

    # This is used to execute the login process only if the file was run directly, and not imported.
    def login(give_a_username, give_a_password, bot_count):

        def main():
            login("username_thing", "password", "bot_count")

    if __name__ == '__main__':
        main()

clear = open("loginerror.txt", "w+")  # This clears out loginerror.txt
clear.close()
# This checks if logins have been attempted yet, and starts the first login attempts if not.
if attempt_number == 0:
    while int(bot_count) > 0:  # This loops through the number of bots
        for i in range(bot_count):
            # This gets the username to login as
            MFR = username_thing + str(bot_count)
            login(MFR, MFR_secret, bot_count)  # This attempts the login
            while result is None:
                pass
            # This decreases the bot count by one after the login attempt
            bot_count = int(bot_count) - 1
    # This increases the attempt number so that this chunk is not triggered again
    attempt_number = attempt_number + 1


def retry_login(password):  # This function retries logns when there are closed connections
    # This opens loginerror.txt to read it
    errors = open("loginerror.txt", "r")
    number_of_errors = 0  # This sets the number of errors to 0 for the next step
    read_errors = errors.read()  # This reads loginerror.txt
    # This makes a list out of the contents of loginerror.txt
    errors_list = read_errors.split("\n")
    for user in errors_list:  # This loops through each user in the errors list
        if user:  # This counts the number of users in the error list
            number_of_errors += 1
    if " " in errors_list:  # This ignores any blank lines, happens sometimes.
        number_of_errors = number_of_errors - 1
    # This checks if there are any errors, if so, attempts to log in.
    if number_of_errors > 0:
        print(bcolors.OKBLUE + emoji.emojize("There are " + str(number_of_errors) + " Fucked connections. Lemme try again..") +
              bcolors.ENDC)  # This lets the user know that the script will retry the login(s)
        ominous_dots(bcolors.OKGREEN +
                     emoji.emojize("This better work!") + bcolors.ENDC)
        print("\n")
        time.sleep(1)  # This waits a second so the user can read
        # This clears the text from loginretry.txt
        clear = open("loginretry.txt", "w+")
        clear.close()  # This closes the file, always a good practice.
        # This opens loginretry.txt to append to it
        oof = open("loginretry.txt", "a+")
        for user in errors_list:  # This loops through each user in errors list and adds them to loginretry.txt
            oof.write(user + "\n")
        oof.close()  # This closes the file, always a good practice.
        # This opens loginretry.txt to read it
        retry = open("loginretry.txt", "r")
        read_retry = retry.read()  # This reads loginretry.txt
        # This splits loginretry.txt into a list
        retry_list = read_retry.split("\n")
        # Clears the text from loginerror.txt
        clear = open("loginerror.txt", "w+")
        clear.close()  # This closes the file, always a good practice.
        for name in retry_list:  # This loops through the failed logins
            if number_of_errors > 0:  # This checks if there are errors remaining before continuing
                if " " in name:  # This makes lines with spaces blank
                    checked_name = name.replace(" ", "")
                else:
                    checked_name = name
                if not not checked_name:  # This ignores blank lines
                    # This attempts to login
                    login(checked_name, password, number_of_errors)
                # This waits 5 seconds between each login to avoid closed connections
                time.sleep(0.1)
                # This subtracts 1 from the error count
                number_of_errors = number_of_errors - 1
        retry.close()  # This closes the file, always a good practice.


errors = open("loginerror.txt", "r")  # This opens loginerror.txt to read it
number_of_errors = 0  # This sets the number of errors to 0 to later count the errors
read_errors = errors.read()  # This reads loginerror.txt
# This splits the contents of loginerror.txt into a list
errors_list = read_errors.split("\n")

for user in errors_list:  # Loops through each user in the list we made above
    if user:  # This counts the number of errors
        number_of_errors += 1
if " " in errors_list:  # This ignores blank lines, happens from time to time.
    number_of_errors = number_of_errors - 1

# This specifies the number of times the bot will retry logins when connections are closed. I recommend you leave it alone.
number_of_attempts = 30
# This checks if it is the first login attempt or not. If not, continues.
while number_of_attempts > 0:
    # This checks if there are any errors left. If there are errors, it continues.
    if number_of_errors > 0:
        retry_login(MFR_secret)  # This attempts login again
    # This subtracts 1 from the number of attemots so that it only retries a specified number of times.
    number_of_attempts = number_of_attempts - 1

jidlist_file = open("jidlist.txt", "r")
jidlist_read = jidlist_file.read()
jid_list = jidlist_read.split("\n")
# keep_alive()
time.sleep(0.02)  # Slight delay so stuff doesnt spam
print(bcolors.OKGREEN + emoji.emojize("\n:black_small_square: \"Spam [JID or Username] w/ [Message]\" - Used to spam a user's PMs.\n:black_small_square: \"Spam Gif [JID or Username] w/ [Query]\" - Used to spam a user's PMs with a gif.\n:black_small_square: \"Poke [JID or username] w/ [Message]\" - Used for forwarding a single message to a user.\n:black_small_square: \"Poke Gif [JID or username] w/ [Query]\" - Used for forwarding a single gif to a user.\n:black_small_square: \"Friend\" - Used to add the bot as a friend so that you can add it to groups.\n:black_small_square: \"SendFriend [JID or Username]\" - Used to send a friend attribution request to a user.\n:black_small_square: \"GroupSpam [Message]\" - Used to spam the group that this command is used in.\n:black_small_square: \"GroupSpam Gif [Query]\" - Used to spam the group that this command is used in with gifs.\n:black_small_square: \"Gif [Query]\" - Used to send a single gif in the group that this command is used in.\n:black_small_square: \"Leave [GJID]\" - Used for making your bot(s) leave groups.\n") + bcolors.ENDC)  # This explains the commands to the user
print(bcolors.OKBLUE + emoji.emojize("\n:warning: You can now use the botnet.\n") +
      bcolors.ENDC)  # This lets the user know the botnet is ready
clear = open("loginretry.txt", "w+")  # This clears the Loginretry.txt file
clear.close()  # This closes the file, always a good practice.

# This keeps the bot idle. (spam is just the variable that happens to be convenient for a while loop)
while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
    # This checks if the user has typed anything into the console
    in_console_message = input("")
    # If they type ping, it will say pong pack.
    if in_console_message.lower() == "ping":
        print(bcolors.OKGREEN + emoji.emojize("\nDADDY.\n") + bcolors.ENDC)
    else:  # If they do not type ping, it reminds them that commands must be sent to the kik bots.
        print(bcolors.FAIL + emoji.emojize("\n:warning: You can't use commands directly in the console! You need to message your bots on Kik.") + bcolors.ENDC)
