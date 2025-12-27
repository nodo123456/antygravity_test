import dlt
import requests
import os

@dlt.resource(table_name="github_events", write_disposition="replace")
def github_events(username):
    """
    Fetches public events for a GitHub user.
    """
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    yield response.json()

def load_data():
    # Create a pipeline connected to a local DuckDB file
    pipeline = dlt.pipeline(
        pipeline_name="github_activity",
        destination=dlt.destinations.duckdb("mds_box.duckdb"),
        dataset_name="raw_github"
    )
    
    # Run the pipeline
    # We use 'nodo123456' as the target user
    load_info = pipeline.run(github_events("nodo123456"))
    print(load_info)

if __name__ == "__main__":
    load_data()
