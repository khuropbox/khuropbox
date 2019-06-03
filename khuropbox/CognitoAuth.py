import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#id108

class Cognito:
    region = 'ap-northeast-2'
    user_pool_id = 'ap-northeast-2_mzexrHyOT'
    app_client_id = '3mum9jtphuqbvmojfv0umhobc3'
    identity_pool_id = 'ap-northeast-2:7355f3db-8b2a-4548-9a56-becce8221aee'
    account_id = 'wjdekdms001'
    token = ''
    credential = {}

    def sign_up(self, username, password, email, UserAttributes):
        client = boto3.client('cognito-idp')
        response = client.sign_up(ClientId=self.app_client_id,
                                  Username=username,
                                  Password=password,
                                  UserAttributes=[{'Name': 'email', 'Value': email}])
        return response

    def confirm_sign_up(self, username, confirm_code):
        client = boto3.client('cognito-idp')
        response = client.confirm_sign_up(ClientId=self.app_client_id,
                                          Username=username,
                                          ConfirmationCode=confirm_code)
        return response

    def sign_in_admin(self, username, password):
        # Get ID Token
        idp_client = boto3.client('cognito-idp')
        response = idp_client.admin_initiate_auth(UserPoolId=self.user_pool_id,
                                              ClientId=self.app_client_id,
                                              AuthFlow='ADMIN_NO_SRP_AUTH',
                                              AuthParameters={'USERNAME': username,'PASSWORD': password})

        provider = 'cognito-idp.%s.amazonaws.com/%s' % (self.region, self.user_pool_id)
        self.token = response['AuthenticationResult']['IdToken']

        # Get IdentityId
        ci_client = boto3.client('cognito-identity')
        response = ci_client.get_id(AccountId=self.account_id,
                                IdentityPoolId=self.identity_pool_id,
                                Logins={provider: self.token})

        # Get Credentials
        response = ci_client.get_credentials_for_identity(IdentityId=response['IdentityId'],
                                                      Logins={provider: self.token})
        return response

    def SetUserCredential(self, credential):
        self.credential = credential