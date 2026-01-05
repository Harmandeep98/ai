import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking chai order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Breqing chai for #{i}")
        time.sleep(3)

# create threads
order_thread = threading.Thread(target=take_orders)
brew_chai = threading.Thread(target=brew_chai);

order_thread.start()
brew_chai.start()

order_thread.join()
brew_chai.join()

print(f"All orders taken and chai brewed")