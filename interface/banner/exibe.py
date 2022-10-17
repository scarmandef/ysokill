from rich import print

def banner() -> str:
  path: str = "interface/banner/banner.txt"
    with open(path) as file:
        content = file.read()
        print(f"[bold white]{content}[/]")

