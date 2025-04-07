###defining resuable constructs


from aws_cdk import aws_s3 as s3, RemovalPolicy


from constructs import Construct

class MyBucket(Construct):
    def __init__(self, scope: Construct, id: str, *, versioned=False):
        super().__init__(scope, id)

        self.bucket = s3.Bucket(
            self, 
            "ReusableBucket",
            versioned = versioned,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects=True

        )