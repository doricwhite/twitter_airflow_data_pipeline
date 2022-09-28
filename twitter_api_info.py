# Replace the '#' with your Twitter API information

class TwitterApiInfo:
    def __init__(self):
        self.api_key = '' 
        self.api_secret_key = '' 
        self.access_token = ''
        self.access_token_secret = '' 
    
    def apiKey(self):
        self.api_key = '#' 
        return self.api_key
    
    def apiSecretKey(self):
        self.api_secret_key = '#'
        return self.api_secret_key
    
    def accessToken(self):
        self.access_token = '#'
        return self.access_token
    
    def accessTokenSecret(self):
        self.access_token_secret = '#'
        return self.access_token_secret