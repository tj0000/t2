import os
from dotenv import load_dotenv
from aws_cdk import Environment, Stack, aws_lambda, Duration, App
from constructs import Construct

load_dotenv()

AWS_ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")
AWS_REGION = os.environ.get("AWS_REGION")
AWS_ENV = Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION)


class MainStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        lambda_image = aws_lambda.EcrImageCode.from_asset_image(
            directory=os.path.join(os.getcwd(), "service")
        ) 

        aws_lambda.Function(self, 
        id="service_lambda", 
        function_name="service_lambda", 
        handler=aws_lambda.Handler.FROM_IMAGE, 
        runtime=aws_lambda.Runtime.FROM_IMAGE,
        memory_size=128,
        timeout=Duration.seconds(30),
        code=lambda_image
        )


app = App()
MainStack(app, "MainStack", env=AWS_ENV)
app.synth()