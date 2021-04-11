import multiprocessing
def mpwrap(func,*input_args):
    p = multiprocessing.Process(target=func, args=input_args)
    p.start()
    p.join()

