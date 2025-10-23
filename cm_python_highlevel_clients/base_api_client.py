# clients/base_client.py
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class BaseClient:
    """
    Base client that provides access to all low-level APIs.
    All specialized clients inherit from this.
    """
    
    def __init__(self, api_token: str, host: Optional[str] = None):
        """
        Initialize the base client.
        
        Args:
            api_token: API access token (required)
            host: API host URL (optional, uses default if not provided)
        """
        from cm_python_openapi_sdk import ApiClient, Configuration
        
        # Create configuration
        config = Configuration()
        if host:
            config.host = host
        
        # Create API client
        self._api_client = ApiClient(configuration=config)
        self._api_cache = {}
        
        # Exchange token for bearer token
        self.exchange_token(api_token)
    
    @property
    def api_client(self):
        """Access to the raw API client."""
        return self._api_client
    
    def exchange_token(self, api_token: str) -> str:
        """
        Exchange an API token for a bearer token and configure the API client to use it.
        
        Args:
            api_token: The API access token to exchange
            
        Returns:
            The bearer token string
            
        Raises:
            Exception: If token exchange fails
        """
        from cm_python_openapi_sdk.models.token_request_dto import TokenRequestDTO
        
        logger.info("Exchanging API token for bearer token")
        
        # Create the token request
        token_request = TokenRequestDTO(refresh_token=api_token)
        
        # Get the authentication API and call get_token
        auth_api = self._get_api('AuthenticationApi')
        token_response = auth_api.get_token(token_request_dto=token_request)
        
        # Extract the bearer token from the response
        bearer_token = token_response.access_token
        
        # Configure the API client to use the bearer token
        self._api_client.configuration.access_token = bearer_token
        
        logger.info("Successfully exchanged token and configured API client")
        
        return bearer_token
    
    def _get_api(self, api_class_name: str):
        """
        Helper to lazily instantiate API classes.
        
        Args:
            api_class_name: Name of the API class (e.g., 'JobsApi', 'DataUploadApi')
            
        Returns:
            Instance of the requested API class
        """
        if api_class_name not in self._api_cache:
            # Dynamically import the API class
            import importlib
            module = importlib.import_module(f'cm_python_openapi_sdk.api.{self._to_snake_case(api_class_name)}')
            api_class = getattr(module, api_class_name)
            self._api_cache[api_class_name] = api_class(self._api_client)
        return self._api_cache[api_class_name]
    
    def _to_snake_case(self, class_name: str) -> str:
        """
        Convert PascalCase to snake_case for module names.
        
        Args:
            class_name: Class name in PascalCase (e.g., 'JobsApi')
            
        Returns:
            Module name in snake_case (e.g., 'jobs_api')
        """
        import re
        # Insert underscore before uppercase letters and convert to lowercase
        snake = re.sub('([A-Z]+)', r'_\1', class_name).lower()
        return snake.lstrip('_')
    
    def __getattr__(self, name: str):
        """
        Automatically expose all *Api classes from generated SDK.
        Usage: client.jobs_api, client.data_upload_api, etc.
        
        Args:
            name: Attribute name in snake_case ending with '_api'
            
        Returns:
            Instance of the requested API class
            
        Raises:
            AttributeError: If the attribute doesn't exist
        """
        if name.endswith('_api'):
            # Convert snake_case to PascalCase
            class_name = ''.join(word.capitalize() for word in name.split('_'))
            try:
                return self._get_api(class_name)
            except (ImportError, AttributeError):
                pass
        
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")
