import typer
from pycmd import settings, console, CustomTyperGroup
from typing_extensions import Annotated
from typer import Context


app = typer.Typer(
    cls=CustomTyperGroup,
    no_args_is_help=True,
    short_help="Debug CLI settings",
    rich_markup_mode="rich",
)

@app.command("commands", help=f"Debug [green b]{settings.project.name}[/] commands")
def commands(
    ctx: Context,
    verbose: Annotated[bool, typer.Option("--verbose", "-v")] = None,
    fmt: Annotated[str, typer.Option("--fmt")] = "table",
):
    """Debug cli commands"""
    verbose and console.log(f'command="{ctx.command_path}"')
    # from pycmd.utils import debug_cli
    # debug_cli(app, settings.project.name, fmt=fmt, verbose=verbose)


if __name__ == "__main__":
    app()
