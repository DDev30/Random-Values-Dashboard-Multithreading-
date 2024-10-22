from flask import Flask, render_template, jsonify, request
import random
import threading
import time

app = Flask(__name__)


random_values = {
    'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0
}


running = True


def update_value(lb, ub, refresh_time, key):
    global running
    while running:
        random_values[key] = random.randint(lb, ub)
        time.sleep(refresh_time)


threads = [
    threading.Thread(target=update_value, args=(10, 20, 10, 'D1')),
    threading.Thread(target=update_value, args=(-10, 10, 20, 'D2')),
    threading.Thread(target=update_value, args=(-100, 0, 8, 'D3')),
    threading.Thread(target=update_value, args=(0, 20, 12, 'D4')),
    threading.Thread(target=update_value, args=(-40, 40, 16, 'D5')),
    threading.Thread(target=update_value, args=(100, 200, 14, 'D6'))
]

# Start all threads
for thread in threads:
    thread.daemon = True
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_values')
def get_random_values():
    return jsonify(random_values)

@app.route('/stop', methods=['POST'])
def stop():
    global running
    running = False
    return "Stopping the background threads!"

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        running = False
        print("Server is stopping...")
