# import threading
# import time


# def process_one():
#     i = 0
#     while i < 3:
#         print("OOOOOO")
#         time.sleep(0.3)
#         i += 1


# def process_two():
#     i = 0
#     while i < 3:
#         print("XXXXXX")
#         time.sleep(0.3)
#         i += 1

# th1 = threading.Thread(target=process_one)
# th2 = threading.Thread(target=process_two)

# th1.start()
# th2.start()


# th1.join()
# th2.join()

# print("Fin du programme")




# import threading
# import time


# class MyProcess(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)

#     def run(self):
#         i = 0
#         while i < 3:
#          print(threading.current_thread())
#          time.sleep(0.3)
#          i += 1




# th1=MyProcess()
# th2=MyProcess()

# th1.start()
# th2.start()


# th1.join()
# th2.join()

# print("Fin du programme")











# import threading
# import time

# #my_lock = threading.RLock


# class MyProcess(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)

#     def run(self):
#         i = 0
#         while i < 3:
#           letters = "ABC"
#           for lt in letters:
#              print(lt)
#              time.sleep(0.3)
#           i += 1




# th1=MyProcess()
# th2=MyProcess()

# th1.start()
# th2.start()


# th1.join()
# th2.join()

# print("Fin du programme")







import threading
import time

my_lock = threading.RLock()


class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i < 3:
          with my_lock:
           letters = "ABC"
           for lt in letters:
              print(lt)
              time.sleep(0.3)
          i += 1




th1=MyProcess()
th2=MyProcess()

th1.start()
th2.start()


th1.join()
th2.join()

print("Fin du programme")