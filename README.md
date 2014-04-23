Pinterest API for Python

Example of use:

http://localhost:8080/api/pinterest  
USE POST

PAYLOAD:
{
"username" : "username",
"password" : "password",
"board": "test",
"title": "This is an awesome product"
}

The board must exist first. Working on an endpoint for creating boards. You can add as many key values as you want. Then you can call get.[key] within the post() function to use that information. ex. get.username(). This can be seen below:

under post() function :  p = get_session(get.user_name(),get.password())
        
       


