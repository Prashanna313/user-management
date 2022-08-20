# user_management_client_v1.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/api/v1/users*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users**](DefaultApi.md#get_users) | **GET** /v1/users | get users


# **get_users**
> GetUsersResponse get_users(x_correlation_id=x_correlation_id, email=email, user_ids=user_ids)

get users

By passing in the appropriate options, you can search for available users in the system 

### Example

```python
from __future__ import print_function
import time
import user_management_client_v1
from user_management_client_v1.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/api/v1/users
# See configuration.py for a list of all supported configuration parameters.
configuration = user_management_client_v1.Configuration(
    host = "https://virtserver.swaggerhub.com/api/v1/users"
)


# Enter a context with an instance of the API client
with user_management_client_v1.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_management_client_v1.DefaultApi(api_client)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
email = 'email_example' # str |  (optional)
user_ids = ['user_ids_example'] # list[str] |  (optional)

    try:
        # get users
        api_response = api_instance.get_users(x_correlation_id=x_correlation_id, email=email, user_ids=user_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_correlation_id** | **str**|  | [optional] 
 **email** | [**str**](.md)|  | [optional] 
 **user_ids** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**GetUsersResponse**](GetUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A List of Users |  * X-Correlation-ID -  <br>  |
**400** | Validation error |  * X-Correlation-ID -  <br>  |
**500** | Internal server error |  * X-Correlation-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

