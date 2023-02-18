# Table of Contents

* [iq\_sim](#iq_sim)
  * [iq\_sim](#iq_sim.iq_sim)
    * [get\_sim\_capabilities](#iq_sim.iq_sim.get_sim_capabilities)
    * [get\_running\_simulations](#iq_sim.iq_sim.get_running_simulations)
    * [stop\_sim](#iq_sim.iq_sim.stop_sim)
    * [stop\_all\_sims](#iq_sim.iq_sim.stop_all_sims)
    * [start\_sim](#iq_sim.iq_sim.start_sim)
    * [get\_connection](#iq_sim.iq_sim.get_connection)
    * [wait\_for\_sim\_ready](#iq_sim.iq_sim.wait_for_sim_ready)

<a id="iq_sim"></a>

# iq\_sim

<a id="iq_sim.iq_sim"></a>

## iq\_sim Objects

```python
class iq_sim()
```

<a id="iq_sim.iq_sim.get_sim_capabilities"></a>

#### get\_sim\_capabilities

```python
def get_sim_capabilities()
```

gets the capabilities of the Intelligent Quads cloud simulation service

**Returns**:

- `Dict` - dict containing information of the different simulation options available

<a id="iq_sim.iq_sim.get_running_simulations"></a>

#### get\_running\_simulations

```python
def get_running_simulations(sim_id: str = None)
```

gets a list of running simulations for a user
if providing a sim_id, will return only return info for that sim_id

**Arguments**:

- `sim_id` _str, optional_ - unique id of a simulation. Defaults to None.
  

**Returns**:

- `Dict` - dict in form of {"running_sims": [{"status": str, "sim_id": str, "fc_instances": str, "creation_time" : str}]}

<a id="iq_sim.iq_sim.stop_sim"></a>

#### stop\_sim

```python
def stop_sim(sim_id: str)
```

stop a simulation running in the Intelligent Quads cloud
will exit 1 if there is an error

**Arguments**:

- `sim_id` _str_ - sim_id of the simulation to stop
  

**Returns**:

- `Dict` - dict in form of {"status": str, "sim_id": str}

<a id="iq_sim.iq_sim.stop_all_sims"></a>

#### stop\_all\_sims

```python
def stop_all_sims()
```

Stops all of a users simulations running in the Intelligent Quads cloud

**Returns**:

- `List` - list of dicts in form of {"status": str, "sim_id": str}

<a id="iq_sim.iq_sim.start_sim"></a>

#### start\_sim

```python
def start_sim(sim_config=None) -> str
```

create a new simulation running in the Intelligent Quads cloud

**Arguments**:

- `sim_config` _Dict, optional_ - configuration for the simulation.
  

**Returns**:

- `str` - sim_id of the simulation

<a id="iq_sim.iq_sim.get_connection"></a>

#### get\_connection

```python
def get_connection(sim_id: str)
```

get the ip address and port of the mavlink interface running in the Intelligent Quads cloud

**Arguments**:

- `sim_id` _str_ - unique id of the simulation
  

**Returns**:

- `Dict` - dict in form of {"status": str, "ip": str, "port": int}

<a id="iq_sim.iq_sim.wait_for_sim_ready"></a>

#### wait\_for\_sim\_ready

```python
def wait_for_sim_ready(sim_id: str, timeout: int = 80)
```

wait for the simulation to be deployed and running in the Intelligent Quads cloud
Note: During High Traffic times, it can take up to a couple of minutes to start a simulation.
try setting timeout higher or try again later.

function will exit 1 if the simulation fails to start

**Arguments**:

- `sim_id` _str_ - unique id of the simulation
- `timeout` _int, optional_ - Defaults to 80.

