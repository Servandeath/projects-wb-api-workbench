import customtkinter as ctk

from app.core.diagnostics import format_diagnostics, run_diagnostics


class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("WB API Workbench")
        self.geometry("1100x720")
        self.minsize(1000, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.current_section = "API Tester"
        self.current_role = "Viewer"
        self.current_mode = "Test"

        self.diagnostics_output: ctk.CTkTextbox | None = None

        self._build_layout()

    def _build_layout(self) -> None:
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_sidebar()
        self._build_topbar()
        self._show_default_section(
            title="API Tester",
            description="Test Wildberries API methods here.",
        )

    def _build_sidebar(self) -> None:
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar.grid_propagate(False)

        title = ctk.CTkLabel(
            self.sidebar,
            text="WB Workbench",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        title.pack(pady=(24, 20), padx=16)

        sections = [
            "API Tester",
            "Keys",
            "Imports",
            "History",
            "Diagnostics",
            "Settings",
        ]

        for section in sections:
            button = ctk.CTkButton(
                self.sidebar,
                text=section,
                anchor="w",
                height=40,
                command=lambda name=section: self.show_section(name),
            )
            button.pack(fill="x", padx=16, pady=6)

    def _build_topbar(self) -> None:
        self.topbar = ctk.CTkFrame(self, height=70, corner_radius=0)
        self.topbar.grid(row=0, column=1, sticky="ew")
        self.topbar.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self.topbar,
            text=self.current_section,
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self.title_label.grid(row=0, column=0, padx=24, pady=18, sticky="w")

        status_text = (
            f"Role: {self.current_role}  |  "
            f"Mode: {self.current_mode}  |  "
            "Key: not set"
        )

        self.status_label = ctk.CTkLabel(
            self.topbar,
            text=status_text,
            font=ctk.CTkFont(size=13),
        )
        self.status_label.grid(row=0, column=1, padx=24, pady=18, sticky="e")

    def _clear_content(self) -> None:
        for widget in self.winfo_children():
            if widget.grid_info().get("row") == 1 and widget.grid_info().get("column") == 1:
                widget.destroy()

    def _create_content_frame(self) -> ctk.CTkFrame:
        self._clear_content()

        content = ctk.CTkFrame(self, corner_radius=12)
        content.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(2, weight=1)

        return content

    def _show_default_section(self, title: str, description: str) -> None:
        content = self._create_content_frame()

        section_title = ctk.CTkLabel(
            content,
            text=title,
            font=ctk.CTkFont(size=28, weight="bold"),
        )
        section_title.grid(row=0, column=0, padx=30, pady=(30, 10), sticky="w")

        section_description = ctk.CTkLabel(
            content,
            text=description,
            font=ctk.CTkFont(size=16),
            justify="left",
        )
        section_description.grid(row=1, column=0, padx=30, pady=10, sticky="nw")

    def _show_diagnostics_section(self) -> None:
        content = self._create_content_frame()

        title = ctk.CTkLabel(
            content,
            text="Diagnostics",
            font=ctk.CTkFont(size=28, weight="bold"),
        )
        title.grid(row=0, column=0, padx=30, pady=(30, 10), sticky="w")

        run_button = ctk.CTkButton(
            content,
            text="Run Diagnostics",
            height=40,
            command=self._run_diagnostics,
        )
        run_button.grid(row=1, column=0, padx=30, pady=10, sticky="w")

        self.diagnostics_output = ctk.CTkTextbox(content, height=360)
        self.diagnostics_output.grid(
            row=2,
            column=0,
            padx=30,
            pady=(10, 30),
            sticky="nsew",
        )
        self.diagnostics_output.insert(
            "1.0",
            "Click Run Diagnostics to check the local app environment.",
        )

    def _run_diagnostics(self) -> None:
        if self.diagnostics_output is None:
            return

        results = run_diagnostics()
        output = format_diagnostics(results)

        self.diagnostics_output.delete("1.0", "end")
        self.diagnostics_output.insert("1.0", output)

    def show_section(self, section_name: str) -> None:
        self.current_section = section_name
        self.title_label.configure(text=section_name)

        descriptions = {
            "API Tester": "Test Wildberries API methods here.",
            "Keys": "Manage temporary, saved and encrypted API keys here.",
            "Imports": "Import local JSON, CSV and Excel files here.",
            "History": "View API request history and saved responses here.",
            "Settings": "Configure app settings, storage modes and access rules here.",
        }

        if section_name == "Diagnostics":
            self._show_diagnostics_section()
            return

        self._show_default_section(
            title=section_name,
            description=descriptions.get(section_name, "Section is under development."),
        )


def run_gui() -> None:
    app = MainWindow()
    app.mainloop()
