import json_manager
import click 

@click.group()
def cli():
    pass

@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='name of the user')
@click.option('--email', help='email of the user')
def update(id, name, email):
            data = json_manager.read_json()
            for user in data:
                if user['id'] == id:
                    if name is not None:
                        user['name'] = name
                    if email is not None:
                        user['email'] = email
                    break
            json_manager.write_json(data)
            print(f"User with id {id} updated successfully")

@cli.command()
@click.option('--name', required=True , help='name of the user')
@click.option('--email', required=True , help='email of the user')
@click.pass_context
def new(ctx, name, email):
    if not name or not email:
        ctx.fail("You must provide a name and email")
    else:
        data = json_manager.read_json()
    new_id = len(data) + 1
    new_user = {
        'id': new_id,
        'name': name,
        'email': email
    }
    data.append(new_user)
    json_manager.write_json(data)
    print(f"User {name} {email} added successfully with id {new_id}")

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['email']}")

@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next ((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['email']}")

       

    
@cli.command()
@click.argument('id', type=int)
def delete (id):
    data = json_manager.read_json()
    user = next ((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id {id} deleted successfully")

if __name__ == '__main__':
    cli()
