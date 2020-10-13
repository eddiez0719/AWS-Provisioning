import boto3

client = boto3.client('ec2')

response = client.describe_instances(
    Filters=[
        {

        }
    ]
)
dic = response['Reservations']
for k in dic:
    for i in k['Instances']:
        for t in i['Tags']:
            if 'Clinic' not in t['Key']:
                print(t, i['InstanceId'])