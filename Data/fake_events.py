from fake_web_events import Simulation

simulation = Simulation(user_pool_size=100, sessions_per_day=10000)
events = simulation.run(duration_seconds=10)
for event in events:
    print(event)