import asyncio
import logging
import sys
import os

from temporalio.client import Client, TLSConfig
from temporalio.service import WorkflowService 
from temporalio.api.common.v1 import WorkflowExecution

from temporalio.api.workflowservice.v1 import DeleteWorkflowExecutionRequest

async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(message)s")
    
    args = sys.argv[1:]
    if len(args) != 3:
        logging.error("Insufficient arguments. Expecting namespace, workflowId and runId")
        exit(1)
    
    namespace = args[0]
    workflowId = args[1]
    runId = args[2]
    logging.info("Attempting to delete workflow history in namespace %s, workflow ID %s, and run ID %s", 
                 namespace, workflowId, runId)
    

    # Get client 
    address = os.getenv("TEMPORAL_ADDRESS","127.0.0.1:7233")
    temporalNamespace = os.getenv("TEMPORAL_NAMESPACE","default")
    tlsCertPath = os.getenv("TEMPORAL_TLS_CERT","")
    tlsKeyPath = os.getenv("TEMPORAL_TLS_KEY","")
    tls = None

    if tlsCertPath and tlsKeyPath:
        with open(tlsCertPath,"rb") as f:
            cert = f.read()
        with open(tlsKeyPath,"rb") as f:
            key = f.read()
                    
        tls = TLSConfig(client_cert=cert,
                        client_private_key=key)

    client = await Client.connect(
        target_host=address, 
        namespace=temporalNamespace,
        tls=tls
    )

    # Delete the workflow history
    # Note that it is possible to have multiple histories with the same 
    # workflow_id, which is why a run_id can be used to specify 
    # exactly which workflow history to delete

    response = await client.workflow_service.delete_workflow_execution(
        DeleteWorkflowExecutionRequest(
            namespace=client.namespace,
            workflow_execution=WorkflowExecution(workflow_id=workflowId,run_id=runId),
        )
    )
    
    # Response doesn't print anything. Figure out what fields/methods are available
    logging.info("Complete. Response is %s", response)

    exit(0)

if __name__ == "__main__":
    asyncio.run(main())