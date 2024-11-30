from rich.prompt import Prompt


class UserView:
    def get_name_view(self):
        name = Prompt.ask("[bold green]Nom :[/bold green]")
        return name

    def get_first_name_view(self):
        first_name = Prompt.ask("[bold green]Prénom :[/bold green]")
        return first_name

    def get_email_view(self):
        email = Prompt.ask("[bold green]Email :[/bold green]")
        return email

    def get_username_view(self):
        username = Prompt.ask("[bold green]Username :[/bold green]")
        return username

    def get_password_view(self):
        password = Prompt.ask("[bold green]Password :[/bold green]")
        return password

    def get_role_view(self):
        role = Prompt.ask("[bold green]Prénom :[/bold green]")
        return role
