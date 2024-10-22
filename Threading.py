import random
import time
import threading

# Global flag to control thread execution
running = True

# Define a function that simulates the task of displaying random values
def task(lb, ub, refresh_time, display_location):
    global running
    while running:
        num = random.randint(lb, ub)
        print(f"{display_location}: {num} (Range: [{lb}, {ub}]) Refresh every {refresh_time}s")
        time.sleep(refresh_time)

# Create threads for each task with specified ranges and refresh times
t1 = threading.Thread(target=task, args=(10, 20, 10, 'D1'))
t2 = threading.Thread(target=task, args=(-10, 10, 20, 'D2'))
t3 = threading.Thread(target=task, args=(-100, 0, 8, 'D3'))
t4 = threading.Thread(target=task, args=(0, 20, 12, 'D4'))
t5 = threading.Thread(target=task, args=(-40, 40, 16, 'D5'))
t6 = threading.Thread(target=task, args=(100, 200, 14, 'D6'))

# Start all threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

# Keep the main thread running to listen for input
try:
    while True:
        time.sleep(0.1)  # Keeps the main thread alive without busy-waiting
except KeyboardInterrupt:
    running = False
    print("Stopping all threads...")
    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    print("All threads have been stopped.")
