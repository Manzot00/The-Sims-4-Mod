import sims4.commands as commands
import shlex

@commands.Command('test', command_type=commands.CommandType.Live)
def test(_connection=None):
    output = commands.CheatOutput(_connection)
    # Imposta il percorso assoluto per il file commands.txt
    file_path = r'C:\Users\Utente\Documents\Electronic Arts\The Sims 4\Mods\commands.txt'
    commands.execute('testingcheats on', _connection)

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for command_line in lines:
            command_line = command_line.strip()
            if command_line:
                try:
                    # Use shlex to split the command line into tokens
                    tokens = shlex.split(command_line)
                    if not tokens:
                        output(f"Errore: La riga è vuota o contiene solo spazi.")
                        continue

                    command_name = tokens[0]
                    # Reconstruct the command line with properly quoted arguments
                    formatted_command_line = ' '.join(tokens)
                    formatted_command_line.strip('"')
                    # Execute the command
                    commands.execute(formatted_command_line, _connection)
                    output(f"Eseguito comando: '{formatted_command_line}'")
                except Exception as e:
                    output(f"Errore durante l'esecuzione del comando '{command_line}': {e}")

    except FileNotFoundError:
        output("Errore: Il file commands.txt non è stato trovato.")