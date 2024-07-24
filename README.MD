# delete-workflow-execution-python
This example shows how to delete a specific workflow history using the Temporal Python SDK

## Set up Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
pip install temporalio
```

## Run Locally
Be sure you set up your Python Virtual Environment before running the worker

```bash
python main.py <namespace> <workflow_id> <run_id>
```

## Run Worker using Temporal Cloud
Be sure you set up your Python Virtual Environment before running the worker

```bash
# set up environment variables
export TEMPORAL_NAMESPACE=<namespace>.<accountId>
export TEMPORAL_ADDRESS=<namespace>.<accountId>.tmprl.cloud:7233
export TEMPORAL_TLS_CERT=/path/to/cert
export TEMPORAL_TLS_KEY=/path/to/key
# run the application
python main.py <namespace> <workflow_id> <run_id>
```

