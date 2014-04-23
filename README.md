Pinterest API for Python

Example of use:

http://localhost:8080/api/pinterest  
POST
PAYLOAD:
{
"username" : "username",
"password" : "password",
"board": "test",
"title": "This is an awesome product"
}

The board must exist first. Working on an endpoint for creating boards. You can add as many key values as you want. Then you can call get.[key] within the post() function to use that information. ex. get.username(). This can be seen below:

def post():
    import traceback
    try:
        get = lib.apihelper
        p = get_session(get.user_name(),get.password())
        boards = p.getBoards()
        print boards
        res = p.createPin(board=boards[get.board()],title=get.title(),
                    media='createdynamicmediahere (this should be a link to an image)',
                    posturl='createdynamicposturlhere (this should be a link)'
                )

        print 'pin created: %s' % res
    except:
        return abort(500, traceback.format_exc())

