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

    def no_events_to_display_view(self):
        text = Text("Aucun événement à afficher.")
        text.stylize("bold red")
        console.print(text)

    def no_customer_to_display_view(self):
        text = Text("Vous n'avez aucun client attribué.")
        text.stylize("bold red")
        console.print(text)

    def no_events_to_create_view(self):
        text = Text("Vous ne pouvez pas créer d'événement pour le moment, car \naucun contrat signé et "
                    "payé n'est disponible.")
        text.stylize("bold red")
        console.print(text)

    def error_date(self):
        text = Text("Une erreur s'est produite, veuillez respecter cet exemple : 31 Décembre 2025 18:00")
        text.stylize("bold red")
        console.print(text)

    def exceeded_number_of_characters(self):
        text = Text("Vous avez dépassé le nombre de caractères autorisé, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)

    def no_contracts_to_create_view(self):
        text = Text("Vous ne pouvez pas créer de contrat pour le moment")
        text.stylize("bold red")
        console.print(text)
