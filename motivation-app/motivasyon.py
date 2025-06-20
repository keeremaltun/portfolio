import random
from rich.console import Console
from rich.panel import Panel

QUOTES_FILE = "quotes.txt"
console = Console()

def load_quotes():
    with open(QUOTES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip().strip('",') for line in lines if line.strip()]

def save_quotes(quotes):
    with open(QUOTES_FILE, "w", encoding="utf-8") as f:
        for quote in quotes:
            f.write(f'"{quote}",\n')

def show_random_quote():
    quotes = load_quotes()
    if quotes:
        quote = random.choice(quotes)
        console.print(Panel(quote, title="Random Quote", style="bold magenta"))
    else:
        console.print("[red]Quote list is empty.[/red]")

def add_quote(new_quote):
    quotes = load_quotes()
    quotes.append(new_quote)
    save_quotes(quotes)
    console.print("[green]Quote added.[/green]")

def remove_quote(quote_to_remove):
    quotes = load_quotes()
    if quote_to_remove in quotes:
        quotes.remove(quote_to_remove)
        save_quotes(quotes)
        console.print("[yellow]Quote removed.[/yellow]")
    else:
        console.print("[red]Quote not found.[/red]")

def main_loop():
    while True:
        console.print("\n[bold cyan]1:[/bold cyan] Show random quote\n[bold cyan]2:[/bold cyan] Add quote\n[bold cyan]3:[/bold cyan] Remove quote\nType '[bold]exit[/bold]' to quit.")
        choice = input("Select: ").strip()
        if choice == "1":
            show_random_quote()
        elif choice == "2":
            new_q = input("Enter new quote: ").strip()
            add_quote(new_q)
        elif choice == "3":
            rem_q = input("Enter quote to remove: ").strip()
            remove_quote(rem_q)
        elif choice.lower() == "exit":
            console.print("[bold green]Exiting...[/bold green]")
            break
        else:
            console.print("[red]Invalid choice.[/red]")

main_loop()
