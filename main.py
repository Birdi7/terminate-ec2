import boto3
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter()

ids = list(map(lambda item: item.id, instances))

ec2.instances.filter(InstanceIds=ids).terminate()