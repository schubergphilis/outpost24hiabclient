import datetime

def set_boolean_value_as_string(xmlelement, boolean):
    if(boolean == True):
        xmlelement.text = 'true'
    elif(boolean == False):
        xmlelement.text='false'
    else:
        raise ValueError

def str_to_bool(str):
    if(str == 'true'):
        return True
    elif(str == 'false'):
        return False
    else:
        raise ValueError

def get_boolean_value_from_string(xmlelement):
        if(xmlelement is None):
            return None
        str = xmlelement.text
        return str_to_bool(str)

def get_str_from_child_if_exists(xmlelement, child):
    for c in xmlelement:
        if(c.tag == child):
            return c.text
    return None

def get_int_from_child_if_exists(xmlelement, child):
    for c in xmlelement:
        if(c.tag == child):
            str = c.text
            if(str is not None and not ""):
                return int(str)
    return None

def get_bool_from_child_if_exists(xmlelement, child):
    str = get_str_from_child_if_exists(xmlelement, child)
    return str_to_bool(str)

def get_date_from_child_if_exists(xmlelement, child):
    for c in xmlelement:
        if(c.tag == child):
            return datetime.datetime.strptime(c.text, '%Y-%m-%d %H:%M')