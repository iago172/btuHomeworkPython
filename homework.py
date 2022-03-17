import boto3

s3 = boto3.client('s3')
def main():
    response = s3.list_buckets()
    print("all backet list:")
    for bucket in response['Buckets']:
        print(f' {bucket["Name"]}')
def listbuckStartProd():
    response = s3.list_buckets()
    print("backet list which start 'prod':")
    for prodbucket in response['Buckets']:
        if prodbucket["Name"].startswith('prod'):
            print(f' {prodbucket["Name"]}')

if __name__== '__main__':
    main()
    print("*"*50)
    listbuckStartProd()