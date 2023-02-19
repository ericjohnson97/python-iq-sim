import iq_sim
import os
from pymavlink import mavutil


token = os.getenv("IQ_SIM_TOKEN")

api = iq_sim.iq_sim(token)
sim_id = api.start_sim()
api.wait_for_sim_ready(sim_id)

connection_info = api.get_connection(sim_id)
print(connection_info)
conn_str = f"tcp:{connection_info['ip']}:{connection_info['port']}"

mavlink_conn = mavutil.mavlink_connection(conn_str)
mavlink_conn.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (mavlink_conn.target_system, mavlink_conn.target_system))

# add pymavlink script here

api.stop_sim(sim_id)
