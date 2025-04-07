#!/usr/bin/env python3
import os

import aws_cdk as cdk


#from ml_research_cdk.ml_research_cdk_stack import MlResearchCdkStack

from stacks.my_stack import MyStack

app = cdk.App()
MyStack(app, "MlResearchCdkStack", 
        stack_name="research-stack-storage", 
        env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')), 
    )

app.synth()
