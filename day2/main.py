import asyncio
from textual import App, Button, Label, Pane, Panel
from textual.reactive import reactive
from textual.widgets import StaticLabel, Highlighter
from textual.utils import resolve_config_value

class LogApp(App):
    def __init__(self):
        super().__init__()

        self.log_file = "log.txt"
        self.json_data = None
        self.yaml_data = None
        self.pane1 = None
        self.pane2 = None

        self.log_lines = self.read_log_lines()

        self.log_pane = Pane()
        self.log_pane.add(self.log_widget())

        self.json_pane = Panel()
        self.json_pane.add(
            StaticLabel(label="JSON Data")
        )

        self.yaml_pane = Panel()
        self.yaml_pane.add(
            StaticLabel(label="YAML Data")
        )

    async def read_log_lines(self):
        with open(self.log_file, "r") as f:
            return [line.strip() for line in f.readlines()]

    async def log_widget(self):
        label = Label(text="", id="log-label", class_name="log-pane")
        self.add_panel(
            Pane([
                (label, 0.5),
            ])
        )

        @self.event("render_log")
        async def on_render_log(message):
            text = message.get("text", "")
            await label.set_text(text)

    async def json_widget(self):
        label = StaticLabel(label="", id="json-label", class_name="json-pane")
        self.add_panel(
            Pane([
                (label, 0.5),
            ])
        )

        @self.event("render_json")
        async def on_render_json(message):
            data = message.get("data", {})
            await label.set_text(str(data))

    async def yaml_widget(self):
        label = StaticLabel(label="", id="yaml-label", class_name="yaml-pane")
        self.add_panel(
            Pane([
                (label, 0.5),
            ])
        )

        @self.event("render_yaml")
        async def on_render_yaml(message):
            data = message.get("data", {})
            await label.set_text(self.yaml_dump(data))

    @reactive
    def on_select_log(pane: Panel) -> None:
        self.log_pane = pane
        pane.content.update()

    @reactive
    def on_select_json(pane: Panel) -> None:
        self.json_pane = pane
        self.json_data = None

    @reactive
    def on_select_yaml(pane: Panel) -> None:
        self.yaml_pane = pane
        self.yaml_data = None

    async def highlight(self, text, keywords):
        lines = text.splitlines()
        highlighted_lines = []
        for line in lines:
            if any(keyword in line for keyword in keywords):
                highlighted_line = f'<{len(line)}>{line}</{len(line)}'
            else:
                highlighted_line = line
            highlighted_lines.append(highlighted_line)
        return "\n".join(highlighted_lines)

    def yaml_dump(self, data):
        import pyyaml as yaml
        return yaml.dump(data)

    async def run(self) -> None:
        await self.log_pane.render_log(log_lines=self.log_lines)
        await self.json_pane.render_json(json_data=self.json_data)
        await self.yaml_pane.render_yaml(yaml_data=self.yaml_data)

if __name__ == "__main__":
    LogApp().run()
