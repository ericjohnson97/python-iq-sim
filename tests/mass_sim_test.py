import iq_sim
import unittest
import os
import time
from pymavlink import mavutil
import multiprocessing

token = os.getenv("IQ_SIM_TOKEN")

def test_create_sim(i):
    try:
        print("test_create_sim")
        api = iq_sim.iq_sim(token)
        sim_id = api.start_sim()
        print(f"sim {i} created with id {sim_id}")
        api.wait_for_sim_ready(sim_id)
        
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        for job in jobs:
            job.terminate()
            job.join()
    finally:
        print("Exiting script")

if __name__ == "__main__":
    # Create a list of jobs and then iterate through
    # the number of processes appending each process to
    # the job list 
    jobs = []
    for i in range(5): # You have 3 test_create_sim calls
        process = multiprocessing.Process(target=test_create_sim, args=(i,))    
        jobs.append(process)
    
    # Start the processes
    for job in jobs:
        job.start()

    try:
        # Ensure all of the processes have finished
        for job in jobs:
            job.join()
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        for job in jobs:
            job.terminate()
            job.join()
    finally:
        print("Exiting main script")
