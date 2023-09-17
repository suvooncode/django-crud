import asana
from asana.rest import ApiException
class AsanaApi :

    def create_asana_task(title, description):
        # Initialize the Asana client with your personal access token
        # client = asana.Client.access_token('')
        configuration = asana.Configuration()
        configuration.access_token = '1/1205492548060687:1b8e3277f1609e6e8f2128cb505da097'
        api_client = asana.ApiClient(configuration)

        api_instance = asana.TasksApi(api_client)
        body = asana.TasksBody({"name": title, "notes": description,}) # TasksBody | The task to create.

        # api_response = api_instance.create_task(body, opt_fields=[])
        try:
            result = api_instance.create_task({
                'workspace': '1205492548060699',
                'projects' : '1205492551710842',
                'name': title,
                'notes': description,
            })

        except ApiException as e:
            result ="Something went wrong"

        return result
