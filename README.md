# Django Test Task

## Documentation

### How to start? 

You have to build images with 
* docker-compose build 
After that, make sure that images are wotking and call
* docker-compose up
, which will run the python image and the db image

### How to use it?

There is a set of endpoints, that will allow you to do certain things.
Using Postman, you can send 



In this notation, [] means Optional, could be unused.

Get, Post, Patch, Delete requests at
* localhost:8000/posts/
* localhost:8000/comments/
but you will need to specify the exact items for delete and patch methods.

* GET localhost:8000/posts/ - returns you a full list of posts
* GET localhost:8000/posts/id_<id> - returns you a post item with id = given id or "Item not found"
* GET localhost:8000/posts/upvote_<id> - an endpoint for upvoting a post. Returns 200 if item exists and 404 if it does not. 
* GET localhost:8000/posts/link_<id> - returns a redirect to a source of the post or 404.

* POST localhost:8000/posts/ - with body = {
    "title": <title_name>,
    "link": <post_link>,
    "author_name": <name_of_the_author>
} - If data is valid, a new item with this data is created and will be returned

* PATCH localhost:8000/posts/id_<id> - with body = {
    ["title": <title_name>,]
    ["link": <post_link>,]
    ["author_name": <name_of_the_author>]
} - If data is valid, and such item exists, it will display the new field and items field will be changed to your value

* DELETE localhost:8000/posts/id_<id> - if an item with id = given id exists, it will be deleted, and also all of it's comments


* GET localhost:8000/comments/ - returns you a full list of comments
* GET localhost:8000/comment/id_<id> - returns you a comment item with id = given id or "Item not found"
* GET localhost:8000/comment/post_<id> - returns you all the comments that relate to one given post.

* POST localhost:8000/comments/ - with body = {
    "post_id": <post_id>, # id of the post you want to comment on
    "content": <content>, # Comment content
    "author_name": <author_name>, # Name of the author
    ["creation_date" : [<creation_date>] # Date of creation]
} - If data is valid, and a post with given id exists, it will create a comment and add its id to a corresponding post

* PATCH localhost:8000/comments/id_<id> - with body = {
    ["post_id": <post_id>,] # id of the post you want to comment on
    ["content": <content>,] # Comment content
    ["author_name": <author_name>,] # Name of the author
    ["creation_date" : [<creation_date>] # Date of creation]
} - If data is valid, and such item exists, it will display the new field and items field will be changed to your value

* DELETE localhost:8000/posts/id_<id> - if an item with id = given id exists, it will be deleted, and its id will be removed from a corresponding post


As simple as that. 
Yeah ._.
by Mykyta Liubshyn
