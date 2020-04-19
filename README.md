# ICA Shopping List API Wrapper

Built to simplify the use of the ICA shopping list API using Python

Example 

    from icaapi import ICAapi
    
    connection = ICAapi(user, psw)
    
    ICAapi.items #return all unchecked items in all shoppinglists
    ICAapi.lists #returns the names of all the shopping lists you have
    ICAapi.items_in_list(list_name) #returns all the items of that specified shopping list
