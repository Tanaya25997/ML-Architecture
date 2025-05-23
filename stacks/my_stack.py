from aws_cdk import Stack
from constructs import Construct
from constructs.my_bucket import MyBucket

class MyStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        my_bucket = MyBucket(self, "researchbuckettanaya", versioned=True)