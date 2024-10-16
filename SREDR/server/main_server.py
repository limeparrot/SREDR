from multiprocessing import Process
from log_processing import log_monitor,app
from log_collector import start_log_collector
from create_db import create_db
#from flask import Flask

def main():
    create_db()
    p1 = Process(target=start_log_collector)
    p1.start()
    #p2 = Process(target=log_monitor)
    #p2.start()
    #p1.join()
    #p2.join()
    app.run(debug=True)

if __name__ == '__main__':
    main()