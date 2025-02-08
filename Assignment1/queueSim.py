import numpy as np
import matplotlib.pyplot as plt

def geometric_distribution(p):
    return np.random.geometric(p) - 1  # Adjust for zero-based index

def simulate_queue(lambda_val, mu, time_slots=10**6):
    queue_length = 0
    total_queue_length = 0
    total_wait_time = 0
    packet_count = 0
    
    p_arrival = lambda_val
    p_service = mu
    
    for _ in range(time_slots):
        if np.random.rand() < p_arrival:  # Packet arrival
            queue_length += 1
            packet_count += 1
        
        if queue_length > 0 and np.random.rand() < p_service:  # Service completion
            queue_length -= 1
            total_wait_time += queue_length
        
        total_queue_length += queue_length
    
    avg_queue_length = total_queue_length / time_slots
    avg_queue_delay = avg_queue_length / lambda_val if lambda_val > 0 else 0  # Little's Law
    
    return avg_queue_length, avg_queue_delay

def theoretical_delay(lambda_vals, mu):
    return [1 / (mu - l) if l < mu else float('inf') for l in lambda_vals]  # M/M/1 formula

# Parameters
mu = 0.75
lambda_vals = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]

theoretical_results = theoretical_delay(lambda_vals, mu)
simulated_results = [simulate_queue(l, mu) for l in lambda_vals]

# Extract simulation results
simulated_delays = [result[1] for result in simulated_results]

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(lambda_vals, theoretical_results, label='Theoretical Delay', linestyle='dashed', color='red')
plt.plot(lambda_vals, simulated_delays, label='Simulated Delay', marker='o', color='blue')
plt.xlabel('Arrival Rate (Lambda)')
plt.ylabel('Expected Queueing Delay')
plt.title('Queueing Delay vs Arrival Rate')
plt.legend()
plt.grid()
plt.show()
