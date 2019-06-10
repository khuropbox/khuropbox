import boto3
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#id108

class Cognito():
    region = config['cognito']['region']
    user_pool_id = config['cognito']['user_pool_id']
    app_client_id = config['cognito']['app_client_id']
    identity_pool_id = config['cognito']['identity_pool_id']
    account_id = config['cognito']['account_id']
    token = ''

    def sign_up(self, username, password, UserAttributes):
        client = boto3.client('cognito-idp', self.region,
                            aws_access_key_id=config['aws']['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=config['aws']['AWS_SECRET_ACCESS_KEY'])

        response = client.sign_up(ClientId=self.app_client_id,
                                  Username=username,
                                  Password=password,
                                  UserAttributes=UserAttributes)
        return response

    def confirm_sign_up(self, username):
        client = boto3.client('cognito-idp', self.region,
                            aws_access_key_id=config['aws']['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=config['aws']['AWS_SECRET_ACCESS_KEY'])

        response = client.admin_confirm_sign_up(UserPoolId=self.user_pool_id, Username=username)
        return response

    def sign_in_admin(self, username, password):
        # Get ID Token
        idp_client = boto3.client('cognito-idp', self.region,
                            aws_access_key_id=config['aws']['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=config['aws']['AWS_SECRET_ACCESS_KEY'])

        response = idp_client.admin_initiate_auth(UserPoolId=self.user_pool_id,
                                              ClientId=self.app_client_id,
                                              AuthFlow='ADMIN_NO_SRP_AUTH',
                                              AuthParameters={'USERNAME': username,'PASSWORD': password})

        provider = 'cognito-idp.%s.amazonaws.com/%s' % (self.region, self.user_pool_id)
        self.token = response['AuthenticationResult']['IdToken']

        # Get IdentityId
        ci_client = boto3.client('cognito-identity', self.region,
                            aws_access_key_id=config['aws']['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=config['aws']['AWS_SECRET_ACCESS_KEY'])

        response = ci_client.get_id(AccountId=self.account_id,
                                IdentityPoolId=self.identity_pool_id,
                                Logins={provider: self.token})

        # Get Credentials
        response = ci_client.get_credentials_for_identity(IdentityId=response['IdentityId'], Logins={provider: self.token})
        return response
