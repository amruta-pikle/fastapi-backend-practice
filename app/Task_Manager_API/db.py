from typing import Dict

users ={
    'amruta': {
        'username' : 'amr',
        'password' : 'password1234',
        'role' : 'admin'
    },
    'abhay' :{
        'username' : 'abh',
        'password' : 'password1122',
        'role' : 'user'
    }
}

tasks: Dict[int, str] ={}
task_id_counter = 1