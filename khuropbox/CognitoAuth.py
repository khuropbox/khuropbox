import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#id108

class Cognito():
    region = 'us-west-2'
    user_pool_id = 'us-west-2_2wqn8wLUE'
    app_client_id = '3qbuc7gaje6nftsqa7aduptnfn'
    identity_pool_id = 'us-west-2:bfca573d-3cfc-42c7-8310-ff9c0218101d'
    account_id = 'wjdekdms001'
    token = ''

    def sign_up(self, username, password, UserAttributes):
        client = boto3.client('cognito-idp', self.region)
        response = client.sign_up(ClientId=self.app_client_id,
                                  Username=username,
                                  Password=password,
                                  UserAttributes=UserAttributes)
        return response

    def confirm_sign_up(self, username, confirm_code):
        client = boto3.client('cognito-idp', self.region)
        response = client.confirm_sign_up(ClientId=self.app_client_id,
                                          Username=username,
                                          ConfirmationCode=confirm_code)
        return response

    def sign_in_admin(self, username, password):
        # Get ID Token
        idp_client = boto3.client('cognito-idp', self.region)
        response = idp_client.admin_initiate_auth(UserPoolId=self.user_pool_id,
                                              ClientId=self.app_client_id,
                                              AuthFlow='ADMIN_NO_SRP_AUTH',
                                              AuthParameters={'USERNAME': username,'PASSWORD': password})

        provider = 'cognito-idp.%s.amazonaws.com/%s' % (self.region, self.user_pool_id)
        self.token = response['AuthenticationResult']['IdToken']

        # Get IdentityId
        ci_client = boto3.client('cognito-identity', self.region)
        response = ci_client.get_id(AccountId=self.account_id,
                                IdentityPoolId=self.identity_pool_id,
                                Logins={'provider': self.token})

        # Get Credentials
        response = ci_client.get_credentials_for_identity(IdentityId=response['IdentityId'])
        return response