# Transit dwell time estimator 

An algorithm to calculate station dwell times for public transit (buses/metros) based on transit stop boarding and alighting data. 

This small project was developed as part of coursework in Public Transportation Systems (CVL746) taught by Prof. Pramesh Kumar at IIT Delhi.

## Algorithm

Dwell time is not simply a static number but it depends dynamically on passenger flow, vehicle capacity, and operating environment. This algorithm calculates the total dwell time ($t_d$) at any given stop using the following parameters:

- **Alighting Time:** 2.0 seconds per passenger.
- **Boarding Time (Seated):** 3.5 seconds per passenger.
- **Boarding Time (Standee):** 4.0 seconds per passenger (incorporates friction/crowding penalty).
- **Door Operation Time:** 4.0 seconds per stop.
- **Vehicle Capacity:** 40 passengers.

### Logic Flow:
1. **Boarding/Alighting:** Passengers Board and fill up the seats/Passengers alight, freeing up capacity.
2. **Capacity Check:** The algorithm tracks current onboard passengers.
3. **Standee Penalty:** As passengers board, if the vehicle exceeds its seated capacity, a higher time penalty is applied to the remaining boarding passengers to simulate the friction of entering a crowded vehicle.
4. **Total Calculation:** `Dwell Time = Alighting Time + Boarding Time + Door Time`


## Why Dwell Time Matters

According to the **Transit Capacity and Quality of Service Manual (TCQSM)**, dwell time is a fundamental variable that dictates the performance, capacity, and reliability of an entire transit network. 

### 1. Role in Transit Corridor Capacity Calculation
Transit corridor (facility) capacity is determined by the capacity of its most constrained node—the "critical bus stop." 
The capacity of a bus loading area ($B_l$) is strictly governed by the amount of time a vehicle occupies it. This occupation time is the sum of **Dwell Time ($t_d$)** and **Clearance Time ($t_c$)**. 

The loading area capacity is calculated using the formula:
$$B_l = \frac{3600(g/C)}{t_c + t_d(g/C) + t_{om}}$$
(Where g/C is the green time ratio and $t_{om}$ is the operating margin).

Because dwell time ($t_d$) is the denominator, **an increase in dwell time decreases the maximum number of buses (and consequently, the person capacity) that can pass through the corridor per hour.**

### 2. Impact on Quality of Service (QoS)
QoS is the overall measured or perceived performance of the transit service from the passenger's point of view. Dwell time influences QoS in several ways:
* **Travel Time & Speed:** Longer dwell times reduce the commercial speed of the route, making transit less competitive against private automobiles.
* **Passenger Comfort:** Extended boarding/alighting times are often a symptom of extreme onboard crowding (standees), which directly lowers the perceived comfort and convenience for the user.

### 3. Mitigating Bus Bunching and Improving Operations
**Bus bunching** is a notoriously difficult operational issue. It occurs when a transit vehicle experiences a slight delay (e.g., higher-than-normal passenger demand at a stop). This increases its dwell time. Because the bus is delayed, the gap between it and the vehicle ahead grows, resulting in even more passengers accumulating at downstream stops. The delayed bus gets slower, while the bus behind it catches up (because it has fewer passengers to pick up and shorter dwell times), eventually causing them to "bunch" together.



## Project Structure

- `dwell_time.py`: The main algorithm script.
- `data/`: Contains the sample input data (`OD_MAGENTA...xlsx`).
- `requirements.txt`: Python dependencies.

## References / Acknowledgments

* "Transit capacity and quality of service" by Prof. Pramesh Kumar for the course CVL746: Public Transportation Systems at the Indian Institute of Technology (IIT) Delhi. Available at: [tcqs.pdf](https://prameshk.github.io/CVL746/Lec/tcqs.pdf)
