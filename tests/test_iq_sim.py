import iq_sim
import unittest
import os
import time
from pymavlink import mavutil


token = os.getenv("IQ_SIM_TOKEN")

class TestIqSim(unittest.TestCase):
    def test_create_sim(self):
        print("test_create_sim")
        api = iq_sim.iq_sim(token)
        result = api.start_sim()
        print(result)
        

    def test_get_running_sims(self):
        print("test_get_running_sims")
        api = iq_sim.iq_sim(token)
        result = api.get_running_simulations()
        print(result)

    def test_stop_sim(self):
        print("test_stop_sim")
        api = iq_sim.iq_sim(token)
        sim_id = api.start_sim()
        running_sims = api.get_running_simulations()
        time_start = time.time()
        while time.time() - time_start < 10:
            for sim in running_sims['running_sims']:
                if sim['sim_id'] == sim_id:
                    print("sim is running")
                    return
        print(running_sims)
        result = api.stop_sim(sim_id)
        print(result)

    def test_get_connection(self):
        print("test_get_connection")
        api = iq_sim.iq_sim(token)
        sim_id = api.start_sim()
        api.wait_for_sim_ready(sim_id)

        connection_info = api.get_connection(sim_id)
        print(connection_info)
        conn_str = f"tcp:{connection_info['ip']}:{connection_info['port']}"
        
        mavlink_conn = mavutil.mavlink_connection(conn_str)
        mavlink_conn.wait_heartbeat()
        print("Heartbeat from system (system %u component %u)" % (mavlink_conn.target_system, mavlink_conn.target_system))

        att_msg = mavlink_conn.recv_match(type='ATTITUDE', blocking=True)
        print(att_msg)
        api.stop_sim(sim_id)
        time.sleep(1)

    def test_stop_all(self):
        api = iq_sim.iq_sim(token)
        sim_id1 = api.start_sim()
        sim_id2 = api.start_sim()
        time.sleep(5)
        result = api.stop_all_sims()
        result = api.get_running_simulations()
        # asset that there are no running sims
        self.assertEqual(len(result['running_sims']), 0)
        


if __name__ == "__main__":
    # api = iq_sim.iq_sim(token)
    # result = api.stop_all_sims()
    unittest.main()
