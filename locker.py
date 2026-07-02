import time

last_activity = time.time()

LOCK_TIME = 60

def update_activity():

    global last_activity

    last_activity = time.time()

def should_lock():

    return (

        time.time() - last_activity

    ) > LOCK_TIME