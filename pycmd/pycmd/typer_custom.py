from typer.core import TyperGroup


class CustomTyperGroup(TyperGroup):
    def list_commands(self, ctx):
        """Alphabetic sort commands"""
        return sorted(list(self.commands))

    def get_command(self, ctx, cmd_name):
        return super().get_command(ctx, cmd_name)
