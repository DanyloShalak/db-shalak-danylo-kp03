from datetime import date
import datetime

def get_query_data(command):
    if command.startswith('delete') or command.startswith('generate'):
        return get_id_paramData(command)
    if command.startswith('update'):
        return get_update_data(command)
    if command.startswith('insertUser'):
        return get_userData(command)
    if command.startswith('insertComment'):
        return get_commentData(command)
    if command.startswith('insertPost'):
        return get_postData(command)
    if command.startswith('analytics'):
        return get_analytics_data(command)
    if command.startswith('activity'):
        return get_activity_data(command)
    if command.startswith('userPost'):
        return get_user_post_data(command)
    

    
def get_update_data(command):
    data = command.split(' ')
    if len(data) != 3:
        raise Exception("Incorrect entered command '{0}'".format(data[0]))
    if len(data[1]) == 0:
        raise Exception("String parameter can not be empty")
    updateId = get_int_param(data[2])
    return (data[1].replace('-', ' '), updateId,)


def get_id_paramData(command):
    data = command.split(' ')
    if len(data) != 2:
        raise Exception("Wrong entered command '{0}'".format(data[0]))

    deleteId = get_int_param(data[1])
    return (deleteId, )


def get_userData(command):
    data = command.split(' ')
    if len(data) != 3:
        raise Exception("Wrong entered command 'insertUser'")
    if len(data[1]) == 0 or len(data[2]) == 0:
        raise Exception("String parameter can not be empty")

    return (data[1], data[2].replace('_', ' '), get_strDate(), )


def get_commentData(command):
    data = command.split(' ')
    if len(data) != 4:
        raise Exception("Wrong entered command 'insertComment'")
    if len(data[1]) == 0:
        raise Exception("String parameter can not be empty")
    postId = get_int_param(data[2])
    authorId = get_int_param(data[3])
    return (data[1].replace('_', ' '), postId, authorId, get_strDate(), )


def get_postData(command):
    data = command.split(' ')
    if len(data) != 4 and len(data) != 3:
        raise Exception("Incorrect entered command 'insertPost'")
    if len(data[1]) == 0:
        raise Exception("String parameter can not be empty")
    authorId = get_int_param(data[2])
    date = get_strDate()
    tags = []
    if len(data) == 4 and len(data[3]) != 0:
        tags = get_tags(data[3])
    return (data[1].replace('_', ' '), authorId, date, tags)


def get_analytics_data(command):
    data = command.split(' ')
    if len(data) != 3 and len(data) != 4:
        raise Exception("Incorrect entered command 'analytics'")
    posible_parameters = ['desc', 'asc']
    if data[1] not in posible_parameters or data[2] not in posible_parameters:
        raise Exception("Incorrect entered 'analytics' filter parameters")
    lim = 'all'
    if len(data) == 4:
        lim = get_int_param(data[3])
    return (data[1], data[2], lim, )


def get_activity_data(command):
    data = command.split(' ')
    if len(data) != 4 and len(data) != 5:
        raise Exception("Incorrect entered command 'analytics'")
    posible_parameters = ['desc', 'asc']
    if data[1] not in posible_parameters or data[2] not in posible_parameters:
        raise Exception("Incorrect entered 'analytics' filter parameters")
    lim = 'all'
    if len(data) == 5:
        lim = get_int_param(data[4])
    date_ = date.fromisoformat(data[3])
    return (data[3], data[1], data[2], lim,)


def get_user_post_data(command):
    data = command.split(' ')
    if len(data) != 4 and len(data) != 5:
        raise Exception("Incorrect entered command 'analytics'")
    posible_parameters = ['desc', 'asc']
    if data[2] not in posible_parameters or data[3] not in posible_parameters:
        raise Exception("Incorrect entered 'analytics' filter parameters")
    lim = 'all'
    if len(data) == 5:
        lim = get_int_param(data[4])
    userId = get_int_param(data[1])
    return (userId, data[2], data[3], lim, )


def get_int_param(rawInt):
    number = 0
    try:
        number = int(rawInt)
    except :
        raise Exception("Incorrect type of integer parameter")
    return number

def get_strDate():
    date = datetime.datetime.now()
    strDate = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
    return strDate


def get_tags(tagData):
    if tagData.startswith('tag:') == False:
        raise Exception('Incorrect entered tag data')
    tags = tagData.replace('tag:', '').split('#')
    return tags