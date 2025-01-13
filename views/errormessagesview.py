from rich.text import Text
from rich.console import Console
console = Console()


class ErrorMessagesView:
    def error_username_password_view(self):
        """
        Fonction qui permet d'afficher un message d'erreur suite à une erreur de saisie
        identifiant / mot de passe.
        """
        text = Text("Erreur !! Identifiant ou mot de passe incorrect.")
        text.stylize("bold red")
        console.print(text)

    def display_error_message_of_values_yes_and_no(self):
        """
        Fonction qui permet d'afficher un message d'erreur indiquant à l'utilisateur de saisir
        les valeurs attendues.
        """
        text = Text("Erreur !! Vous devez saisir les valeurs suivantes [Y/N].")
        text.stylize("bold red")
        console.print(text)

    def display_error_message_choice_view(self):
        """
        Fonction qui permet d'afficher un message d'erreur lorsque l'utilisateur saisi
        une valeur inatendue.
        """
        text = Text("Choix invalide, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)

    def error_message_empty_field_view(self):
        """
        Fonction qui permet d'afficher un message d'erreur lorsque l'utilisateur valide
        un champ vide.
        """
        text = Text("Le champ ne peut être vide, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)

    def error_message_field_contains_number(self):
        """
        Fonction qui permet d'afficher un message d'erreur indiquant à l'utilisateur de saisir
        que des lettres majuscules et minuscules
        """
        text = Text("Le champ doit contenir que des lettres majuscules et minuscules, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)

    def error_message_choices_com_ges_sup_view(self):
        """
        Fonction qui permet d'afficher un message d'erreur indiquant à l'utilisateur de saisir
        les valeurs [COM/GES/SUP]
        """
        text = Text("Vous devez saisir les valeurs suivantes [COM/GES/SUP].")
        text.stylize("bold red")
        console.print(text)

    def display_message_error_database_view(self, x):
        text = Text("Erreur!! lors de la saisie du nom de la database.\nVous ne pouvez pas utiliser le(s)"
                    f"caractère()s suivant(s): {x}")
        text.stylize("bold red")
        console.print(text)

    def display_message_error_numerical_value_view(self):
        text = Text("Erreur!! Vous devez saisir une valeur numérique.")
        text.stylize("bold red")
        console.print(text)

    def no_contract_to_display_view(self):
        text = Text("Aucun contrat à afficher.")
        text.stylize("bold red")
        console.print(text)
