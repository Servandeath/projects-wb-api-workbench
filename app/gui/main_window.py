import customtkinter as ctk


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

        self._build_layout()

    def _build_layout(self) -> None:
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_sidebar()
        self._build_topbar()
        self._build_content()

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

    def _build_content(self) -> None:
        self.content = ctk.CTkFrame(self, corner_radius=12)
        self.content.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(1, weight=1)

        self.section_title = ctk.CTkLabel(
            self.content,
            text="API Tester",
            font=ctk.CTkFont(size=28, weight="bold"),
        )
        self.section_title.grid(row=0, column=0, padx=30, pady=(30, 10), sticky="w")

        self.section_description = ctk.CTkLabel(
            self.content,
            text="Test Wildberries API methods here.",
            font=ctk.CTkFont(size=16),
            justify="left",
        )
        self.section_description.grid(row=1, column=0, padx=30, pady=10, sticky="nw")

    def show_section(self, section_name: str) -> None:
        self.current_section = section_name
        self.title_label.configure(text=section_name)
        self.section_title.configure(text=section_name)

        descriptions = {
            "API Tester": "Test Wildberries API methods here.",
            "Keys": "Manage temporary, saved and encrypted API keys here.",
            "Imports": "Import local JSON, CSV and Excel files here.",
            "History": "View API request history and saved responses here.",
            "Diagnostics": "Run environment, database, permissions and key storage checks here.",
            "Settings": "Configure app settings, storage modes and access rules here.",
        }

        self.section_description.configure(
            text=descriptions.get(section_name, "Section is under development.")
        )


def run_gui() -> None:
    app = MainWindow()
    app.mainloop()
