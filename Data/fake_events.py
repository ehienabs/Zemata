from fake_web_events import Simulation
from google.cloud import pubsub_v1

publisher_options = pubsub_v1.types.PublisherOptions(enable_message_ordering=True)
client_options = {"api_endpoint":"us-east1-pubsub.googleapis.com:443"}
publisher = pubsub_v1.PublisherClient(
    publisher_options = publisher_options, client_options = client_options
)
project_id = "zematadata"
topic_id = "zematadata"
topic_path = publisher.topic_path(project_id, topic_id)
simulation = Simulation(user_pool_size=100, sessions_per_day=10000)
events = simulation.run(duration_seconds=10)


for event in events:
    events = list(events)
    future = publisher.publish(topic_path, str.encode(str(event)), "utf-8")
future.result()